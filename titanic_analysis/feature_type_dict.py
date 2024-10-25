def create_feature_type_dict(df):
    # Initialize the dictionary to hold feature types
    feature_types = {
        'numerical': {
            'continuous': ['Age', 'Fare'],  # Age and Fare are continuous numerical features
            'discrete': ['SibSp', 'Parch']  # SibSp and Parch are discrete numerical features
        },
        'categorical': {
            'nominal': ['Sex', 'Embarked'],  # Sex and Embarked are nominal categorical features
            'ordinal': ['Pclass']  # Pclass is an ordinal categorical feature
        }
    }
    
    return feature_types
