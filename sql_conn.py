import sqlite3


class Database():
    
    
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
    
    
    def __enter__(self):
        return self
    
    
    def __exit__(self, ext_type, exc_value, traceback):
        self.c.close()
        self.conn.commit()
        self.conn.close()
        
        
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS websites
          (title TEXT, url TEXT)''')
        

    def insert(self):
        self.c.execute('''INSERT INTO websites (title, url) VALUES ('google', 'https://www.google.com')''')


    def fetch_all(self):
        
        self.c.execute('SELECT * FROM websites')
        websites = self.c.fetchall()

        return websites


