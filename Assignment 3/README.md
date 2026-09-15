# Assignment 3: Preprocessing Pipeline

This assignment builds a scikit-learn pipeline for the Titanic dataset. It
identifies numerical and categorical features, imputes missing values, scales
numeric columns, one-hot encodes categorical columns, and selects the ten best
features.

## Contents

- `src/`: preprocessing, feature selection, and pipeline code.
- `data/titanic.csv`: input dataset.
- `models/feature_pipeline.pkl`: serialized fitted pipeline.
- `output/transformed_data.csv`: transformed feature data.
- `terminal.txt`: captured execution notes.

Run `src/pipeline.py` from this assignment after adjusting its dataset path for
the local machine.