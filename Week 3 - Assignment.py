# ==========================================
# GENERIC NUMPY + PANDAS DATA PROCESSING
# No hardcoded column names
# ==========================================

import pandas as pd
import numpy as np

# -------------------------------
# 1. LOAD DATA (USER INPUT FILE)
# -------------------------------
file_path = input("Enter file path (CSV/Excel): ")

# Detect file type automatically
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format")
    exit()

print("\nOriginal Dataset:\n")
print(df)


# -------------------------------
# 2. HANDLE MISSING VALUES
# -------------------------------

# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(exclude=np.number).columns

for col in categorical_cols:
    if not df[col].mode().empty:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nAfter Handling Missing Values:\n")
print(df)


# -------------------------------
# 3. NUMPY ANALYSIS (ALL NUMERIC)
# -------------------------------

print("\nNumPy Statistics:\n")

for col in numeric_cols:
    arr = df[col].to_numpy()
    print(f"{col}:")
    print(" Mean:", np.mean(arr))
    print(" Max :", np.max(arr))
    print(" Min :", np.min(arr))
    print("-" * 30)


# -------------------------------
# 4. AUTOMATIC AGGREGATION
# -------------------------------

# If categorical column exists, group by first one
if len(categorical_cols) > 0:
    group_col = categorical_cols[0]
    
    grouped = df.groupby(group_col)[numeric_cols].mean()
    
    print(f"\nGrouped by '{group_col}' (Average):\n")
    print(grouped)


# -------------------------------
# 5. FEATURE ENGINEERING
# -------------------------------

# Create High/Low columns dynamically
for col in numeric_cols:
    df[col + "_Level"] = np.where(df[col] > df[col].mean(), "High", "Low")

print("\nDataset with New Features:\n")
print(df)


# -------------------------------
# 6. SAVE OUTPUT
# -------------------------------

output_file = "cleaned_output.csv"
df.to_csv(output_file, index=False)

print(f"\nCleaned dataset saved as '{output_file}'")