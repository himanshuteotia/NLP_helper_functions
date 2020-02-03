## Install and import all the necessary libraries

import requests
import json

## Extracting text from JSON file

#json from "https://quotes.rest/qod.json"
r = requests.get("https://quotes.rest/qod.json")
res = r.json()
print(json.dumps(res, indent = 4))