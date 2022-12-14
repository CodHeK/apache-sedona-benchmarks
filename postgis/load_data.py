import utils
import psycopg2
from postgis.psycopg import register

db = psycopg2.connect(dbname="benchmark", user="postgres", password="sour punk")
register(db)
cursor = db.cursor()

data_path = '../sedona_osm_data/all_points_1K.wkt'
table = 'all_points_1K'
column = 'point'

# utils.delete_table(db, cursor, table)
# utils.load_points(db, cursor, data_path, table)
# utils.view(db, table, 5)

data_path = '../sedona_osm_data/all_points_10K.wkt'
table = 'all_points_10K'
column = 'point'

# utils.delete_table(db, cursor, table)
# utils.load_points(db, cursor, data_path, table)
# utils.view(db, table, 5)


data_path = '../sedona_osm_data/all_source_1K.wkt'
table = 'all_source_1K'
column = 'polygon'

# utils.delete_table(db, cursor, table)
# utils.load_polygons(db, cursor, data_path, table)
# utils.view(db, table, 2)

data_path = '../sedona_osm_data/all_source_10K.wkt'
table = 'all_source_10K'
column = 'polygon'

# utils.delete_table(db, cursor, table)
# utils.load_polygons(db, cursor, data_path, table)
# utils.view(db, table, 2)