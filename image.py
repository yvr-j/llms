from clarifai.rest import ClarifaiApp

def recognize_vegetables(api_key, image_url):
    # Initialize the Clarifai application
    app = ClarifaiApp(api_key=api_key)

    # Use the general model for image recognition
    model = app.public_models.general_model

    # Predict concepts (vegetable names) in the image
    response = model.predict_by_url(url=image_url)

    # Extract vegetable names from the response
    vegetable_names = [concept['name'] for concept in response['outputs'][0]['data']['concepts']]

    return vegetable_names

if __name__ == "__main__":
    # Replace 'YOUR_CLARIFAI_API_KEY' with your actual Clarifai API key
    clarifai_api_key = "980acfdaf3f8428189c2a31c9cb00fba"
    
    # Replace 'URL_OF_YOUR_IMAGE' with the actual URL of your image
    image_url = 'https://tse2.mm.bing.net/th?id=OIP.TolZQyNqeb6l4n0CCAEaewHaE9&pid=Api&P=0&h=180'

    vegetable_names = recognize_vegetables(clarifai_api_key, image_url)

    if vegetable_names:

        print("Recognized vegetables in the image:")
        for veg in vegetable_names:
            print("-", veg)
    else:
        print("No vegetables recognized in the image.")
