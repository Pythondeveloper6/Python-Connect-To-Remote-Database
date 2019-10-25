import mysql.connector
from mysql.connector import Error


## infor for connecting
HOST = "  "       ## SERVER IP ADDRESS
PORT =            ## PORT NUMBER
USER = " "        ## DATABASE USERNAME
PASSWORD = "  "   ## DATABASE PASSWORD
DB = "  "         ## DATABASE NAME


try:
    connection = mysql.connector.connect(host=HOST,db=DB,user=USER,port=PORT,passwd=PASSWORD)
    print('connected')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)
except Error as e :
    print ("Error while connecting to MySQL", e)

finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")