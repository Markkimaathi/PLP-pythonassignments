num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")


def format_num(n):
    return str(int(n)) if n.is_integer() else str(n)


if op == '+':
    result = num1 + num2
    print(f"{format_num(num1)} + {format_num(num2)} = {format_num(result)}")
elif op == '-':
    result = num1 - num2
    print(f"{format_num(num1)} - {format_num(num2)} = {format_num(result)}")
elif op == '*':
    result = num1 * num2
    print(f"{format_num(num1)} * {format_num(num2)} = {format_num(result)}")
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{format_num(num1)} / {format_num(num2)} = {format_num(result)}")
else:
    print("Invalid operation entered.")