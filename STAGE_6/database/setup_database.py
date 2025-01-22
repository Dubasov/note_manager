import sqlite3

def setup_database():
    with sqlite3.connect('nt_mngr_dtbs.db') as conn:
        cursor = conn.cursor()

        cursor.execute(
    '''CREATE TABLE IF NOT EXISTS notes (
        ID              INTEGER PRIMARY KEY AUTOINCREMENT,
        username        TEXT NOT NULL,
        title           TEXT NOT NULL,
        content         TEXT NOT NULL,
        status          TEXT NOT NULL,
        created_date    TEXT NOT NULL,
        issue_date      TEXT NOT NULL
        );''')

        conn.commit()



if __name__ == "__main__":
    setup_database()