import sqlite3
import hashlib

def hash_password(password):
    # Create a new sha256 hash object
    hasher = hashlib.sha256()
    # Update the hash object with the bytes of the string, providing the password
    hasher.update(password.encode('utf-8'))
    # Return the hexadecimal digest of the hash
    return hasher.hexdigest()

def create_db():
    conn = sqlite3.connect("ResultManagementSystem.db")
    cur = conn.cursor()

    # Table Creation for Course
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course(
            cid INTEGER PRIMARY KEY,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)

    # Table Creation for Student
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            roll INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT,
            course TEXT,
            state TEXT,
            city TEXT,
            address TEXT
        )
    """)

    # Table Creation for Result
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result(
            rid INTEGER PRIMARY KEY,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_obtain TEXT,
            full_marks TEXT,
            percentage TEXT
        )
    """)

    # Table Creation for Users
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Table Creation for AllUsers (Extended User Details)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS AllUsers(
            eid INTEGER PRIMARY KEY,
            f_name TEXT,
            l_name TEXT,
            contact TEXT,
            email TEXT,
            question TEXT,
            answer TEXT,
            password TEXT,
            u_name TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()

create_db()
