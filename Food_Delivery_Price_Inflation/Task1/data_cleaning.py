import pandas as pd

# Load dataset with correct encoding
df = pd.read_csv("food_delivery_price_inflation_raw.csv", encoding="latin1")

# Rename columns EXACTLY based on your CSV file
df = df.rename(columns={
    'Restaurant Name': 'restaurant_name',
    'Food Item': 'food_item',
    'Dine-in Price (?)': 'dine_in_price',
    'App Price (?)': 'app_price',
    'Discount Shown (%)': 'discount_shown',
    'Delivery Platform': 'delivery_platform',
    'City': 'city',
    'Cuisine Type': 'cuisine_type'
})

# Remove duplicate rows
df = df.drop_duplicates()

# Remove invalid prices
df = df[(df['dine_in_price'] > 0) & (df['app_price'] > 0)]

# Calculate price inflation
df['price_inflation'] = df['app_price'] - df['dine_in_price']

# Calculate actual discount percentage
df['actual_discount_percent'] = round(
    ((df['dine_in_price'] - df['app_price']) / df['dine_in_price']) * 100, 2
)

# Create inflation flag
df['inflation_flag'] = df['price_inflation'].apply(
    lambda x: 'Inflated Price' if x > 0 else 'No Inflation'
)

# Save cleaned dataset
df.to_csv("food_delivery_price_inflation_cleaned.csv", index=False)

print("✅ Task 1 data cleaning completed successfully.")
