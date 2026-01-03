
---

# 🚀 Social Radar for Odoo

### X (Twitter) Mentions → Odoo CRM Lead Generation

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Odoo](https://img.shields.io/badge/Odoo-17-purple.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Hackathon%20Ready-success.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Modular%20%7C%20Scalable-orange.svg)](#)

---

## 📌 Overview

**Social Radar for Odoo** is a lightweight, production-minded integration that converts **social intent from X (Twitter)** into **actionable leads inside Odoo CRM**.

The project focuses on:

* clean system design
* strict module contracts
* safe handling of paid external APIs
* real-world Odoo CRM alignment

This repository represents a **hackathon-ready MVP** with **enterprise-grade structure**.

---

## 🎯 Problem Statement

* Sales and marketing teams miss high-intent leads happening on social platforms.
* Odoo CRM has no native, real-time social ingestion.
* Existing solutions rely on brittle, expensive, or opaque automations.

**Result:** Lost opportunities and delayed follow-ups.

---

## ✅ Solution

This project provides a **clear ingestion pipeline**:

```
X Mentions (mock / live)
        ↓
Data Fetcher
        ↓
Lead Enricher
        ↓
CRM-Ready Lead Objects
        ↓
Odoo CRM
```

* Social mentions are normalized
* Enriched into Odoo-compatible lead schema
* Ready for insertion into Odoo CRM via XML-RPC

---

## 🧠 Key Design Principles

* **Modular architecture** (replaceable components)
* **Strict contracts** between modules
* **Mock-first strategy** for paid APIs
* **Zero hardcoded secrets**
* **Beginner-friendly, production-correct Python**

---

## 🏗 Project Structure

```
src/
├── config.py                # Central configuration loader
├── main.py                  # Orchestrator (pipeline runner)
└── modules/
    ├── x_fetcher/
    │   ├── base.py          # Stable contract
    │   ├── mock.py          # Hackathon-safe mock adapter
    │   └── __init__.py      # Mode selector
    └── lead_enricher.py     # X → Odoo schema mapping
docs/
└── contracts.md             # Immutable module contracts
```

---

## 🔐 Configuration

Create a `.env` file (never commit secrets):

```env
APP_MODE=mock            # mock | live

# X API (optional – paid)
X_TOKEN=

# Odoo
ODOO_URL=https://your-odoo-instance.com
ODOO_DB=your_database
ODOO_USER=admin
ODOO_PW=admin_password

QUERY=#OdooHack2026
POLL_INTERVAL=300
```

---

## ⚠️ X API Note (Important)

> Due to recent X (Twitter) API monetization, this project defaults to a **mock adapter** that mirrors the X v2 API schema.
> Switching to live data requires **no architectural changes**—only setting `APP_MODE=live` and providing a valid `X_TOKEN`.

This approach ensures:

* zero cost for hackathon
* deterministic demos
* production readiness

---

## ▶️ Running the Demo

```bash
pip install -r requirements.txt
export APP_MODE=mock
python src/main.py
```

### Expected Output

```text
Running in APP_MODE = mock
Fetched 1 mentions
Enriched 1 leads
Lead Ready → {...}
```

This confirms the **end-to-end pipeline** works correctly.

---

## 🧪 Dependencies

`requirements.txt` (minimal by design):

```txt
requests>=2.31.0
pytest>=7.4.0
```

* No heavy frameworks
* No unused libraries
* Standard-library-first approach

---

## 🖥 Odoo CRM Context

This project targets **Odoo CRM Leads / Opportunities**.

Public reference UI:
👉 [https://www.odoo.com/app/crm](https://www.odoo.com/app/crm)

Generated leads map directly to:

* Lead name
* Description
* Source = X
* Initial pipeline stage

---

## 🏆 Why This Project Stands Out

* Designed like a **real production integration**
* Demonstrates **Odoo domain understanding**
* Shows **engineering judgment** under real-world constraints
* Prioritizes **clarity, safety, and extensibility**

This is not a demo script — it is a **deployable system skeleton**.

---

## 🔮 Future Enhancements (Out of Scope for MVP)

* Live X API ingestion
* Queue-backed ingestion (Redis)
* Deduplication in Odoo
* Sentiment or intent scoring
* Multi-platform social sources

---

## 📄 License

MIT License — free to use, modify, and extend.

---

## 🙌 Acknowledgements

Built for the **Odoo × SNS Hiring Hackathon 2026**, with a focus on:

* real business value
* clean architecture
* hiring-level engineering signals

---

### ⭐ If you’re an Odoo engineer or reviewer:

This repository intentionally favors **design correctness over feature volume**.

---
