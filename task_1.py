#О бробіть виняток IndexError, коли програма намагається отримати доступ
# до неправильного індексу в списку.
def fun_index_error():
    my_list = ["apple", "orange", "strawberry", "raspberry", "peach", "cherry"]
    index_input = int(input("Enter the index you want to view: "))
    try:
        print(my_list[index_input])  # Спроба доступу до неіснуючого індексу
    except IndexError:
        print("Error: Invalid list index!!!")
