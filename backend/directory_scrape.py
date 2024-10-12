import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import json # built-in

SERP_API_KEY = "38f66aa076de1bc1a5a6df347ce75bfd2c23770e23f9471f9781a793fff36cf4"

def search_location(business_name):
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_maps",
        "q": business_name,
        "api_key": SERP_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(f"{data=}")
    if "place_results" not in data:
        return None
    if "gps_coordinates" not in data["place_results"]:
        return None
    return data["place_results"]["gps_coordinates"]



url = "https://www.fcrevite.org/made-fairfax/directory"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


titles = [x.text for x in soup.find_all('h4')]
descriptions = [x.text for x in soup.find_all('h3')]

output_json = {}

for title, description in zip(titles, descriptions):
    output_json[title] = {
        "description": description
    }


with open('./resources/directory.json', 'w') as f:
    json.dump(output_json, f)

directory = {}
with open('./resources/directory.json', 'r') as f:
    directory = json.load(f)
    for business_name, business_data in directory.items():
        print(f"{business_name=}, {business_data=}")
        if "gps_coordinates" not in business_data.keys() or business_data["gps_coordinates"] == None:
            directory[business_name]["gps_coordinates"] = search_location(business_name)
            print(f"Added gps coordinates for {business_name}")
            print(f"{directory[business_name]=}")

with open('./resources/directory.json', 'w') as f:
    json.dump(directory, f)