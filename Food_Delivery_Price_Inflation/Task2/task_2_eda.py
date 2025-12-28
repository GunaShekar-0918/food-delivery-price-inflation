print("🚀 Task 2 EDA started")

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("food_delivery_price_inflation_cleaned.csv")

print("\nDataset loaded successfully")
print(df.head())

# -----------------------------
# Analysis
# -----------------------------
avg_inflation = df['price_inflation'].mean()
print("\nAverage Price Inflation (₹):", round(avg_inflation, 2))

platform_inflation = df.groupby('delivery_platform')['price_inflation'].mean()
print("\nPlatform-wise Inflation:")
print(platform_inflation)

city_inflation = df.groupby('city')['price_inflation'].mean()
print("\nCity-wise Inflation:")
print(city_inflation)

cuisine_inflation = df.groupby('cuisine_type')['price_inflation'].mean()
print("\nCuisine-wise Inflation:")
print(cuisine_inflation)

# -----------------------------
# Visualization (SAFE METHOD)
# -----------------------------

# Platform-wise bar chart
plt.figure()
plt.bar(platform_inflation.index, platform_inflation.values)
plt.title("Average Price Inflation by Delivery Platform")
plt.xlabel("Delivery Platform")
plt.ylabel("Price Inflation (₹)")
plt.tight_layout()
plt.savefig("platform_wise_inflation.png")
plt.close()

# City-wise bar chart
plt.figure()
plt.bar(city_inflation.index, city_inflation.values)
plt.title("Average Price Inflation by City")
plt.xlabel("City")
plt.ylabel("Price Inflation (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("city_wise_inflation.png")
plt.close()

print("\n✅ Task 2 EDA completed successfully")
print("📊 Charts saved as image files.")
