import json
import os

expenses = []
def save_expenses_to_json(expenses, filename="expenses.json"):
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent=4)
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
while True:
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View  Spendings")
    print("4. Exit")

    option = int(input("Enter the Number You want to choose:"))

    if option <= 0 or option > 4:
        print("Enter a valid number between 1 and 4")
        continue
    if option == 1 :
        date = input("Enter the Date:(YYYY-MM-DD)")
        category=  input("Enter the Category:")
        amount  = float(input("Enter the amount:"))
        note  = input("Enter the note")
        expenses.append({"date": date, "category": category, "amount": amount, "note": note})
        print("Expense added successfully!")

    elif option == 2:# show
       print("How do u want to view expenses:")
       sub = int(input("1.All expenses         2.Filter by date              3.Filter by category"))
       if not expenses:
           print("No expenses recorded  yet")
       if sub == 1:
           for idx,exp in enumerate(expenses,start=1):
               print(f"{idx}. Date:{exp['date']} | Category:{exp['category']}|Amount:{exp['amount']} Note:{exp['note']}")

       elif sub == 2:
           date_input = input("Enter the Date(YYYY-MM-DD):")
           found = False
           for idx,exp in enumerate(expenses,start=1):
               if exp['date'] == date_input:
                   print(
                       f"{idx}. Date:{exp['date']} | Category:{exp['category']}|Amount:{exp['amount']} Note:{exp['note']}")
                   found = True
           if not found:
               print("No expenses on the date")
       else:
           category_input = input("Enter the needed category")
           found = False
           for idx,exp in enumerate(expenses,start=1):
               if exp['category'].lower() == category_input.lower():
                print(f"{idx}. Date:{exp['date']} | "
                     f"category:{exp['category']}|"
                     f"amount:{exp['amount']}"
                     f"note:{exp['note']}")
                found = True
           if not found:
               print("No expenses on the category")
    elif option == 3:
        if not expenses:
            print("No expense recorded")
        else:
            total = sum(exp["amount"] for exp in expenses)
            print(f"Total spending : {total}")
    elif option == 4:
        save_expenses_to_json(expenses)
        print("Expenses saved to 'expenses.json'. Thank you!")
        break
print("Thank You for using , Have a nice day")

