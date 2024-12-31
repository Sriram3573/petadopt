from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import bcrypt  # Import bcrypt

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
        user_id = session['user_id']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM users WHERE id=?', (user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            username = user[0]
            return render_template('home.html', username=username, message="You have successfully logged in!")
    
    return redirect(url_for('login'))

@app.route('/home')
def home2():
    if 'user_id' in session:
        return render_template('home.html', message="You have successfully logged in!")
    return redirect(url_for('login'))

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')  # Encode password to bytes
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password, user[3].encode('utf-8')):  # Verify hashed password
            session['user_id'] = user[0]
            return redirect(url_for('home1'))
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('login.html')

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())  # Hash password

        # Check if the email already exists in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        existing_user = cursor.fetchone()
        conn.close()

        if existing_user:
            # Email already exists, display error message
            return render_template('register.html', error="This email is already registered. Please use a different email.")
        
        # If email does not exist, proceed with registration
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password.decode('utf-8')))
        conn.commit()
        conn.close()

        return redirect(url_for('home1'))

    return render_template('register.html')

@app.route('/adopt', methods=['GET', 'POST'])
def adopt():
    return render_template("adopt.html")

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template("blog.html")

@app.route('/get-involved', methods=['GET', 'POST'])
def get_involved():
    return render_template("get-involved.html")

@app.route('/about-us', methods=['GET', 'POST'])
def about_us():
    return render_template("about-us.html")

@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    return render_template("contact-us.html")

@app.route('/popup.html', methods=['GET', 'POST'])
def popup():
    return render_template("popup.html")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
