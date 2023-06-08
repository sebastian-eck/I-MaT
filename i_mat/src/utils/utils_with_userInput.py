import sys

from i_mat.src.cli.cli_menu_userInput import text_menu_selection_repeat
from music21 import environment, key, roman

from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_chooseKey, \
    text_general_exportSuccessful, text_general_input_RestrictedToYesAndNo, text_general_proceed
from i_mat.src.cli.cli_menu_entries import module_navigation_conversion
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn, \
    open_submenu_data_withoutExplanationsColumn
from i_mat.src.pattern_search.patternsearch import keys_list
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_userInput_isAffirmative, \
    utility_userInput_isNegative


def menu_askUser_repeatPreviousTool(previousTool):
    try:
        while True:
            utility_clear_screen()

            user_input = input(text_menu_selection_repeat())
            print("")

            if utility_userInput_isAffirmative(user_input):
                utility_clear_screen()

                previousTool()

                break

            elif utility_userInput_isNegative(user_input):
                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

                loop_done = False

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def score_export():
    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_conversion())

            if user_selection == "XML":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = temporary_selectedScore.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "XML_chords":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                selectedScore_chordConnection = temporary_selectedScore.chordify()

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

            elif user_selection == "XML_chords_figuredBass":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                selectedScore_chordConnection = temporary_selectedScore.chordify()

                for (
                        item
                ) in selectedScore_chordConnection.recurse().getElementsByClass(
                    "Chord"
                ):
                    item.closedPosition(forceOctave=4, inPlace=True)

                    item.annotateIntervals()

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

            elif user_selection == "XML_chords_romanNumerals":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                utility_clear_screen()

                print(text_general_chooseKey())
                print("")

                input(text_general_proceed())
                print("")

                Tonart = open_submenu_data_withoutExplanationsColumn(keys_list())

                selectedScore_chordConnection = temporary_selectedScore.chordify()

                for (
                        item
                ) in selectedScore_chordConnection.recurse().getElementsByClass(
                    "Chord"
                ):
                    rn = roman.romanNumeralFromChord(item, key.Key(Tonart))

                    item.addLyric(str(rn.figure))

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

            elif user_selection == "MIDI":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".midi"
                )

                mf = temporary_selectedScore.write("midi", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".midi"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "TXT_music21":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".txt"
                )

                mf = temporary_selectedScore.write("txt", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".txt"))
                print()

                input(text_general_proceed())

            elif user_selection == "TXT_music21_textline":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".txt"
                )

                mf = temporary_selectedScore.write("textline", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".txt"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "TXT_braille":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".txt"
                )

                mf = temporary_selectedScore.write("braille", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".txt"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "lilypond":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".ly"
                )

                mf = temporary_selectedScore.write("lily", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".ly"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "PDF":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName().replace(" ", "_"))
                print("")

                path_and_filename = str(score_export_path) + \
                                    "\\" + str(filename)

                mf = temporary_selectedScore.write("lily.pdf", fp=str(path_and_filename))

                print(text_general_exportSuccessful(score_export_path, filename, ".pdf"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "PNG":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName().replace(" ", "_"))
                print("")

                path_and_filename = str(score_export_path) + \
                                    "\\" + str(filename)

                mf = temporary_selectedScore.write("lily.png", fp=str(path_and_filename))

                print(text_general_exportSuccessful(score_export_path, filename, ".png"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
