import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Year"] = df["Date"].dt.year
df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)

print("=== AOV by region ===")
aov = df.groupby("Region").apply(lambda g: g["Revenue"].sum()/g["OrderID"].nunique())
print(aov.sort_values(ascending=False))

print("\n=== Quarterly revenue & profit ===")
q = df.groupby("Quarter").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
print(q)
q.to_csv("quarterly_summary.csv")

print("\n=== Totals ===")
print("Orders:", df["OrderID"].nunique())
print("Revenue:", df["Revenue"].sum())
print("Profit:", df["Profit"].sum())
print("Overall margin:", df["Profit"].sum()/df["Revenue"].sum()*100)
print("AOV:", df["Revenue"].sum()/df["OrderID"].nunique())

print("\n=== Product summary (revenue, units, profit, margin) ===")
prod = df.groupby("Product").agg(Revenue=("Revenue","sum"), Units=("Quantity","sum"), Profit=("Profit","sum"))
prod["AvgPrice"] = (prod["Revenue"]/prod["Units"]).round(2)
prod["Margin%"] = (prod["Profit"]/prod["Revenue"]*100).round(1)
prod = prod.sort_values("Revenue", ascending=False)
print(prod)
prod.to_csv("product_summary.csv")

print("\n=== Category summary ===")
cat = df.groupby("Category").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
cat["Margin%"] = (cat["Profit"]/cat["Revenue"]*100).round(1)
cat = cat.sort_values("Revenue", ascending=False)
print(cat)
cat.to_csv("category_revenue.csv")

print("\n=== Region summary ===")
region = df.groupby("Region").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
region["Margin%"] = (region["Profit"]/region["Revenue"]*100).round(1)
region["AOV"] = aov
region = region.sort_values("Revenue", ascending=False)
print(region)
region.to_csv("region_revenue.csv")

print("\n=== Region x Category matrix (revenue) ===")
pivot = df.pivot_table(index="Region", columns="Category", values="Revenue", aggfunc="sum", fill_value=0)
print(pivot)
pivot.to_csv("region_category_pivot.csv")

monthly = df.groupby("Month").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
monthly.to_csv("monthly_revenue.csv")
print("\n=== Monthly (last 6) ===")
print(monthly.tail(6))
