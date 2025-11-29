<div align="center">

# Market Pulse Pro
Real-time Stock & Crypto Dashboard

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat&logo=supabase&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/jkdevelopx/market-data-pipeline/daily-etl.yml?branch=main&label=Daily%20ETL&style=flat&color=2ea44f)

**Live Demo** → https://jkdevelopx-market-data-pipeline-streamlit-app.streamlit.app

</div>

## What it does
A simple, clean dashboard that shows up-to-date prices and candlestick charts for 10 popular stocks and cryptocurrencies.  
Everything updates automatically every day — no manual work needed.

## Features
- Daily data update (runs automatically at 07:00 ICT via GitHub Actions)
- Data from Yahoo Finance (using yfinance)
- Stored in Supabase (PostgreSQL) with proper unique constraints
- Interactive charts with Plotly
- Dark-mode, responsive UI built with Streamlit
- Always online and ready to show

## Assets included
AAPL · MSFT · NVDA · TSLA · GOOGL · BTC-USD · ETH-USD · SOL-USD · ADA-USD · DOGE-USD

## Tech stack
- Python + pandas + yfinance
- Supabase (database)
- Streamlit + Plotly (frontend)
- GitHub Actions (automation)

## Quick start
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Project structure
textmarket-data-pipeline/
├── scripts/etl.py              # daily data update
├── streamlit_app.py            # dashboard
├── .github/workflows/          # GitHub Actions (runs every day)
├── requirements.txt
└── .streamlit/secrets.toml     # credentials (not in repo)

## Automation
GitHub Actions pulls fresh data and updates the database every morning.
The dashboard always shows the latest prices even if my laptop is off.

  Built by jkdevelopx — November 2025

