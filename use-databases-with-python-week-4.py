import json
import sqlite3

conn = sqlite3.connect("use-database-with-python-week-4.sqlite")
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    
    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    );
    CREATE TABLE Member (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        role TEXT NOT NULL
    );
''')

data = json.loads(open("roster_data.json", "r").read())
for item in data:
    print(item[0], item[1], item[2])
    cur.execute("INSERT OR IGNORE INTO User (name) VALUES ( ? )", (item[0],))
    cur.execute("SELECT id FROM User WHERE name = ? ", (item[0],))
    user_id = cur.fetchone()[0]

    cur.execute(
        "INSERT OR IGNORE INTO Course (title) VALUES ( ? )", (item[1],))
    cur.execute("SELECT id FROM Course WHERE title = ? ", (item[1],))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role) 
    VALUES ( ?, ?, ? )
    ''', (user_id, course_id, item[2]))
conn.commit()

cur.execute('''
    SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
''')
for item in cur.fetchall():
    print(item)

cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
''')
print(cur.fetchone())
