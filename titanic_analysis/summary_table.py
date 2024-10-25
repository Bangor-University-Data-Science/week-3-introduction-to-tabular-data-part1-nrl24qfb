import pandas as pd

def create_summary_table(df):
    # Create a new DataFrame to hold the summary information
    summary_df = pd.DataFrame({
        'Feature Name': df.columns,  # Column names
        'Data Type': [df[col].dtype for col in df.columns],  # Data type for each column
        'Number of Unique Values': [df[col].nunique() for col in df.columns],  # Number of unique values for each column
        'Has Missing Values?': [df[col].isnull().any() for col in df.columns]  # Check if any column has missing values
    })
    
    # Ensure the columns are in the correct order
    summary_df = summary_df[['Feature Name', 'Data Type', 'Number of Unique Values', 'Has Missing Values?']]
    
    # Debug: Print column names for verification
    print("Columns in summary_df:", summary_df.columns.tolist())
    
    # Return the summary DataFrame containing the required information
    return summary_df