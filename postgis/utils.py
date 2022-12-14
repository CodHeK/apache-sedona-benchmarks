import psycopg2
from postgis import Point, Polygon
from postgis.psycopg import register
from shapely import wkt
import pandas as pd


def load_points(db, cursor, data_path, table):
    sql = 'CREATE TABLE IF NOT EXISTS {0} ("point" geometry(Point) NOT NULL)'.format(table)
    cursor.execute(sql)
    f = open(data_path, 'r')

    for line in f:
        shape = line.split('\t')[1]
        point = wkt.loads(shape)
        sql = "INSERT INTO {0} (point) VALUES (ST_SetSRID(ST_MakePoint({1}, {2}), 4326))".format(table, point.x, point.y)
        cursor.execute(sql)
        db.commit()

    row_count = pd.read_sql('SELECT COUNT(point) FROM ' + table, db)
    print(row_count)


def load_polygons(db, cursor, data_path, table):
    sql = 'CREATE TABLE IF NOT EXISTS {0} ("polygon" geometry(Polygon) NOT NULL)'.format(table)
    cursor.execute(sql)
    f = open(data_path, 'r')

    for line in f:
        polygon = line.split('\t')[1]
        sql = "INSERT INTO {0} (polygon) VALUES (ST_SetSRID(ST_GeomFromText('{1}'), 4326))".format(table, polygon)
        cursor.execute(sql)
        db.commit()

    row_count = pd.read_sql('SELECT COUNT(polygon) FROM ' + table, db)
    print(row_count)


def delete_table(db, cursor, table):
    sql = 'DROP TABLE {0}'.format(table)
    cursor.execute(sql)
    db.commit()


def view(db, table, rows):
    rows = pd.read_sql('SELECT * FROM ' + table + ' LIMIT ' + str(rows), db)
    print(rows)


def create_index(db, cursor, table, column):
    # CREATE INDEX name ON table USING gist(column);
    sql = 'CREATE INDEX {1}_{0}_idx ON {1} USING GIST({0})'.format(column, table)
    cursor.execute(sql)
    db.commit()


def drop_index(db, cursor, table, column):
    sql = 'DROP INDEX IF EXISTS {1}_{0}_idx'.format(column, table)
    cursor.execute(sql)
    db.commit()
