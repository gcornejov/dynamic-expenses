from src.category_analytics import (calculate_month_expenses,
                                    calculate_percentages, load_data)

if "__name__" == "__name__":
    groups, expenses, periodic_expenses = load_data()

    calculate_percentages(expenses)
    calculate_month_expenses(periodic_expenses, 2023, 7, 1500000)
