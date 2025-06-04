import requests
import arrstack.payloads as payloads

def add_DownloadClient(apiKey, url, dc):
    request_url = url + "/downloadclient"
    payload = payloads.payload_downloadClient(dc)
    headers = {
        "accept": "application/json",
        "X-Api-Key": apiKey,
        "Content-Type": "application/json",
    }
    response = requests.post(request_url, headers=headers, json=payload)
    return response