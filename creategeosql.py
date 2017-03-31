import sqlite3
import sys
import csv
from sqlite3 import Error

def connect_db(file):
    try:
        conn = sqlite3.connect(file)
        return conn
    except Error as error:
        print(Error)
        sys.exit(1)


def setup_db():
    dbconn = connect_db('geoip')
    sql_create_table =" CREATE TABLE geoip (id int(10), ipstart varchar(255),ipend varchar(255),lat varchar(255),long varchar(255),country_short varchar(255),country_long varchar(255),PRIMARY KEY( id ));"

    table=dbconn.cursor()
    table.execute(sql_create_table)
    dbconn.close()


def read_record_from_csv():
    with open("GeoIPCountryWhois.csv", "rb") as f:
        reader = csv.


            reader(f, delimiter="\t")
        for i in reader:
            print(row[i][1])

if __name__ == '__main__':
    read_record_from_csv()
    sys.exit(0)
