# ==========================================
# WEEK 4: DATA VISUALIZATION PROJECT
# ==========================================
# Objective:
# Create visualizations for dataset analysis
# using scatter plots, histograms, bar charts,
# correlation heatmaps, and dashboard layout.
#
# Concepts Used:
# - Pandas
# - NumPy
# - Matplotlib
# - Dataset Analysis
# - Data Visualization
# ==========================================

# -------------------------------
# Import Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Create Sample Dataset
# -------------------------------
np.random.seed(10)

data = {
    "Age": np.random.randint(20, 60, 100),
    "Salary": np.random.randint(30000, 120000, 100),
    "Experience": np.random.randint(1, 20, 100),
    "PerformanceScore": np.random.randint(50, 100, 100),
    "Department": np.random.choice(
        ["HR", "IT", "Finance", "Sales"],
        100
    )
}

df = pd.DataFrame(data)

# -------------------------------
# Display First 5 Rows
# -------------------------------
print("\n===== DATASET =====")
print(df.head())

# -------------------------------
# Dataset Information
# -------------------------------
print("\n===== DATASET INFO =====")
print(df.info())

# -------------------------------
# Statistical Summary
# -------------------------------
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# ==========================================
# DASHBOARD CREATION
# ==========================================

# Create Figure
plt.figure(figsize=(15, 10))

# ------------------------------------------
# 1. Scatter Plot
# Relationship between Experience & Salary
# ------------------------------------------
plt.subplot(2, 2, 1)
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

# ------------------------------------------
# 2. Histogram
# Salary Distribution
# ------------------------------------------
plt.subplot(2, 2, 2)
plt.hist(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

# ------------------------------------------
# 3. Bar Chart
# Average Salary by Department
# ------------------------------------------
plt.subplot(2, 2, 3)

avg_salary = df.groupby("Department")["Salary"].mean()

plt.bar(avg_salary.index, avg_salary.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# ------------------------------------------
# 4. Correlation Heatmap
# ------------------------------------------
plt.subplot(2, 2, 4)

correlation = df[
    ["Age", "Salary", "Experience", "PerformanceScore"]
].corr()

plt.imshow(correlation)

plt.xticks(range(len(correlation.columns)),
           correlation.columns,
           rotation=45)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Correlation Heatmap")

# Add correlation values
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(
            j,
            i,
            round(correlation.iloc[i, j], 2),
            ha='center',
            va='center'
        )

# ------------------------------------------
# Adjust Layout
# ------------------------------------------
plt.tight_layout()

# ------------------------------------------
# Show Dashboard
# ------------------------------------------
plt.show()

# ==========================================
# SUMMARY OF CONCEPTS LEARNED
# ==========================================

print("\n===== CONCEPTS LEARNED =====")

concepts = [
    "1. Creating datasets using Pandas and NumPy",
    "2. Data analysis using describe() and info()",
    "3. Scatter plots for relationship analysis",
    "4. Histograms for distribution analysis",
    "5. Bar charts for categorical comparison",
    "6. Correlation heatmap for feature relationships",
    "7. Building dashboards using Matplotlib subplots"
]

for concept in concepts:
    print(concept)

print("\nProject Completed Successfully!")