import json


def pretty_response(response):
    # Pretty-print JSON
    try:
        data = response.json()
        print(json.dumps(data, indent=2))
    except ValueError:
        print("Non-JSON response:")
        print(response.text)
