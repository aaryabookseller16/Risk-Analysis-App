'''
Goal: is to create a portfolio
- can hold multiple Positions (probably in a dataframe)
'''
from portfolio.position import Position
import pandas as pd

class Portfolio:
    """
    Represents a financial portfolio consisting of multiple stock positions.

    Attributes:
        principal (float): Total capital available for investment.
        total_allocation (float): Cumulative allocation percentage used (0–1).
        positions (pd.DataFrame): Tabular summary of all added positions.
            Columns: ["Stock", "Value", "Allocation", "Allocation_Value"]
    """

    def __init__(self, principal : float):
        """
        Initialize a new portfolio with a given principal amount.

        Args:
            principal (float): The total capital allocated to this portfolio.
    """
        self.total_allocation = 0.0 # tracks how much % is being used 
        self.positions  = pd.DataFrame(columns= ["Stock", "Value", "Allocation", "Allocation_Value"]) # a df to store different positions
        self.principal = principal #total amount of money in the portfolio


    def add_position(self, position : Position) -> pd.DataFrame:
        """
        Add a new stock position to the portfolio.

        Args:
            position (Position): A Position object containing stock details.

        Returns:
            pd.DataFrame: Updated DataFrame of all positions.

        Raises:
            ValueError: If total allocation exceeds 100%.
        """

        #make sure that we cannot buy more than our principal
        if self.total_allocation + position.allocation_pct > 1.0:
            raise ValueError(f"allocation_pct exceeds total value")

        #append to self.positions
        self.total_allocation += position.allocation_pct #update new allocation

        #allocation value of that stock
        allocation_value = position.get_value_on(position.purchase_date)

        new_row = pd.DataFrame(
        [[position.ticker, position.purchase_price, position.allocation_pct, allocation_value]], 
        columns =["Stock", "Value", "Allocation", "Allocation_Value"] 
        )
        self.positions = pd.concat([self.positions, new_row], ignore_index= True)
        
        return self.positions

    
    def remaining_amount(self,position : Position) -> float:
        """
        Calculate how much capital remains after allocating funds to a given position.

        Args:
            position (Position): The position whose allocation is being evaluated.

        Returns:
            float: Remaining investable capital after adding this position.
        """

        amt = self.principal *(1- position.allocation_pct)

        return amt

        
if __name__ == "__main__":
    from portfolio.position import Position
    from portfolio.portfolio import Portfolio

    # Step 1: Create Portfolio
    portfolio = Portfolio(principal=10000)

    # Step 2: Create a Position
    position = Position(
        ticker="TSLA",
        allocation_pct=0.5,
        purchase_date="2023-01-01",
        end_date="2023-01-10",
        portfolio_value=10000
    )
    
    # Step 3: Add position to portfolio
    result = portfolio.add_position(position)

    # Step 4: Print portfolio summary
    print("\n✅ Portfolio after adding position:")
    print(result)
    print("\nTotal Allocation Used:", portfolio.total_allocation)
    print("Principal = ", portfolio.principal)

