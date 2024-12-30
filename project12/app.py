from flask import Flask, render_template, request, redirect, url_for, session, flash
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






































app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        user_id INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS likes_dislikes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        article_id INTEGER,
                        user_id INTEGER,
                        type TEXT CHECK(type IN ('like', 'dislike')),
                        FOREIGN KEY (article_id) REFERENCES articles(id),
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        UNIQUE (article_id, user_id))''')
    
    conn.commit()
    conn.close()

# Home Route
@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

# Blog Route (Display Articles)
@app.route('/blog')
def blog():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT a.id, a.title, a.content, a.created_at, u.username 
                      FROM articles a
                      JOIN users u ON a.user_id = u.id''')
    articles = cursor.fetchall()
    conn.close()
    
    return render_template('blog.html', articles=articles)

# Add Article Route
@app.route('/add-article', methods=['GET', 'POST'])
def add_article():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, user_id) VALUES (?, ?, ?)', 
                       (title, content, user_id))
        conn.commit()
        conn.close()
        
        flash('Article added successfully!', 'success')  # Feedback to the user
        return redirect(url_for('blog'))
    
    return render_template('add_article.html')

# Like/Dislike Article
@app.route('/like-dislike/<article_id>/<action>')
def like_dislike(article_id, action):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Check if the user has already liked/disliked the article
    cursor.execute('SELECT * FROM likes_dislikes WHERE article_id = ? AND user_id = ?', 
                   (article_id, user_id))
    existing = cursor.fetchone()
    
    if existing:
        # Update like/dislike
        cursor.execute('UPDATE likes_dislikes SET type = ? WHERE article_id = ? AND user_id = ?', 
                       (action, article_id, user_id))
    else:
        # Insert new like/dislike
        cursor.execute('INSERT INTO likes_dislikes (article_id, user_id, type) VALUES (?, ?, ?)', 
                       (article_id, user_id, action))
    
    conn.commit()
    conn.close()
    
    flash(f'You have {action}d the article successfully!', 'success')  # Feedback to the user
    return redirect(url_for('blog'))

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                       (username, email, password))
        conn.commit()
        conn.close()
        
        flash('Registration successful. Please log in.', 'success')  # Feedback to the user
        return redirect(url_for('login'))
    
    return render_template('register.html')

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
            flash('Login successful!', 'success')  # Feedback to the user
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'error')  # Feedback to the user
            return redirect(url_for('login'))
    
    return render_template('login.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
