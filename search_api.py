import requests


def getSearchResults(query):
    # URL for the API endpoint
    url = "https://sentry.propertyguru.com/api/226/envelope/?sentry_key=ac0e80162bfc40348aa4b34cd05d9924&sentry_version=7&sentry_client=sentry.javascript.browser%2F7.59.2"

    # Parameters for the API request
    params = {
        "q": query,
    }

    # Send the request to the API
    response = requests.get(url, params=params)

    # If the request was successful, return the results
    if response.status_code == 200:
        return response.json()['results']
    else:
        return None