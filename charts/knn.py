import utils


'''
    Single node benchmarks
'''

# Points:
for size in [ '1k', '10k', '100k' ]:
    # KDB-Tree partitioning
    utils.plot_k(
        'Points: KDB-Tree partitioning : ' + size,
        '../benchmarks/knn/single_node/points/index_comparision_' + size + '_kdb_partition.csv',
        '../benchmarks/knn/single_node/points/plots/index_comparision_' + size + '_kdb_partition.png'
    )

    # Quad-Tree partitioning
    utils.plot_k(
        'Points: Quad-Tree partitioning : ' + size,
        '../benchmarks/knn/single_node/points/index_comparision_' + size + '_quad_partition.csv',
        '../benchmarks/knn/single_node/points/plots/index_comparision_' + size + '_quad_partition.png'
    )

# Overall: KDB-Tree partitioning : K = 500
utils.plot_size(
    'Points: KDB-Tree partitioning : K = 500',
    '../benchmarks/knn/single_node/points/index_comparision_kdb_partition.csv',
    '../benchmarks/knn/single_node/points/plots/index_comparision_kdb_partition.png'
)

# Overall: Quad-Tree partitioning : K = 500
utils.plot_size(
    'Points: Quad-Tree partitioning : K = 500',
    '../benchmarks/knn/single_node/points/index_comparision_quad_partition.csv',
    '../benchmarks/knn/single_node/points/plots/index_comparision_quad_partition.png'
)

# Polygons:
for size in [ '1k', '10k' ]:
    # KDB-Tree partitioning
    utils.plot_k(
        'Polygons: KDB-Tree partitioning : ' + size,
        '../benchmarks/knn/single_node/polygons/index_comparision_' + size + '_kdb_partition.csv',
        '../benchmarks/knn/single_node/polygons/plots/index_comparision_' + size + '_kdb_partition.png'
    )

    # Quad-Tree partitioning
    utils.plot_k(
        'Polygons: Quad-Tree partitioning : ' + size,
        '../benchmarks/knn/single_node/polygons/index_comparision_' + size + '_quad_partition.csv',
        '../benchmarks/knn/single_node/polygons/plots/index_comparision_' + size + '_quad_partition.png'
    )

# Overall: KDB-Tree partitioning : K = 500
utils.plot_size(
    'Polygons: KDB-Tree partitioning : K = 500',
    '../benchmarks/knn/single_node/polygons/index_comparision_kdb_partition.csv',
    '../benchmarks/knn/single_node/polygons/plots/index_comparision_kdb_partition.png'
)

# Overall: Quad-Tree partitioning : K = 500
utils.plot_size(
    'Points: Quad-Tree partitioning : K = 500',
    '../benchmarks/knn/single_node/polygons/index_comparision_quad_partition.csv',
    '../benchmarks/knn/single_node/polygons/plots/index_comparision_quad_partition.png'
)


'''
    Cluster benchmarks
'''

# Points:
for size in [ '1k', '10k', '100k' ]:
    # KDB-Tree partitioning
    utils.plot_k(
        'Points: KDB-Tree partitioning : ' + size,
        '../benchmarks/knn/cluster/points/index_comparision_' + size + '_kdb_partition.csv',
        '../benchmarks/knn/cluster/points/plots/index_comparision_' + size + '_kdb_partition.png'
    )

    # Quad-Tree partitioning
    utils.plot_k(
        'Points: Quad-Tree partitioning : ' + size,
        '../benchmarks/knn/cluster/points/index_comparision_' + size + '_quad_partition.csv',
        '../benchmarks/knn/cluster/points/plots/index_comparision_' + size + '_quad_partition.png'
    )

# Overall: KDB-Tree partitioning : K = 500
utils.plot_size(
    'Points: KDB-Tree partitioning : K = 500',
    '../benchmarks/knn/cluster/points/index_comparision_kdb_partition.csv',
    '../benchmarks/knn/cluster/points/plots/index_comparision_kdb_partition.png'
)

# Overall: Quad-Tree partitioning : K = 500
utils.plot_size(
    'Points: Quad-Tree partitioning : K = 500',
    '../benchmarks/knn/cluster/points/index_comparision_quad_partition.csv',
    '../benchmarks/knn/cluster/points/plots/index_comparision_quad_partition.png'
)

# Polygons:
for size in [ '1k', '10k' ]:
    # KDB-Tree partitioning
    utils.plot_k(
        'Polygons: KDB-Tree partitioning : ' + size,
        '../benchmarks/knn/cluster/polygons/index_comparision_' + size + '_kdb_partition.csv',
        '../benchmarks/knn/cluster/polygons/plots/index_comparision_' + size + '_kdb_partition.png'
    )

    # Quad-Tree partitioning
    utils.plot_k(
        'Polygons: Quad-Tree partitioning : ' + size,
        '../benchmarks/knn/cluster/polygons/index_comparision_' + size + '_quad_partition.csv',
        '../benchmarks/knn/cluster/polygons/plots/index_comparision_' + size + '_quad_partition.png'
    )

# Overall: KDB-Tree partitioning : K = 500
utils.plot_size(
    'Overall: KDB-Tree partitioning : K = 500 (Cluster v/s Single-node)',
    '../benchmarks/knn/cluster/polygons/index_comparision_kdb_partition.csv',
    '../benchmarks/knn/cluster/polygons/plots/index_comparision_kdb_partition.png'
)

# Overall: Quad-Tree partitioning : K = 500
utils.plot_size(
    'Overall: Quad-Tree partitioning : K = 500 (Cluster v/s Single-node)',
    '../benchmarks/knn/cluster/polygons/index_comparision_quad_partition.csv',
    '../benchmarks/knn/cluster/polygons/plots/index_comparision_quad_partition.png'
)



'''
    Overall benchmarks
'''

# Points:
utils.plot_k(
    'Points: Cluster v/s single-node : 10K : No index',
    '../benchmarks/knn/overall/points_10k/overall_comparision_no_index.csv',
    '../benchmarks/knn/overall/points_10k/overall_comparision_no_index.png'
)

utils.plot_k(
    'Points: Cluster v/s single-node : 10K : R-Tree index',
    '../benchmarks/knn/overall/points_10k/overall_comparision_r_tree_index.csv',
    '../benchmarks/knn/overall/points_10k/overall_comparision_r_tree_index.png'
)

# Polygons:
utils.plot_k(
    'Polygons: Cluster v/s single-node : 10K : No index',
    '../benchmarks/knn/overall/polygons_10k/overall_comparision_no_index.csv',
    '../benchmarks/knn/overall/polygons_10k/overall_comparision_no_index.png'
)

utils.plot_k(
    'Polygons: Cluster v/s single-node : 10K : R-Tree index',
    '../benchmarks/knn/overall/polygons_10k/overall_comparision_r_tree_index.csv',
    '../benchmarks/knn/overall/polygons_10k/overall_comparision_r_tree_index.png'
)