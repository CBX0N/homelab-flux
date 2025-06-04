import requests

def get_request(apiKey, url):
    headers = {
        "accept": "application/json",
        "X-Api-Key": apiKey,
        "Content-Type": "application/json",
    }
    response = requests.get(url=url, headers=headers)
    return response


def get_downloadClients(apiKey, url):
    requests_url = url + '/downloadclient'
    response = get_request(apiKey, requests_url)
    return response

def get_applications(apiKey, url):
    requests_url = url + '/applications'
    response = get_request(apiKey, requests_url)
    return response