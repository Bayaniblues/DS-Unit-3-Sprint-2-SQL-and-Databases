import sqlite3


def chinook_db():
    conn = sqlite3.connect('chinook.db')
    cursor = conn.cursor()
    return cursor


def new_db():
    # make new database
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()
    return cursor


def rpg_db():
    # make new database
    conn = sqlite3.connect('rpg_db.sqlite3')
    cursor = conn.cursor()
    return cursor




def total_chars():
    conn = sqlite3.connect('rpg_db.sqlite3')
    cursor = conn.cursor()
    query = '''
    SELECT
        character_id,
        name
    FROM 
        charactercreator_character
    '''
    result = cursor.execute(query).fetchall()
    total = str(len(result)) + " " + "total characters"
    return total


def total_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    cursor = conn.cursor()
    query = '''
    SELECT
        *
    FROM 
        armory_item
    '''
    result = cursor.execute(query).fetchall()
    total = len(result)
    return str(total) + " " + "total items"


def total_weapons():
    conn = sqlite3.connect('rpg_db.sqlite3')
    cursor = conn.cursor()
    query = '''
    SELECT
        *
    FROM 
        armory_weapon
    '''

    total = cursor.execute(query).fetchall()
    return str(len(total)) + " " + "total weapons"


def total_not_weapons():
    conn = sqlite3.connect('rpg_db.sqlite3')
    cursor = conn.cursor()
    query = '''
    SELECT item_id FROM armory_item
    EXCEPT 
    SELECT item_ptr_id FROM armory_weapon
    '''

    total = cursor.execute(query).fetchall()
    return str(len(total)) + " " + "total not Weapons"


def total_character_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    cursor = conn.cursor()
    query = '''
    SELECT item_id FROM armory_item
    EXCEPT 
    SELECT item_ptr_id FROM armory_weapon
    '''

    total = cursor.execute(query).fetchall()
    return str(len(total)) + " " + "total not Weapons"

if __name__ == '__main__':
    print(total_chars())
    print(total_items())
    print(total_weapons())
    print(total_not_weapons())

