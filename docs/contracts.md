# Module Contracts

## Module 1: X Data Fetcher
- **Public Function**: `fetch_mentions(query: str, since_id: str | None) -> list[dict]`
- **Input Schema**: `{"query": str, "since_id": str | None}`
- **Output Schema**: `[{"id": str, "text": str, "author_id": str, "created_at": str, "author_username": str}]`
- **Errors**: `ValueError`, `APIError`, `TimeoutError`
- **Must Not**: Store data, authenticate users, enrich data.

## Module 2: Lead Enricher
- **Public Function**: `enrich_leads(raw_tweets: list[dict]) -> list[dict]`
- **Input Schema**: List of raw tweet dicts
- **Output Schema**: `[{"name": str, "description": str, "source": "X", "stage": "New", "external_id": str}]`
- **Errors**: `ValueError`, `ValidationError`
- **Must Not**: Query external APIs, apply business logic.

## Module 3: Queue Manager
- **Public Functions**: `enqueue(lead: dict) -> str`, `dequeue_batch(size: int = 10) -> list[dict]`
- **Input Schema**: Lead dict (enqueue), size int (dequeue)
- **Output Schema**: Queue ID (str), list of leads (list[dict])
- **Errors**: `QueueFullError`, `ValueError`
- **Must Not**: Process leads, persist data.

## Module 4: Odoo Integrator
- **Public Function**: `create_leads_batch(leads: list[dict]) -> list[dict]`
- **Input Schema**: List of enriched leads
- **Output Schema**: `[{"external_id": str, "odoo_id": int | None, "status": str, "error": str | None}]`
- **Errors**: `AuthError`, `APIError`, `DuplicateError`
- **Must Not**: Read from Odoo, validate leads.

## Module 5: Dashboard Renderer
- **Public Function**: `get_leads_view(filters: dict) -> str`
- **Input Schema**: `{"filters": dict}`
- **Output Schema**: XML/JSON string (Odoo view)
- **Errors**: `QueryError`, `ValueError`
- **Must Not**: Write data, export raw data.

## Module 6: Logger/Monitor
- **Public Functions**: `log_event(level: str, message: str, metadata: dict | None) -> None`, `get_metrics(period: str) -> dict`
- **Input Schema**: Level, message, metadata (log); period str (metrics)
- **Output Schema**: None (log), dict (metrics)
- **Errors**: `IOError`, `ValueError`
- **Must Not**: Alter flow, store PII.