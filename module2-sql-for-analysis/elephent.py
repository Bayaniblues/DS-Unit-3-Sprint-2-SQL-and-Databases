import psycopg2

DB_NAME = 'heitayel'
DB_USER = 'heitayel'
DB_PASS = 'RhW5CgSB2xKvKDK41Hu3CFs3srcGJawO'
DB_HOST = 'lallah.db.elephantsql.com'

# connect to elephant sql
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()

#cursor.execute('SELECT * from test_table;')

#results = cursor.fetchall()
#print(results)

### sql lite for RPG data ###

import sqlite3

s1_conn = sqlite3.connect('rpg_db.sqlite3')
s1_cursor = s1_conn.cursor()
characters = s1_cursor.execute('SELECT * FROM charactercreator_character;').fetchall()
print(characters)

### create character table in postgres and insert data

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''

cursor.execute(create_character_table_query)

conn.commit()

for character in characters[0:10]:
    insert_qiery = f"""INSERT"""