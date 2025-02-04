import sqlite3

def init_db():
    connection = sqlite3.connect("data.db")  # Create a connection to the database
    cursor = connection.cursor()  # Create a cursor object

    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.executescript('''

    CREATE TABLE IF NOT EXISTS costumer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_num INTEGER NOT NULL,
        location TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS deferred (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cos_name TEXT NOT NULL,
        cos_phone INTEGER NOT NULL,
        cos_location TEXT NOT NULL,
        price INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_mat TEXT NOT NULL,
        count INTEGER NOT NULL,
        type TEXT NOT NULL,
        com_name TEXT NOT NULL,
        buy_price_for_set INTEGER NOT NULL,
        buy_price_for_unit INTEGER NOT NULL,
        sile_price_set INTEGER NOT NULL,
        sel_price INTEGER NOT NULL,
        expiry DATE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount INTEGER NOT NULL,
        date DATE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS bill_detals (
        id INTEGER ,
        mat_name TEXT NOT NULL,
        unit_price INTEGER NOT NULL,
        count INTEGER NOT NULL,
        total_price INTEGER NOT NULL,
        date DATE NOT NULL
    );
''')

    connection.commit()
    connection.close()
    print("Database and tables created successfully.")

init_db()
