#!/usr/bin/env python3
"""
Main orchestrator script for X → Odoo Lead Generation.
Runs the complete pipeline: Fetch → Enrich → Queue → Integrate → Log.
"""
import os
import time
import sys
from datetime import datetime

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import modules (others will be added as implemented)
from modules.x_fetcher import fetch_mentions, APIError
# Future imports:
# from modules.lead_enricher import enrich_leads
# from modules.queue_manager import enqueue, dequeue_batch
# from modules.odoo_integrator import create_leads_batch
# from modules.logger_monitor import log_event, get_metrics


def load_config():
    """Load configuration from environment variables."""
    config = {
        "query": os.getenv("QUERY", "#OdooHack2026"),
        "poll_interval": int(os.getenv("POLL_INTERVAL", "300")),
        "batch_size": int(os.getenv("BATCH_SIZE", "10")),
    }
    
    # Validate required config
    if not os.getenv("X_TOKEN"):
        print("❌ ERROR: X_TOKEN environment variable is required")
        sys.exit(1)
    
    return config


def mock_enrich(tweets):
    """Mock enrichment for testing (replace with real Module 2 later)."""
    enriched = []
    for tweet in tweets:
        enriched.append({
            "name": tweet.get("author_username", "Unknown"),
            "description": tweet.get("text", "")[:500],
            "source": "X",
            "stage": "New",
            "external_id": tweet.get("id", "")
        })
    return enriched


def mock_log(level, message, metadata=None):
    """Mock logging for testing (replace with real Module 6 later)."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    meta_str = f" | {metadata}" if metadata else ""
    print(f"[{timestamp}] {level}: {message}{meta_str}")


def run_pipeline_cycle(config, last_id=None):
    """
    Run one complete pipeline cycle.
    
    Args:
        config: Configuration dictionary
        last_id: Last processed tweet ID for pagination
    
    Returns:
        New last_id for next cycle
    """
    print(f"🔄 Starting pipeline cycle at {datetime.now()}")
    
    try:
        # Step 1: Fetch mentions from X
        print(f"   📡 Fetching mentions with query: {config['query']}")
        raw_tweets = fetch_mentions(config["query"], last_id)
        
        if not raw_tweets:
            print("   ℹ️  No new mentions found")
            return last_id
        
        print(f"   ✅ Fetched {len(raw_tweets)} tweets")
        
        # Update last_id for pagination
        new_last_id = raw_tweets[-1]["id"]
        print(f"   📝 Last tweet ID: {new_last_id}")
        
        # Step 2: Enrich tweets (mock for now)
        print("   🎨 Enriching tweets...")
        enriched_leads = mock_enrich(raw_tweets)
        print(f"   ✅ Enriched {len(enriched_leads)} leads")
        
        # Step 3: Queue leads (mock for now)
        print("   📥 Queuing leads...")
        for lead in enriched_leads:
            # In real implementation: enqueue(lead)
            pass
        print(f"   ✅ Queued {len(enriched_leads)} leads")
        
        # Step 4: Process batch (mock for now)
        print("   🔄 Processing batch...")
        # In real implementation: batch = dequeue_batch(config['batch_size'])
        # In real implementation: results = create_leads_batch(batch)
        
        # Mock logging
        mock_log("INFO", f"Processed {len(enriched_leads)} leads", 
                {"cycle_time": datetime.now().isoformat()})
        
        return new_last_id
        
    except APIError as e:
        print(f"   ❌ API Error: {e}")
        mock_log("ERROR", f"API Error: {e}")
        return last_id
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        mock_log("ERROR", f"Unexpected error: {e}", {"error": str(e)})
        return last_id


def main():
    """Main orchestrator function."""
    print("=" * 60)
    print("🚀 X → Odoo Real-Time Lead Generation Pipeline")
    print("=" * 60)
    
    # Load configuration
    config = load_config()
    print(f"📋 Configuration loaded:")
    print(f"   Query: {config['query']}")
    print(f"   Poll Interval: {config['poll_interval']} seconds")
    print(f"   Batch Size: {config['batch_size']}")
    print()
    
    last_id = None
    cycle_count = 0
    
    try:
        while True:
            cycle_count += 1
            print(f"\n📊 Cycle #{cycle_count}")
            print("-" * 40)
            
            # Run one pipeline cycle
            last_id = run_pipeline_cycle(config, last_id)
            
            # Wait for next cycle
            print(f"\n⏳ Waiting {config['poll_interval']} seconds for next cycle...")
            print("-" * 60)
            time.sleep(config["poll_interval"])
            
    except KeyboardInterrupt:
        print("\n\n👋 Pipeline stopped by user")
        print("✅ Clean shutdown completed")
        sys.exit(0)


if __name__ == "__main__":
    main()
