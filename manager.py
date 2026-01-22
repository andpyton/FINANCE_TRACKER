from user import User
from transaction import Transaction

class FinanceManager:

    def __init__(self, user):

        self.user = user

    def show_menu(self):

        print("\n --- Personal Finance Tracker ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. View Balance")
        print("4. View summary by category")
        print("5. Exit")

    def run(self):

        while True:

            self.show_menu()
            choice = input('Choose an option: ')

            if choice == '1':

                try:

                    amount=float(input("Enter income amount: "))
                    category=input("Enter category: ")
                    description=input("Enter description (optional): ")

                    transaction = Transaction(

                        amount=amount,
                        category=category,
                        t_type="income",
                        description=description,

                    )

                    self.user.add_transaction(transaction)
                    print("Income added succefully!")

                except ValueError as e:
                    print(f"Error: {e}")
            

            elif choice == '2':
                
                try:

                    amount = float(input("Enter expense amount: "))
                    category = input("Enter category: ")
                    description = input("Enter description: ")

                    transaction = Transaction(

                        amount=amount,
                        category=category,
                        t_type="expense",
                        description=description,

                    )

                    self.user.add_transaction(transaction)
                    print("Expense added succefully")

                except ValueError as e:
                    print(f"Error: {e}")

            elif choice =='3':
                balance = self.user.get_balance()
                print(f'Current balance is {balance}')

            elif choice == '4':
                
                summary = self.user.get_summary_by_category()

                if not summary:
                    print("No expenses recorded yet.")

                else:
                    print("\n--------Expense Summary by Category--------")
                    for category, total in summary.items():
                        print(f'{category}: {total}')

            elif choice =='5':
                print('Goodbye...')
                break
            else:
                print("Invalid option, try again...")


