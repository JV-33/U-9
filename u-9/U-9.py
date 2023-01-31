x = int(input('''kalkulatora iespejas
        1) pieskaitīt
        2) atņemt
        3) reizināt
        4) dalīt
: '''))

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

if x == 1:
    result = num1 + num2

elif x == 2:
    result = num1 - num2

elif x == 3:
    result = num1 * num2

elif x == 4:
    result = num1 / num2

else:
    print("nederīga opcija")
    result = None

if result is not None:
    print(result)
