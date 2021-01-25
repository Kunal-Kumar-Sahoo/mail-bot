import mysql.connector #pip install mysql-connector-python

client = mysql.connector.connect(host="localhost", user="root")
mycursor = client.cursor()

def create_database_and_table(database_name, table_name, schema):
    try:
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        mycursor.execute(f"USE {database_name}")
        mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({schema})")
    except Exception as e:
        print(e)

def insertData(database_name, table_name, name, email):
    try:
        mycursor.execute(f"USE {database_name} ")
        mycursor.execute(f"INSERT INTO {table_name} VALUES(%s, %s)",(name, email))
        client.commit()
    except Exception as e:
        print(e)

def readData(database_name, table_name):
    try:
        mycursor.execute(f"USE {database_name}")
        mycursor.execute(f"SELECT * FROM {table_name}")
        tuples = mycursor.fetchall()
        return tuples
    except Exception as e:
        print(e)

