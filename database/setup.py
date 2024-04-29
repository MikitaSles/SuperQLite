import sqlite3

def create_database():
    connection = sqlite3.connect(r'C:\Users\Nik-Asus\Desktop\S.TZ\pythonProject\database\superheroes.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS superheroes (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        intelligence INTEGER,
                        strength INTEGER,
                        speed INTEGER,
                        power INTEGER
                   )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS appearance (
                        id INTEGER PRIMARY KEY,
                        gender TEXT,
                        race TEXT,
                        height INTEGER,
                        weight INTEGER,
                        hero_id INTEGER,
                        FOREIGN KEY(hero_id) REFERENCES superheroes(id)
                    )''')


    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()