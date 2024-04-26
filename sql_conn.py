import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS websites
          (title TEXT, url TEXT)''')

c.execute('''INSERT INTO websites (title, url) VALUES ('google', 'https://www.google.com')''')

conn.commit()

c.execute('SELECT * FROM websites')
websites = c.fetchall()

for website in websites:
    print(website)


conn.close()