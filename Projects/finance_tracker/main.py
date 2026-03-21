import pandas as pd
import csv
import os
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.CSV_FILE):
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry added successfully!")

def search():
    df = pd.read_csv(CSV.CSV_FILE)

    search_type = input("Search by date or category? (d/c): ")

    if search_type == "d":
        date = input("Enter date (DD-MM-YYYY): ")
        print(df[df["date"] == date])

    elif search_type == "c":
        category = input("Enter category (Income or Expense): ")
        print(df[df["category"] == category])

    else:
        print("Invalid choice")

def add():
    CSV.initialize_csv()

    date = get_date("Enter the date of transaction (DD-MM-YYYY): ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)



add()
search()