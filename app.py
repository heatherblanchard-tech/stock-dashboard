import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Heather's AI Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Heather's AI Trading Dashboard")
st.success("Dashboard is live and analyzing stocks!")

tickers = ["NVDA", "AVGO", "MU", "IONQ", "RGTI", "CEG", "FCX", "AMD", "NET"]

data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.fast_info

    last_price = info.get("last_price", 0)
    day_high = info.get("day_high", 0)
    day_low = info.get("day_low", 0)
    previous_close = info.get("previous_close", 0)

    if previous_close and last_price:
        day_change_percent = ((last_price - previous_close) / previous_close) * 100
    else:
        day_change_percent = 0

    if day_change_percent <= -3:
        rating = "🟢 Possible Buy"
    elif day_change_percent >= 5:
        rating = "🟠 Consider Trim"
    else:
        rating = "🟡 Hold / Watch"

    data.append({
        "Ticker": ticker,
        "Last Price": round(last_price, 2),
        "Day Change %": round(day_change_percent, 2),
        "Day High": round(day_high, 2),
        "Day Low": round(day_low, 2),
        "Recommendation": rating
    })

df = pd.DataFrame(data)

st.header("Live Watchlist")
st.dataframe(df, use_container_width=True)

st.header("How to read this")
st.write("🟢 Possible Buy = down 3% or more today")
st.write("🟡 Hold / Watch = normal movement")
st.write("🟠 Consider Trim = up 5% or more today")
