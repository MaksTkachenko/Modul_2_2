import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7
import task_8
import task_9


if __name__ == '__main__':
    value = int(input("Choose a task: "))
    match value:
        case 1:
            task_1.fun_index_error()
        case 2:
            task_2.fun_input_user()
        case 3:
            task_3.fun_file_not_found_error()
        case 4:
            task_4.fun_zero_division_error()
        case 5:
            task_5.fun_read_count_word()
        case 6:
            task_6.fun_input_user_read_file()
        case 7:
            task_7.fun_copy_file()
        case 8:
            task_8.fun_open_two_file_riad()
        case 9:
            task_9.fun_delete_line()
        case _:
            print("Incorrect number")
