from pyspark.sql import SparkSession

from sedona.register import SedonaRegistrator
from sedona.utils import SedonaKryoRegistrator, KryoSerializer
from sedona.core.enums import GridType, IndexType
from sedona.core.formatMapper import WktReader
from sedona.core.geom.envelope import Envelope
from sedona.core.spatialOperator import RangeQuery
import time, pprint

'''
spark-submit --master yarn --jars hdfs:/data/geotools-wrapper-1.1.0-25.2.jar,hdfs:/data/sedona-python-adapter-3.0_2.12-1.2.0-incubating.jar code.py --deploy-mode cluster
'''

if __name__ == '__main__':
    spark = SparkSession. \
        builder. \
        appName('RANGE_QUERY_POINTS'). \
        config("spark.serializer", KryoSerializer.getName). \
        config("spark.kryo.registrator", SedonaKryoRegistrator.getName). \
        config('spark.jars.packages',
               'org.apache.sedona:sedona-python-adapter-3.0_2.12:1.2.0-incubating,'
               'org.datasyslab:geotools-wrapper:1.1.0-25.2'). \
        getOrCreate()

    SedonaRegistrator.registerAll(spark)

    output_file = open('output.csv', 'w+')
    pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)

    DATA_PATH = 'hdfs:/data/'

    sc = spark.sparkContext

    points_rdd = WktReader.readToGeometryRDD(sc, DATA_PATH + '/all_points_100K.wkt', 1, True, False)
    points_rdd.analyze()

    len = 100000

    points_rdd.spatialPartitioning(GridType.KDBTREE)

    query_envelope = Envelope(-85.01, -60.01, 34.01, 50.01)

    for i in range(3):
        if i == 0:
            pp.pprint("No Index")
            using_index = False
        elif i == 1:
            pp.pprint("R-Tree Index")
            # using R-tree index
            using_index = True

            build_on_spatial_partitioned_rdd = False ## Set to TRUE only if run join query
            points_rdd.buildIndex(IndexType.RTREE, build_on_spatial_partitioned_rdd)
        elif i == 2:
            pp.pprint("Quad-Tree Index")
            # using Quad-tree index
            using_index = True

            build_on_spatial_partitioned_rdd = False ## Set to TRUE only if run join query
            points_rdd.buildIndex(IndexType.QUADTREE, build_on_spatial_partitioned_rdd)


        pp.pprint("n,time(s)")
        s = time.time()
        result = RangeQuery.SpatialRangeQuery(points_rdd, query_envelope, True, using_index)
        result.collect()
        d = time.time() - s
        pp.pprint(str(len) + "," + str(round(d, 3)))


