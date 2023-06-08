import os
import sys

from music21 import environment

from i_mat.src.cli.cli_feedback import text_environmentFile_configure_musescorePath, \
    text_environmentFile_configure_scratchPath, text_environmentFile_createNewFile, \
    text_environmentFile_createNewFile_created, \
    text_environmentFile_createNewFile_noFileCreated, text_environmentFile_reconfigure_askDelete, \
    text_environmentFile_reconfigure_deleted, text_environmentFile_reconfigure_notDeleted, text_environmentFile_showPath
from i_mat.src.cli.cli_general_display import text_general_checkEntry, text_general_enter_newPath, \
    text_general_input_RestrictedToYesAndNo, text_general_proceed, text_general_show_enteredPath
from i_mat.src.cli.cli_menu_entries import environment_list
from i_mat.src.cli.cli_results_export import text_menu_headers, text_menu_headers_withExplanationsColumn
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_userInput_isAffirmative, \
    utility_userInput_isNegative


def check_environmentFile():
    try:
        us = environment.UserSettings()

        environmentFile_path = us.getSettingsPath()

        if os.path.exists(environmentFile_path) == False:
            loop_done = False

            while not loop_done:
                utility_clear_screen()

                input_text = input(text_environmentFile_createNewFile(environmentFile_path))
                print("")

                if utility_userInput_isAffirmative(input_text):
                    utility_clear_screen()

                    try:
                        us.create()

                        us["autoDownload"] = "allow"

                        print(
                            text_environmentFile_createNewFile_created(
                                us.getSettingsPath()
                            )
                        )
                        print()

                        input_text = input(text_general_proceed())
                        print("")

                        utility_clear_screen()

                        environmentFile_enterPath_MuseScore3()

                        environmentFile_enterPath_scratchFolder()

                        loop_done = True

                    except Exception as e:
                        print(text_exception_general(
                            e, sys._getframe().f_code.co_name))
                        print("")

                        loop_done = True

                        input_text = input(text_general_proceed())
                        print("")

                elif utility_userInput_isNegative(input_text):
                    utility_clear_screen()

                    print(text_environmentFile_createNewFile_noFileCreated())
                    print("")

                    loop_done = True

                    input_text = input(text_general_proceed())
                    print("")

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop_done = False

                    input_text = input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input_text = input(text_general_proceed())
        print("")

    utility_clear_screen()


def environmentFile_enterPath_MuseScore3():
    loop_done = False

    while not loop_done:
        utility_clear_screen()

        try:
            print(text_environmentFile_configure_musescorePath())
            print("")

            MuseScore3_Pfad_Input = str(input(text_general_enter_newPath()))
            print("")

            MuseScore3_Pfad = MuseScore3_Pfad_Input.replace('"', "")

            print(text_general_show_enteredPath(MuseScore3_Pfad))
            print("")

            loop2Done = False

            while not loop2Done:
                user_input = input(text_general_checkEntry())
                print("")

                if utility_userInput_isAffirmative(user_input):
                    loop_done = True
                    loop2Done = True

                    us = environment.UserSettings()

                    us["musescoreDirectPNGPath"] = MuseScore3_Pfad

                    us["musicxmlPath"] = MuseScore3_Pfad

                    print("\n")

                    utility_clear_screen()

                elif utility_userInput_isNegative(user_input):
                    loop_done = False
                    loop2Done = True

                    utility_clear_screen()

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop2Done = False

                    input(text_general_proceed())
                    print("")

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")

            loop_done = False

    utility_clear_screen()


def environmentFile_enterPath_scratchFolder():
    loop_done = False

    while not loop_done:
        utility_clear_screen()

        try:
            print(text_environmentFile_configure_scratchPath())
            print("")

            Scratch_Ordner_Pfad_Input = str(
                input(text_general_enter_newPath()))
            print("")

            Scratch_Ordner_Pfad = Scratch_Ordner_Pfad_Input.replace('"', "")

            print(text_general_show_enteredPath(Scratch_Ordner_Pfad))
            print("")

            loop2Done = False

            while not loop2Done:
                user_input = input(text_general_checkEntry())
                print("")

                if utility_userInput_isAffirmative(user_input):
                    loop_done = True
                    loop2Done = True

                    us = environment.UserSettings()

                    us["directoryScratch"] = Scratch_Ordner_Pfad

                    utility_clear_screen()

                elif utility_userInput_isNegative(user_input):
                    loop_done = False
                    loop2Done = True

                    utility_clear_screen()

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop2Done = False

                    input(text_general_proceed())
                    print("")

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")

            loop_done = False

    utility_clear_screen()


def environmentFile_path():
    utility_clear_screen()

    try:
        us = environment.UserSettings()

        print(text_environmentFile_showPath(us.getSettingsPath()))
        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


def show_environmentFile_settings():
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        us = environment.UserSettings()

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(environment_list(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    utility_clear_screen()


def environmentFile_settings_reconfigure():
    try:
        us = environment.UserSettings()

        environmentFile_path = us.getSettingsPath()

        if os.path.exists(environmentFile_path):
            loop_done = False

            while not loop_done:
                utility_clear_screen()

                print(text_environmentFile_showPath(environmentFile_path))
                print("")

                user_input = input(text_environmentFile_reconfigure_askDelete())
                print("")

                if utility_userInput_isAffirmative(user_input):
                    os.remove(environmentFile_path)

                    print(text_environmentFile_reconfigure_deleted())
                    print("")

                    input(text_general_proceed())
                    print("")

                    utility_clear_screen()

                    us.create()

                    us["autoDownload"] = "allow"

                    print(
                        text_environmentFile_createNewFile_created(
                            us.getSettingsPath())
                    )
                    print("")

                    input(text_general_proceed())
                    print("")

                    utility_clear_screen()

                    environmentFile_enterPath_MuseScore3()

                    environmentFile_enterPath_scratchFolder()

                    loop_done = True

                elif utility_userInput_isNegative(user_input):
                    loop_done = True

                    print(text_environmentFile_reconfigure_notDeleted())
                    print()

                    input(text_general_proceed())
                    print("")

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    input(text_general_proceed())
                    print("")

                    loop_done = False

        else:
            loop_done = False

            while not loop_done:
                utility_clear_screen()

                user_input = input(text_environmentFile_createNewFile(us.getSettingsPath()))
                print("")

                if utility_userInput_isAffirmative(user_input):
                    us.create()

                    us["autoDownload"] = "allow"

                    print(
                        text_environmentFile_createNewFile_created(
                            us.getSettingsPath())
                    )
                    print("")

                    input(text_general_proceed())
                    print("")

                    utility_clear_screen()

                    environmentFile_enterPath_MuseScore3()

                    environmentFile_enterPath_scratchFolder()

                    loop_done = True

                elif utility_userInput_isNegative(user_input):
                    print(text_environmentFile_createNewFile_noFileCreated())
                    print("")

                    input(text_general_proceed())
                    print("")

                    loop_done = True

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop_done = False

                    input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
