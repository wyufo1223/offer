# -*-coding:utf-8-*-
import pymysql

DB_CONFIG = {
	'user': 'root', 
	'password': '',               
	'host': '127.0.0.1',
	#'database': 'joboffer',
	'charset': 'utf8'
}

DB_NAME = 'joboffer'
JOBOFFER = '''
    CREATE TABLE JOBOFFER(
        ID BIGINT PRIMARY KEY NOT NULL,
        salary VARCHAR(100) NOT NULL,
        site VARCHAR(100) NOT NULL,
		site VARCHAR(100) NOT NULL,
		site VARCHAR(100) NOT NULL,
		site VARCHAR(100) NOT NULL,
		site VARCHAR(100) NOT NULL,
        site VARCHAR(100) NOT NULL
    )
'''

conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except pymysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)	



def create_table_joboffer(cursor):
	try:
        cursor.execute("CREATE TABLE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except pymysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


create_database(cursor)



