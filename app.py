# === app.py ===
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from budget_ai import get_suggestions
from ocr_reader import extract_text_from_image
import os

# Load or initialize CSV file
data_file = 'expenses.csv'
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Notes'])

st.title("💰 AI-Based Personal Finance Tracker")

# Expense Entry
st.header("➕ Add a New Expense")
date = st.date_input("Date")
category = st.selectbox("Category", ['Food', 'Transport', 'Shopping', 'Education', 'Others'])
amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)
notes = st.text_input("Notes")

if st.button("Add Expense"):
    new_data = pd.DataFrame([[date, category, amount, notes]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(data_file, index=False)
    st.success("Expense added successfully!")

# Upload Bill
st.header("🧾 Upload Bill Image")
image = st.file_uploader("Upload an image of your receipt", type=['png', 'jpg', 'jpeg'])
if image:
    extracted_text = extract_text_from_image(image)
    st.text_area("Extracted Text", extracted_text)

# View Expenses
st.header("📊 Expense Dashboard")
st.dataframe(df)

# Pie chart
if not df.empty:
    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)

# Suggestions
st.header("🤖 AI Budget Suggestions")
suggestions = get_suggestions(df)
for s in suggestions:
    st.write("- ", s)


