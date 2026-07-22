import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

# Page Configuration
st.set_page_config(page_title="CAPM Web Application", page_icon="📈", layout="wide")

# Main Header
st.title("Capital Asset Pricing Model (CAPM) Calculator")
st.markdown("Calculate the expected return of any publicly traded asset based on market risk.")

# Sidebar for User Input
st.sidebar.header("User Inputs")

# 1. Market Selection Toggle
market_choice = st.sidebar.radio("Select Market Benchmark", ("US (S&P 500)", "India (Nifty 50)"))

# 2. Dynamic Inputs based on Market
if market_choice == "US (S&P 500)":
    ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    market_ticker = '^GSPC'
    default_rf = 4.63
else:
    ticker = st.sidebar.text_input("Enter Stock Ticker (Add .NS for NSE)", "RELIANCE.NS")
    market_ticker = '^NSEI'
    default_rf = 6.81

time_horizon = st.sidebar.slider("Select Time Horizon (Years)", 1, 10, 5)
user_rf_rate = st.sidebar.number_input("Risk-Free Rate (%)", value=default_rf, step=0.1)

# Calculate Dates
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=time_horizon * 365)

st.write(f"### Fetching historical data for **{ticker}** from {start_date} to {end_date}...")

# Fetch Data Button
if st.sidebar.button("Run CAPM Analysis"):
    try:
        # Extract data for the Stock and the Selected Market
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        market_data = yf.download(market_ticker, start=start_date, end=end_date)
        
        # SQUEEZE FIX: Flatten the multi-level API data
        stock_close = stock_data['Close'].squeeze()
        market_close = market_data['Close'].squeeze()
        
       # Display Line Chart
        st.write(f"#### {ticker} Historical Closing Prices")
        
        chart_df = pd.DataFrame({"Price": stock_close})
        chart_df = chart_df.dropna()
        
        # Strip the timezone metadata
        if chart_df.index.tz is not None:
            chart_df.index = chart_df.index.tz_localize(None)
            
        st.line_chart(chart_df)
        
        # Calculate Daily Returns
        stock_returns = stock_close.pct_change().dropna()
        market_returns = market_close.pct_change().dropna()
        
        # Align the data into a single table
        returns_df = pd.concat([stock_returns, market_returns], axis=1, join='inner')
        returns_df.columns = ['Stock', 'Market']
        
        # Calculate Beta 
        covariance = returns_df.cov().iloc[0, 1]
        market_variance = returns_df['Market'].var()
        beta = float(covariance / market_variance)
        
        # Convert User Risk-Free Rate to decimal
        rf_rate = user_rf_rate / 100
        
        # Calculate Expected Market Return
        expected_market_return = float(market_returns.mean()) * 252
        
        # Execute the CAPM Formula
        expected_stock_return = rf_rate + beta * (expected_market_return - rf_rate)
        
        # Display the final metrics
        st.write("### CAPM Calculation Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Beta (β)", f"{beta:.2f}")
        col2.metric("Risk-Free Rate", f"{user_rf_rate:.2f}%")
        col3.metric("Expected Return", f"{expected_stock_return * 100:.2f}%")
        
        st.success("Analysis Complete!")
        
    except Exception as e:
        st.error(f"Error computing data: {e}. Please ensure the ticker symbol is correct.")