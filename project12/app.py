from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Home Route
@app.route('/')
def home1():
    if 'user_id' in session:
        return render_template('home.html', message="You have successfully logged in!")
    return redirect(url_for('login'))

@app.route('/home.html')
def home2():
    if 'user_id' in session:
        return render_template('home.html', message="You have successfully logged in!")
    return redirect(url_for('login'))

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('login.html')

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/adopt.html', methods=['GET', 'POST'])
def adopt():
    return render_template("adopt.html")

@app.route('/blog.html', methods=['GET', 'POST'])
def blog():
    return render_template("blog.html")

@app.route('/get-involved.html', methods=['GET', 'POST'])
def get_involved():
    return render_template("get-involved.html")

@app.route('/about-us.html', methods=['GET', 'POST'])
def about_us():
    return render_template("about-us.html")

@app.route('/contact-us.html', methods=['GET', 'POST'])
def contact_us():
    return render_template("contact-us.html")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
