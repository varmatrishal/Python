print("Welcome to Trishal's Calculator Application")
#modification made November 2nd 2021


# Returns the sum of the sum
def add(num1, num2):
    return num1 + num2
# Returns subtracted
def sub(num1, num2):
    return num1 - num2

# Returns multiplication
def mul(num1, num2):
    return num1 * num2
#Returns division of two numbers
def div(num1, num2):
    return num1 / num2

# Return the mod of the number "%"
def mod(num1, num2):
    return num1 % num2

def main():
    operation = input("what do you want to do [ + , - , / , * ]   ? :    ")
    if(operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "%"):
        #invalid operation
        print("You must enter a valid operation: ")

    else:
        var1 = int(input("Enter the first number: "))
        var2 = int(input("Enter the second number: "))
        if(operation == '+'):
            print(add(var1, var2))
        if (operation == "-"):
            print(sub(var1, var2))
        if (operation == "*"):
            print(mul(var1, var2))
        if (operation == "/"):
            print(div(var1, var2))
        if (operation == "%"):
            print(mod(var1, var2))

main()
