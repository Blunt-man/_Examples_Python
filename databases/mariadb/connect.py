import mariadb
dbuser = "db_admin"
dbpassword = "password"
dbhost = "hostName"
dbport = 3306
dbdatabase = "db_name"

try:
    conn = mariadb.connect(
        user=dbuser,
        password=dbpassword,
        host=dbhost,
        port=dbport,
        database=dbdatabase
    )
except mariadb.Error as e:
    print('Error connecting to MariaDB Platform:', e)

cur = conn.cursor()                     # get Cursor

cur.execute("SHOW TABLES")
for (Tables_in_Main_Box_DB) in cur:
    print ( Tables_in_Main_Box_DB[0] )