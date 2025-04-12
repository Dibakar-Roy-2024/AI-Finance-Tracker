# === budget_ai.py ===
def get_suggestions(df):
    suggestions = []
    if df.empty:
        return ["No data available for suggestions."]

    total_spent = df['Amount'].sum()
    by_category = df.groupby('Category')['Amount'].sum()
    average_spent = total_spent / len(by_category)

    for cat, amt in by_category.items():
        if amt > average_spent:
            suggestions.append(f"You spent ₹{amt:.2f} on {cat}. Try to reduce it below ₹{average_spent:.2f}.")
        else:
            suggestions.append(f"Good job! You're within budget for {cat}.")
    return suggestions


