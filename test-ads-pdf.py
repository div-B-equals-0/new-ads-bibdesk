import sys
import os
import json
import requests
from urllib.parse import quote

LINK_GATEWAY_BASE_URL = "https://ui.adsabs.harvard.edu/link_gateway"

def retrieve_article_pdf_from_ads(bibcode, eprint_or_pub="PUB"):
    """
    Get the PDF file for a given bibcode
    """
    endpoint = f"{eprint_or_pub.upper()}_PDF"
    safe_bibcode = quote(bibcode)
    pdf_filename = f"{safe_bibcode}_{eprint_or_pub.lower()}.pdf"
    url = f"{LINK_GATEWAY_BASE_URL}/{safe_bibcode}/{endpoint}"
    r = requests.get(
        url,
        allow_redirects=True,
    )
    with open(pdf_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)
    return pdf_filename

try:
    bibcode = str(sys.argv[1])
except:
    sys.exit(f"Usage: {sys.argv[0]} BIBCODE")

print(retrieve_article_pdf_from_ads(bibcode, "EPRINT"), end="")
