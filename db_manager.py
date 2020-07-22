import sqlite3 as sql

print(
"""


+--------------------+
|  DATABASE MANAGER  |
+--------------------+

+-----------------+
|  DELETE TABLES  |
+-----------------+

#GooglePlzHireMe
#ICodeInTwoLangs
#CHN

"""
)

"""
manager of database
"""

table_name = str(input('[DATABASE MANAGER] TABLE NAME:  '))

query = f'DROP TABLE {table_name}';

conn = sql.connect('database.db')
c = conn.cursor()
c.execute(query)
conn.commit()
conn.close()

