def get_numerical_df(df, numerical_features):
    # Filter the dataframe to include only the numerical features
    numerical_df = df[numerical_features]
    
    # Return the filtered dataframe
    return numerical_df