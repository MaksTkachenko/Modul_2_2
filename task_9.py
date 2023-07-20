# Створіть функцію, яка видаляє вказаний рядок з текстового файлу.

def fun_delete_line():

    file_name = "task_9_1.txt"
    choose_line_delete = int(input("Choose number line for delete: "))
    try:

        file = open(file_name, 'r')
        try:
            text_file = file.readlines()
            file.close()

            if choose_line_delete < 1 or choose_line_delete > len(text_file):
                print("Incorrect term number!!!")

            del text_file[choose_line_delete - 1]  # delete the term with the specified number

            file = open(file_name, 'w')
            file.writelines(text_file)

        except Exception as e_1:
            print(e_1)
        finally:
            file.close()

    except FileNotFoundError:
        print("File not found")
    except Exception as e_2:
        print(e_2)
    finally:
        print("The program is finished")
