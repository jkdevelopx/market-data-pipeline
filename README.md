<div align="center">

# Market Pulse Pro  
**Real-time Stock & Crypto Dashboard**  
อัพเดทข้อมูลทุกวันอัตโนมัติ • สวยระดับโลก • Production-Ready

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Yahoo Finance](https://img.shields.io/badge/Yahoo_Finance-7F2CCB?logo=yahoo&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/jkdevelopx/market-data-pipeline/daily-etl.yml?branch=main&label=ETL)

**[Live Demo (เปิดดูได้ทันที)](http://207.46.224.84:8501)** ← กดเลย! (Codespaces External URL)

https://github.com/user-attachments/assets/41f2c2d3-2f8e-4d8f-9c5a-3e8f8d7b9c1a

</div>

## Features
- ดึงข้อมูลจริงจาก **Yahoo Finance** (10 สินทรัพย์: AAPL, MSFT, NVDA, TSLA, GOOGL, BTC, ETH, SOL, ADA, DOGE)
- เก็บใน **Supabase** (Production DB + Unique Constraint)
- **ETL อัตโนมัติทุกวัน 07:00 น.** ด้วย GitHub Actions
- Dashboard สวยระดับโลก (Dark mode + Glassmorphism + Hover effects)
- Responsive + Real-time metrics + Candlestick chart
- ภาษาอังกฤษ 100% → เอาไปสัมภาษณ์งานต่างประเทศได้เลย

## Tech Stack
```text
Yahoo Finance → yfinance
Supabase      → supabase-py
Frontend      → Streamlit + Plotly
Automation    → GitHub Actions
Hosting       → GitHub Codespaces (Live demo)
