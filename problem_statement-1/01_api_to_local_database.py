import sqlite3
from pathlib import Path

import requests


API_URL = "https://openlibrary.org/search.json?q=AI+ML"

# Database path relative to script location
BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "books.db"

# fetching the books info
def fetch_books():
    response = requests.get(API_URL , timeout = 10)

    if response.status_code != 200 :
        print("Failed to fetch data from API")
        return []

    data = response.json()

    books = []

    for book in data.get("docs" , [])[:5] :
        title = book.get("title" , "Unknown")
        authors = book.get("author_name" , ["unknown"])
        author  = authors[0] if authors else "Unknown"
        publication_year = book.get("first_publication_year")

        books.append((title , author , publication_year
                      ))

    return books

# creatung database for data storage
def create_database() :
    connection = sqlite3.connect(DATABASE_FILE
                                 )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS BOOKS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT  UNIQUE,
            author TEXT,
            publication_year INTEGER)
    
        """ )

    connection.commit()
    return connection 

def insert_books(connection , books):
    cursor = connection.cursor()

    cursor.executemany("""
    INSERT OR IGNORE INTO BOOKS
    (title,author , publication_year)
    VALUES (?,?,?)
    """ , books)
    connection.commit()

def display_books(connection):
    cursor = connection.cursor()

    cursor.execute("""
    select id , title ,author ,  publication_year
    from BOOKS
    """)

    books = cursor.fetchall()

    print('\nBooks in Database:')

    for book in books:
        print(
            f"ID:{book[0]}|"
            f"Title : {book[1]}|"
            f"Author: {book[2]}|"
            f"publication_year: {book[3]}"
        )

    print(f"Total books: { len(books)}")

def main() :
    books = fetch_books()

    if not books :
        print("Does not fetched any book from API")
        return
    connection = create_database()
    insert_books(connection , books)
    display_books(connection)

    connection.close()

if __name__== "__main__":
    main()