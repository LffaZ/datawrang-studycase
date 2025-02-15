import json
import csv
import requests
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
print(os.getenv("BEARER_TOKEN"))

url = "http://localhost:8080/"

# # response = requests.request("GET", url, )
result = requests.get(url, timeout=2.50, verify=False)

responsejson = result.json()

if 'data' in responsejson:
    data = responsejson['data']
else:
    print("No 'data' key found in the response.")
    data = []

with open('response.csv', 'w', newline='') as csvfile:
    fieldnames = ['author_id', 'created_at', 'id', 'text', 'username']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writeheader()
    
    for row in data:
        print("Row:", row)  # Print the current row to check its structure
        if isinstance(row, dict):  # Ensure the row is a dictionary
            writer.writerow(row)
        else:
            print(f"Skipping invalid row: {row}")

print("Data has been written to response.csv.")