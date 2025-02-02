import sqlite3
import os

# Ensure the database is stored in the 'databases' folder
DB_PATH = os.path.join(os.path.dirname(__file__), '../databases/klientelys.db')

def create_klientelys_table():
    conn = sqlite3.connect(DB_PATH)  # Save inside databases folder
    cursor = conn.cursor()

    # Create the klientlist table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS klientelys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode TEXT,
            client_name TEXT,
            address_line1 TEXT,
            address_line2 TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_client(kode, client_name, address_line1, address_line2):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO klientelys (kode, client_name, address_line1, address_line2)
        VALUES (?, ?, ?, ?)
    ''', (kode, client_name, address_line1, address_line2))

    conn.commit()
    conn.close()

def print_klientelys():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM klientelys')
    clients = cursor.fetchall()

    for client in clients:
        print(client)

    conn.close()

def delete_client(kode):
    """Deletes a client from the database using their kode."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if the client exists
    cursor.execute("SELECT * FROM klientelys WHERE kode = ?", (kode,))
    client = cursor.fetchone()

    if client:
        cursor.execute("DELETE FROM klientelys WHERE kode = ?", (kode,))
        conn.commit()
        print(f"Client with kode '{kode}' has been deleted.")
    else:
        print(f"No client found with kode '{kode}'.")

    conn.close()