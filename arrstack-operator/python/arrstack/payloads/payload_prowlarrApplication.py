def payload_prowlarrApplication(app):
    payload = {
        "syncLevel": "fullSync",
        "enable": True,
        "name": app["app_name"],
        "fields": [
            {
                "order": 0,
                "name": "prowlarrUrl",
                "label": "Prowlarr Server",
                "value": app["prowlarr_url"],
            },
            {
                "order": 1,
                "name": "baseUrl",
                "label": app["app_name"] + " Server",
                "value": app["app_url"],
            },
            {
                "order": 2,
                "name": "apiKey",
                "label": "API Key",
                "value": app["app_apiKey"],
            },
        ],
        "implementation": app["app_name"],
        "configContract": app["app_configContract"],
    }
    return payload