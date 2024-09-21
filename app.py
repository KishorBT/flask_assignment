
import os
from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

# Database connection
def get_db_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def home():
    return render_template('home.html')

# Route to display Hello World
@app.route('/hello')
def hello():
    return "Hello World!"

# Route to retrieve and display all users
@app.route('/users')
def show_users():
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return render_template('users.html', users=users)
    except Error as e:
        return f"Error fetching users: {e}", 500
    finally:
        conn.close()

# Route to render the form to add a new user
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        conn = get_db_connection()
        if conn is None:
            return "Database connection failed", 500
        
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
            conn.commit()
            return redirect('/users')
        except Error as e:
            return f"Error adding user: {e}", 500
        finally:
            conn.close()
    
    return render_template('new_user.html')

# Route to retrieve a specific user's details
@app.route('/users/<int:id>')
def get_user(id):
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
        if user:
            return render_template('user.html', user=user)
        else:
            return "User not found", 404
    except Error as e:
        return f"Error fetching user: {e}", 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
