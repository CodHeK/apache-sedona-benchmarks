import utils
import psycopg2
from postgis.psycopg import register
import time, pprint
import pandas as pd
from shapely import wkt
import numpy as np

# Edit your postgis server credentials here
db = psycopg2.connect(dbname="benchmark", user="postgres", password="sour punk")
register(db)
cursor = db.cursor()

k_vals = [ 1, 5, 10, 20, 30, 50, 100, 500, 1000 ]

'''
    Points:
'''
coords = [73.512247, 4.083805]

def knn_points(t, k):
    sql = "SELECT * FROM {2} ORDER BY point <-> 'SRID=4326;POINT({0} {1})'::geometry LIMIT {3}".format(coords[0], coords[1], t, k)
    pd.read_sql(sql, db)

t = 'all_points_1K'
len = 1000

output_file = open('knn_points.csv', 'w+')
pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)


pp.pprint("No index")
utils.drop_index(db, cursor, t, 'point')

s = time.time()
for k in k_vals:
    s = time.time()
    knn_points(t, k)
    d = time.time() - s
    pp.pprint(str(k) + "," + str(round(d, 3)))


pp.pprint("R-Tree index")
utils.create_index(db, cursor, t, 'point')

s = time.time()
for k in k_vals:
    s = time.time()
    knn_points(t, k)
    d = time.time() - s
    pp.pprint(str(k) + "," + str(round(d, 3)))



'''
    Polygons:
'''
polygon = open("../sedona_osm_data/knn_polygon.tsv", "r").read()

def knn_polygon(t, k):
    sql = "SELECT * FROM {0} ORDER BY polygon <-> (ST_SetSRID(ST_GeomFromText('{2}'), 4326)) LIMIT {1}".format(t, k, polygon)
    pd.read_sql(sql, db)

t = 'all_source_1K'
len = 1000

output_file = open('knn_polygons.csv', 'w+')
pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)


pp.pprint("No index")
utils.drop_index(db, cursor, t, 'polygon')

s = time.time()
for k in k_vals:
    s = time.time()
    knn_polygon(t, k)
    d = time.time() - s
    pp.pprint(str(k) + "," + str(round(d, 3)))


pp.pprint("R-Tree index")
utils.create_index(db, cursor, t, 'polygon')

s = time.time()
for k in k_vals:
    s = time.time()
    knn_polygon(t, k)
    d = time.time() - s
    pp.pprint(str(k) + "," + str(round(d, 3)))