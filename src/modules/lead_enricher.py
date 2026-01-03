# src/modules/lead_enricher.py
"""
Module: Lead Enricher
Responsibility:
- Transform raw X mentions into Odoo CRM lead-ready objects
"""

from typing import List, Dict


class ValidationError(Exception):
    """Raised when input data is invalid."""
    pass


def enrich_leads(raw_tweets: List[Dict]) -> List[Dict]:
    """
    Public API (STABLE CONTRACT)

    Input:
        raw_tweets: List of tweet dictionaries from X Fetcher

    Output:
        List of enriched lead dictionaries ready for Odoo

    Must NOT:
        - Call external APIs
        - Persist data
        - Apply business rules
    """

    if not isinstance(raw_tweets, list):
        raise ValueError("raw_tweets must be a list")

    enriched_leads: List[Dict] = []

    for tweet in raw_tweets:
        # --- Validation ---
        required_keys = ["id", "text", "author_username"]
        if not all(key in tweet for key in required_keys):
            raise ValidationError(f"Missing keys in tweet: {tweet}")

        # --- Mapping logic ---
        description = tweet["text"][:500]  # Odoo-safe length

        lead = {
            "name": tweet["author_username"],      # Lead name
            "description": description,             # Lead notes
            "source": "X",                           # Source tag
            "stage": "New",                          # Default stage
            "external_id": tweet["id"],              # For deduplication
        }

        enriched_leads.append(lead)

    return enriched_leads
