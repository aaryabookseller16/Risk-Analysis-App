from portfolio.position import Position

def calculate_stock_return(position: Position) -> tuple[list[float], list[float], float]:
    """
    Calculate Buy & Hold return for a single Position.

    Args:
        position (Position): Stock position object.

    Returns:
        stock_info (list): [purchase_price, sell_price]
        position_info (list): [initial_value, final_value]
        net_return (float): % return over the holding period
    """
    ticker = position.ticker
    purchase_price = position.purchase_price
    sell_price = position.sell_price

    print(f"You bought {ticker} at ${purchase_price:.2f}")
    print(f"You sold {ticker} at ${sell_price:.2f}")

    initial_value = position.get_value_on(position.purchase_date)
    final_value = position.get_value_on(position.end_date)

    print(f"Initial position value: ${initial_value:.2f}")
    print(f"Final position value:   ${final_value:.2f}")

    net_return = ((final_value - initial_value) / initial_value) * 100

    stock_info = [purchase_price, sell_price]
    position_info = [initial_value, final_value]

    return stock_info, position_info, net_return

if __name__ == '__main__':
    position = Position(
        ticker="TSLA",
        allocation_pct=0.5,
        purchase_date="2023-01-03",
        end_date="2023-01-10",
        portfolio_value=10000
    )
    
    stock_info, position_info, net_return = calculate_stock_return(position)
    
    print(f"\n📈 Your net return for {position.ticker} = {net_return:.2f}%")
