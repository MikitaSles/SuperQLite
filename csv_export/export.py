import os
import csv

def export_to_csv(data, headers, filename):
    print("Starting to export data...")
    directory = r"C:\Users\Nik-Asus\Desktop\S.TZ\pythonProject"
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    print(f"Writing data to {filepath}")
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        if data:
            writer.writerows(data)
        else:
            print("No data provided to write!")

