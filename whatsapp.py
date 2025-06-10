import sqlite3
import os
import shutil

def extract_chat_history(db_file):
    # Make a copy of the database file to avoid modifying the original
    db_copy = db_file + '_copy'
    shutil.copy(db_file, db_copy)

    # Connect to the copied database
    conn = sqlite3.connect(db_copy)
    cursor = conn.cursor()

    # Get the chat history
    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()

    # Print the chat history
    for row in rows:
        print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")

    # Close the connection and remove the copied database
    conn.close()
    os.remove(db_copy)

# Replace 'path/to/your/whatsapp.db' with the actual path to your WhatsApp database file
extract_chat_history('/data/data/com.whatsapp/databases/')