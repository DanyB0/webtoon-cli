import argparse
import os
import sys

import utils

BASE_DIR = os.getcwd()

parser = argparse.ArgumentParser(
    description="Webtoons utility tool",
    epilog="Enjoy the program! :)",
)

parser.add_argument(
    "-v", "--view", help="view the webtoon details", action="store_true"
)
parser.add_argument(
    "-d", "--download", help="download the webtoon", action="store_true"
)
parser.add_argument(
    "-s",
    "--search",
    help="search the webtoon on the default website",
    type=str,
    action="store",
)
parser.add_argument(
    "-n", "--name", help="name of the webtoon", type=str, action="store"
)

parser.add_argument(
    "--change-website", help="change the website", type=str, action="store"
)

args = parser.parse_args()

# get all the website info (globals.py file)
(
    website_name,
    website_domain,
    page_link,
    webtoon_page_link,
    search_link,
) = utils.get_website_info(BASE_DIR)


if args.name:
    webtoon_name = args.name
    if args.view:
        print("\nwork in progress...\n")
        # print(f"{page_link}{webtoon_name}")
    elif args.download:
        print("\nwork in progress...\n")
    # elif args.change-website:
        # print("\nwork in progress...\n")
    else:
        print(f"\n{page_link}{webtoon_name}\n")

elif args.search:
    query = args.search
    complete_search_link = f"{search_link}{query}"
    names_list = utils.scrape.search(complete_search_link)
    for i, name in enumerate(names_list):
        print(f"{i+1}) {name}")
