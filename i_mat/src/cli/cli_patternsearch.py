import sys

from i_mat.src.cli.cli_menu_userInput import text_menu_selection_header, text_menu_selection_input

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_proceed
from i_mat.src.cli.cli_results_export import text_menu_headers, text_menu_headers_withoutExplanationsColumn
from i_mat.src.cli.cli_text_output import text_menu_exception_selectionOutOfRange
from i_mat.src.utils.utils_without_userInput import utility_clear_screen


def module_navigation_patternSearch():
    list_de = [
        [
            "REPT: Neue Suchmusterauswahl",
            "repeatSelection",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "EXPT: Ergebnisse als CSV-Datei exportieren",
            "export_CSV",
            "<Exportiert und speichert die Ergebnisse als CSV-Datei>",
        ],
        [
            "GRPH: Ergebnisse als XML-Datei exportieren",
            "Export_Notentext",
            "<Exportiert und speichert die Ergebnisse farblich markiert als XML-Datei>",
        ],
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New search pattern selection", "repeatSelection", "<Repeat the tool with new score selection>",
        ],
        [
            "EXPT: Export results as CSV file",
            "export_CSV",
            "<Exports and saves the results as CSV file>",
        ],
        [
            "GRPH: Export results as XML file",
            "Export_Notentext",
            "<Exports and saves the results highlighted in a xml file>",
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def text_patternSearch_showPatternSelection(selection):
    text_de = "Auswahl (englische Tonnamen): " + str(selection)

    text_en = "Selection: " + str(selection)

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_patternSearch_deleteSelection():
    text_de = "Die Eingabe wurde gelöscht. Bitte geben Sie die Suchmuster erneut ein."

    text_en = "The entry has been deleted. Please re-enter the search pattern."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_patternSearch_patternsFound(result_quantity):
    text_de = "Das eingegebene Suchmuster wurde genau " + \
              str(result_quantity) + "-mal gefunden."

    text_en = "The search pattern entered was found exactly " + \
              str(result_quantity) + " times."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_patternSearch_includeRests():
    text_de = (
        "Sollen Muster über Pausen hinweg gesucht werden?\n\n"
        "[ja = Pausen werden bei der Mustersuche ignoniert] (ja/nein): "
    )

    text_en = (
        "Should patterns be searched across rests?\n\n"
        "[yes = rests are ignored in the pattern search] (yes/no): "
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_patternSearch_enter_customRhythm():
    text_de = (
        "Bitte geben Sie nachfolgend einen selbstgewählten Rhythmuswert ein.\n\n"
        "Hinweis 1: 1.0 = Viertelnote; 2.0 = Halbe Note etc.\n\n"
        "Komplexe Rhythmen, z.B. Triolen/Quintolen, können als Brüche eingegeben werden: z.B. 1/3 oder 1/5\n\n"
        "Siehe hierzu: https://web.mit.edu/music21/doc/usersGuide/usersGuide_19_duration2.html\n\n"
        "Hinweis 2: Es sind nur Zahlen, z.B. '1.0', '1' oder '1/3' zulässig.\n\n"
        "Eingabe: "
    )

    text_en = (
        "Please enter a custom rhythm value below.\n\n"
        "Note 1: 1.0 = quarter note; 2.0 = half note etc.\n\n"
        "Complex rhythms, e.g. triplets/quintuplets, can be entered as fractions: e.g. 1/3 or 1/5\n\n"
        "See also: https://web.mit.edu/music21/doc/usersGuide/usersGuide_19_duration2.html\n\n"
        "Note 2: Only numbers, e.g. '1.0', '1' or '1/3' are permitted.\n\n"
        "Input: "
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def open_submenu_patternSearch(received_list):
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_patternSearch_showPatternSelection(config.global_searchPattern))
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplanationsColumn()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(received_list, 1):
            print("{:<4} {:<65}".format(index, item[0]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(received_list):
                utility_clear_screen()

                return received_list[userInput_menuSelection_int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(received_list)))
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(received_list)))
            print("")

            input(text_general_proceed())
            print("")
