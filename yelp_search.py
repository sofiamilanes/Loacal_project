
from unicodedata import category
import requests
import os 


API_KEY = os.environ['API_KEY']
url = "https://api.yelp.com/v3/businesses/search"
HEADER = {'Authorization': 'Bearer %s ' % API_KEY}

#this function will be called in server on the '/results' with the info they input

def get_results(term, location):

    url_params = {
    'term': f"locally {term}",
    'location': location,
    'limit': 15,
    # 'radius': 35000
    }

    res =  requests.get(url, headers=HEADER, params=url_params)
    res = res.json()

    return res

def search_by_id(id):
    id_url = f"https://api.yelp.com/v3/businesses/{id}"

    res = requests.get(id_url, headers= HEADER )
    res = res.json()

    return res

# for place in res['businesses']:
#     print(place['name'])

# AIzaSyA3IF29yT9xLhavg3w6jOW8mP33CChEi1Q