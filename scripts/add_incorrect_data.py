import pandas as pd
import numpy as np

file_path = '../data/raw/Employee.csv'
df = pd.read_csv(file_path)


def add_missing_and_incorrect_data(df, missing_percentage=0.1):
    n_rows, n_cols = df.shape
    total_values = n_rows * n_cols
    n_missing = int(total_values * missing_percentage)

    np.random.seed(1)
    missing_indices = [(np.random.randint(0, n_rows), np.random.randint(0, n_cols)) for _ in range(n_missing)]

    for row, col in missing_indices:
        if df.dtypes[col] in ['int64', 'float64']:
            df.iloc[row, col] = np.random.randint(-999, 999)
        else:
            df.iloc[row, col] = np.nan if np.random.random() < 0.5 else 'incorrect_value'

    return df

df_with_missing = df.copy()
df_with_missing = add_missing_and_incorrect_data(df_with_missing)

print(df_with_missing.head())

df_with_missing.to_csv('../data/processed/Employee_with_missing_data.csv', index=False)