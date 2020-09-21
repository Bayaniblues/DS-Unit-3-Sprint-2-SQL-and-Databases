import sqlite3
import psycopg2
import pandas as pd

#read in csv
df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'"," ")

df.info()

#create sqlite3
conn = sqlite3.connect('titanic.sqlite3')
#create cursor
curs = conn.cursor()
#convert to sql
df.to_sql('titanic', conn)

#pulling out data from the sql base we just made
get_titanic = 'SELECT * FROM titanic;'
passangers = curs.execute(get_titanic).fetchall()


DB_NAME = 'heitayel'
DB_USER = 'heitayel'
DB_PASS = 'RhW5CgSB2xKvKDK41Hu3CFs3srcGJawO'
DB_HOST = 'lallah.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                           password=DB_PASS, host=DB_HOST)

create_table_statement = """
CREATE TABLE titanic1 ( 
    id SERIAL PRIMARY KEY, 
    Survived INTEGER,
    pclass INTEGER,
    name VARCHAR (140),
    sex VARCHAR (10),
    age FLOAT(1),
    siblings_spouses_aboard INTEGER, 
    parents_children_aboard INTEGER,
    fare FLOAT(4) 
);
"""
#CREATE NEW CURSOR
pg_curs = pg_conn.cursor()

#EXECUTE
pg_curs.execute(create_table_statement)

for x in passangers:
    insert_passanger = """
    INSERT INTO titanic1 
    (Survived, Pclass, Name, Sex, Age, 
    Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES """ + str(x[1:]) + ";"
    pg_curs.execute(insert_passanger)


pg_conn.commit()