class Account:
    
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.balance = int(file.read())
    
    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        self.balance -= amount
    
    def commit(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))

# Inheritance demo
class Checking(Account):
    
    def __init__(self, file_path):
        Account.__init__(self, file_path)

    def transfer(self, amount):
        self.balance -= amount

checking = Checking('balance.txt')
checking.transfer(100)
checking.commit()


# account = Account('balance.txt')
# account.debit(200)
# account.commit()
# print(account.balance)