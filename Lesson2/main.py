import api

def render(restaurant):
    print('Restaurant Name: {}'.format(restaurant.name))
    print('Restaurant Address: {}'.format(restaurant.address))
    print('Image URL: {}'.format(restaurant.image_url))
    print()

if __name__ == '__main__':
    interests = (
        ('Tokyo, Japan', 'Pizza'),
        ('Jakarta, Indonesia', 'Tacos'),
        ('Maputo, Mozambique', 'Tapas'),
        ('Cairo, Egypt', 'Falafel'),
        ('New Delhi, India', 'Spaghetti'),
        ('Geneva, Switzerland', 'Cappuccino'),
        ('Los Angeles, California', 'Sushi'),
        ('La Paz,  Bolivia', 'Steak'),
        ('Sydney, Australia', 'Gyros'),
    )

    for (address, cusine) in interests:
        restaurant = api.get_top_restaurant(address, cusine)

        render(restaurant)
