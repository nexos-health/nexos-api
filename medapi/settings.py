import os

from dotenv import load_dotenv

load_dotenv()

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

