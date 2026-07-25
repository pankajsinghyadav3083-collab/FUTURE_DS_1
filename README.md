# Task 1: Business Sales Performance Analytics

**Track:** Data Science & Analytics | Future Interns
**Repo name:** FUTURE_DS_01

## Objective
Analyze company sales data to identify revenue trends, top-selling products, high-value categories, and regional performance — and turn those findings into actionable business recommendations.

## Tools Used
Python (pandas, matplotlib) for analysis · Chart.js (HTML/JS) for the interactive dashboard

## Dataset
`sales_data.csv` — 3,000 transactions across 2 years (2024–2025), covering 12 products, 7 categories, and 5 regions. Columns: OrderID, Date, Product, Category, Region, UnitPrice, Quantity, Revenue, Cost, Profit.

## Approach
1. Loaded and cleaned the transaction data (parsed dates, derived Month/Year/Quarter fields)
2. Aggregated revenue and profit by month, product, category, and region
3. Calculated year-over-year growth, profit margins, and average order value
4. Built an interactive dashboard with live filters (Year / Region / Category)
5. Translated findings into business recommendations

## Executive Summary
Over 2024–2025, the business generated **$498,883 in revenue and $171,940 in profit** (34.5% overall margin) across 3,000 orders, growing **7.3% year-over-year**. Growth is concentrated in two product categories, one standout region, and a predictable Q4 seasonal spike. The most important nuance: **the single biggest revenue category (Displays) is also the second-lowest margin category** — meaning revenue growth and profit growth aren't the same story here, and treating them as interchangeable would lead to the wrong priorities.

## Key Insights

**1. Revenue growth is real but seasonal, not steady.**
YoY revenue growth was +7.3% ($240.7K → $258.2K); profit grew slightly faster, +7.8% ($82.7K → $89.2K). Every November–December, revenue jumps 25–35% above surrounding months. Q4 2025 was the strongest quarter in the dataset for both revenue ($72.7K) and profit ($25.5K) — and Q4 has led every year, so this is a reliable pattern to plan around, not a one-off.

**2. The top revenue category is not the top profit category.**
Displays leads revenue ($102.8K) but sits at only 27.7% margin — one of the two lowest-margin categories, alongside Furniture (21.6%). Meanwhile **Wearables has the highest margin of any category (45.0%)** and Accessories isn't far behind (42.0%), despite both ranking below Displays in raw revenue. A revenue-only view would over-prioritize Displays; a profit-aware view says Wearables and Accessories deserve more attention than their revenue rank suggests.

**3. Volume leaders and revenue leaders are different products — and margin cuts across both.**
Laptop Stand is the #1 product by units sold (1,648) but only #5 by revenue (low price point, ~$26 avg) — yet it carries a healthy 42.1% margin, making it a good low-friction upsell anchor. Smartwatch is the standout: #2 in revenue *and* a strong 45% margin. Standing Desk and Gaming Chair are the opposite problem — high price, low volume, *and* the lowest margins in the catalog (21.5% and 21.9%), making them the weakest performers on every axis.

**4. Regional revenue gaps are large — but margins are nearly flat across regions.**
North leads all regions in revenue ($141.3K), 37% ahead of South. Central is the weakest by revenue (63% less than North). But margins tell a different story: **Central actually has the highest profit margin of any region (35.1%)**, essentially tied with the others (33–35% across the board). This means Central's problem is genuinely about *demand or reach*, not pricing or cost structure — a marketing/distribution fix, not a pricing fix.

**5. East region customers spend more per order than anywhere else.**
East ranks only 3rd in total revenue but has the **highest average order value of any region ($183.14)** — 19% above Central's. Combined with insight #4 (flat margins everywhere), this says East is underpenetrated rather than low-value: the same profitable transaction behavior, just fewer of them.

## Recommendations
- **Shift marketing spend earlier — into October, not November** — the Nov–Dec spike already happens organically every year; earlier spend can extend it rather than just ride it.
- **Prioritize Wearables and Accessories in promotions over Displays**, despite Displays having higher raw revenue — a dollar of marketing spend converts to more profit in the higher-margin categories.
- **Bundle Laptop Stand with Smartwatch or 27" Monitor** at checkout — pairs a high-volume, decent-margin anchor with either a high-margin or high-revenue product, lifting both AOV and blended margin.
- **Treat Central as a demand-generation problem, not a pricing problem** — since its margin is actually the best of any region, the fix is more marketing reach and regional partnerships, not discounting.
- **Test premium upsells in the East region specifically** — customers there already spend the most per order; East is the most efficient region to trial higher-priced bundles.
- **Re-evaluate Standing Desk and Gaming Chair.** They're the only products weak on revenue, volume, *and* margin simultaneously (133 and 25 units sold in 2 years, ~21% margin) — worth deciding whether to reposition, discount clear, or drop.

## Deliverable
- `sales_data.csv` — source data (includes Cost/Profit columns)
- `analyze.py` — core analysis script (revenue, profit, margin, trends)
- `deeper_analysis.py` — extended analysis (AOV, quarterly, region×category breakdown); regenerates all summary CSVs
- `dashboard_interactive.html` — **primary deliverable**: interactive dashboard with live Year/Region/Category filters, KPI cards, and 6 chart views (open in any browser)
- `dashboard.png` — static image version of the dashboard (for GitHub README preview, LinkedIn posts, or anywhere HTML can't be embedded)
- `charts.py` — script that generates `dashboard.png`
- Summary CSVs: `monthly_revenue.csv`, `quarterly_summary.csv`, `category_revenue.csv`, `region_revenue.csv`, `product_summary.csv`, `region_category_pivot.csv`
- `README.md` — this report
