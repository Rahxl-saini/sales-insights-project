"""
ai_insights.py
---------------
Uses the Groq API (fast, free-tier LLM inference) to turn raw summary
statistics into a clear, natural-language business insights report — the
kind a data analyst would hand to a non-technical stakeholder.

Setup:
    pip install groq
    export GROQ_API_KEY="your-key-here"

Run:
    python ai_insights.py
"""

import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def build_prompt(stats: dict) -> str:
    return f"""
You are a senior data analyst. Write a concise, business-friendly insights
summary (5-6 bullet points) based on the following sales KPIs from 2025:

- Total Revenue: ${stats['total_revenue']:,}
- Total Orders: {stats['total_orders']}
- Average Order Value: ${stats['avg_order_value']}
- Top Category: {stats['top_category']}
- Top Region: {stats['top_region']}
- Best Performing Month: {stats['best_month']}
- Online Sales Share: {stats['online_share_pct']}%

For each bullet, explain what the number means for the business and
suggest one concrete, actionable recommendation. Keep the tone professional
and easy for a non-technical stakeholder to understand.
"""


def generate_insights(stats_path="summary_stats.json", model="llama-3.3-70b-versatile"):
    with open(stats_path) as f:
        stats = json.load(f)

    prompt = build_prompt(stats)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    insights = response.choices[0].message.content
    with open("ai_generated_insights.md", "w") as f:
        f.write("# AI-Generated Sales Insights Report\n\n")
        f.write(insights)

    print("Insights saved -> ai_generated_insights.md\n")
    print(insights)
    return insights


if __name__ == "__main__":
    generate_insights()
