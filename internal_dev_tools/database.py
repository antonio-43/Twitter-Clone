import psycopg2
import sys

banner = """


+--------------------+
|  DATABASE MANAGER  |
+--------------------+

+------------------+
|   CHECK TABLES   |
|------------------|
|DELETE ALL TABLES |
|------------------|
|       INFO       |
+------------------+

#GooglePlzHireMe


"""
    
try:
    conn = psycopg2.connect(
        user = 'fxlnjkqd',
        password = 'hO9EXKi9DXEzZLUupaiKGMN9jqMAzZSA',
        host = '35.246.126.180',
        port = '5432',
        database = 'fxlnjkqd')
    print(banner)
except:
    print('[DATABASE]: CONNECTION ERROR!')

cur = conn.cursor()

print('[SELECT] :  CHOSE ONE')

while True:
    move = str(input('[SELECT] $  '))

    if move == 'CHECK TABLES':
        print('[DATABASE] :  TABLE NAME:')
        table_name = str(input('[DATABASE] :  $'))
        query = f'SELECT * FROM {table_name};'
        cur.execute(query)
        query_response = cur.fetcall()
        print(query_response)
    elif move == 'INFO':
        info = """
        
        DATABASE MANAGER
        ----------------

        DATABASE MANAGER IS A INTERNAL DEV TOOL FOR TAKE A LOOK INTO
        THE DATA BASE.

        THIS CONNECTS FOR THIS SERVICE:

        https://www.elephantsql.com/

        """
        print(info)
    elif move == 'DELETE ALL TABLES':
        print('[DATABASE] :  TABLE NAME:')
        table_name = str(input('[DATABASE] :  $'))
        query = f'DROP TABLE {table_name};'
        cur.execute(query)
    else:
        print('[DATABASE MANAGER] :  SCHOSE ONE')
        move = str(input('[SELECT] $  '))
