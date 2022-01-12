class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.id, self.first_name, self.last_name, self.email)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0
        self.pin = 11111

    def verify_pin(self, pin):
        if self.pin == pin:
            return True
        else:
            return False


    def deposit(self, amount):
            self._balance += amount
            print("\n Money deposited:", amount)

    def charge(self, pin, amount):
        pin = input("\n Please Enter pin: ")
        tries = 0
        while tries < 5:
            if self.verify_pin(pin):
                print("Pin accepted!")
                if  self._balance >= amount-5:
                    self._balance -= amount
                    print("\n Withdrew: ", amount)
                else:
                    print("\n Withdrawal not covered.")
                return True
            else:
                print("Invalid pin")
                tries += 1
        print("To many incorrect tries. Could not log in")
        return False

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self.pin, self._balance)

class SavingsAccount(Account):
    interest_rate = 0.02
    def calc_interest(self):
        self._balance += self.interest_rate * self._balance

class CheckingAccount(Account):
    pass

class Bank:
    def __init__(self):
        self.cust_list = []
        self.acc_list = []
  #      self.from_account_id = id
   #     self.to_account_id = id
    def new_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c
    def new_account(self, customer, is_savings=True):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a
#    def transfer(self, from_account_id, to_account_id, amount):
 #       self.from_account_id(amount)
  #      ._balance -= amount
   #     self.to_account_id(amount)
    #    ._balance += amount
    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()
c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)
a3 = b.new_account(c2, is_savings=True)
a4 = b.new_account(c2, is_savings=False)
#b.transfer(1, 2, 20)


print(a2)
#a1.deposit(2500)
a2.charge(c1, 100)

#a2.deposit(500)
#a2.charge(c2, 200)

#print(b)
#print(a1)
#print(a2)
#print(a3)
#print(a4)
