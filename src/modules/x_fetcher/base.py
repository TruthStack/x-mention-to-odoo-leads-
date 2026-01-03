# base.py
from typing import List, Dict, Optional

def fetch_mentions(query: str, since_id: Optional[str] = None) -> List[Dict]:
    """
    CONTRACT:
    Input: query, optional since_id
    Output: list of tweet dicts
    """
    raise NotImplementedError
