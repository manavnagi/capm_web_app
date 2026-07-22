# Capital Asset Pricing Model (CAPM) Web Application

## 📌 Project Overview
A fully interactive financial web application deployed via Streamlit that calculates the expected return of publicly traded assets utilizing the Capital Asset Pricing Model (CAPM). The tool features dynamic dual-market support, allowing users to benchmark equities against both US (S&P 500) and Indian (Nifty 50) markets.

**Live Application:** [[Insert Streamlit Link Here](https://capmwebapp-manavnagi.streamlit.app/)]

## 🛠️ Technology Stack
*   **Frontend & Hosting:** Python (Streamlit)
*   **Data Extraction:** Yahoo Finance API (`yfinance`)
*   **Data Processing & Mathematics:** Pandas, NumPy
*   **Visualization:** Streamlit Native Charts

## 🏗️ Application Architecture
1.  **Dynamic Data Ingestion:** Connects directly to the Yahoo Finance API to extract historical closing prices for user-defined equities, market indices (`^GSPC`, `^NSEI`), and risk-free rates (`^TNX`).
2.  **Financial Mathematics Engine:** Calculates daily percentage returns and computes the asset's Beta ($\beta$) by determining the covariance of the stock's returns against the market index.
3.  **Cross-Market Logic:** Implements conditional  routing to ensure Indian equities (.NS) are properly benchmarked against the Nifty 50 and localized risk-free rates rather than US metrics.
4.  **UI/UX:** Features an interactive sidebar for dynamic variable adjustment (time horizons, risk-free rates) with automatic, timezone-adjusted chart rendering to visualize historical asset volatility.

## 💡 Financial Impact
*   **Investment Analysis:** Allows analysts to rapidly determine if an asset is historically overvalued or undervalued relative to its risk profile.
*   **Portfolio Management:** Simplifies the extraction of Beta ($\beta$) metrics, vital for understanding how a specific asset reacts to broader market swings.

---
*Author: Manav Nagi*