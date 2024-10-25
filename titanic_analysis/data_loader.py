import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    Args:
        filepath (str): Path to the Titanic CSV file.
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv("titanic.csv")
    
    # Return the loaded DataFrame
    return df