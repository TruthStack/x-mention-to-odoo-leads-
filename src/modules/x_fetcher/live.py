import os
import requests
from .base import fetch_mentions

def fetch_mentions(query: str, since_id=None):
    token = os.getenv("X_TOKEN")
    if not token:
        raise RuntimeError("X_TOKEN missing")

    # Real API logic here (unchanged contract)
