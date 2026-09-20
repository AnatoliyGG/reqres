import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://reqres.in")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))