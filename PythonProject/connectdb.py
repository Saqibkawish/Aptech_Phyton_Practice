# pip install mysql-connector-python
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_db"
)

query_chalao = con.cursor()

name = input("Enter Your Name : ")
price = input("Enter price  : ")
category = input("Enter category name : ")
brand = input("Enter brand name : ")

insert = "insert into my_db(name, price, category, brand) values (%s, %s, %s, %s)"
v = (name, price, category, brand)

query_chalao.execute(insert, v)
con.commit()
con.close()

print(f"{name} record has been saved successfully")
