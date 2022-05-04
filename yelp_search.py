
import requests
import os 


API_KEY = 
url = "https://api.yelp.com/v3/businesses/search"
HEADER = {'Authorization': 'Bearer %s ' % API_KEY}

# url_params = {
#     'term': "local coffee",
#     'location': 'San Jose',
#     'limit': 20
# }

# res =  requests.get(url, headers=HEADER, params=url_params)
# res = res.json()
# print(res)
#print(res['businesses'][0]['name']) #this will resutn the whole buissness object with 20 buissnesses
# for place in res['businesses']:
#     print(place['name'])

#! Have hardcoded this api request, make sure to change it to the infomations you get back from




def get_results(term, location):

    url_params = {
    'term': f"local {term}",
    'location': location,
    'limit': 20
    }

    res =  requests.get(url, headers=HEADER, params=url_params)
    res = res.json()

    return res