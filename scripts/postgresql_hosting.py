
from supabase import create_client, Client
from supabase.client import ClientOptions
import os
from dotenv import load_dotenv, dotenv_values 
import csv
import json

os.environ.clear()
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key, options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
    ))

response = supabase.table("nasa_data_treasure_hunt").select("*").execute()
data = response.data
# print(response.data[0].keys())


with open('./data/postgresql/response.csv', 'w', newline='') as csvfile:
    fieldnames = response.data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    
    for row in response.data:
        print("Row:", row) 
        if isinstance(row, dict):  
            writer.writerow(row)
        else:
            print(f"Skipping invalid row: {row}")

    print("Data has been written to response.csv.")
