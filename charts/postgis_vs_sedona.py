import utils


'''
    Single node comparision: PostGIS vs Sedona
'''


utils.plot_size(
    'Polygons: Spatial JOIN query',
    '../benchmarks/postgis_vs_sedona/join.csv',
    '../benchmarks/postgis_vs_sedona/plots/join.png'
)

utils.plot_size(
    'Polygons: KNN query : K = 500',
    '../benchmarks/postgis_vs_sedona/knn.csv',
    '../benchmarks/postgis_vs_sedona/plots/knn.png'
)

utils.plot_size(
    'Polygons: Range query',
    '../benchmarks/postgis_vs_sedona/range.csv',
    '../benchmarks/postgis_vs_sedona/plots/range.png'
)

utils.plot_comparision(
    'Overall: Sedona v/s PostGIS : 10K Polygons',
    '../benchmarks/postgis_vs_sedona/overall.csv',
    '../benchmarks/postgis_vs_sedona/plots/overall.png'
)