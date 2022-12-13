from pyspark.sql import SparkSession

from sedona.register import SedonaRegistrator
from sedona.utils import SedonaKryoRegistrator, KryoSerializer
from sedona.core.enums import GridType, IndexType
from sedona.core.formatMapper import WktReader

from sedona.core.spatialOperator import KNNQuery
from shapely.geometry import Point
import time

'''
spark-submit --master yarn --jars hdfs:/data/geotools-wrapper-1.1.0-25.2.jar,hdfs:/data/sedona-python-adapter-3.0_2.12-1.2.0-incubating.jar knn_points.py --deploy-mode cluster
'''

if __name__ == '__main__':
    spark = SparkSession. \
        builder. \
        appName('KNN_POINTS'). \
        config("spark.serializer", KryoSerializer.getName). \
        config("spark.kryo.registrator", SedonaKryoRegistrator.getName). \
        config('spark.jars.packages',
               'org.apache.sedona:sedona-python-adapter-3.0_2.12:1.2.0-incubating,'
               'org.datasyslab:geotools-wrapper:1.1.0-25.2'). \
        getOrCreate()

    SedonaRegistrator.registerAll(spark)

    DATA_PATH = 'hdfs:/data/'

    sc = spark.sparkContext

    points_rdd = WktReader.readToGeometryRDD(sc, DATA_PATH + '/all_points_1K.wkt', 1, True, False)
    points_rdd.analyze()

    len = 1000

    coords = [73.512247, 4.083805]

    points_rdd.spatialPartitioning(GridType.KDBTREE)

    point = Point(coords)

    for i in range(2):
      using_index = False
      if i == 1:
        # using R-tree index
        using_index = True

        build_on_spatial_partitioned_rdd = False ## Set to TRUE only if run join query
        points_rdd.buildIndex(IndexType.RTREE, build_on_spatial_partitioned_rdd)

      k_vals = [ 1, 5, 10, 20, 30, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 75000 ]

      print("k,time(s)")
      for k in k_vals:
        if k <= len:
          s = time.time()
          result = KNNQuery.SpatialKnnQuery(points_rdd, point, k, using_index)
          d = time.time() - s
          print(str(k) + "," + str(round(d, 3)))


