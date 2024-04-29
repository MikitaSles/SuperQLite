import sqlite3
from config import DATABASE_PATH

def query_top_strength():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM superheroes ORDER BY strength DESC LIMIT 5")
    result = cursor.fetchall()
    connection.close()
    return result

def query_tall_strong_heroes():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM superheroes
        JOIN appearance ON superheroes.id = appearance.hero_id
        WHERE appearance.height > 180 AND superheroes.strength > 80
    """)
    result = cursor.fetchall()
    connection.close()
    return result

def query_average_by_gender():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT gender, AVG(intelligence) AS avg_intelligence, AVG(strength) AS avg_strength,
        AVG(speed) AS avg_speed, AVG(power) AS avg_power
        FROM superheroes
        JOIN appearance ON superheroes.id = appearance.hero_id
        GROUP BY gender
    """)
    result = cursor.fetchall()
    connection.close()
    return result
