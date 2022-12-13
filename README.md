
## Apache sedona benchmarks

  

The following repository contains experiments run on both a 4-node cluster and on a single-node for 3 types of queries:

- K Nearest Neighbor query (`KNNQuery.SpatialKnnQuery`)

- Range query (`RangeQuery.SpatialRangeQuery`)

- Spatial Join query (`JoinQuery.SpatialJoinQuery`)

  
  

### Pre-processing:

  

#### 1. Creating datasets:

We use three sizes 1K, 10K, 100K for benchmarking. Using the `head` command we create different sized chunks of the complete data.

```
Points wkt file:

$ head -1000 /all_points_1K.wkt
$ head -10000 /all_points_10K.wkt
$ head -100000 /all_points_100K.wkt

Similarly for Polygons wkt file:

$ head -1000 /all_polygons_1K.wkt
$ head -10000 /all_polygons_10K.wkt
$ head -100000 /all_polygons_100K.wkt
```

#### 2. Correcting the format:

We remove single quotes and using tab-spacing for allow easy loading into sedona. To do this, we run:

```
$ python3 pre_process.py
```

### Single node experiments:

  

All the single-node based experiments were done on google colab, the code for which is saved in the folder `/single_node_exps` in the `.ipynb` files.

  
  

### Cluster based experiments:

  

All the cluster based experiments were done on GCP using 4 `n1-standard-4` worker nodes each of size 500 GB and one master node of the same type. Each node runs `2.0.51-ubuntu18`. All the experiments run on the cluster are saved in the folder `/cluster_exps`.

  
  

### Experiments:

  

We divide the experiments based on the type of partition used and the type of indexing used. We first run all experiments on `points` and similarly on `polygons` with increasing size of data.

  

Sedona mainly offers two kinds of partioning algorithms using the following data structures:

- KDB-Tree

- Quad-Tree

  

Additionally, we can index the spatial data using built-in algorithms provided by sedona using the data structures:

- R-Tree

- Quad-Tree

  
  

### Benchmarks:

  

All the benchmarks are kept in the `/benchmarks` folder based on the query type.