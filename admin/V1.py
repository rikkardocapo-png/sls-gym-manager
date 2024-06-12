import schedule
import datetime as datetime
import V1_Lib as lib
import mysql.connector as mysql
import time

current_date = datetime.datetime.now().strftime("%Y_%m_%d")

connection = mysql.connect(
    host="127.0.0.1",
    port="8888",
    user="system_updater_mod",
    password="",
    database="IA_User-data"
)
cursor = connection.cursor()
"""
while True:
    time.sleep(600)
    if current_date != datetime.datetime.now().strftime("%Y_%m_%d"):
        current_date = datetime.datetime.now().strftime("%Y_%m_%d")
        cursor.execute()
        """






