import pandas as pd

# Load the raw CSV file with all columns as strings
file_name = "ebay_tech_deals.csv"
df = pd.read_csv(file_name, dtype=str)

# Clean the price and original_price columns
def clean_price(price):
    if pd.isna(price) or price.strip() in ["N/A", ""]:
        return None
    price = price.replace("US $", "").replace("$", "").replace(",", "").strip()
    try:
        return float(price)
    except ValueError:
        return None  # Return None if conversion fails


df["price"] = df["price"].apply(clean_price)
df["original_price"] = df["original_price"].apply(clean_price)

# Replace missing original_price with price
df["original_price"].fillna(df["price"], inplace=True)

# Clean the shipping column
def clean_shipping(shipping):
    if pd.isna(shipping) or shipping.strip() == "" or shipping.strip() == "N/A":
        return "Shipping info unavailable"
    return shipping.strip()

df["shipping"] = df["shipping"].apply(clean_shipping)

# Compute discount percentage
def calculate_discount(price, original_price):
    if price is not None and original_price is not None and original_price > 0:
        return round(100 * (original_price - price) / original_price, 2)
    return 0.0

df["discount_percentage"] = df.apply(lambda row: calculate_discount(row["price"], row["original_price"]), axis=1)

# Save the cleaned data
df.to_csv("cleaned_ebay_deals.csv", index=False)

print("Data cleaning complete. Saved as 'cleaned_ebay_deals.csv'.")
