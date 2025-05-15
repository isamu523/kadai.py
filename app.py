from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('drill.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS drills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    conn = sqlite3.connect('drill.db')
    c = conn.cursor()
    c.execute('SELECT * FROM drills')
    drills = c.fetchall()
    conn.close()
    return render_template('index.html', drills=drills)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    conn = sqlite3.connect('drill.db')
    c = conn.cursor()
    c.execute('INSERT INTO drills (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
