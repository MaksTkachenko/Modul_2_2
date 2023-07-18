# Напишіть програму, яка відкриває файл для читання та обробляє помилку
# FileNotFoundError, якщо файл не знайдено.

def fun_file_not_found_error():
    try:
        file = open("test_1.txt", "r")
        print("File opened")
        content = file.read()
        print(content)
        file.close()
        print("File closed")
    except FileNotFoundError:
        print("File does not exist")
