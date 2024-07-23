import logging
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def make_request(url):
    logging.debug('Making request to %s', url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.debug('Request successful')
        return response.text
    except requests.RequestException as e:
        logging.error('Request failed: %s', e)
        return None

# Example usage
url = 'https://jsonplaceholder.typicode.com/posts/1'
result = make_request(url)
if result:
    print(result)
