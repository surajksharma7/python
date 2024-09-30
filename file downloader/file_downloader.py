import requests
import os

def download_file(url, file_name):
    # Generate extension from URL
    file_name = f"{file_name}.{url.split('.')[-1].lower()}"
    
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a local file in binary write mode and save the content
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File '{file_name}' downloaded successfully.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = 'https://www.python.org/static/img/psf-logo.png'
    file_name = 'file'
    download_file(url, file_name)
