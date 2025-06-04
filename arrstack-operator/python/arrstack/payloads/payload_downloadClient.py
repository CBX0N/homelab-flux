import json
def payload_downloadClient(dc):    
  payload = {
    "enable": True,
    "protocol": dc["downloadclient_protocol"],
    "priority": 1,
    "categories": [],
    "supportsCategories": True,
    "name": dc["downloadclient_name"],
    "fields": [
      {
        "order": 0,
        "name": "host",
        "label": "Host",
        "value": dc["downloadclient_ip"]
      },
      {
        "order": 1,
        "name": "port",
        "label": "Port",
        "value": dc["downloadclient_port"]
      },
      {
        "order": 4,
        "name": "username",
        "label": "Username",
        "value": dc["downloadclient_username"]
      },
      {
        "order": 5,
        "name": "password",
        "label": "Password",
        "value": dc["downloadclient_password"]
      }
    ],
    "implementation": dc["downloadclient_name"],
    "configContract": dc["downloadclient_name"] + "Settings",
  }
  return payload