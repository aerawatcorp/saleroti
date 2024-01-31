import requests

cdn_meta = "https://cdn.saleroti.com/v1/master.json" # This path should have the lowest TTL  - 300 seconds

meta = requests.get(cdn_meta)

print(meta.json())

