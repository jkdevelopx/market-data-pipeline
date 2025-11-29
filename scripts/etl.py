import yfinance as yf
import pandas as pd
from supabase import create_client
import os
from datetime import datetime

# ใช้ environment variables แทน st.secrets → ทำงานได้ทั้ง local และ GitHub Actions
supabase = create_client(
    url=os.getenv("SUPABASE_URL"),
    key=os.getenv("SUPABASE_KEY")
)

SYMBOLS = ["AAPL","MSFT","NVDA","TSLA","GOOGL","BTC-USD","ETH-USD","SOL-USD","ADA-USD","DOGE-USD"]

def run_etl():
    print(f"ETL Started: {datetime.now():%Y-%m-%d %H:%M:%S}")
    updated = 0
    for symbol in SYMBOLS:
        try:
            print(f"Fetching {symbol:<9} → ", end="")
            df = yf.Ticker(symbol).history(period="7d", interval="1d")
            if df.empty: 
                print("no new data")
                continue
                
            records = []
            sym = symbol.replace("-USD", "")
            for date, row in df.iterrows():
                records.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "symbol": sym,
                    "Open": round(row["Open"], 6),
                    "High": round(row["High"], 6),
                    "Low": round(row["Low"], 6),
                    "Close": round(row["Close"], 6),
                    "Volume": int(row["Volume"]) if pd.notna(row["Volume"]) else 0
                })
            supabase.table("daily_prices").upsert(records, on_conflict="date,symbol").execute()
            print("updated")
            updated += 1
        except Exception as e:
            print(f"error → {e}")
    print(f"ETL Completed! Updated {updated}/{len(SYMBOLS)} assets")
    
if __name__ == "__main__":
    run_etl()
