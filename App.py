class vikas :
    def __init__(self,name,age,education, grade)


from Demo import sum

add = sum()


## Concept of class and object

class ABC:
    num1 = 200
    num = 100
    print("Hello world")

obj = ABC()

print(obj.num + obj.num1)


class abc:
    print('Hii')


obj = abc() #Creating Object ---> obj;,  and abc is a class which is assigned to object abc

class my_class():
    """A Simple example class"""
    i = 12345 #Attribute
    def f(self): 
        return 'Hello World'



x = my_class()
print(x.i)


#Constructor:__init__

class abc:
    def __init__(self, num1, num2):
        self.num1 = 1000
        self.num2= 2000



    def show_data(self):
        print(f'The value of num1 is {self.num1} and the value of num2 is {self.num2}.')
x = abc(1,2)

# print(x.num1)
print(x.show_data())


class my_car:
    def __init__(self, brand,model,colour,fuel_type):
        self.brand = brand
        self.model = model
        self.colour  = colour 
        self.fuel_type = fuel_type
    
    def show_data(self):
        print(f'This {self.brand} has a model name {self.model} and the colour is {self.colour} with {self.fuel_type} engine')

car1 = my_car("BMW","M5", "BLACK","PETROL")
car2 = my_car("SUZUKI","Swift Dzire","White","Gas")
car3 = my_car("Mercedies","MayBac","Black","petrol")
car4 = my_car("Mahindra","Thar Rox","Black","Petrol")
car5 = my_car("Tata", "Nano","Yellow","Diesel")

car1.show_data()


car2.show_data() 
car3.show_data()
car4.show_data()
car5.show_data()

class Banking:
    def __init__(self):
        self.Balance = 100000
        
        self.Withdraw = float(input("Enter The Withdrawal Amount : "))

    def BALANCE(self):
        if(self.Balance < self.Withdraw):
            print("Insufficient Balance")
        else:
            self.Balance -= self.Withdraw

    def show_Balance(self):
        print(f"The Balance amount is : {self.Balance}")

user = Banking()
user.BALANCE()
user.show_Balance()

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()
d.bark()


class bank:
    def __init__(self,balance,saving,deposit):
        self.balance = balance
        self.saving = saving
        self.deposit = deposit

    def Balance(bank):
        print(f'The balance amount is {self.balance}')
    def Saving(bank):
        print(f'The balance amount is {self.saving}')
    def Deposit(bank):
        print(f'The balance amount is {self.deposist}')

sbi = bank(10000,5000,6000)  
sbi.balance()
sbi.deposit()
sbi.saving()



class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def show_balance(self):
        print(f'Current Balance : Rs.{self.balance}')
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn Successfully.")

class SavingsAccount(BankAccount):
    def deposit(self,amount):
        self.balance += amount
        print(f"Rs.{amount} deposited successfully.")

my_account = SavingsAccount(10000)

deposit_amount = float(input("Enter amount to deposit : "))
my_account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw : "))
my_account.withdraw(withdraw_amount)

my_account.show_balance()




################################################## POLYMORPHISM ################################################################################
# Poly-Morphism -- Ek hi functiob bahot saare kaam krega wo bhi bahot function ke liye it's known as poly-morphism
# {Many Instances}



class bear(object):
    def sound(self):
        print("Goarrr")

class Dog(object):
    def sound(self):
        print("Woof woof!")

def makesound(animalType):
    animalType.sound()


bearObj = bear()
dogObj = Dog()

makesound(bearObj)
makesound(dogObj)



class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

class cat(Animal):
    def speak(self):
        return "Meow!"

#POLYMORPHISM

animals = [Dog(), cat()]

for Animal in animals:
    print(Animal.speak())
