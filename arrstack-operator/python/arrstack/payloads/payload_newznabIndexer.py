def payload_newznabIndexer(nzb):
    payload = {
            "enable": True,
            "redirect": True,
            "supportsRss": True,
            "supportsSearch": True,
            "supportsRedirect": True,
            "supportsPagination": True,
            "appProfileId": 1,
            "protocol": "usenet",
            "privacy": "private",
            "priority": 25,
            "downloadClientId": 0,
            "name": nzb["nzbName"],
            "fields": [
                {
                    "order": 0,
                    "name": "baseUrl",
                    "label": "Url",
                    "value": nzb["nzbUrl"],
                },
                {
                    "order": 2,
                    "name": "apiKey",
                    "label": "API Key",
                    "value": nzb["nzbApiKey"],
                },
                {
                    "order": 4,
                    "name": "vipExpiration",
                    "label": "VIP Expiration",
                    "value": nzb["nzbExpiryDate"],
                },
            ],
            "implementation": "Newznab",
            "configContract": "NewznabSettings",
        }
    return payload