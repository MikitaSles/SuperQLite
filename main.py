from database.api import populate_database, clear_tables
from data_processing.processing import query_top_strength, query_tall_strong_heroes, query_average_by_gender
from csv_export.export import export_to_csv


def main():
    try:
        print("Clearing tables...")
        clear_tables()
        print("Tables cleared.")

        print("Populating database...")
        populate_database(1, 100)
        print("Database populated.")

        print("Querying top 5 strength...")
        top_5_strength = query_top_strength()
        if top_5_strength:
            print("Top 5 strength data:", top_5_strength)
            export_to_csv(top_5_strength, ['ID', 'Name', 'Intelligence', 'Strength', 'Speed', 'Power'], 'top_5_strength.csv')
        else:
            print("No data to export for top 5 strength.")

        print("Querying tall strong heroes...")
        tall_strong_heroes = query_tall_strong_heroes()
        if tall_strong_heroes:
            print("Tall strong heroes data:", tall_strong_heroes)
            export_to_csv(tall_strong_heroes, ['ID', 'Name', 'Intelligence', 'Strength', 'Speed', 'Power', 'Gender', 'Race', 'Height', 'Weight'], 'tall_strong_heroes.csv')
        else:
            print("No data to export for tall strong heroes.")

        print("Querying average by gender...")
        average_by_gender = query_average_by_gender()
        if average_by_gender:
            print("Average by gender data:", average_by_gender)
            export_to_csv(average_by_gender, ['Gender', 'Avg_Intelligence', 'Avg_Strength', 'Avg_Speed', 'Avg_Power'], 'average_by_gender.csv')
        else:
            print("No data to export for average by gender.")

    except Exception as e:
        print(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()


