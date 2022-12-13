from pyspark.sql import SparkSession

from sedona.register import SedonaRegistrator
from sedona.utils import SedonaKryoRegistrator, KryoSerializer
from sedona.core.enums import GridType, IndexType
from sedona.core.formatMapper import WktReader
from sedona.core.spatialOperator import JoinQuery
import time, pprint

'''
spark-submit --master yarn --jars hdfs:/data/geotools-wrapper-1.1.0-25.2.jar,hdfs:/data/sedona-python-adapter-3.0_2.12-1.2.0-incubating.jar code.py --deploy-mode cluster
'''

if __name__ == '__main__':
    spark = SparkSession. \
        builder. \
        appName('JOIN_QUERY'). \
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
    polygon_rdd = WktReader.readToGeometryRDD(sc, DATA_PATH + '/all_source_1K.wkt', 1, True, False)

    points_rdd.analyze()
    polygon_rdd.analyze()

    len = 100000

    points_rdd.spatialPartitioning(GridType.KDBTREE)
    polygon_rdd.spatialPartitioning(points_rdd.getPartitioner())

    for i in range(3):
        using_index = False

        if i == 0:
            pp.pprint("No Index")
        elif i == 1:
            pp.pprint("R-Tree Index")
            # using R-tree index
            using_index = True

            build_on_spatial_partitioned_rdd = True ## Set to TRUE only if run join query
            polygon_rdd.buildIndex(IndexType.RTREE, build_on_spatial_partitioned_rdd)
        elif i == 2:
            pp.pprint("Quad-Tree Index")
            # using Quad-tree index
            using_index = True

            build_on_spatial_partitioned_rdd = True ## Set to TRUE only if run join query
            polygon_rdd.buildIndex(IndexType.QUADTREE, build_on_spatial_partitioned_rdd)


        pp.pprint("n,time(s)")
        s = time.time()
        result = JoinQuery.SpatialJoinQuery(points_rdd, polygon_rdd, True, using_index)
        # result.count()
        d = time.time() - s
        pp.pprint(str(len) + "," + str(round(d, 3)))


