# Welcome message
print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# Sample quarterly sales data
# Format: [product_name, category, price, quantity_sold, employee_id]s
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

# Employee info
# Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

# TODO 1: Sales Analysis Functions

def calculate_total_sales():
    """
    Calculates the total revenue from all sales.

    Returns:
        float: The total sales revenue.
    """
    total = 0
    for product in sales_data:
        total += product[2] * product[3]
    return total


def calculate_category_sales(category):
    """
    Calculates the total revenue from sales in a specific product category.
    
    Args:
        category (str): The product category to calculate sales for.
        
    Returns:
        float: The total sales revenue for the specified category.
    """
    total = 0
    for product in sales_data:
        if product[1] == category:
            total += product[2] * product[3]
    return total


def find_best_selling_product():
    """
    Finds the best-selling product based on total revenue.
    
    Returns:
        tuple: (product_name, total_revenue)
    """
    best_product = None
    best_revenue = 0
    for product in sales_data:
        revenue = product[2] * product[3]
        if revenue > best_revenue:
            best_product = product[0]
            best_revenue = revenue
    return (best_product, best_revenue)

# TODO 2: Commission Calculation Functions

def calculate_employee_commission(employee_id):
    """
    Calculates the commission earned by a specific employee.
    
    Args:
        employee_id (str): The unique identifier of the employee.
        
    Returns:
        float: The commission amount earned.
    """
    if employee_id not in employees:
        return 0.0
    rate = employees[employee_id][1]
    total_sales = sum(p[2] * p[3] for p in sales_data if p[4] == employee_id)
    return total_sales * rate


def calculate_total_commission():
    """
    Calculates the total commission for all employees.
    
    Returns:
        float: The total commission.
    """
    return sum(calculate_employee_commission(eid) for eid in employees)

# TODO 3: Report Generation Functions

def generate_sales_summary(include_categories=True):
    """
    Generates a formatted sales summary report.
    
    Args:
        include_categories (bool, optional): Whether to include category breakdown.
            Defaults to True.
        
    Returns:
        str: Formatted report string.
    """
    report = []
    report.append(f"Total Sales: ${calculate_total_sales():,.2f}")
    if include_categories:
        report.append("\nCategory Breakdown:")
        categories = set(p[1] for p in sales_data)
        for c in categories:
            report.append(f" - {c}: ${calculate_category_sales(c):,.2f}")
    best_product, revenue = find_best_selling_product()
    report.append(f"\nBest-Selling Product: {best_product} - ${revenue:,.2f}")
    return "\n".join(report)


def generate_employee_report():
    """
    Generates an employee performance report.
    
    Returns:
        str: Report string with employee sales and commissions.
    """
    report = []
    for eid, info in employees.items():
        name, _ = info
        sales_total = sum(p[2] * p[3] for p in sales_data if p[4] == eid)
        commission = calculate_employee_commission(eid)
        report.append(f"{name}: Sales = ${sales_total:,.2f}, Commission = ${commission:,.2f}")
    return "\n".join(report)

# TODO 4: Utility Functions

def get_products_by_category(category):
    """
    Returns all products belonging to a specific category.
    
    Args:
        category (str): The product category to filter by.
        
    Returns:
        list: List of products in the specified category.
    """
    return [p for p in sales_data if p[1] == category]


def calculate_average_sale_price():
    """
    Calculates the average sale price across all transactions.
    
    Returns:
        float: Average sale price.
    """
    total_revenue = calculate_total_sales()
    total_quantity = sum(p[3] for p in sales_data)
    return total_revenue / total_quantity if total_quantity else 0

# MAIN

def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    
    # Calculate and display total sales
    print("\nTOTAL QUARTERLY SALES:")
    print(f"${calculate_total_sales():,.2f}")
    
    # Display category sales
    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    for c in categories:
        print(f"{c}: ${calculate_category_sales(c):,.2f}")
    
    # Display best-selling product
    print("\nBEST-SELLING PRODUCT:")
    product, revenue = find_best_selling_product()
    print(f"{product} - ${revenue:,.2f}")
    
    # Display employee commissions
    print("\nEMPLOYEE COMMISSIONS:")
    for eid, info in employees.items():
        name = info[0]
        commission = calculate_employee_commission(eid)
        print(f"{name}: ${commission:,.2f}")
    
    # Generate and display sales summary report
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    print(generate_sales_summary(include_categories=False))
    
    # Generate and display employee performance report
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    print(generate_employee_report())

# Run the MAIN

if __name__ == "__main__":
    main()



    