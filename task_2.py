# Створіть функцію, яка приймає два числа від користувача та обробляє
# помилку, якщо введені дані не є числами.

def fun_input_user():
    try:
        number_input_1 = int(input("Enter number_1: "))
        number_input_2 = int(input("Enter number_2: "))

        print(f"You enter: {number_input_1} and {number_input_2}")
    except ValueError:
        print("Incorrect data entered. Please enter the numbers.")
