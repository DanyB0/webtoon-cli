import os
import sys

BASE_DIR = os.path.dirname(__file__)

# adding the important folders to the system path
sys.path.insert(0, f"{BASE_DIR}/webtooncli")
sys.path.insert(0, f"{BASE_DIR}/webtooncli/scrape")

from .webtooncli import *
