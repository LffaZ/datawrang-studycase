import requests
import json
import csv
import os
from dotenv import load_dotenv, dotenv_values 
import http.client

url = "https://api.x.com/2/tweets/search/recent"

os.environ.clear()
load_dotenv()
headers = {"Authorization": f"Bearer {os.getenv("BEARER_TOKEN")}"}

twt = ["author_id","id","attachments","created_at","source","text"]
media = ["url","preview_image_url","type"]
place = ["country","country_code","full_name","place_type"]
user = ["verified","username","name","protected","location"]
query = "techbros"

querystring = {"tweet.fields":twt,
               "query":query,
               "user.fields":user,
               "place.fields":place,
               "media.fields":media,
               "max_results":"100",
               "sort_order":"recency"}

try: 
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code != 200:
        description = http.client.responses.get(response.status_code, "Unknown Status Code")
        print(f"Fetch from API failed. Status Code {response.status_code}: {description}")
    else:
        try:
            data = response.json().get('data', [])

            with open('./data/api_x_data/response.csv', 'w', newline='') as csvfile:
                fieldnames = twt + user + place + media
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_MINIMAL)

                writer.writeheader()
                
                for row in data:
                    print("Row:", row) 
                    if isinstance(row, dict):  
                        writer.writerow(row)
                    else:
                        print(f"Skipping invalid row: {row}")

                print("Data has been written to response.csv.")
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

except requests.exceptions.RequestException as e:
    print("An error occurred: ", e)