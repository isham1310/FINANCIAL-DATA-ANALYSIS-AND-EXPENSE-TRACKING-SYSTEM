import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(filename='financial_data.csv'):
    """Generates a realistic dataset for a student/professional in Pune."""
    categories = ['Food', 'Transport', 'Rent', 'Subscriptions', 'Education', 'Entertainment']
    data = []

    # Generate 1 year of data
    start_date = datetime(2025, 1, 1)
    
    for i in range(300):
        date = start_date + timedelta(days=random.randint(0, 364))
        category = random.choice(categories)
        transaction_type = "Expense"
        
        # Realistic pricing for a student in India
        if category == 'Rent':
            amount = 8500
        elif category == 'Food':
            amount = random.randint(100, 500)
        elif category == 'Transport':
            amount = random.randint(50, 1000)
        else:
            amount = random.randint(200, 2000)
            
        data.append([date.strftime('%Y-%m-%d'), category, amount, transaction_type])

    # Add Monthly Income (Stipend/Allowance)
    for month in range(1, 13):
        data.append([f"2025-{month:02d}-01", "Allowance/Salary", 75000, "Income"])

    df = pd.DataFrame(data, columns=['Date', 'Category', 'Amount', 'Type'])
    df.to_csv(filename, index=False)
    print(f"✔️ Success: '{filename}' created with {len(df)} records.")
    return df

def run_analysis(df):
    """Performs the 'Hidden Angle' Strategic Analysis."""
    print("\n--- Strategic Financial Analysis ---")
    
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    savings = total_income - total_expense
    
    print(f"Total Income:  ₹{total_income:,}")
    print(f"Total Expense: ₹{total_expense:,}")
    print(f"Net Savings:   ₹{savings:,}")
    
    # --- Constants for the scenario ---
    SALARY_HIKE_PERCENTAGE = 15
    SPENDING_REDUCTION_PERCENTAGE = 10

    # What-if Scenario
    print(f"\n--- 'What-If' Scenario: {SALARY_HIKE_PERCENTAGE}% Salary Hike & {SPENDING_REDUCTION_PERCENTAGE}% Less Spending ---")
    projected_income = total_income * (1 + SALARY_HIKE_PERCENTAGE / 100)
    projected_expense = total_expense * (1 - SPENDING_REDUCTION_PERCENTAGE / 100)
    new_savings = projected_income - projected_expense
    
    print(f"Projected Monthly Savings: ₹{new_savings/12:,.2f}")
    print(f"Annual Improvement:        ₹{new_savings - savings:,.2f}")

if __name__ == "__main__":
    # 1. Generate the CSV file
    financial_df = generate_data()
    
    # 2. Run Python Analysis
    run_analysis(financial_df)
    
    print("\nNext Step: Open Power BI and import 'financial_data.csv' to build your dashboard.")