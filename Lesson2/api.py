import google_api
import foursquare_api

def get_top_restaurant(address, cusine):
    geocode = google_api.get_geocode(address)
    restaurant = foursquare_api.get_top_restaurant(geocode, cusine)

    return restaurant
