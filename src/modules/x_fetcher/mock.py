from .base import fetch_mentions
from typing import List, Dict

def fetch_mentions(query: str, since_id=None) -> List[Dict]:
    return [
        {
            "id": "mock_001",
            "text": "Looking for Odoo CRM integrations",
            "author_id": "user_1",
            "author_username": "demo_user",
            "created_at": "2026-01-03T10:00:00Z"
        }
    ]
