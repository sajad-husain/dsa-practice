import requests
import sys

req = requests.get(f"fetch('https://dummyjson.com/{sys.argv[1]}")
print(req.status_code())