# Financial Data Generator & Strategic Analysis

A Python-based personal finance simulator and analysis tool. This project generates a realistic, year-long dataset of daily transactions for a student or young professional living in Pune, India. It also runs a baseline financial analysis and projects future savings based on "What-If" scenarios.

The generated dataset is perfectly formatted for importing into Business Intelligence tools like **Power BI** or **Tableau** to build interactive financial dashboards.

## Features

* **Automated Data Generation:** Simulates a full year of transactions (Income and Expenses) including categories like Food, Transport, Rent, Subscriptions, Education, and Entertainment.
* **CSV Export:** Outputs a clean, ready-to-use `financial_data.csv` file.
* **Baseline Analysis:** Instantly calculates your Annual Total Income, Total Expenses, and Net Savings.
* **Strategic 'What-If' Scenarios:** Calculates projected monthly savings and annual improvements based on dynamic variables (e.g., a 15% salary hike and a 10% reduction in spending).
* **Power BI Ready:** Bridges the gap between raw data generation and visual data analytics.

## Prerequisites

* Python 3.x
* `pandas` library

## Installation & Usage

1. **Clone the repository** (or download the script).
2. **Install the required dependencies**:
   `pip install pandas`
3. **Run the script**:
   `python financial_analysis.py`

## What's Next? (Power BI Integration)

Once the script finishes running, it will generate a `financial_data.csv` file in the same directory.

1. Open **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Select `financial_data.csv` and load the data.
4. Build your interactive dashboard to visualize spending trends, category breakdowns, and monthly cash flow!

## Customization

You can easily tweak the script to fit different scenarios:
* Update the `categories` list to reflect your actual spending habits.
* Modify `SALARY_HIKE_PERCENTAGE` and `SPENDING_REDUCTION_PERCENTAGE` to test different financial goals.
* Adjust the monthly income or fixed expenses within the script.
