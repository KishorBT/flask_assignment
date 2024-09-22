# Flask User Management Application

## Documentation

### Overview
This is a Flask web application that allows users to manage user information stored in a MySQL database. The application includes features for displaying users, adding new users, and viewing user details.

### Setup and Running the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KishorBT/flask_assignment.git
   cd flask_assignment

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv\Scripts\activate
    ```
3. **Install Required Python Libraries:**
   ```bash
   pip install Flask mysql-connector-python python-dotenv
   ```
4. **Create a .env file:** Create a file named .env in the root directory of your project and add the following content:
   ```bash
   DB_HOST=localhost
   DB_USER=root  
   DB_PASSWORD=your_password 
   DB_NAME=users
   ```
 5. Set up the MySQL database:

     (i)Log in to your MySQL server and create a new database named users.
     ```
     CREATE DATABASE users;
    USE users;
     ```
     (ii)Run the following SQL commands to create the users table:
    ```bash
    CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(255)
    );
    ```
    
 7. Run the application:
    ```
    python app.py
    ```
 ### SQL Query

 1. To insert sample data into the users table, use the following SQL commands:
    ```
    INSERT INTO users (name, email, role) VALUES ('Kishor Bhushan', 'kishor@example.com', 'Admin');
    INSERT INTO users (name, email, role) VALUES ('Hemant Kumar', 'Hemant@example.com', 'User');
    INSERT INTO users (name, email, role) VALUES ('Mukesh Kumar', 'mukesh@example.com', 'user');
    INSERT INTO users (name, email, role) VALUES ('Rahul Singh', 'rahul@example.com', 'user');
    INSERT INTO users (name, email, role) VALUES ('Aryan Soni', 'aryan@example.com', 'user');
    ```
 2. To Retrieve all users from the "users" table.
    ```
    SELECT * FROM users;
    ```
 3. To Retrieve a specific user by their ID.
    ```
    SELECT * FROM users WHERE id = 1;
    ```
    This will display details of user whose id = 1. 
    

 

   
     
   
