import streamlit as st

st.set_page_config(
    page_title="Heather's AI Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Heather's AI Trading Dashboard")

st.success("Dashboard is working!")

st.header("Portfolio")

st.write("This is where your Fidelity portfolio will appear.")

st.header("Today's AI Recommendations")

st.info("No recommendations yet. We'll add the AI engine next.")
