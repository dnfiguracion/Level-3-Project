import pickle

def display_menu():
    print("\n---Personal Budgeting Tool---")
    print("1. Set Income")
    print("2. Add expense")
    print("3. Set Savings Goals")
    print("4. View Budget Summary")
    print("5. Save and Exit")
    print("--------------------------------")
#display menu options function

def calculate_total_expenses(expenses):
    return sum(expenses.values())
#Function that calculates total expenses

def view_budget_summary(income, expenses, saving_goal):
    total_expenses = calculate_total_expenses(expenses)
    remaining_balance = income - total_expenses
    print("\n---Budget Summary---")
    print(f"Income: ${income}")
    print(f"Expenses: {sum(expenses.values())}")
    for category, amount in expenses.items():
        print(f"{category}: ${amount}")
    print(f"Savings Goal: ${saving_goal}")
    print(f"Remaining Balance: ${remaining_balance}")
    if remaining_balance < 0:
        print("Warning: You have exceeded your budget!")
    else:
        print("You are within your budget!")
#Function for viewing current budget summary

def save_data(data):
    with open('budget_data.pkl', 'wb') as f:
        pickle.dump(data, f)
    print("Data saved sucessfully.")
#function to save data using pickle module

def load_data():
    try:
        with open('budget_data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {"income": 0, "expenses": {}, "savings_goal": 0}
#Function to load saved data using pickle module

def main():
    data = load_data()
    income = data['income']
    expenses = data['expenses']
    savings_goal = data['savings_goal']
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            income = float(input("Enter your monthly income: $"))
            data['income'] = income

        elif choice == '2':
            category = input("Enter expense type i.e house, car")
            amount = float(input(f"Enter amount for {category}: $"))
            expenses[category] = amount
            data['expenses'] = expenses

        elif choice == '3':
            savings_goal = float(input("Enter your savings goal: $"))
            data['savings_goal'] = savings_goal

        elif choice == '4':
            view_budget_summary(income, expenses, savings_goal)

        elif choice == '5':
            save_data(data)
            print("Exiting the budgeting tool. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
#Creates the main loop. it will continue to loop until user inputs 5 to exit
