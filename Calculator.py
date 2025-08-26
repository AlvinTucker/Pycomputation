def Add():
    while True:
        A = float(input("Enter first number (9990 to quit): "))
        if A == 9990:
            break
        B = float(input("Enter second number (9990 to quit): "))
        if B == 9990:
            break

        result = A + B
        print("The sum is " + str(result))

def Min():
    while True:
        A = float(input("Enter first number (9990 to quit): "))
        if A == 9990:
            break
        B = float(input("Enter second number (9990 to quit): "))
        if B == 9990:
            break

        result = A - B
        print("The difference is " + str(result))


print("For addition, type 'Add'. For subtraction, type 'Min'.")
function = input()

if function == "Add":
    Add()
elif function == "Min":
    Min()
