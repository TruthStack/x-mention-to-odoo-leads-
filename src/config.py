# src/config.py
"""
Central configuration loader.
Keeps env handling out of business logic.
"""

import os

def get_config() -> dict:
    """
    Loads configuration from environment variables.
    Returns a dictionary so code stays clean and testable.
    """

    config = {
        # Mode control
        "APP_MODE": os.getenv("APP_MODE", "mock"),  # mock | live

        # X (optional in hackathon)
        "X_TOKEN": os.getenv("X_TOKEN", ""),

        # Odoo
        "ODOO_URL": os.getenv("ODOO_URL", ""),
        "ODOO_DB": os.getenv("ODOO_DB", ""),
        "ODOO_USER": os.getenv("ODOO_USER", ""),
        "ODOO_PW": os.getenv("ODOO_PW", ""),

        # App behavior
        "QUERY": os.getenv("QUERY", "#OdooHack2026"),
        "POLL_INTERVAL": int(os.getenv("POLL_INTERVAL", "300")),
    }

    return config
