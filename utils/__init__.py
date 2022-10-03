import sys

from .globals import *

BASE_DIR = os.getcwd()

# adding the scrape folder to the system path
sys.path.insert(0, f"{BASE_DIR}/utils/scrape")

from .scrape import *
