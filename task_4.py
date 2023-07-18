# Реалізуйте функцію, яка ділить два числа, але обробляє помилку
# **`ZeroDivisionError`**, якщо друге число дорівнює нулю.

def fun_zero_division_error():
    try:
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
        result = num_1 / num_2
        print(f"{num_1}/{num_2}={result}")
    except ZeroDivisionError:
        print("Incorrect data entered. Please enter the numbers.")
