import requests
import json

def recognize_vegetables(image_url):
    # Open Food Facts API endpoint for product recognition
    api_url = "https://world.openfoodfacts.org/cgi/product_name_search.pl"

    # Set up the parameters for the API request
    params = {
        'search_terms': '',
        'imgurl': image_url,
        'json': 1,
    }

    # Make the API request
    response = requests.get(api_url, params=params)
    data = response.json()

    # Extract vegetable names from the API response
    vegetable_names = []

    if 'products' in data:
        for product in data['products']:
            if 'product_name' in product:
              vegetable_names.append(product['product_name'])

    return vegetable_names


    