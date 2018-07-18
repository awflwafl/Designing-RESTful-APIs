import requests
from query_string import build_query_string
from restaurant import Restaurant

FOURSQUARE_CLIENT_ID = '<FOURSQUARE_CLIENT_ID>'
FOURSQUARE_CLIENT_SECRET = '<FOURSQUARE_CLIENT_SECRET>'
FOURSQUARE_VENUE_ENDPOINT = 'https://api.foursquare.com/v2/venues/search'
FOURSQUARE_API_VERSION = '20180701'

PLACEHOLDER_IMAGE_URL = 'http://via.placeholder.com/300x300'

def format_name(restaurant):
    name = restaurant['name']

    return name

def format_address(restaurant):
    address = ', '.join(restaurant['location']['formattedAddress'])

    return address

def format_image(restaurant):
    categories = restaurant['categories']

    if len(categories) == 0: return PLACEHOLDER_IMAGE_URL

    icon = categories[0]['icon']
    image_url = '{}{}'.format(icon['prefix'], icon['suffix'])

    return image_url

def build_url(geocode, cusine):
    parameters = { 'll': geocode, 'radius': '100000', 'query': cusine, 'intent': 'browse', 'client_id': FOURSQUARE_CLIENT_ID, 'client_secret': FOURSQUARE_CLIENT_SECRET, 'v': FOURSQUARE_API_VERSION, 'limit': '1' }
    query_string = build_query_string(parameters)
    url = '{}?{}'.format(FOURSQUARE_VENUE_ENDPOINT, query_string)

    return url

def format_response(response):
    restaurants = response.json()['response']['venues']

    if len(restaurants) == 0: return None

    restaurant = restaurants[0]

    name = format_name(restaurant)
    address = format_address(restaurant)
    image_url = format_image(restaurant)

    return Restaurant(name, address, image_url)

def get_top_restaurant(geocode, cusine):
    url = build_url(geocode, cusine)
    response = requests.get(url)
    restaurant = format_response(response)

    return restaurant
