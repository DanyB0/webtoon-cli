import json
import os


# get the informations from the websites.json file
def get_website_info(BASE_DIR_LOCAL):

    with open(f"{BASE_DIR_LOCAL}/src/websites.json", "r") as websites_list:
        data = json.load(websites_list)

    website_name = data["name"]
    website_domain = data["domain"]
    page_link = data["webtoon_page_link"]
    webtoon_page_link = data["single_webtoon_page_link"]
    search_link = data["search_link"]

    return website_name, website_domain, page_link, webtoon_page_link, search_link
