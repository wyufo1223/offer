# -*-coding:utf-8-*-
import pymysql

DB_CONFIG = {
	'user': 'root', 
	'password': '',               
	'host': '127.0.0.1',	
	'charset': 'utf8mb4'
}

DB_NAME = 'joboffer'
CREATE_TABLE_JOB = """
	#USE `JOBOFFER`;
    CREATE TABLE IF NOT EXISTS `JOB`(
        `ID` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
        `MONTHLYSALARY` VARCHAR(100),
        `WORKINGPLACE` VARCHAR(100),
		`RELEASEDATE` VARCHAR(100),
		`JOBTYPE` VARCHAR(100),
		`WORKEXPERIENCE` VARCHAR(100),
		`LOWESTDEGREE` VARCHAR(100),
		`RECRUITMENTNUMBER` VARCHAR(100),
		`POSITIONCATEGORY` VARCHAR(100),
		`DEMAND` VARCHAR(10000)
    )ENGINE=INNODB DEFAULT CHARSET=UTF8;
"""

conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except pymysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)	



def create_table_job(cursor):
    cursor.execute(CREATE_TABLE_JOB)
 

conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()
create_database(cursor)

conn = pymysql.connect(database='joboffer', **DB_CONFIG)
cursor = conn.cursor()
create_table_job(cursor)



