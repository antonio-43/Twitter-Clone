import psycopg2 as sql

def new_user(username, password):
    
    name = str(username)  # make sure that is a string
    secretword = str(password)  # make sure that is a string

    conn = sql.connect('db.db')
    c = conn.cursor()
    c.execute('INSERT INTO User VALUES (?,?)', (name, secretword))
    conn.commit()
    conn.close()

def pick_user(username, password):

    exist = None
    conn = sql.connect(user = 'fxlnjkqd',
        password = 'hO9EXKi9DXEzZLUupaiKGMN9jqMAzZSA',
        host = '35.246.126.180',
        port = '5432',
        database = 'fxlnjkqd')
    c = conn.cursor()
    c.execute('SELECT * FROM accounts_user WHERE username= %s AND password= %s;', (username, password))  # find username and password
    data = c.fetchall() 
    conn.close()
        
    if len(data) == 1:
        exist = True
    else:
        exist = False

    return exist
    
def login(username, password):

    if pick_user(username, password):
        login = True
    else:
        login = False

    print(f'{username}, {password} --> {login}')

    return login
