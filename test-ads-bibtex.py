import sys
import ads
# import ads.sandbox as ads

def retrieve_bibtex_from_ads(bibcode):
    """
    Get the bibtex entry for a given bibcode
    """
    q = ads.ExportQuery(bibcode, format="bibtex")
    export = q.execute()
    return export

try:
    bibcode = str(sys.argv[1])
except:
    sys.exit(f"Usage: {sys.argv[0]} BIBCODE")

print(retrieve_bibtex_from_ads(bibcode))
