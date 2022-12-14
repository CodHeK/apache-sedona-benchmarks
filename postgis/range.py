import utils
import psycopg2
from postgis.psycopg import register
import time, pprint
import pandas as pd

db = psycopg2.connect(dbname="benchmark", user="postgres", password="sour punk")
register(db)
cursor = db.cursor()

envelope = (-85.01, -60.01, 34.01, 50.01)

def range_query(t):
    sql = "SELECT COUNT(*) FROM {0} WHERE ST_Intersects(point, (ST_SetSRID(ST_Envelope('LINESTRING({1} {2}, {3} {4})'::geometry), 4326)))".format(t, *envelope)
    pd.read_sql(sql, db)


t = 'all_points_1K'
len = 1000

output_file = open('range.csv', 'w+')
pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)


pp.pprint("No index")
utils.drop_index(db, cursor, t, 'point')

s = time.time()
range_query(t)
d = time.time() - s
pp.pprint(str(len) + "," + str(round(d, 3)))


pp.pprint("R-Tree index")
utils.create_index(db, cursor, t, 'point')

s = time.time()
range_query(t)
d = time.time() - s
pp.pprint(str(len) + "," + str(round(d, 3)))