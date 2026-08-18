import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully")
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nDataset Shape:")
    print(df.shape)
    print("\nDataset Information:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())
    return df


def identify_features(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    print("\nNumerical Features:")
    print(numerical_features)
    print("\nCategorical Features:")
    print(categorical_features)
    return X, y, numerical_features, categorical_features