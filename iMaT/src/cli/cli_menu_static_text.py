def text_general_title():
    text_en = (
        '\nI-MaT - Interactive Music Analysis Tool, Version 2.2, January 2022\n\n'
        'Project Title: "Computer-Assisted Music Analysis"\n\n'
        'Fellowship for Innovations in Digital University Teaching (University of Music Franz Liszt Weimar)\n\n'
        '----------------------------------------------------------------------\n'
    )

    return text_en
#
# text_environmentFile_createNewFile_created_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "A new environment file has been created in the following directory:"],
#         ["Message 2", str(received_environmentFile_path)],
#         ["Message 3", 'If you cannot see the file in Explorer / Finder, you have to activate the option "View hidden files":'],
#         ["Message 4", "WINDOWS: Explorer > View > Show/hide > Hidden items"],
#         ["Message 5", 'MAC: In the Finder key combination "Command key (cmd / command) + Shift key + period"'],
#     ]
# }
#
# text_environmentFile_createNewFile_noFileCreated_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "If you do not create the Environment file, you can use the program, but you cannot view score files in your Score Editor or download score files from the Internet."],
#         ["Message 2", 'To create the Environment file later, open "SETT: Settings > Environment: Reconfigure Settings.'],
#         ["Message 3", "It is strongly advised to create and configure the environments file."]
#     ]
# }
#
# text_environmentFile_reconfigure_askDelete_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Do you want to delete the Environment file? (yes/no): "]
#     ]
# }
#
# text_environmentFile_reconfigure_deleted_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The Environment file was deleted successfully."]
#     ]
# }
#
# text_environmentFile_reconfigure_notDeleted_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The Environment file was not deleted."]
#     ]
# }
#
# text_environmentFile_showPath_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The path of the environment file is: " + str(received_environmentFile_path)],
#         ["Message 2", 'If you cannot see the file, you have to activate the option "Show hidden files":'],
#         ["Message 3", "WINDOWS: Explorer > View > Show / hide > Hidden items"],
#         ["Message 4", 'MAC: In the Finder key combination "Command key (cmd / command) + Shift key + period"']
#     ]
# }
#
# text_environmentFile_configure_musescorePath_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Please enter the path to your MuseScore3.exe (Windows) or MuseScore3.app (Mac) file."],
#         ["Message 2", "Under Windows you will usually find this in the folder: C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe"],
#         ["Message 3", "On Mac you can usually find this in the folder: Applications\\MuseScore3.app"],
#         ["Message 4", 'WINDOWS: To do this, simply drag the "MuseScore3.exe" file from the folder into the terminal and press "Enter"'],
#         ["Message 5", 'MAC: Right click on "MuseScore3.app" and select "Copy MuseScore3.app as path name"'],
#         ["Message 6", 'Insert the link below with "command + v"'],
#         ["Message 7", "Be careful not to put any spaces at the end of the path"]
#     ]
# }
#
# text_environmentFile_configure_scratchPath_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Please enter the path to the folder in which your files exported by music21 should be saved."],
#         ["Message 2", 'WINDOWS: To do this, simply drag the icon of the desired folder into the terminal and press "Enter"'],
#         ["Message 3", 'MAC: Right-click on the desired folder and select "Copy <folder name> as path name"'],
#         ["Message 4", 'Then insert the path of the desired folder with "command + v"'],
#         ["Message 5", "Be careful not to put any spaces at the end of the path"]
#     ]
# }
#
# text_exception_modules_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Packages are missing on your system. Please contact a tutor (error code: MOD). The following packages are required:"],
#         ["Message 2", "python==3.10.*\nnumpy==1.20.*\nmatplotlib==3.4.*\npandas==1.2.*\nipython==7.24.*\nscipy==1.6.*\nmusic21==6.7.*"],
#         ["Message 3", "Error in line: PLACEHOLDER FOR LINE NUMBER -> PLACEHOLDER FOR EXCEPTION TEXT"],
#         ["Message 4", "If the problem persists, please contact project support.\n\nSupport: analyse@hfm-weimar.de"]
#     ]
# }
#
# text_general_title_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "\nI-MaT - Interactive music analysis tool, (2.2, 01.2022)\n\n"],
#         ["Message 2", 'Fellowship project "Computer-assisted Music Analysis"\n\n\n'],
#         ["Message 3", "Fellowship for innovations in digital university teaching\n\n"],
#         ["Message 4", "----------------------------------------------------------------------\n"]
#     ]
# }
#
# text_general_checkEntry_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Is the entry correct? (yes/no): "]
#     ]
# }
#
# text_general_proceed_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "<To continue, please press Enter>"]
#     ]
# }
#
# text_general_input_RestrictedToYesAndNo_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "<Input restricted to yes/no (alternatively: 1/0). Please re-enter.>"]
#     ]
# }
#
# text_general_input_restrictedToNumbers_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Error: '" + input_text + "' - Input restricted to numbers. Please re-enter."]
#     ]
# }
#
# text_general_close_museScore3_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Note 1: Please close MuseScore to continue.\n\n"],
#         ["Message 2", "Note 2: to export the file as PDF in MuseScore please use '> File > Export ...'.\n\n"],
#         ["Message 3", "IMPORTANT: Loading time varies with the size of the imported file."]
#     ]
# }
#
# text_general_close_audioPlayer_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Note: please close the audio player to continue."]
#     ]
# }
#
# text_general_enter_newPath_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Enter Path/URL: "]
#     ]
# }
#
# text_general_show_enteredPath = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", 'The following path/URL was entered: "{Your Entered Path/URL}"']
#     ]
# }
#
# text_general_projectDescription = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the project description:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Courses on musical analysis are an integral part..."],
#         ["Message 2", "and musicians at universities and conservatories..."],
#         ["Message 3", "The goal of the fellowship project is to design..."],
#         #...
#         # Repeat this for all paragraphs
#         ["Message N", "University of Music Franz Liszt Weimar"],
#         ["Message N+1", "Institute for Musicology Weimar | Jena"],
#         ["Message N+2", "University Center at the Horn"],
#         ["Message N+3", "Carl-Alexander-Platz 1"],
#         ["Message N+4", "99425 Weimar"],
#     ]
# }
#
# text_general_chooseKey = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following instruction:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Please select the key of the selected score section in the following selection menu."]
#     ]
# }
#
# text_general_exportToDiagrammUnavailable = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "data_values export as a graphic is not intended for this tool."]
#     ]
# }
#
# text_general_noResults = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Error: The analysis of the score file did not produce any results."]
#     ]
# }
#
# text_display_showScoreSelection_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Would you like to display the selected/entered music text? (yes/no):"],
#     ]
# }
#
# text_export_fileName_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Under what name should the file be saved? Filename:"],
#     ]
# }
#
# text_general_terminateProgram_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "<To terminate the program, please press Enter>"],
#     ]
# }
#
# text_general_exportSuccessful_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The file was saved successfully."],
#         ["Message 2", "Location: " + str(path)],
#         ["Message 3", "Filename: " + str(filename) + str(extension)],
#     ]
# }
#
# text_general_exportGraph_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The file was saved successfully."],
#         ["Message 2", "Location: " + str(path)],
#         ["Message 3", "In order to be able to continue, you may have to close the graphic views that have just opened."],
#     ]
# }
#
# text_general_exportGraphName_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Please select a title for the graphic diagram to be exported:"],
#     ]
# }
#
# text_patternSearch_showPatternSelection_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Selection: " + str(selection)],
#     ]
# }
#
# text_patternSearch_deleteSelection_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The entry has been deleted. Please re-enter the search pattern."],
#     ]
# }
#
# text_patternSearch_patternsFound_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "The search pattern entered was found exactly " + str(result_quantity) + " times."],
#     ]
# }
#
# text_patternSearch_includeRests_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Should patterns be searched across rests?"],
#         ["Message 2", "[yes = rests are ignored in the pattern search] (yes/no):"],
#     ]
# }
#
# text_patternSearch_enter_customRhythm_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Please enter a custom rhythm value below."],
#         ["Message 2", "Note 1: 1.0 = quarter note; 2.0 = half note etc."],
#         ["Message 3", "Complex rhythms, e.g. triplets/quintuplets, can be entered as fractions: e.g. 1/3 or 1/5"],
#         ["Message 4", "See also: https://web.mit.edu/music21/doc/usersGuide/usersGuide_19_duration2.html"],
#         ["Message 5", "Note 2: Only numbers, e.g. '1.0', '1' or '1/3' are permitted."],
#         ["Message 6", "Input:"],
#     ]
# }
#
# text_menu_selection_header_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Please select:"],
#     ]
# }
#
# text_menu_selection_input_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Which menu item should be executed? (<No. of menu item>):"],
#     ]
# }
#
# text_menu_selection_repeat_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "Would you like to repeat the tool with a different score selection? 'no' => main menu (yes/no):"],
#     ]
# }
#
# text_menu_selection_noPreviousSelection_dict = {
#     "menu_displayed_text": [
#         "-- message to the user --",
#         "Please read the following message:",
#         "<To continue, please press Enter>",
#         ["", "Message"]
#     ],
#     "menu_entries_text": [
#         ["Message 1", "There is not yet a selection of notes that can be used."],
#         ["Message 2", "Please choose from menu item 1 or 2."],
#     ]
# }
