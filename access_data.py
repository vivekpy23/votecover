import sqlite3

# Connect to the database
conn = sqlite3.connect('book_covers.db')
cursor = conn.cursor()

# Query data from the covers table
# cursor.execute('SELECT * FROM covers')
# covers = cursor.fetchall()
# print("Covers Table:")
# for row in covers:
#     print(row)

# Query data from the ratings table
cursor.execute('select * from ratings')
ratings = cursor.fetchall()
print("\nRatings Table:")
for row in ratings:
    print(row)

# Close the connection
conn.close()


