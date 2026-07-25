import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["font.family"] = "DejaVu Sans"

FOREST = "#1B7A5C"
GOLD = "#B8862B"
RUST = "#C2542A"
INK = "#182238"
SOFT = "#5A6478"
PALETTE = ["#1B7A5C","#3F9C7C","#B8862B","#D9A54A","#C2542A","#D98963","#7C8AA6"]

df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

total_sales = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
total_qty = df["Quantity"].sum()
margin = total_profit/total_sales*100

fig = plt.figure(figsize=(16, 11))
gs = gridspec.GridSpec(4, 4, height_ratios=[0.55, 1.3, 1.3, 1.3], hspace=0.55, wspace=0.35)

# ---- Title ----
fig.text(0.06, 0.965, "Business Sales Performance Dashboard", fontsize=22, fontweight="bold", color=INK)
fig.text(0.06, 0.945, "Future Interns · Data Science & Analytics · Task 01  |  Jan 2024 – Dec 2025", fontsize=10.5, color=SOFT)

# ---- KPI cards ----
kpis = [
    ("TOTAL SALES", f"${total_sales:,.0f}", FOREST),
    ("TOTAL PROFIT", f"${total_profit:,.0f}", GOLD),
    ("TOTAL ORDERS", f"{total_orders:,}", FOREST),
    ("TOTAL QUANTITY", f"{total_qty:,}", FOREST),
]
for i, (label, value, color) in enumerate(kpis):
    ax = fig.add_subplot(gs[0, i])
    ax.axis("off")
    ax.add_patch(plt.Rectangle((0,0), 0.02, 1, transform=ax.transAxes, color=color, clip_on=False))
    ax.text(0.08, 0.75, label, fontsize=9.5, color=SOFT, transform=ax.transAxes, fontweight="bold")
    ax.text(0.08, 0.25, value, fontsize=20, color=INK, transform=ax.transAxes, fontweight="bold", family="monospace")
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    for spine in ax.spines.values():
        spine.set_visible(True); spine.set_color("#D7DEEA")

# ---- Monthly trend (sales + profit) ----
ax1 = fig.add_subplot(gs[1, 0:2])
monthly = df.groupby("Month").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
ax1.plot(monthly.index, monthly["Revenue"], marker="o", color=FOREST, linewidth=2, markersize=3, label="Sales")
ax1.plot(monthly.index, monthly["Profit"], marker="o", color=RUST, linewidth=2, markersize=3, label="Profit")
ax1.set_title("Monthly Sales & Profit Trend", fontsize=11, fontweight="bold", loc="left", color=INK)
ax1.tick_params(axis='x', rotation=90, labelsize=6.5)
ax1.legend(fontsize=8, frameon=False)
ax1.grid(axis="y", alpha=0.2)
for spine in ["top","right"]: ax1.spines[spine].set_visible(False)

# ---- Sales by region (pie) ----
ax2 = fig.add_subplot(gs[1, 2])
region_rev = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
ax2.pie(region_rev.values, labels=region_rev.index, autopct="%1.0f%%", startangle=140,
        colors=PALETTE, textprops={"fontsize":8})
ax2.set_title("Sales by Region", fontsize=11, fontweight="bold", loc="left", color=INK)

# ---- Profit by region (bar) ----
ax3 = fig.add_subplot(gs[1, 3])
profit_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
ax3.bar(profit_region.index, profit_region.values, color=GOLD)
ax3.set_title("Profit by Region", fontsize=11, fontweight="bold", loc="left", color=INK)
ax3.tick_params(axis='x', rotation=45, labelsize=7.5)
ax3.tick_params(axis='y', labelsize=7.5)
ax3.grid(axis="y", alpha=0.2)
for spine in ["top","right"]: ax3.spines[spine].set_visible(False)

# ---- Top 10 products ----
ax4 = fig.add_subplot(gs[2, 0:2])
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)
ax4.barh(top_products.index[::-1], top_products.values[::-1], color=FOREST)
ax4.set_title("Top 10 Products by Sales", fontsize=11, fontweight="bold", loc="left", color=INK)
ax4.tick_params(labelsize=8)
ax4.grid(axis="x", alpha=0.2)
for spine in ["top","right"]: ax4.spines[spine].set_visible(False)

# ---- Sales by category ----
ax5 = fig.add_subplot(gs[2, 2:4])
cat_rev = df.groupby("Category")["Revenue"].sum().sort_values(ascending=True)
ax5.barh(cat_rev.index, cat_rev.values, color="#3F9C7C")
ax5.set_title("Sales by Category", fontsize=11, fontweight="bold", loc="left", color=INK)
ax5.tick_params(labelsize=8.5)
ax5.grid(axis="x", alpha=0.2)
for spine in ["top","right"]: ax5.spines[spine].set_visible(False)

# ---- Sales vs profit scatter (by product, bubble = qty) ----
ax6 = fig.add_subplot(gs[3, 0:2])
prod = df.groupby("Product").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"), Qty=("Quantity","sum"))
sizes = (prod["Qty"] / prod["Qty"].max()) * 800 + 40
ax6.scatter(prod["Revenue"], prod["Profit"], s=sizes, color=FOREST, alpha=0.55, edgecolors=FOREST, linewidth=1)
ax6.set_title("Sales vs Profit by Product (bubble = qty sold)", fontsize=11, fontweight="bold", loc="left", color=INK)
ax6.set_xlabel("Sales ($)", fontsize=8.5)
ax6.set_ylabel("Profit ($)", fontsize=8.5)
ax6.tick_params(labelsize=7.5)
ax6.grid(alpha=0.2)
for spine in ["top","right"]: ax6.spines[spine].set_visible(False)

# ---- Category margin % ----
ax7 = fig.add_subplot(gs[3, 2:4])
cat_margin = (df.groupby("Category")["Profit"].sum() / df.groupby("Category")["Revenue"].sum() * 100).sort_values(ascending=True)
colors_margin = [RUST if v < 30 else GOLD if v < 40 else FOREST for v in cat_margin.values]
ax7.barh(cat_margin.index, cat_margin.values, color=colors_margin)
ax7.set_title("Profit Margin % by Category", fontsize=11, fontweight="bold", loc="left", color=INK)
ax7.set_xlabel("Margin (%)", fontsize=8.5)
ax7.tick_params(labelsize=8.5)
ax7.grid(axis="x", alpha=0.2)
for spine in ["top","right"]: ax7.spines[spine].set_visible(False)

fig.text(0.06, 0.01, "Source: sales_data.csv (3,000 orders, 2024–2025)  |  FUTURE_DS_01 — Future Interns", fontsize=8, color=SOFT)

plt.savefig("dashboard.png", dpi=160, bbox_inches="tight", facecolor="white")
print("saved dashboard.png")
