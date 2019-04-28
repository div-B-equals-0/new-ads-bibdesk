import sys
import os
import json
import requests

TOKEN_FILE = "~/.ads/dev_key"
# See https://github.com/adsabs/adsabs-dev-api/blob/master/Export_API.ipynb and
# https://github.com/adsabs/adsabs-dev-api/blob/master/Converting_curl_to_python.ipynb
EXPORT_BASE_URL = "https://api.adsabs.harvard.edu/v1/export"

def obtain_api_token():
    try:
        with open(os.path.expanduser(TOKEN_FILE)) as fp:
            token = fp.read().strip()
    except IOError:
        sys.exit(f"Failed to read token from {TOKEN_FILE}")
    return token

def retrieve_bibtex_from_ads(bibcode, format_="bibtexabs"):
    """
    Get the bibtex+abstract entry for a given bibcode
    """
    token = obtain_api_token()
    url = f"{EXPORT_BASE_URL}/{format_}"
    r = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json",
        },
        data=json.dumps({"bibcode": [bibcode]}),
    )
    response = r.json()
    return response["export"]

try:
    bibcode = str(sys.argv[1])
except:
    sys.exit(f"Usage: {sys.argv[0]} BIBCODE")

print(retrieve_bibtex_from_ads(bibcode))
