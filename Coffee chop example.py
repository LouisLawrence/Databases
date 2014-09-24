import sqlite3

def create_table(db_name,table_name,sql):
    #open existing or new database
    with sqlite3.connect(db_name) as db:
        #create cursor
        cursor = db.cursor()
        cursor.execute("Select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} alread exists, do you wish to recreate it (y/n)?: ".format(table_name))
            if response == "y":
                print("The {0} able wil be recreated - all existing data will e lost".format(table_name))
                cursor.execute("drop table is exists{0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")    
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def get_data():
    db_name = "coffee_shop.db"
    table_name = "coffee_shop"
    sql = """insert into Product(Name,Price)
             values (?,?)"""
    name = input("Enter Name: ")
    price = float(input("Enter Price: "))
    query_values = (name,price)
    
    return db_name,table_name,sql

if __name__ == "__main__":
    db_name,table_name,sql = get_data()
    create_table(db_name,table_name,sql)
    
