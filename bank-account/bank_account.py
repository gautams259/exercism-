class BankAccount(object):
    def __init__(self):
        self.banalce = 0
        self.ac = False

    def get_balance(self):
        if self.ac:
            return self.banalce
        else:
            raise Exception("Account closed")

    def open(self):
        if not self.ac:
            self.ac = True
        else:
            raise Exception("Account already open...")

    def deposit(self, amount):
        if self.ac and  amount >0:
            self.banalce = self.banalce + amount
            return self.banalce
        else:
            raise Exception("Can't deposit") 

    def withdraw(self, amount):
        if self.ac:
            if amount > 0 and self.banalce >= amount:
                self.banalce = self.banalce - amount
                return self.banalce
            else:
                raise Exception("Cannot withdraw  ")
        else:
            raise Exception("Account closed...") 

    def close(self):
        if self.ac:
            self.ac = False
            self.banalce = 0
            return self.ac
        else:
            raise Exception("Account already closed..")

if __name__ == '__main__':
    ob = BankAccount()
    ob.open()
    ob.get_balance()
    ob.deposit(3434)
    prinnt("hello world re build")
