from portfolio.position import Position

if __name__ == "__main__":
    # Initialize a position in Apple with 25% of a $100,000 portfolio
    aapl = Position(
        ticker="AAPL",
        allocation_pct=0.25,
        purchase_date="2024-12-15",
        end_date = "2024-12-21",
        portfolio_value=100000
    )

    # Print number of shares purchased
    print(f"Shares bought: {aapl.shares:.2f}")

    # Print the value of the position on a later date
    print(f"Value on {aapl.purchase_date}: ${aapl.get_value_on(aapl.purchase_date):.2f}")
