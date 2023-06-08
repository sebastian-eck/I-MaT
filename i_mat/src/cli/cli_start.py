import sys

from i_mat.src.cli.cli_menu_userInput import text_menu_selection_header, text_menu_selection_input

from i_mat.src.cli.cli_general_display import text_general_proceed
from i_mat.src.cli.cli_results_export import text_menu_headers, text_menu_headers_withExplanationsColumn
from i_mat.src.cli.cli_text_output import text_menu_exception_selectionOutOfRange
from i_mat.src.utils.utils_without_userInput import utility_clear_screen
from i_mat_new.src.cli.cli_menu_entries import startmenue_entries


def open_startmenu():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(startmenue_entries(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        utility_clear_screen()

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(startmenue_entries()):
                utility_clear_screen()

                startmenue_entries()[userInput_menuSelection_int][1]()

                utility_clear_screen()

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(startmenue_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(startmenue_entries()))
            )
            print("")

            input(text_general_proceed())
            print("")


