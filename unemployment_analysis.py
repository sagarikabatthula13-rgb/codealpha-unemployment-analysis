import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Basic information
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Average unemployment by region
avg_unemployment = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean()

print("\nAverage Unemployment Rate by Region:")
print(avg_unemployment.sort_values(ascending=False))

# Plot unemployment trend
plt.figure(figsize=(10,5))
plt.plot(
    df["Date"],
    df["Estimated Unemployment Rate (%)"]
)
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()