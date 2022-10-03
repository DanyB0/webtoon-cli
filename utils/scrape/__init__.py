import requests
import bs4

from .globals import *

print(BASE_DIR)

r = requests.get(website_domain)
print(r)
