import utils
import psycopg2
from postgis.psycopg import register
import time, pprint
import pandas as pd

db = psycopg2.connect(dbname="benchmark", user="postgres", password="sour punk")
register(db)
cursor = db.cursor()

envelope = (-85.01, -60.01, 34.01, 50.01)


# '''
#     Points:
# '''
# def range_query_point(t):
#     sql = "SELECT COUNT(*) FROM {0} WHERE ST_Intersects(point, (ST_SetSRID(ST_Envelope('LINESTRING({1} {2}, {3} {4})'::geometry), 4326)))".format(t, *envelope)
#     pd.read_sql(sql, db)


# t = 'all_points_1K'
# len = 1000

# output_file = open('range_points.csv', 'w+')
# pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)


# pp.pprint("No index")
# utils.drop_index(db, cursor, t, 'point')

# s = time.time()
# range_query_point(t)
# d = time.time() - s
# pp.pprint(str(len) + "," + str(round(d, 3)))


# pp.pprint("R-Tree index")
# utils.create_index(db, cursor, t, 'point')

# s = time.time()
# range_query_point(t)
# d = time.time() - s
# pp.pprint(str(len) + "," + str(round(d, 3)))



'''
    Polygons:
'''
def range_query_polygon(t):
    sql = "SELECT * FROM {0} WHERE ST_Intersects(polygon, (ST_SetSRID(ST_Envelope('LINESTRING({1} {2}, {3} {4})'::geometry), 4326)))".format(t, *envelope)
    pd.read_sql(sql, db)


t = 'all_source_100K'
len = 100000

output_file = open('range_polygon.csv', 'w+')
pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)

pp.pprint("No index")
utils.drop_index(db, cursor, t, 'polygon')

s = time.time()
range_query_polygon(t)
d = time.time() - s
pp.pprint(str(len) + "," + str(round(d, 3)))


pp.pprint("R-Tree index")
utils.create_index(db, cursor, t, 'polygon')

s = time.time()
range_query_polygon(t)
d = time.time() - s
pp.pprint(str(len) + "," + str(round(d, 3)))