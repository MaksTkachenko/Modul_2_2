# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст,
# виводячи рядки, які є у першому файлі, але відсутні у другому.


def fun_open_two_file_riad():

    file_name_1 = "task_8_1.txt"
    file_name_2 = "task_8_2.txt"
    try:
        file_1 = open(file_name_1, 'r')
        file_2 = open(file_name_2, 'r')

        try:
            while True:
                text_file_1 = file_1.readline()
                text_file_2 = file_2.readline()
                if text_file_1 != text_file_2:
                    print(text_file_1, end='')

                if not text_file_1:
                    break
            print("\n")

        except Exception as e_1:
            print(e_1)
        finally:
            file_1.close()
            file_2.close()
    except FileNotFoundError:
        print("File not found")
    except Exception as e_2:
        print(e_2)
    finally:
        print("The program is finished")
