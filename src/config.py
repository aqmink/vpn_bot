import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token")

DATABASE_URL = os.getenv("DATABASE_URL")

PANEL_USERNAME=os.getenv("PANEL_USERNAME")

PANEL_PASSWORD=os.getenv("PANEL_PASSWORD")

URL = os.getenv("URL")
