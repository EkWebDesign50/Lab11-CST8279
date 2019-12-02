import sqlite3
from base64 import b64decode
from webbrowser import open

conn = sqlite3.connect('../Week-10/week10.db')
c = conn.cursor()

link = c.execute('SELECT Link FROM Lab10')
links = [b64decode(row[0]).decode('utf-8') for row in link]
lname = c.execute('SELECT City, country FROM Lab10')
name = [row[0] + ', ' + row[1] for row in lname]
places = dict(zip(name,links))
print(places['Gujarat, India'])