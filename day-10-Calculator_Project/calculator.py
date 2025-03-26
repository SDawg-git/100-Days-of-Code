def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = input("Please enter the first number: ")

keepLooping = True
while keepLooping == True:

    operator = input("Please enter the mathematical operator: "
                     "\n+"
                     "\n-"
                     "\n*"
                     "\n/"
                     "\n")
    n2 = input("Please enter the second number: ")

    print(operations[operator](int(n1), int(n2)))

    answer = input("Do you want to do another calculation with the previous result? Y/N: ")
    if answer == "N":
        print("Cheerio")
        keepLooping = False
    else:
        n1 = operations[operator](float(n1), float(n2))




