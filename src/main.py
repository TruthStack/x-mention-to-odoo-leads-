# src/main.py
"""
Main Orchestrator
Runs the pipeline:
Fetch → Enrich → (later: Queue → Odoo)
"""

from config import get_config
from modules.x_fetcher import fetch_mentions
from modules.lead_enricher import enrich_leads


def run_once() -> None:
    """
    Executes one pipeline cycle.
    """

    config = get_config()

    print(f"🚀 Running in APP_MODE = {config['APP_MODE']}")

    # 1️⃣ Fetch mentions (mock or live decided internally)
    tweets = fetch_mentions(config["QUERY"])

    print(f"📥 Fetched {len(tweets)} mentions")

    # 2️⃣ Enrich leads
    leads = enrich_leads(tweets)

    print(f"🧩 Enriched {len(leads)} leads")

    # 3️⃣ Result (hackathon-safe demo output)
    for lead in leads:
        print("✅ Lead Ready →", lead)


if __name__ == "__main__":
    run_once()
