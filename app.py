from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = 'book_covers.db'


def get_covers():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, filename FROM covers')
    covers = cursor.fetchall()
    conn.close()
    return covers


@app.route('/')
def home():
    covers = get_covers()
    return render_template('index.html', covers=covers)


@app.route('/submit', methods=['POST'])
def submit_ratings():
    # Get the user name
    name = request.form.get('name')
    if not name:
        return "Name is required!", 400

    # Collect ratings from the form
    ratings = {key: value for key, value in request.form.items() if key != 'name'}

    # Debug: Print the collected data
    print(f"Name: {name}")
    print(f"Ratings: {ratings}")

    # Insert data into the database
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        for cover_id, rating in ratings.items():
            if rating:  # Only process non-empty ratings
                cursor.execute(
                    'INSERT INTO ratings (user_name, cover_id, rating) VALUES (?, ?, ?)',
                    (name, cover_id, int(rating))
                )
        conn.commit()
    except Exception as e:
        print(f"Database Error: {e}")
        return "An error occurred while saving data!", 500
    finally:
        conn.close()

    return "Thank you for submitting your ratings!"



if __name__ == '__main__':
    app.run(debug=True)
