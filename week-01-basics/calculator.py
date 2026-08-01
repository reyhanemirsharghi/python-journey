first_number = int(input("first number: "))
operator = input("operator: ")
second_number = int(input("second number: "))
result = None

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("Division by zero is not allowed.")
    else:
        result = first_number / second_number
           
    
else:
    print("Invalid operator.")

if result is not None:
    print(result)