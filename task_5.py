# Напишіть програму, яка читає вміст текстового файлу та виводить
# кількість слів у ньому.


def fun_read_count_word():
    try:
        file = open("task_5_1.txt", "r")
        content = file.read()
        count = len(content.split(" "))
        print(f"There are only {count} words in the file")
        file.close()
    except FileNotFoundError:
        print("File does not exist")
