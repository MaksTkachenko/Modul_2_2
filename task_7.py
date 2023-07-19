# Реалізуйте програму, яка копіює вміст одного файлу в інший.

def fun_copy_file():

    name_file_1 = "task_6_1.txt"
    name_file_2 = "task_7_1.txt"
    try:
        file_1 = open(name_file_1, 'r')
        text_file = file_1.read()
        file_1.close()
        print(f"First file {name_file_1} open and close successful!")

        try:
            file_2 = open(name_file_2, 'w')
            file_2.write(text_file)
            file_2.close()
            print(f"Second file {name_file_2} open and close successful!")
        except FileNotFoundError:
            print(f"File {name_file_2} does not exist")
        except Exception as e_1:
            print(e_1)

    except FileNotFoundError:
        print(f"File {name_file_1} does not exist")
    except Exception as e_2:
        print(e_2)
    finally:
        print("The END")


