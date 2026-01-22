from transaction import Transaction

class User:

    def __init__(self, name):

        self.name = name
        self.transactions = []

    # Adding transactions:
    def add_transaction(self, transaction):

        # Verify if transaction is a object of Transaction Class
        if not isinstance(transaction, Transaction):
            raise TypeError("Expected a transaction object")
        
        # Adding each object to self.transactions list.
        self.transactions.append(transaction)

    def get_balance(self):

        balance = 0

        for transaction in self.transactions:

            if transaction.t_type== 'income':
                balance+=transaction.amount
            else:
                balance-=transaction.amount

        return balance  

    def get_summary_by_category(self):

        summary = {}

        for transaction in self.transactions:

            if transaction.t_type=='expense':
                
                category = transaction.category
                amount = transaction.amount

                if category in summary:

                    summary[category]+=amount
            
                else:

                    summary[category] = amount
            
        return summary






