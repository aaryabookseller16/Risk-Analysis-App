import pandas as pd
from portfolio.position import Position
from strategy_engine.returns.returns import calculate_stock_return

def buy_and_hold_portfolio(portfolio_df: pd.DataFrame) -> float:
    """
    Compute Buy & Hold return for a portfolio represented as a DataFrame.

    Args:
        portfolio_df (pd.DataFrame): DataFrame with position data.

    Returns:
        float: Weighted average portfolio return (%).
    """
    total_return = 0.0
    total_weight = 0.0

    for _, row in portfolio_df.iterrows():
        # Create Position object from DataFrame row
        position = Position(
            ticker=row['ticker'],
            allocation_pct=row['allocation_pct'],
            purchase_date=row['purchase_date'],
            end_date=row['end_date'],
            portfolio_value=row['portfolio_value']
        )
        # Calculate return
        _, _, net_return = calculate_stock_return(position)
        weighted_return = row['allocation_pct'] * net_return
        total_return += weighted_return
        total_weight += row['allocation_pct']

    # Normalize in case weights don't sum to 1
    if total_weight == 0:
        return 0.0

    total_return /= total_weight
    print(f"\n📊 Overall Portfolio Return: {total_return:.2f}%")
    return total_return


if __name__ == "__main__":
    data = {
        'ticker': ['TSLA', 'AAPL'],
        'allocation_pct': [0.5, 0.5],
        'purchase_date': ['2023-01-03', '2023-01-03'],
        'end_date': ['2023-01-10', '2023-01-10'],
        'portfolio_value': [10000, 10000]
    }

    portfolio_df = pd.DataFrame(data)
    buy_and_hold_portfolio(portfolio_df)
