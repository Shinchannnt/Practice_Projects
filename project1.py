import csv
class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return (f"Date: {self.date}\n  Category: {self.category}\n Amount: {self.amount}\n Description: {self.description}")
    def to_list(self):
        return [self.date, self.category, self.amount,self.description]


class ExpenseTracker:
    def __init__(self):
        self.expenses = []  # list of Expense objects
    

    def add_expense(self,new_expense):
        self.expenses.append(new_expense)
        ...
    def remove_expense(self, index):
        self.expenses.pop(index)
        print(f"The expense at index {index} has been removed")
        ...
    def total(self):
        self.total=0
        self.total=sum(expense.amount for expense in self.expenses)
        x=float(self.total)
        return x
        ...
    def total_by_category(self, given_category):
        self.total_by_category=0
        for expense in self.expenses:
            if  expense.category==given_category:
                self.total_by_category+=expense.amount
                b=self.total_by_category
                return b
            else:
                print(f"No expenses found for category '{given_category}'")
        

    def save_to_file(self,record):
        with open("expense.csv", mode="w", newline="", encoding="utf-8") as file:
             writer = csv.writer(file)
             for expense in self.expenses:
                 record=expense.to_list()
                 writer.writerow(record)
                


        
    def load_from_file(self):
        with open("expense.csv", mode="r") as file:
            reader = csv.reader(file)
            for line in reader:
                new_expense = Expense(*line)
                self.expenses.append(new_expense)
def main():
    tracker = ExpenseTracker()
    while True:
        print("_____________Expense*Tracker*Beta_____________\n" 
        "Enter 1 to add expense\n"
        "Enter 2 to remove expense\n"
        "Enter 3 to Print total\n"
        "ENter 4 to print by category\n"
        "Enter 5 to save to file\n" 
        
        "Enter 6 to Load to file\n"
        "Enter anything else to exit the menu\n"
        )
        usr=int(input("Enter your number:"))
        match usr:
            case 1:
                date = input("Enter the date (YYYY-MM-DD): ")
                category = input("Enter the category: ")
                amount = float(input("Enter the amount: "))
                description = input("Enter the description: ")
                new_expense = Expense(date, category, amount, description)
                tracker.add_expense(new_expense)
            case 2:
                idx=int(input("Enter the index to remove"))
                tracker.remove_expense(idx)
            case 3:
                
                print(f"Total expenses: {tracker.total()}")
            case 4:
                category = input("Enter the category to calculate total: ")
                print(f"Total expenses for category '{category}': {tracker.total_by_category(category)}")
                
            case 5:
                tracker.save_to_file(tracker.expenses)

            case 6:
                tracker.load_from_file()

            case _:
                print("Exiting the menu...")
                return False

            
    

if __name__ == "__main__":
    main()

