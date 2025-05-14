import yfinance as yf
import pandas as pd
import logging
import os

from pathlib import Path
from datetime import datetime, timedelta

def fetch_stock_price(ticker: str, start: str, end: str = None, save_path: str = "data/raw") -> pd.DataFrame:
    """
    Fetch historical adjusted close prices for a stock using Yahoo Finance API.

    Args:
        ticker (str): Stock symbol (e.g., 'AAPL').
        start (str): Start date in 'YYYY-MM-DD'.
        end (str, optional): End date. If None, fetch only from start.
        save_path (str): Directory where CSV will be saved.

    Returns:
        pd.DataFrame: Series of adjusted close prices.
    """
    try:
        # Fetch data using yfinance
        if end:
            df = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
        else:
            df = yf.download(ticker, start=start, progress=False, auto_adjust=False)

        # If no data returned
        if df.empty:
            logging.warning(f"No data available for {ticker} from {start} to {end}")
            return pd.DataFrame()

        # Reset index to expose 'Date' column
        df.reset_index(inplace=True)
        df = df.sort_values("Date")

        # Save the data to CSV for caching/reproducibility
        Path(save_path).mkdir(parents=True, exist_ok=True)
        file_path = os.path.join(save_path, f"{ticker}.csv")
        df.to_csv(file_path, index=False)

        # Return only the adjusted close column
        return df['Adj Close']

    except Exception:
        logging.error(f"Error fetching {ticker}", exc_info=True)
        return pd.DataFrame()
