import pandas as pd

def normalize_prices(price_df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize asset prices to 1.0 at the first date for comparison across assets.
    
    Parameters:
        price_df (pd.DataFrame): DataFrame with datetime index and each column representing an asset's price.
        
    Returns:
        pd.DataFrame: Normalized price DataFrame where each column starts at 1.0.
    """
    # Divide each price series by its first value
    first_price =  price_df.iloc[0] 
    return price_df.divide(first_price)


    """"
    Future work: z-score normalizer, normalizing according to the starting price etc
    """
