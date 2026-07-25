import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M")
df["Year"] = df["Date"].dt.year

print("=== 1. REVENUE & PROFIT TREND OVER TIME ===")
monthly = df.groupby("Month").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
print(monthly.tail(6))
print()

print("=== 2. TOP-SELLING PRODUCTS (by revenue) ===")
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(top_products.head(5))
print()

print("=== 3. TOP-SELLING PRODUCTS (by units sold) ===")
top_units = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(top_units.head(5))
print()

print("=== 4. HIGH-VALUE CATEGORIES (revenue & profit margin) ===")
cat = df.groupby("Category").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
cat["Margin%"] = (cat["Profit"]/cat["Revenue"]*100).round(1)
print(cat.sort_values("Revenue", ascending=False))
print()

print("=== 5. REGIONAL PERFORMANCE (revenue & profit) ===")
region = df.groupby("Region").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
region["Margin%"] = (region["Profit"]/region["Revenue"]*100).round(1)
print(region.sort_values("Revenue", ascending=False))
print()

print("=== 6. YEAR OVER YEAR GROWTH ===")
yearly = df.groupby("Year").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
print(yearly)
growth = (yearly["Revenue"].iloc[1] - yearly["Revenue"].iloc[0]) / yearly["Revenue"].iloc[0] * 100
print(f"Revenue YoY growth: {growth:.1f}%")

print("\n=== 7. OVERALL PROFIT MARGIN ===")
print(f"{df['Profit'].sum()/df['Revenue'].sum()*100:.1f}%")
