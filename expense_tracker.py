import streamlit as st
import json
import os
from datetime import datetime

# Load or initialize expenses
expenses = []
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as f:
        expenses = json.load(f)

def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

# Streamlit UI
st.title(" Personal Expense Tracker")

menu = st.sidebar.selectbox("Choose Action", ["Add Expense", "View Expenses", "View Total Spending", "Exit"])

if menu == "Add Expense":
    st.subheader("➕ Add a New Expense")

    date = st.date_input("Enter Date")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    note = st.text_input("Note")

    if st.button("Add Expense"):
        expenses.append({
            "date": str(date),
            "category": category,
            "amount": amount,
            "note": note
        })
        save_expenses()
        st.success("Expense added successfully!")

elif menu == "View Expenses":
    st.subheader(" View Expenses")

    if not expenses:
        st.warning("No expenses recorded yet.")
    else:
        sub_option = st.radio("Filter By", ["All", "Date", "Category"])

        if sub_option == "All":
            for idx, exp in enumerate(expenses, start=1):
                st.write(f"**{idx}.** Date: `{exp['date']}`, Category: `{exp['category']}`, Amount: ₹{exp['amount']}, Note: {exp['note']}")

        elif sub_option == "Date":
            date_input = st.date_input("Enter date to filter")
            found = False
            for idx, exp in enumerate(expenses, start=1):
                if exp["date"] == str(date_input):
                    st.write(f"**{idx}.** Date: `{exp['date']}`, Category: `{exp['category']}`, Amount: ₹{exp['amount']}, Note: {exp['note']}")
                    found = True
            if not found:
                st.error("No expenses found on this date.")

        elif sub_option == "Category":
            cat_input = st.text_input("Enter category to filter").lower()
            found = False
            for idx, exp in enumerate(expenses, start=1):
                if exp["category"].lower() == cat_input:
                    st.write(f"**{idx}.** Date: `{exp['date']}`, Category: `{exp['category']}`, Amount: ₹{exp['amount']}, Note: {exp['note']}")
                    found = True
            if not found:
                st.error("No expenses found in this category.")

elif menu == "View Total Spending":
    st.subheader(" Total Spending")
    if not expenses:
        st.warning("No expenses to show.")
    else:
        total = sum(exp["amount"] for exp in expenses)
        st.success(f"Your total spending is ₹{total:.2f}")

elif menu == "Exit":
    st.info("You can close the browser tab to exit.")


