# creating a class for calculator

class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        return self.num1 + self.num2

    def Subtract(self):
        return self.num1 - self.num2

    def Multiply(self):
        return self.num1 * self.num2

    def Divide(self):
        if (self.num1 == 0 or self.num2 == 0):
            return " can't divide by 0"
        else:
            return self.num1 / self.num2

    def Modulos(self):
        if (self.num1 == 0 or self.num2 == 0):
            return " can't divide by 0"
        else:
            return self.num1 % self.num2

# using a while loop for the menu driven program
while True:
    print("Enter the operation you want to perform ")
    print("0.Exit \n1.Add \n2.Subtract \n3.Multiply \n4.Divide \n5.Modulos")

    user = input("Enter your choice\n")

    num1 = int(input("Enter your first  number\n"))
    num2 = int(input("Enter your second number\n"))

# Creating an object of the class and invoking the methods using that object.
    obj = calculator(num1, num2)
# If condition will run according to user input
    if (user == "1" or user == "Add"):
        print(f"The sum of {num1} and {num2} is ", obj.Add())
    elif (user == "2" or user == "subtract"):
        print(f"The subtraction of {num1} and {num2} is ", obj.Subtract())
    elif (user == "3" or user == "Multiply"):
        print(f"The Multiplication of {num1} and {num2} is ", obj.Multiply())
    elif (user == "4" or user == "Division"):
        print(f"The Quotient of {num1} and {num2} is ", obj.Divide())
    elif (user == "5" or user == "Modulos"):
        print(f"The Quotient of {num1} and {num2} is ", obj.Modulos())
    elif user == "0":
        print("ExITING TO MAIN MENU")
        break

    else:
        print("INVALID INPUT ***please enter a valid input e.g 1 or Add\n")
