import streamlit as st

st.set_page_config(
    page_title="MarketPilot AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Sidebar ----------
st.sidebar.title("📈 MarketPilot AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Portfolio",
        "Opportunity Scanner",
        "Watchlist",
        "Research Center",
        "Trade Journal",
        "Settings"
    ]
)

# ---------- Dashboard ----------
if page == "Dashboard":

    st.title("📈 MarketPilot AI")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Portfolio Value", "$44,183")
    col2.metric("Today's P/L", "-$487")
    col3.metric("Cash Available", "$11,127")
    col4.metric("Portfolio Grade", "A-")

    st.divider()

    left, right = st.columns([2,1])

    with left:

        st.subheader("Today's Action Center")

        st.info("🟢 Buy Opportunity: MU")
        st.warning("🟠 Watch: IONQ")
        st.error("🔴 Risk: RKLB")
        st.success("✅ Hold: NVDA")

    with right:

        st.subheader("Market Status")

        st.write("S&P 500")
        st.progress(.62)

        st.write("NASDAQ")
        st.progress(.73)

        st.write("AI Sector")
        st.progress(.91)

# ---------- Other Pages ----------
else:
    st.title(page)
    st.write("Coming Soon...")
