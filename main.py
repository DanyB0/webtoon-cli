import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--view", help="view the webtoon details", action="store_true")
parser.add_argument("-d", "--download", help="download the webtoon", action="store_true")
parser.add_argument("-s", "--search", help="search the webtoon on the default website", action="store_true")
parser.add_argument("--change-website", type=int, help="change the website")

args = parser.parse_args()

if args.view:
    print("ok")
