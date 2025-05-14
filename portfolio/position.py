from data.fetcher import fetch_stock_price
import logging

class Position:
    """
    Represents a single stock position in a portfolio.
    Calculates number of shares purchased and can get value on a future date.
    """

    def __init__(self, ticker: str, allocation_pct: float, purchase_date: str, end_date : str, portfolio_value: int) -> None:
        """
        Initializes the Position object.

        Args:
            ticker (str): Stock symbol.
            allocation_pct (float): Percentage of portfolio value allocated (0 < x ≤ 1).
            purchase_date (str): Date when the stock was bought.
            portfolio_value (int): Total value of the portfolio in dollars.
        """
        if not (0 < allocation_pct <= 1):
            raise ValueError(f"Invalid allocation_pct: {allocation_pct}. Must be > 0 and ≤ 1.")

        self.ticker = ticker
        self.allocation_pct = allocation_pct
        self.purchase_date = purchase_date
        self.portfolio_value = portfolio_value
        self.end_date = end_date

        # Fetch price data on the purchase date
        price_df = fetch_stock_price(ticker=ticker, start=purchase_date, end= end_date)

        # Error if price data isn't found
        if price_df.empty:
            raise ValueError(f"No price data found for {ticker} on {purchase_date}")

        # Use the first available price (there should only be one)
        self.purchase_price = price_df.iloc[0].item()

        # Calculate how many shares were bought = (allocation % * total value) / price per share
        self._shares = (allocation_pct * portfolio_value) / self.purchase_price

    @property
    def shares(self) -> float:
        """Return the number of shares purchased."""
        return self._shares

    def get_value_on(self, date: str) -> float:
        """
        Get the value of this position on a specific date.

        Args:
            date (str): Date in 'YYYY-MM-DD'.

        Returns:
            float: Value of this position on that day.
        """
        df = fetch_stock_price(ticker=self.ticker, start=date, end = self.end_date) #call fetch stock price for that particular time and date

        if df.empty:
            logging.warning(f"No price data for {self.ticker} on {date}")
            return 0.0

        # Try to get exact match by date
        try:
            price = df.loc[date].item()
        except KeyError:
            # Fallback: use first available row (usually same day)
            logging.warning(f"{date} not found. Using first available price.")
            price = df.iloc[0].item()

        return price * self.shares
