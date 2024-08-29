from dotenv import load_dotenv
from .src.views import (student, show_user_selection,
                        show_return_selection, show_wrong_selection)
from .src.utils.common import clear_screen


def process_view_student():
    clear_screen()
    student.view_students()
    show_return_selection()
    input()
    clear_screen()


def choose_function():
    while (True):
        show_user_selection()
        user_input = input()
        if user_input == '1':
            process_view_student()
            break
        elif user_input == '0':
            return
        else:
            clear_screen()
            show_wrong_selection()

    choose_function()


if __name__ == "__main__":
    load_dotenv()
    choose_function()
