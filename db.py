import sqlite3

# This module handles the SQLite database operations for storing and retrieving encrypted messages.
# Ensure the database and table are initialized
def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encrypted TEXT NOT NULL,
            `key` TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Save an encrypted message and its key to the database
# param encrypted: The encrypted message
# param key: The key used for encryption
def save_message(encrypted, key):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (encrypted, `key`) VALUES (?, ?)", (encrypted, key))
    conn.commit()
    conn.close()

# Retrieve all messages from the database
# param: None
# return: A list of tuples containing message ID, encrypted message, and key
def get_all_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, encrypted, `key` FROM messages")
    rows = cursor.fetchall()
    conn.close()
    return rows
