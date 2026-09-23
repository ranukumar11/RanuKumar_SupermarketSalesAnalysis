import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Collect and load the CSV dataset directly from the provided Google Sheet
    print("Loading dataset...")
    url = "https://docs.google.com/spreadsheets/d/1QIX__4VObHFMEXnRM2xJyXmB5JAB2peHrJcQ41_U9TE/export?format=csv"
    df = pd.read_csv(url)

    # 2. Check the data for missing or incorrect values
    print("\n--- Data Information ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # 3. Calculate Sales (Quantity * Unit Price) to verify data integrity
    df['Calculated_Sales'] = df['Quantity'] * df['Unit Price']

    # 4. Group and summarize the data (Live Analysis)
    print("\n--- Live Analysis Results ---")
    
    # Which product generates the highest sales?
    product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    print(f"1. Highest Selling Product: {product_sales.index[0]} (₹{product_sales.iloc[0]:.2f})")

    # Which branch performs best?
    branch_sales = df.groupby(['Branch', 'City'])['Sales'].sum().sort_values(ascending=False)
    best_branch = branch_sales.index[0]
    print(f"2. Best Performing Branch: Branch {best_branch[0]} ({best_branch[1]}) with ₹{branch_sales.iloc[0]:.2f}")

    # Which category sells the most?
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    print(f"3. Top Selling Category: {category_sales.index[0]} (₹{category_sales.iloc[0]:.2f})")

    # What is the most popular payment method?
    payment_counts = df['Payment'].value_counts()
    print(f"4. Most Popular Payment Method: {payment_counts.index[0]} ({payment_counts.iloc[0]} transactions)")

    # Do Members spend more than Normal customers?
    customer_spending = df.groupby('Customer Type')['Sales'].mean()
    print("5. Average Spending by Customer Type:")
    print(f"   - Member: ₹{customer_spending.get('Member', 0):.2f}")
    print(f"   - Normal: ₹{customer_spending.get('Normal', 0):.2f}")

    # What is the average customer rating?
    avg_rating = df['Rating'].mean()
    print(f"6. Average Customer Rating: {avg_rating:.2f} out of 5")

    # 5. Create charts to compare the results
    sns.set_theme(style="whitegrid")
    
    # Chart 1: Total Sales by Category
    plt.figure(figsize=(10, 5))
    sns.barplot(x=category_sales.index, y=category_sales.values, palette="viridis")
    plt.title('Total Sales by Category')
    plt.ylabel('Total Sales (₹)')
    plt.xlabel('Category')
    plt.tight_layout()
    plt.show()

    # Chart 2: Total Sales by Branch
    plt.figure(figsize=(8, 5))
    # Formatting branch names for the chart
    branch_labels = [f"Branch {b[0]}\n({b[1]})" for b in branch_sales.index]
    sns.barplot(x=branch_labels, y=branch_sales.values, palette="magma")
    plt.title('Total Sales by Branch')
    plt.ylabel('Total Sales (₹)')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
