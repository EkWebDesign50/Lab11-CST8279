from flask import Flask, render_template
app = Flask(__name__)

import sqlite3
from base64 import b64decode
from webbrowser import open

conn = sqlite3.connect('../Week-10/week10.db')
c = conn.cursor()

link = c.execute('SELECT Link FROM Lab10')
links = [b64decode(row[0]).decode('utf-8') for row in link]
lname = c.execute('SELECT City, country FROM Lab10')
name = [row[0] + ', ' + row[1] for row in lname]
places = [x for x in zip(name,links)]
print([x for x in places][0])

@app.route('/')
def index():
    return render_template('index.html', pairs = places, the_title="Maps")

# your code here
# @app.route('/president/<num>')
# def detail(num):
#     for student in name:
#         if(student['Presidency'] == num):
#             pres_dict = president
#             break
#     return render_template('students.html', pres=link, the_title=pres_dict['President'])
    

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
