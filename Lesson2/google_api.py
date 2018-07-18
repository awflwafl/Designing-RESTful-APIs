import requests
from query_string import build_query_string

GOOGLE_API_KEY = '<GOOGLE_API_KEY>'
GOOGLE_API_GEOCODE_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'

def build_url(address):
    parameters = { 'key': GOOGLE_API_KEY, 'address': address }
    query_string = build_query_string(parameters)
    url = '{}?{}'.format(GOOGLE_API_GEOCODE_ENDPOINT, query_string)

    return url

def format_response(response):
    location = response.json()['results'][0]['geometry']['location']
    geocode = '{},{}'.format(location['lat'], location['lng'])

    return geocode

def get_geocode(address):
    url = build_url(address)
    response = requests.get(url)
    geocode = format_response(response)

    return geocode
