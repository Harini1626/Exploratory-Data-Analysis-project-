# Exploratory Data Analysis (EDA) Project
# Internship Task

import pandas as pd
import matplotlib.pyplot as plt
import os

print("===================================")
print(" EXPLORATORY DATA ANALYSIS PROJECT")
print("===================================")

# Load dataset
file_path = input("Enter your CSV file name: ")

df = pd.read_csv(file_path)

# Create output folder
os.makedirs("output", exist_ok=True)

# 1. Dataset Preview
print("\n--- Dataset Preview ---")
print(df.head())

# 2. Dataset Information
print("\n--- Dataset Information ---")
print(df.info())

# 3. Statistical Summary
print("\n--- Statistical Summary ---")
print(df.describe())

# 4. Missing Values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 5. Duplicate Rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# 6. Save Statistical Summary
df.describe().to_csv("output/statistical_summary.csv")

# 7. Missing Values Visualization
missing = df.isnull().sum()

if missing.sum() > 0:
    missing.plot(kind="bar", figsize=(8, 5))
    plt.title("Missing Values")
    plt.xlabel("Columns")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("output/missing_values.png")
    plt.show()

# 8. Histograms for Numerical Columns
numeric_columns = df.select_dtypes(include="number")

if not numeric_columns.empty:
    numeric_columns.hist(figsize=(12, 8), bins=20)
    plt.suptitle("Numerical Data Distribution")
    plt.tight_layout()
    plt.savefig("output/histograms.png")
    plt.show()

# 9. Correlation Analysis
if len(numeric_columns.columns) >= 2:
    correlation = numeric_columns.corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(correlation, aspect="auto")
    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=45
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("output/correlation.png")
    plt.show()

    print("\n--- Correlation Matrix ---")
    print(correlation)

# 10. Categorical Data Analysis
categorical_columns = df.select_dtypes(include="object")

for column in categorical_columns.columns[:5]:
    df[column].value_counts().head(10).plot(kind="bar", figsize=(8, 5))

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()

    plt.savefig(f"output/{column}_chart.png")
    plt.show()

# 11. Remove Duplicate Rows
cleaned_df = df.drop_duplicates()

cleaned_df.to_csv("output/cleaned_dataset.csv", index=False)

# 12. Generate Report
with open("output/EDA_Report.txt", "w") as report:

    report.write("EXPLORATORY DATA ANALYSIS REPORT\n")
    report.write("===============================\n\n")

    report.write(f"Dataset Shape: {df.shape}\n\n")

    report.write("Column Names:\n")
    report.write(str(list(df.columns)) + "\n\n")

    report.write("Missing Values:\n")
    report.write(str(df.isnull().sum()) + "\n\n")

    report.write("Duplicate Rows:\n")
    report.write(str(df.duplicated().sum()) + "\n\n")

    report.write("Statistical Summary:\n")
    report.write(str(df.describe()) + "\n")

print("\n===================================")
print("EDA ANALYSIS COMPLETED SUCCESSFULLY")
print("Check the output folder!")
print("===================================")
