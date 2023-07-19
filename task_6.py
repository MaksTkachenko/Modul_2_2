# Створіть функцію, яка приймає рядок від користувача та записує його у файл.


def fun_input_user_read_file():
    try:
        file = open("task_6_1.txt", 'w')
        file.write(input("Enter any test for wried in file:"))
        print("The text was successfully written to the file.")
        file.close()
    except FileNotFoundError:
        print("File does not exist")
    finally:
        print("The work is completed")
