import utils

'''
    Single node benchmarks
'''

# Points: KDB-Tree
utils.plot_size(
    'Points: KDB-Tree partitioning: Polygons = 1K',
    '../benchmarks/join/single_node/points/index_comparision_kdb_partition.csv',
    '../benchmarks/join/single_node/points/index_comparision_kdb_partition.png'
)

# Points: Quad-Tree
utils.plot_size(
    'Points: Quad-Tree partitioning: Polygons = 1K',
    '../benchmarks/join/single_node/points/index_comparision_quad_partition.csv',
    '../benchmarks/join/single_node/points/index_comparision_quad_partition.png'
)

# Polygons: KDB-Tree
utils.plot_size(
    'Polygons: KDB-Tree partitioning: Points = 1K',
    '../benchmarks/join/single_node/polygons/index_comparision_kdb_partition.csv',
    '../benchmarks/join/single_node/polygons/index_comparision_kdb_partition.png'
)

# Polygons: Quad-Tree
utils.plot_size(
    'Polygons: Quad-Tree partitioning: Points = 1K',
    '../benchmarks/join/single_node/polygons/index_comparision_quad_partition.csv',
    '../benchmarks/join/single_node/polygons/index_comparision_quad_partition.png'
)


'''
    Cluster benchmarks
'''

# Points: KDB-Tree
utils.plot_size(
    'Points: KDB-Tree partitioning: Polygons = 1K',
    '../benchmarks/join/cluster/points/index_comparision_kdb_partition.csv',
    '../benchmarks/join/cluster/points/index_comparision_kdb_partition.png'
)

# Points: Quad-Tree
utils.plot_size(
    'Points: Quad-Tree partitioning: Polygons = 1K',
    '../benchmarks/join/cluster/points/index_comparision_quad_partition.csv',
    '../benchmarks/join/cluster/points/index_comparision_quad_partition.png'
)

# Polygons: KDB-Tree
utils.plot_size(
    'Polygons: KDB-Tree partitioning: Points = 1K',
    '../benchmarks/join/cluster/polygons/index_comparision_kdb_partition.csv',
    '../benchmarks/join/cluster/polygons/index_comparision_kdb_partition.png'
)

# Polygons: Quad-Tree
utils.plot_size(
    'Polygons: Quad-Tree partitioning: Points = 1K',
    '../benchmarks/join/cluster/polygons/index_comparision_quad_partition.csv',
    '../benchmarks/join/cluster/polygons/index_comparision_quad_partition.png'
)


'''
    Overall benchmarks: All Using KDB-Tree partitioning
'''

# Points: No index
utils.plot_size(
    'Points: Cluster v/s Single-node : No index',
    '../benchmarks/join/overall/points/overall_comparision_no_index.csv',
    '../benchmarks/join/overall/points/overall_comparision_no_index.png'
)

# Points: Quad-Tree index
utils.plot_size(
    'Points: Cluster v/s Single-node : Quad-Tree index',
    '../benchmarks/join/overall/points/overall_comparision_quad_tree_index.csv',
    '../benchmarks/join/overall/points/overall_comparision_quad_tree_index.png'
)

# Points: R-Tree index
utils.plot_size(
    'Points: Cluster v/s Single-node : R-Tree index',
    '../benchmarks/join/overall/points/overall_comparision_r_tree_index.csv',
    '../benchmarks/join/overall/points/overall_comparision_r_tree_index.png'
)


# Polygons: No index
utils.plot_size(
    'Polygons: Cluster v/s Single-node : No index',
    '../benchmarks/join/overall/polygons/overall_comparision_no_index.csv',
    '../benchmarks/join/overall/polygons/overall_comparision_no_index.png'
)

# Polygons: Quad-Tree index
utils.plot_size(
    'Polygons: Cluster v/s Single-node : Quad-Tree index',
    '../benchmarks/join/overall/polygons/overall_comparision_quad_tree_index.csv',
    '../benchmarks/join/overall/polygons/overall_comparision_quad_tree_index.png'
)

# Polygons: R-Tree index
utils.plot_size(
    'Polygons: Cluster v/s Single-node : R-Tree index',
    '../benchmarks/join/overall/polygons/overall_comparision_r_tree_index.csv',
    '../benchmarks/join/overall/polygons/overall_comparision_r_tree_index.png'
)

