from user import User
from manager import FinanceManager

if __name__ == "__main__":

    name = input("Enter your name: ")
    user = User(name)
    manager = FinanceManager(user)
    manager.run()
