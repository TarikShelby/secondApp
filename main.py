a = float(input("Введите первое число : "))
b = float(input("Введите второе число : "))

operation = input("Что сделать ? ( + , - , * , / ):")

if operation == "+":
    print(a + b )
elif operation == "-":
    print(a - b )
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b )