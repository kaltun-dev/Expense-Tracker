# Import the JSON module so we can read and write data to a JSON file
import json

#function that loads expenses from a JSON file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except:
        return[]

# function that saves expenses to a JSON file
def save_expenses(expenses):
     # Open the file in write mode
     with open ("expenses.json", "w") as file:
         # Write the expenses data to the file in JSON format
         json.dump(expenses, file, indent=4)

#function to add an expense to the list of expenses
def add_expense(expenses):
     # Ask the user to input expense details
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    amount = float(input("Enter the amount of the expense: "))
    category = input("Enter the category of the expense:")
    description = input("Enter a description of the expense: ")

    # Create a dictionary to represent the expense
    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
        }
