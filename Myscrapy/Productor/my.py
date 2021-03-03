import pymysql

MYSQL_LOCAL_CONF = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "db": "scrapy"
}


con = pymysql.connect(**MYSQL_LOCAL_CONF)
cursor = con.cursor()
print(cursor)