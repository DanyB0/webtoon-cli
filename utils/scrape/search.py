import requests
from bs4 import BeautifulSoup

# this function returns only the first 10 results
def search(search_link):
    names_list = []
    # get the web page
    r = requests.get(search_link)
    soup = BeautifulSoup(r.content, "html.parser")
    
    # get all the div containing the title with the given word
    names = soup.find_all("div", {"class": "tt"})

    # crate a list containing only the title of the webtoons
    for val in names:
        names_list.append(val.get_text(strip=True))

    return names_list
