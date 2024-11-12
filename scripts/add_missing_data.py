import pandas as pd
import numpy as np
import os

file_path = '../data/raw/Employee.csv'
output_path = '../data/processed/Employee_with_missing_data.csv'

df = pd.read_csv(file_path)

# Dodanie brakujących danych (ok. 10%)
missing_indices = df.sample(frac=0.1).index

for col in df.columns:
    if df[col].dtype == 'object':  # Dla kolumn tekstowych
        df.loc[missing_indices, col] = np.nan
    else:  # Dla kolumn liczbowych
        df.loc[missing_indices, col] = np.nan

os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Przetworzony plik został zapisany do {output_path}")