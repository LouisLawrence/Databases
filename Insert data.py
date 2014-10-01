import sqlite3

with sqlite3.connect("coffee_shop.db") as db:
    cursor = db.cursor()
    
    sql = """insert into Product(Name,Price)
          values(?,?)"""
    new_coffee = ("Latte",23.35)
    cursor.execute(sql,new_coffee)
    db.commit
