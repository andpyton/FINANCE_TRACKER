class Transaction:

    def __init__(self, amount, category, t_type, description=""):

        # This will verify if amount is a number...
        if not isinstance(amount, (int, float)):
            raise TypeError
        # This will verify if amount is >= 0.
        if amount<=0:
            raise ValueError("Value must be greater than zero.")
        # This will verify if t_type is 'income' or 'expense'.
        if t_type not in ("income", "expense"):
            raise ValueError("Transaction type must be 'Income' or 'expense'")
        
        self.amount=amount
        self.category = category
        self.t_type = t_type
        self.description = description
        
