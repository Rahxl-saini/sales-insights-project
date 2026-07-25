# AI-Powered Sales Data Insights Dashboard

A Python data analytics project that cleans messy real-world-style sales data,
runs exploratory data analysis, generates business visualizations, and uses
the Groq API to auto-generate plain-language, stakeholder-ready insights.

## Why this project
Raw business data is rarely clean. This project simulates that reality —
duplicate rows, missing prices, invalid entries — and walks through the full
analyst workflow: **clean → analyze → visualize → summarize with AI.**

## Features
- 🧹 **Data Cleaning** — handles duplicates, missing values (median imputation
  by category), and invalid/negative entries
- 📊 **Exploratory Data Analysis** — revenue by category, region, channel,
  weekday vs weekend performance, monthly trend analysis
- 📈 **Visualizations** — matplotlib/seaborn charts saved automatically
- 🤖 **AI-Generated Insights** — Groq API (fast LLM inference) turns raw KPIs into a natural-
  language business report with actionable recommendations
- 🗂️ Clean, modular code split by responsibility (cleaning / EDA / AI layer)

## Tech Stack
- Python 3
- Pandas, NumPy — data cleaning & aggregation
- Matplotlib, Seaborn — visualization
- Groq API — fast, free-tier LLM inference for insight generation

## Project Structure
```
sales-insights-project/
├── sales_data_raw.csv        # raw, intentionally messy dataset
├── data_cleaning.py          # cleaning + feature engineering
├── sales_data_clean.csv      # output of cleaning step
├── eda_visualizations.py     # EDA + chart generation
├── summary_stats.json        # key KPIs extracted from the data
├── ai_insights.py            # Groq-powered insights generator
├── ai_generated_insights.md  # sample AI output
├── charts/                   # generated PNG charts
└── requirements.txt
```

## How to Run
```bash
pip install -r requirements.txt

# 1. Clean the raw data
python data_cleaning.py

# 2. Run EDA + generate charts
python eda_visualizations.py

# 3. Generate AI insights (requires a free Groq API key)
export GROQ_API_KEY="your-key-here"   # get one free at console.groq.com/keys
python ai_insights.py
```

## Sample KPIs (from generated dataset)
| Metric | Value |
|---|---|
| Total Revenue | $1,454,451 |
| Total Orders | 3,000 |
| Avg. Order Value | $484.82 |
| Top Category | Electronics |
| Top Region | North |
| Best Month | August |
| Online Sales Share | 67.2% |

## Sample Insight Output
> - **Electronics drives the largest share of revenue** — consider expanding
>   inventory depth and running targeted promotions in this category.
> - **Online channel accounts for 67% of sales** — prioritize UX and page-load
>   improvements on the online store, as it's the primary revenue driver.
> - **North region leads all regions** — investigate what's working there
>   (marketing, demographics) and test replicating it in underperforming
>   regions.

*(Full report is generated dynamically per dataset via `ai_insights.py`.)*

## Author
Rahul Saini — [GitHub](https://github.com/Rahxl-saini) | [LinkedIn](https://linkedin.com/in/rahul-saini2522)
