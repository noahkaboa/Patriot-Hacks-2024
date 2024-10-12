import requests
from bs4 import BeautifulSoup
import json
from geopy.geocoders import Nominatim
import googlemaps




url = "https://www.fcrevite.org/made-fairfax/directory"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

titles = [x.text for x in soup.find_all('h4')]
descriptions = [x.text for x in soup.find_all('h3')]

output_json = {}
loc = Nominatim(user_agent="GetLoc")


for title, description in zip(titles, descriptions):
    output_json[title] = {
        "description": description
    }
    # location = loc.geocode(title + " Fairfax, VA")
    # output_json[title]["latitude"] = location.latitude
    # output_json[title]["longitude"] = location.longitude

with open('../resources/directory.json', 'w') as f:
    json.dump(output_json, f)