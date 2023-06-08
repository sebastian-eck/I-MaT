import sys

from music21 import environment, key, roman

from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_chooseKey, \
    text_general_close_museScore3, text_general_exportSuccessful, text_general_proceed
from i_mat.src.cli.cli_results_export import module_navigation_transformedScores
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn, \
    open_submenu_data_withoutExplanationsColumn
from i_mat.src.pattern_search.patternsearch import keys_list
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_with_userInput import menu_askUser_repeatPreviousTool
from i_mat.src.utils.utils_without_userInput import utility_clear_screen


def visualizations_MuseScore():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

        print(text_general_close_museScore3())
        print()

        # --- Unterhalb: Code des Tools ---

        temporary_selectedScore.show()

        # --- Oberhalb: Code des Tools ---

        # --- Nachfolgend: Fragt den User, ob das previousTool mit einer neuen Notenauswahl wiederholt werden soll

        menu_askUser_repeatPreviousTool(visualizations_MuseScore)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def visualizations_chordConnections():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore_chordConnection = temporary_selectedScore.chordify()

        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_transformedScores()
            )

            if user_selection == "visualizations_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif user_selection == "save_file":
                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "repeatSelection":
                visualizations_chordConnections()

                break

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def visualization_chordConnections_figuredBass():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore_chordConnection = temporary_selectedScore.chordify()

        for item in selectedScore_chordConnection.recurse().getElementsByClass(
                "Chord"
        ):
            item.closedPosition(forceOctave=4, inPlace=True)

            item.annotateIntervals()

        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_transformedScores()
            )

            if user_selection == "visualizations_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif user_selection == "save_file":
                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "repeatSelection":
                visualization_chordConnections_figuredBass()

                break

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def visualization_chordConnections_romanNumerals():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        utility_clear_screen()

        print(text_general_chooseKey())
        print("")

        input(text_general_proceed())
        print("")

        Tonart = open_submenu_data_withoutExplanationsColumn(keys_list())

        selectedScore_chordConnection = temporary_selectedScore.chordify()

        for item in selectedScore_chordConnection.recurse().getElementsByClass(
                "Chord"
        ):
            rn = roman.romanNumeralFromChord(item, key.Key(Tonart))

            item.addLyric(str(rn.figure))

        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_transformedScores()
            )

            if user_selection == "visualizations_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif user_selection == "save_file":
                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "repeatSelection":
                visualization_chordConnections_romanNumerals()

                break

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
