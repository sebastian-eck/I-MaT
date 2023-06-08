import sys
from os import name, system

import pandas as pd
from IPython.core.display import HTML
from IPython.core.display_functions import display

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_close_audioPlayer, text_general_proceed, \
    text_general_terminateProgram, text_general_title
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_with_userInput import menu_askUser_repeatPreviousTool


def utility_playback_MIDI():
    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    print(text_general_close_audioPlayer())
    print("")

    # --- Unterhalb: Code des Tools ---

    try:
        temporary_selectedScore.show("midi")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    # --- Oberhalb: Code des Tools ---

    # --- Nachfolgend: Fragt den User, ob das previousTool mit einer neuen Notenauswahl wiederholt werden soll

    menu_askUser_repeatPreviousTool(utility_playback_MIDI)


def utility_getKeyToValue(val, dictionary):
    try:
        for key, value in dictionary.items():
            if val == value:
                return key

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def utility_count(num_list):
    try:
        count_dict = {}

        for num in num_list:
            count_dict[num] = num_list.count(num)

        return dict(sorted(count_dict.items(), key=lambda x: x[1]))

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def utility_clear_screen():
    try:
        if name == "nt":
            _ = system("cls")

        # for mac and linux(here, os.name is 'posix')

        else:
            _ = system("clear")

        print(text_general_title())

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        user_input = input(text_general_terminateProgram())
        print("")

        utility_terminateProgram()


def utility_userInput_isAffirmative(user_input):
    if user_input == "ja" or user_input == "1" or user_input == "yes":
        return True

    else:
        return False


def utility_userInput_isNegative(user_input):
    if user_input == "nein" or user_input == "0" or user_input == "no":
        return True

    else:
        return False


def utility_userInput_isNumber(user_input):
    try:
        float(user_input)

        return True

    except:
        try:
            m, n = map(float, user_input.split("/"))

            return True

        except:
            return False


def utility_terminateProgram():
    exit()


def utility_export_as_csv(
        data,
        columns,
        save_at,
        do_print=False,
        do_return_pd=False,
        sep=";",
        index=False,
        header=True,
):
    # data = [[row1 column1, row1 column2], [row2 column1, row2 column2] ...]

    try:
        """
        data (list): nd array as list
        columns (list): list of column header in strings
        save_at (str) : path the csv to be saved
        """

        pd_data = pd.DataFrame(data, columns=columns)
        pd_data.to_csv(save_at, sep=";", index=index, header=header)
        if do_print:
            display(HTML(pd_data.to_html(index=False)))
        if do_return_pd:
            return pd_data

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def utility_listToString(received_list):
    try:
        string = " ".join(
            [
                str(item)
                .replace("'", "")
                .replace(" ", "")
                .replace(",", ": ")
                .replace("[", "")
                .replace("]", "")
                for item in received_list
            ]
        )

        return string

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def change_LANGUAGE():

    if config.LANGUAGE == "DE":
        config.LANGUAGE = "EN"

    elif config.LANGUAGE == "EN":
        config.LANGUAGE = "DE"
