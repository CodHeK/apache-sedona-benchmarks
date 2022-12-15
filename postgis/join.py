import utils
import psycopg2
from postgis.psycopg import register
import time, pprint
import pandas as pd

db = psycopg2.connect(dbname="benchmark", user="postgres", password="sour punk")
register(db)
cursor = db.cursor()

def join(t1, t2):
    sql = 'SELECT * FROM {0} as points_table JOIN {1} as polygon_table ON ST_Contains(polygon_table.polygon, points_table.point)'.format(t1, t2)
    pd.read_sql(sql, db)


t1 = 'all_points_1K'
t2 = 'all_source_100K'
len = 10000

output_file = open('join.csv', 'w+')
pp = pprint.PrettyPrinter(indent=4, compact=True, stream=output_file)


pp.pprint("No index")
utils.drop_index(db, cursor, t1, 'point')
utils.drop_index(db, cursor, t2, 'polygon')

s = time.time()
join(t1, t2)
d = time.time() - s
pp.pprint("'" + str(len) + "," + str(round(d, 3)) + "'")


pp.pprint("R-Tree index")
utils.create_index(db, cursor, t1, 'point')
utils.create_index(db, cursor, t2, 'polygon')

s = time.time()
join(t1, t2)
d = time.time() - s
pp.pprint("'" + str(len) + "," + str(round(d, 3)) + "'")