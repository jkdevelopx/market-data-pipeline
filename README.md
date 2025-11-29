<div align="center">

# Market Pulse Pro  
**Real-time Stock & Crypto Dashboard**  
Live Data • Daily Automated Pipeline • Production-Ready • Stunning UI

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com)
[![Streamlit](https://img.shields.io/badge/ badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo_Finance-720e9e?logo=yahoo&logoColor=white)](https://finance.yahoo.com)
[![ETL Status](https://img.shields.io/github/actions/workflow/status/jkdevelopx/market-data-pipeline/daily-etl.yml?branch=main&label=Daily%20ETL&color=brightgreen)](https://github.com/jkdevelopx/market-data-pipeline/actions)

**[Live Demo – Open Instantly](https://jkdevelopx-market-data-pipeline-streamlit-app.streamlit.app)**  
(หรือใช้ External URL จาก Codespaces ก็ได้เหมือนกัน)

![](https://github.com/user-attachments/assets/41f2c2d3-2f8e-4d8f-9c5a-3e8f8d7b9c1a)

</div>

## Why This Project Stands Out (Perfect for Your Resume/Interviews)
- Fully automated daily ETL pipeline using GitHub Actions (runs every day at 07:00 ICT – zero maintenance)
- Production-grade Supabase backend with proper unique constraints & upsert logic
- Ultra-clean, dark-mode, glassmorphism dashboard (Plotly candlestick + real-time metrics)
- 100% English + pixel-perfect UI → ready to show international companies
- Deployed and accessible 24/7 (Codespaces + Streamlit Community Cloud)

Perfect proof of skills in:
**Python • Data Engineering • ETL • Supabase • Streamlit • CI/CD • Full-Stack Data Apps**

## Tech Stack
| Layer          | Technology                          |
|----------------|-------------------------------------|
| Data Source    | Yahoo Finance (yfinance)            |
| Database       | Supabase (PostgreSQL)               |
| Backend/ETL        | Python + pandas + supabase-py       |
| Frontend       | Streamlit + Plotly                  |
| Automation     | GitHub Actions (daily schedule)     |
| Hosting        | GitHub Codespaces + Streamlit Cloud |

## Assets Tracked (10 symbols)
`AAPL • MSFT • NVDA • TSLA • GOOGL • BTC-USD • ETH-USD • SOL-USD • ADA-USD • DOGE-USD`

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
