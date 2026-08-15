import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="Tauheed@123",
        database="bank_system"
    )