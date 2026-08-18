import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from preprocessing import load_data
from preprocessing import identify_features
from feature_selection import feature_selector

DATA_PATH = "C:/VITP Academics/Sem 5/MLOps/Assignment 3/data/titanic.csv"
TARGET = "Survived"

df = load_data(DATA_PATH)
df = df.drop_duplicates()

X, y, numerical_features, categorical_features = identify_features(df, TARGET)

numerical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)
    ]
)

selector = feature_selector(k=10)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("selector", selector)
    ]
)

X_processed = pipeline.fit_transform(X, y)

print("Original Shape :", X.shape)
print("Transformed Shape :", X_processed.shape)

processed_df = pd.DataFrame(X_processed)
processed_df.to_csv(
    "../output/transformed_data.csv",
    index=False
)
print("\nTransformed Dataset Saved.")

joblib.dump(
    pipeline,
    "../models/feature_pipeline.pkl"
)

print("Pipeline Saved Successfully.")

loaded_pipeline = joblib.load(
    "../models/feature_pipeline.pkl"
)

sample = X.head(5)
sample_transformed = loaded_pipeline.transform(sample)

print("\nPipeline Loaded Successfully.")
print("Sample Data Transformed Successfully.")
print(sample_transformed)