# Python CLI Expense Tracker

A simple **Command Line Interface (CLI) expense tracker built with Python**.
This project allows users to record daily expenses, view stored transactions, and generate summaries by category. Data is stored locally using a JSON file.

---

## Project Overview

This application demonstrates core Python programming concepts including:

* Python scripting
* File handling with JSON
* Functions and program structure
* Command-line interfaces (CLI)
* Basic data processing

The program runs in the terminal and allows users to manage personal expenses without needing a graphical interface.

---

## Features

### Add Expenses

Users can enter:

* Date
* Amount
* Category
* Notes

Each expense is saved to a local JSON file.

### View All Expenses

Displays a list of previously stored expenses in a readable format.

Example:

```
2026-03-08 | £12.50 | Food | Lunch
2026-03-07 | £5.00  | Transport | Bus
```

### Category Summary

Shows how much money was spent in each category.

Example:

```
Spending by category:
Food: £45.20
Transport: £20.00
Entertainment: £15.00
```

### Persistent Storage

All data is saved to:

```
expenses.json
```

This allows expenses to persist between program runs.

---

## Project Structure

```
expense-tracker/
│
├── tracker.py        # Main Python application
├── expenses.json     # Stores expense data
└── README.md         # Project documentation
```

---

## Requirements

* Python 3.8+
* Visual Studio Code or any Python-compatible editor

Verify Python installation:

```
python --version
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/expense-tracker.git
```

Navigate to the project folder:

```
cd expense-tracker
```

---

## Running the Program

Run the application from the terminal:

```
python tracker.py
```

The program will display a menu:

```
Expense Tracker
1. Add Expense
2. View Expenses
3. View Summary by Category
4. Exit
```

---

## Example Expense Data

Example `expenses.json` file:

```json
[
  {
    "date": "2026-03-08",
    "amount": 12.5,
    "category": "Food",
    "notes": "Lunch"
  },
  {
    "date": "2026-03-07",
    "amount": 5.0,
    "category": "Transport",
    "notes": "Bus ticket"
  }
]
```

---

## Skills Demonstrated

This project highlights the following technical skills:

* Python scripting
* CLI application development
* JSON data storage
* Software structure using functions
* Basic data aggregation

---

## Possible Improvements

Future enhancements could include:

* Editing existing expenses
* Deleting expenses
* Monthly summaries
* Data visualization with charts
* Exporting to CSV
* Input validation

---

## Author

Developed as a beginner Python project for learning programming fundamentals and building a technical portfolio.
