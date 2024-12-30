import sqlite3
import os

# Paths
DATABASE = 'book_covers.db'
COVERS_FOLDER = 'static/covers'


# Initialize the database
def initialize_database():
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Truncate (clear) the existing tables
    cursor.execute('DELETE FROM covers')
    cursor.execute('DELETE FROM ratings')

    # Reset the auto-increment counters
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="covers"')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="ratings"')

    # Insert files from the covers folder into the covers table
    files = [f for f in os.listdir(COVERS_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg'))]
    for file in files:
        cursor.execute('INSERT INTO covers (filename) VALUES (?)', (file,))

    conn.commit()
    conn.close()
    print("Database truncated and updated with new cover files.")


if __name__ == '__main__':
    initialize_database()
