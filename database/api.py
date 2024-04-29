import requests
from config import API_KEY, DATABASE_PATH
import sqlite3

def fetch_superhero(id):
    url = f"https://superheroapi.com/api/{API_KEY}/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Data for ID {id}: {data}")
        return data
    else:
        print(f"Failed to fetch superhero with ID {id}: {response.status_code}")
        return None

def validate_data(data):
    necessary_keys = ['id', 'name', 'powerstats', 'appearance']
    for key in necessary_keys:
        if key not in data or data[key] is None or data[key] == 'null':
            print(f"Missing or invalid {key} in data: {data}")
            return False
    return True

def clear_tables():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()


    cursor.execute('DELETE FROM superheroes')


    cursor.execute('DELETE FROM appearance')

    connection.commit()
    connection.close()
    print("Tables have been cleared.")


def parse_height(height):
    if '"' in height:
        parts = height.split("'")
        feet = int(parts[0])
        inches = int(parts[1].replace('"', ''))
        return 12 * feet + inches
    elif height.strip() == '-':
        return None
    else:
        return None

def insert_superhero(data):
    strength = data['powerstats']['strength']
    if strength == 'null':
        strength = 0
    else:
        strength = int(strength)

    if validate_data(data):
        try:
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()


            superhero_data = (
                data['id'], data['name'], int(data['powerstats']['intelligence']),
                strength, int(data['powerstats']['speed']), int(data['powerstats']['power'])
            )
            cursor.execute('INSERT INTO superheroes VALUES (?, ?, ?, ?, ?, ?)', superhero_data)


            height = data['appearance']['height'][1] if isinstance(data['appearance']['height'], list) else data['appearance']['height']
            weight = data['appearance']['weight'][1] if isinstance(data['appearance']['weight'], list) else data['appearance']['weight']
            parsed_height = int(height.split()[0])
            parsed_weight = int(weight.split()[0]) if weight.split()[0].isdigit() else 0

            appearance_data = (
                data['appearance']['gender'], data['appearance']['race'],
                parsed_height, parsed_weight, data['id']
            )
            cursor.execute('INSERT INTO appearance VALUES (NULL, ?, ?, ?, ?, ?)', appearance_data)

            connection.commit()
            print(f"Successfully inserted superhero with ID {data['id']}")
        except Exception as e:
            print(f"An error occurred while inserting superhero with ID {data['id']}: {e}")
        finally:
            connection.close()
    else:
        print(f"Data validation failed for superhero with ID {data['id']}")



def populate_database(start_id, end_id):
    for i in range(start_id, end_id + 1):
        print(f"Fetching superhero with ID: {i}")
        superhero = fetch_superhero(i)
        if superhero:
            print(f"Inserting superhero with ID: {superhero['id']}")
            insert_superhero(superhero)
        else:
            print(f"No data returned for superhero with ID: {i}")

