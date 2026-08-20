import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file and loads it into the environment

BASE_URL = os.getenv("BASE_URL")
TEST_USERNAME = os.getenv("TEST_USERNAME")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")