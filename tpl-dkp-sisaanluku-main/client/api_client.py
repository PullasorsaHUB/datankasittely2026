# TODO: 
# Import requests library
# Define fetch_data function, that takes an API URL as parameter
# Use try - except structure to
# - make a GET request to the given URL with athe requests library,
# - raise an exception if the response status code indicates an error,
# - return the response data as JSON
# - print an error message if something goes wrong with the request, and return None.

import requests

def fetch_data(api_url):
    try:
        get_url = requests.get(api_url)
        get_url.raise_for_status()
        data = get_url.json()
        #print(get_url)
    except requests.exceptions.InvalidURL as err:
        print("Invalid Url: ", err)
        print("No Work")
        return None
    except requests.exceptions.MissingSchema as err:
        print("Missing schema: HTTP", err)
        print("No Work")
        return None
    except AssertionError as err:
        print("Köh: ", err)
        return None
    except:
        return None
    return data