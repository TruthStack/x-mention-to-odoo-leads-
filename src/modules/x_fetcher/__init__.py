import os

MODE = os.getenv("APP_MODE", "mock")

if MODE == "live":
    from .live import fetch_mentions
else:
    from .mock import fetch_mentions
