from data.mongo import get_collection
from portfolio.position import Position
from datetime import datetime

def main():
    while True:
        ans = input("Would you like to add a new stock to your portfolio (y/n) :")
        if ans.lower() == 'y:'
            username = input("Enter your username: ")
            portfolio_name = input("Enter portfolio name: ")
            ticker = input("Enter stock ticker: ")
            allocation_pct = float(input("Enter allocation percentage (0 < x <= 1): "))
            portfolio_value = float(input("Enter total portfolio value: "))
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            cash_balance = float(input("Enter remaining cash balance: "))
        else:
            break

    # Create Position object
    position = Position(ticker, allocation_pct, purchase_date, end_date, portfolio_value)

    # Prepare document to save
    collection = get_collection("portfolios")
    document = {
        "user_id": username,
        "portfolio_name": portfolio_name,
        "created_at": datetime.now(),
        "positions": [
            {
                "ticker": position.ticker,
                "allocation_pct": position.allocation_pct,
                "purchase_price": position.purchase_price,
                "shares": position.shares,
                "purchase_date": position.purchase_date,
                "end_date": position.end_date
            }
        ],
        "cash_balance": cash_balance
    }

    # Insert into MongoDB
    result = collection.insert_one(document)
    print(f"Portfolio saved with ID: {result.inserted_id}")

if __name__ == "__main__":
    main()
