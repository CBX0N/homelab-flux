#!/usr/bin/env python3
import arrstack
from pretty_response import pretty_response


prowlarrEnabled = True
radarrEnabled = True
sonarrEnabled = True
prowlarrApi = "http://localhost:9696/api/v1"
radarrApi="http://localhost:7878/api/v3"
sonarrApi="http://localhost:8989/api/v3"
prowlarrApiKey = "375775723f6345298a3e97679929be0b"
radarrApiKey = "d4e43a7189034493b4aac1028585c572"
sonarrApiKey = "e4df81520095443e90125b1dc02be79c"
prowlarrUrl = "http://10.88.0.3:9696"
radarrUrl = "http://10.88.0.5:7878"
sonarrUrl = "http://10.88.0.4:8989"

nzb_indexers = [
    {
        "nzbUrl": "https://api.nzbgeek.info",
        "nzbName": "nzbGeek",
        "nzbApiKey": "gntcYkgmpc98VZ0EIKXyC8FvRKj6AQJF",
        "nzbExpiryDate": "2025-05-31",
    }
]

apps = [
    {
        "prowlarr_url": prowlarrUrl,
        "app_url": sonarrUrl,
        "app_apiKey": sonarrApiKey,
        "app_configContract": "SonarrSettings",
        "app_name": "Sonarr",
    },
    {
        "prowlarr_url": prowlarrUrl,
        "app_url": radarrUrl,
        "app_apiKey": radarrApiKey,
        "app_configContract": "RadarrSettings",
        "app_name": "Radarr",
    },
]

downloadclients = [
  {
    "downloadclient_ip": "10.88.0.6",
    "downloadclient_port": "8080",
    "downloadclient_username": "admin",
    "downloadclient_password": "ptRbP5QRJ",
    "downloadclient_name": "QBittorrent",
    "downloadclient_protocol": "torrent"
  },
  {
    "downloadclient_ip": "10.88.0.7",
    "downloadclient_port": "6789",
    "downloadclient_username": "nzbget",
    "downloadclient_password": "tegbzn6789",
    "downloadclient_name": "Nzbget",
    "downloadclient_protocol": "usenet"
  },
  
]


def configure_downloadClients(apikey,url):
    for downloadclient in downloadclients:
        print("Adding " + downloadclient["downloadclient_name"] + " download client.....", end=' ')
        r = arrstack.add_DownloadClient(apikey,url,dc=downloadclient)
        if r.status_code == 400:
            print("Something went wrong!")
            pretty_response(r)
        else:
            print("Done!")

try:
    if radarrEnabled:
        configure_downloadClients(radarrApiKey, radarrApi)
    if prowlarrEnabled:
        configure_downloadClients(prowlarrApiKey, prowlarrApi)

except ValueError:
    print("Configuration did not complete successfully.")
