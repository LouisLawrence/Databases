#1
sql = """select filmID,title,releaseyear where title = ?"""
title = ("Alien",)

#2
sql = """select * from user where userOccupation  = ?"""
occupation = ("technician",)

#3
sql = """select *where userOccupation = ? AND userAge <= ?"""
details = ("technician", 30)

#4
sql = """from
