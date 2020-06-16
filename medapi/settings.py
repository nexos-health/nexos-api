import os

from dotenv import load_dotenv

load_dotenv()

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")

# AUTH0 SETTINGS
AUTH0_AUDIENCE = os.environ.get("AUTH0_AUDIENCE")
AUTH0_CALLBACK_URL = os.environ.get("AUTH0_CALLBACK_URL")
AUTH0_DEFAULT_SCOPE = os.environ.get("AUTH0_DEFAULT_SCOPE", "medrecruitment")
AUTH0_STATELESS_SCOPE = os.environ.get("AUTH0_STATELESS_SCOPE", "auth:stateless")
AUTH0_MFA_SCOPE = os.environ.get("AUTH0_MFA_SCOPE", "auth:mfa")
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "medrecruitment.au.auth0.com")
AUTH0_REALM = os.environ.get("AUTH0_REALM")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")
AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
AUTH0_ALGORITHM = os.environ.get("AUTH0_ALGORITHM", "RS256")

# Professionals host
PEEPS_HOST = os.environ.get("PEEPS_HOST", "https://doctorsaustralia.fun:8000")
