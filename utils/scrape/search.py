import requests
from bs4 import BeautifulSoup


def get_search_webtoons(search_link):
    # get the web page
    r = requests.get(search_link)
    soup = BeautifulSoup(r.content, "html.parser")

    # get all the div containing the title with the given word
    names = soup.find_all("div", {"class": "tt"})

    return soup, names


def search(soup, names):
    other_pages_links = []
    titles = []

    try:
        # get all the other results pages (if they  exist)
        other_pages = soup.find_all("a", {"class": "page-numbers"}, href=True)

        # delete the element in the last position (is the 'next page button')
        other_pages.pop(-1)

        # append every next page link to the list
        for link in other_pages:
            other_pages_links.append(link["href"])
    except IndexError:
        pass

    # crate a list containing only the title of the webtoons
    for val in names:
        titles.append(val.get_text(strip=True))

    # get the webtoons name list for every page after the 1st and append it
    # to the titles list
    try:
        for link in other_pages_links:
            soup, names = get_search_webtoons(link)
            for val in names:
                titles.append(val.get_text(strip=True))
    except:
        pass

    return titles
