import sqlite3


class Database():
    
    
    def __init__(self):
        self.conn = None
        self.c = None
    
    def connect(self):
        try:
            self.conn = sqlite3.connect('data.db')
            self.c = self.conn.cursor()
            print("CONNECTED TO DATABASE")
        except sqlite3.Error as error:
            print(error)
            
    
    def close(self):
        self.c.close()
        self.conn.commit()
        self.conn.close()
        print("DB CLOSED")
        
        
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS websites
          (title TEXT UNIQUE, url TEXT)''')
        

    def insert(self):
        self.c.execute('''INSERT OR REPLACE INTO websites (title, url) VALUES 
                       ('google', 'https://www.google.com'),
                       ('yandex', 'https://www.yandex.ru'),
                       ('microsoft', 'https://www.microsoft.com')''')


    def fetch_all(self) -> list:
        
        self.c.execute('SELECT * FROM websites')
        websites = self.c.fetchall()

        return websites


