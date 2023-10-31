import datetime
import matplotlib.pyplot as plt


class PersonalFinanceManager:
    def __init__(self):
        self.expenses = {}
        self.incomes = {}
        self.budgets = {}
        self.expense_history = []
        self.income_history = []

    def add_expense(self, category, amount):
        self.expenses[category] = self.expenses.get(category, 0) + amount
        self.expense_history.append((datetime.date.today(), category, amount))
        self.check_budget(category)

    def add_income(self, source, amount):
        self.incomes[source] = self.incomes.get(source, 0) + amount
        self.income_history.append((datetime.date.today(), source, amount))

    def set_budget(self, category, amount):
        self.budgets[category] = amount

    def check_budget(self, category):
        if category in self.budgets:
            if self.expenses.get(category, 0) > self.budgets[category]:
                print(f"Warning! You have exceeded your budget for {category}!")

    def get_total_expense(self):
        return sum(self.expenses.values())

    def get_total_income(self):
        return sum(self.incomes.values())

    def financial_insight(self):
        net = self.get_total_income() - self.get_total_expense()
        if net > 0:
            return f"You have a net positive of ${net}. Keep it up!"
        elif net == 0:
            return "You're breaking even. Try saving more!"
        else:
            return f"Ooops!! You have a net negative of ${abs(net)}.Consider cutting down expenses!"

    def display_summary(self):
        print("Your Income Summary:")
        for source, amount in self.incomes.items():
            print(f"{source}: ${amount}")

        print("\nYour Expense Summary:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")

        print("\nSuggested Financial Insights:")
        print(self.financial_insight())

        self.plot_summary_graph()


    def plot_summary_graph(self):
        print('This is a chart showiwng an overview of your Finances')
        labels = list(self.incomes.keys()) + list(self.expenses.keys())
        income_values = [self.incomes.get(source, 0) for source in labels]
        expense_values = [self.expenses.get(category, 0) for category in labels]
        budget_values = [self.budgets.get(category, 0) for category in labels]

        x = range(len(labels))
        width = 0.25

        fig, ax = plt.subplots(figsize=(10, 6))
        income_bars = ax.bar([i - width for i in x], income_values, width, label='Income', align='center')
        expense_bars = ax.bar(x, expense_values, width, label='Expense', align='center')
        budget_bars = ax.bar([i + width for i in x], budget_values, width, label='Budget', align='center')

        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha='right')
        ax.set_xlabel('Categories')
        ax.set_ylabel('Amount ($)')
        ax.set_title('Income, Expenses, and Budget')

        ax.legend()
        plt.tight_layout()

        plt.show()



    def historical_analysis(self):
        print("\nYour Income History:")
        for entry in self.income_history:
            print(f"Date: {entry[0]}, Source: {entry[1]}, Amount: ${entry[2]}")

        print("\nYour Expense History:")
        for entry in self.expense_history:
            print(f"Date: {entry[0]}, Category: {entry[1]}, Amount: ${entry[2]}")
def description():
    print("Hello!!")
    name= input("You mind if i know your name? ").lower()
    college= input("What college are you currently enrolled in? ").lower()
    print("\n--- Welcome to College Student Personal Finance Manager" + name.capitalize() + "---")
    print("\n Brief Description about this Finance Manager: ")
    print("Our finance manager is tailor-made for college students, offering a versatile solution for financial management and providing valuable financial insights.\nWith this tool, you can effortlessly track your income and expenses, whether it's for the past month, year, or any specific time frame that suits your needs. \nAdditionally, you can create and manage budgets to ensure your finances remain on track.")
    print("I hope this tool becomes useful to you. Have fun " + name.capitalize() + "!!")
def main():
    manager = PersonalFinanceManager()
    while True:
        print("1. Add Income and source")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. Display Summary")
        print("5. Historical Analysis")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            source = input("Enter income source: ")
            amount = float(input("Enter amount (only digits): "))
            manager.add_income(source, amount)
        elif choice == 2:
            print("You can enter multiple or several expenses by choosing the 2nd option over and over again")
            print("Expenses can be food, tuition, housing, data plan ad more")
            category = input("Enter expense category: ")
            amount = float(input("Enter amount (only digits): "))
            manager.add_expense(category, amount)
        elif choice == 3:
            category = input("Enter category for budget: ")
            amount = float(input("Set budget amount (only digits): "))
            manager.set_budget(category, amount)
        elif choice == 4:
             manager.display_summary()
        elif choice == 5:
            manager.historical_analysis()
        elif choice == 6:
            print("Goodbye!")
            print("Have a nice day.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    description()
    main()
