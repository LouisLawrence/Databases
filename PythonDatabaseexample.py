import sqlite3

#open existing or new database
with sqlite3.connect("store.db") as db:
    #create cursor
    cursor = db.cursor()
    cursor.execute("Select ame from sqlite_master where name=?",(table_name,))
    result = cursor.fetchall()
    if len(result) == 1:
        response = input("The table {0} alread exists, do you wish to recreate it (y/n)?: ".format(table_name))
        if response == "y":
            print("The {0} able wil be recreated - all existing data will e lost".format(table_name))
                         
    cursor.execute("""create table Product(
ProductID integer,
Name text,
Price real,
Primary Key(ProductID))""")
    db.commit() #most important line
