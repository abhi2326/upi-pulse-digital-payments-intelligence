# UPI Pulse: India's Digital Payments Intelligence Platform

**Role:** Data Analyst  |  **Market:** India  |  **Portfolio project:** 01/13

## Business problem
Understand payment success, failure reasons, merchant performance, customer cohorts and revenue leakage across a simulated UPI ecosystem.

## Why it matters
Helps a payments operations team prioritise failure hotspots, identify high-value merchant segments and reduce avoidable payment friction.

## Key business / model metrics
- Payment success rate
- Failure rate by bank / PSP
- Merchant TPV
- Repeat payer rate
- Failure value at risk

## Technology
SQL, Python, Pandas, Power BI, DAX, Streamlit, Plotly

## Repository structure
```text
upi-pulse-digital-payments-intelligence/
├── app.py
├── project.json
├── requirements.txt
├── src/
│   ├── generate_data.py
│   └── pipeline.py / train.py
├── data/
│   ├── raw/
│   └── processed/
├── sql/
├── tests/
├── docs/
└── reports/
```

## Quick start
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python -m src.generate_data --rows 10000
python -m src.pipeline\nstreamlit run app.py\n```

## Data sources and realism
The repository ships with **synthetic demonstration data** so that the code runs without credentials or private records. It does not claim to contain actual NPCI, ONDC, GSTN, bank, farmer, CPCB or EV-operator data.

Suggested public/contextual sources to obtain and cite when extending the project:
- NPCI UPI product statistics (public aggregate context)
- RBI payment system indicators
- Synthetic transaction-level demo data

Check current terms, licensing, attribution and API access before downloading or redistributing data. Never upload personal, financial, health or other sensitive records to a public repository.

## Architecture
```mermaid
flowchart LR
  A[Public / synthetic source data] --> B[Ingestion & validation]
  B --> C[Clean / feature layer]
  C --> D[SQL analytics or ML model]
  D --> E[Dashboard / API / data mart]
  E --> F[Business action with human oversight]
```

## Business impact hypothesis
Helps a payments operations team prioritise failure hotspots, identify high-value merchant segments and reduce avoidable payment friction.

This is a measurable hypothesis, not a claimed realised outcome. To quantify impact, define a baseline, run a controlled pilot, compare before/after metrics and document costs and confidence intervals.

## Limitations and responsible use
- Demo data is synthetic; model metrics on it are not evidence of production performance.
- Validate against representative, time-appropriate and legally usable data.
- Document missingness, leakage risks, sampling bias and distribution shift.
- Human review is required for consequential decisions.
- Do not infer sensitive personal attributes or automate denial of public services, credit, healthcare or other essential access.

## GitHub publishing
1. Create a separate public repository using this folder name.
2. Upload the contents of this folder (not the parent portfolio folder).
3. Keep raw data, secrets, local databases and model binaries out of Git.
4. Add verified screenshots and benchmark results only after running on a documented dataset.
