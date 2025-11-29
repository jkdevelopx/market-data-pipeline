import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from supabase import create_client
from datetime import datetime

st.set_page_config(
    page_title="Market Pulse Pro",
    page_icon="https://em-content.zobj.net/source/apple/118/chart-with-upwards-trend_1f4c8.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# Premium CSS
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #0c0e1a 0%, #1a1f2e 100%); color: #ffffff;}
    h1 {font-family: 'SF Pro Display', sans-serif; font-weight: 700; font-size: 4rem; background: linear-gradient(90deg, #00d4aa, #0099ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .metric-card {background: rgba(255,255,255,0.05); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 1.8rem 1rem; text-align: center; transition: all 0.4s;}
    .metric-card:hover {transform: translateY(-10px); box-shadow: 0 25px 50px rgba(0,212,170,0.25);}
    .stSelectbox > div > div {background: rgba(255,255,255,0.1); border-radius: 16px; backdrop-filter: blur(10px);}
    .stPlotlyChart {border-radius: 20px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.5);}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Market Pulse Pro</h1>", unsafe_allow_html=True)
st.markdown("### Real-time Financial Data • Stocks & Cryptocurrencies")

# Symbols
@st.cache_data(ttl=3600)
def get_symbols():
    data = supabase.table("daily_prices").select("symbol").execute()
    return sorted({row["symbol"] for row in data.data})

symbols = get_symbols()
selected = st.sidebar.selectbox("Select Asset", symbols, index=symbols.index("BTC") if "BTC" in symbols else 0)

# Data
@st.cache_data(ttl=300)
def get_data(sym):
    resp = supabase.table("daily_prices").select("*").eq("symbol", sym).order("date").execute()
    df = pd.DataFrame(resp.data)
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    return df

df = get_data(selected)

# Metrics
latest = df.iloc[-1]
prev = df.iloc[-2]
change = latest.Close - prev.Close
change_pct = (change / prev.Close) * 100
is_up = change >= 0

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(f"<div class='metric-card'><h2>${latest.Close:,.4f}</h2><p style='margin:0; opacity:0.8;'>Price</p></div>", unsafe_allow_html=True)
with col2:
    color = "#00ff88" if is_up else "#ff3366"
    st.markdown(f"<div class='metric-card'><h2 style='color:{color}'>{change:+.4f}</h2><p style='margin:0; opacity:0.8;'>24h Change</p></div>", unsafe_allow_html=True)
with col3:
    color = "#00ff88" if is_up else "#ff3366"
    st.markdown(f"<div class='metric-card'><h2 style='color:{color}'>{change_pct:+.2f}%</h2><p style='margin:0; opacity:0.8;'>24h %</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-card'><h2>{latest.Volume:,}</h2><p style='margin:0; opacity:0.8;'>Volume</p></div>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<div class='metric-card'><h2>{len(df):,}</h2><p style='margin:0; opacity:0.8;'>Days of Data</p></div>", unsafe_allow_html=True)

# Chart – แก้สีให้ Plotly ยอมรับแล้ว
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df.Open, high=df.High, low=df.Low, close=df.Close,
    increasing_line_color="#00ff88",
    decreasing_line_color="#ff3366",
    increasing_fillcolor="rgba(0, 255, 136, 0.15)",   # แก้ตรงนี้
    decreasing_fillcolor="rgba(255, 51, 102, 0.15)"   # แก้ตรงนี้
)])
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    font_color="#b0b0b0", height=720,
    xaxis_rangeslider_visible=False,
    title=f"{selected} • Live Chart",
    hovermode="x unified",
    margin=dict(l=20, r=20, t=80, b=20)
)
st.plotly_chart(fig, use_container_width=True)

# Table
st.markdown("### Recent 30 Days")
st.dataframe(df.tail(30)[["Open","High","Low","Close","Volume"]].round(4), use_container_width=True, hide_index=False)

# Footer
st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%d %B %Y • %H:%M UTC')} • Automated daily pipeline")
