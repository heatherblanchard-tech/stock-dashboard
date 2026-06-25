import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Heather's AI Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Heather's AI Trading Dashboard")

st.success("Dashboard is live and pulling stock data!")

tickers = ["NVDA", "AVGO", "MU", "IONQ", "RGTI", "CEG", "FCX", "AMD", "NET"]

st.header("Live Watchlist")

data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.fast_info

    data.append({
        "Ticker": ticker,
        "Last Price": round(info.get("last_price", 0), 2),
        "Day High": round(info.get("day_high", 0), 2),
        "Day Low": round(info.get("day_low", 0), 2),
        "Previous Close": round(info.get("previous_close", 0), 2),
    })

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.header("Today's AI Recommendations")
st.info("Next we will add Buy / Hold / Trim / Sell logic.")
