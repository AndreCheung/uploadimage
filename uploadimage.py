#! python3
# uploadimage.py - upload image via HTTP Post
# Last update: 20230801
# Author: Andre Cheung
# Organizaton: RoboticsCats.com
import requests

# upload image to LookOut via HTTP Post
def upload_image(url, image_path):
    try:
        # Open the image file in binary mode and read its contents
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            
        image_file.close()

        # Set the headers for the HTTP POST request
        headers = {
            'Content-Type': 'image/jpeg'  # Set the correct content type for JPEG images
        }

        # Make the HTTP POST request with the image data
        response = requests.post(url, headers=headers, data=image_data)
        return response

    except Exception as e:
        print(f"Error: {e}")
        return response
