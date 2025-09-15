import os

BASE_URL = os.getenv("BASE_URL", "http://www.saucedemo.com/")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"