# --------------------------------------

# # Menüeinträge

# ## Startmenü (erste Ebene)

def startmenu_entries():
    return {
        "menu_displayed_text": [
            "Start Menu Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["PROG: Analysis of a single piece of music", mainmenu_individualPiece_entries, "<Analysis of a single piece of music>"],
            ["TOKE: Tokenisation of one sheet music file", tokenisation_menu, "<Tokenisation of sheet music files>"],
            ["SETT: Settings", some_function, "<View the settings in the music21 environment file>"],
            ["HELP: Project overview", some_function, '<Information about the project "Computer-Aided Music Analysis">'],
            ["LANG: Change config.LANGUAGE", some_function, "<Change the output language of the program>"],
            ["EXIT: Exit program", some_function, "<Exits the Python script>"],
        ]
    }

# ### Tokenisation of a sheet music file

def tokenisation_menu():
    return {
        "menu_displayed_text": [
            "Tokenisation Menu Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): ",
        ],
        "menu_entries": [
            ["Option 1", some_function, "<Function description>"],
            ["Option 2", some_function, "<Function description>"],
            ["Option 3", some_function, "<Function description>"],
            ["Option 4", some_function, "<Function description>"],
            ["Option 5", some_function, "<Function description>"],
            ["Option 6", some_function, "<Function description>"],
            ["Option 7", some_function, "<Function description>"],
            ["Option 8", some_function, "<Function description>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ],
    }

# ### Analysis of a single piece of music


# #### Hauptmenü Einzelwerk (zweite Ebene)

def mainmenu_individualPiece_entries():
    return {
        "menu_displayed_text": [
            "Mainmenu Individual Piece Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["FILE: Menu selection", submenu_individualPiece_files_entries, "<Basic functions>"],
            ["TOOL: Menu selection (statistical analysis)", submenu_individualPiece_statisticalAnalyses_entries, "<Selection of various statistical analysis tools>"],
            ["TOOL: Menu selection (visualisation)",submenu_individualPiece_visualizations_entries, "<Selection of different visualisation tools>"],
            ["TOOL: Menu selection (pattern search)", submenu_individualPiece_patternSearch_entries, "<Selection of different tools for pattern search>"],
            ["SETT: Settings", submenu_individualPiece_settings_entries, "<Settings in the music21 environment file/language settings>"],
            ["HELP: Project overview", some_function, '<Information about the project "Computer-Aided Music Analysis">'],
            ["EXIT: Exit program", some_function, "<Exits the Python script>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, File)

def submenu_individualPiece_files_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Files Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["FILE: Select new score", some_function, "<Allows you to select a new score>"],
            ["SHOW: Show metadata (score)", some_function, "<Displays the metadata of the selected score>"],
            ["PLAY: Play selected score (midi)", some_function, "<Plays score as midi>"],
            ["NAME: Change the names of the individual parts/voices", some_function, "<Allows you to rename the individual parts/voices>"],
            ["NAME: Show names of individual parts/voices", some_function, "<Displays the names of the individual parts/voices>"],
            ["EXPO: Export file", some_function, "<Saves a selection of notes as .xml/.midi/.ly/.pdf file>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, statistische Analysen, Seite 1)

def submenu_individualPiece_statisticalAnalyses_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Statistical Analyses Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["STAT: Ambitus", some_function, ""],
            ["STAT: Ambitus (comparison)", some_function, ""],
            ["STAT: Interval types", some_function, "<Attention: currently only consistently monodic melody lines are correctly analyzed>."],
            ["STAT: Interval types and frequency", some_function, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
            ["STAT: Interval types and frequency (comparison)", some_function, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
            ["STAT: Number of intervals", some_function, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
            ["STAT: Number of tones", some_function, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
            ["HIST: Sound events per pitch", some_function, "<A histogram of the pitch space>"],
            ["HIST: Sound events per pitch class", some_function, "<A pitch class histogram>"],
            ["HIST: Sound events per tone durations", some_function, "<A histogram of the pitch lengths>"],
            ["BARS: Pitches over time (pitch lengths)", some_function, "<A graph of events sorted by pitch space over time>"],
            ["BARS: Pitch classes over time (pitch durations)", some_function, "<A graph of events sorted by pitch space over time>"],
            ["HIST: Tone starting frequency on types of metrical positions", some_function, "<Metric weight; Explanations: https://analyse.hfm-weimar.de/doku.php?id=basics1>"],
            ["MORE: Further graphs", submenu_individualPiece_statisticalAnalyses_visualizations_entries, "<Two-dimensional frequency distributions/scatter diagrams>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }

# ##### Untermenü Einzelwerk (vierte Ebene, statistische Analysen, Seite 2)

def submenu_individualPiece_statisticalAnalyses_visualizations_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Statistical Analyses Visualizations Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["SCTR: Pitch over durations", some_function, "<A scatter diagram of the sound events, sorted by pitch over durations>"],
            ["BARS: Number of pitches over durations (3D)", some_function, "<A 3D histogram of pitch and duration>"],
            ["SCTR: Pitch classes over durations", some_function, "<A scatter diagram of the sound events, sorted by pitch class, over the durations>"],
            ["SCTR: Pitch classes over time (cues)", some_function, "<A scatter plot of pitch class and offset>"],
            ["SCTR: Dynamics over pitches", some_function, "<A scatter plot of the dynamics used by each pitch class>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, Darstellungen)

def submenu_individualPiece_visualizations_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Visualizations Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["SHOW: Show sheet music selection (MuseScore)", some_function, "<Opens MuseScore and displays the selected scores>"],
            ["SHOW: Sheet music selection (chord connections)", some_function, "<Saves a selection of scores, shown as chord connections>"],
            ["SHOW: Sheet music selection (figured bass)", some_function, "<Saves a selection of scores, shown as chord connections with figured bass>"],
            ["SHOW: Sheet music selection (chord-scale system)", some_function, "<Saves a score selection, shown as chord connections with numbering>"],
            ["SHOW: Pianorolls", some_function, "<A graph of events sorted by pitch space over time>"],
            ["SHOW: Voice progression (line plot)", some_function, "<Prone to error: Only works with consistently monodic parts>"],
            ["SHOW: Dolan", some_function, "<Change in volume over time>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, Mustersuche)

def submenu_individualPiece_patternSearch_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Pattern Search Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["SEAR: Pattern search (without rhythmic values)", some_function, "<Search for a sequence of notes (without rhythmic values)>"],
            ["SEAR: Pattern search (without rhythmic values/transposed)", some_function, "<Search for a sequence of notes and all of its transpositions (without rhythmic values)>"],
            ["SEAR: Pattern search (with rhythmic values)", some_function, "<Search for a sequence of notes (with rhythmic values)>"],
            ["SEAR: Pattern search (with rhythmic values/transposed)", some_function, "<Search for a sequence of notes and all of its transpositions (with rhythmic values)>"],
            ["SEAR: Pattern search (only rhythm)", some_function, "<Search for a specific rhythm>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, Einstellungen)

def submenu_individualPiece_settings_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Settings Header",
            "Please make a selection from the options below by entering the entry index number:",
            ["Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["ENVT: Environment file (path)", some_function, "<Outputs the path of the environment file (if available)>"],
            ["ENVT: Show settings", some_function, "<Display the settings in the environment file>"],
            ["ENVT: Reconfigure settings", some_function, "<Reconfiguration of the environment file>"],
            ["LANG: Change config.LANGUAGE", some_function, "<Change the output language of the program>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }



#
# # --------------------------------------
#
# # ### Menüeinträge
#
# # #### Hauptmenü Einzelwerk (erste Ebene)

# def startmenue_entries():
#     list_de = [
#         [
#             "PROG: Analyse eines einzelnen Werkes",
#             open_mainmenu_individualPiece,
#             "<Analyse eines einzelnen Werkes>",
#         ],
#         [
#             "SETT: Einstellungen",
#             open_submenu_individualPiece_settings,
#             "<Einstellungen in der music21 environment-Datei>",
#         ],
#         [
#             "HELP: Projektübersicht",
#             text_general_projectDescription,
#             '<Informationen über das Projekt "Computergestützte Musikanalyse">',
#         ],
#         [
#             "LANG: Change config.LANGUAGE to ENGLISH",
#             change_LANGUAGE,
#             "<Change the output config.LANGUAGE of the program to German>",
#         ],
#         ["EXIT: Programm beenden", utility_terminateProgram, "<Beendet das Python-Skript>"],
#     ]
# 
#     list_en = [
#         [
#             "PROG: Analysis of a single piece of music",
#             open_mainmenu_individualPiece,
#             "<Analysis of a single piece of music>",
#         ],
#         [
#             "SETT: Settings",
#             open_submenu_individualPiece_settings,
#             "<View the settings in the music21 environment file>",
#         ],
#         [
#             "HELP: Project overview",
#             text_general_projectDescription,
#             '<Information about the project "Computer-Aided Music Analysis">',
#         ],
#         [
#             "LANG: Ändere Ausgabesprache auf DEUTSCH",
#             change_LANGUAGE,
#             "<Ändert die Ausgabesprache des Programms auf Deutsch>",
#         ],
#         ["EXIT: Exit programm", utility_terminateProgram, "<Exits the Python script>"],
#     ]
# 
#     if config.LANGUAGE == "DE":
#         return list_de
# 
#     elif config.LANGUAGE == "EN":
#         return list_en
# #
# def mainmenu_individualPiece_entries():
#     return {
#         "menu_displayed_text": [
#             "Mainmenu Individual Piece Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["FILE: Menu selection", submenu_individualPiece_files_entries, "<Basic functions>"],
#             ["TOOL: Menu selection (statistical analysis)", submenu_individualPiece_statisticalAnalyses_entries, "<Selection of various statistical analysis tools>"],
#             ["TOOL: Menu selection (visualisation)", submenu_individualPiece_statisticalAnalyses_visualizations_entries, "<Selection of different visualisation tools>"],
#             ["TOOL: Menu selection (pattern search)", submenu_individualPiece_patternSearch_entries, "<Selection of different tools for pattern search>"],
#             ["SETT: Settings", submenu_individualPiece_settings_entries, "<Settings in the music21 environment file/language settings>"],
#             ["HELP: Project overview", text_general_projectDescription, '<Information about the project "Computer-Aided Music Analysis">'],
#             ["EXIT: Exit program", utility_terminateProgram, "<Exits the Python script>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
# # #### Untermenü Einzelwerk (zweite Ebene, File)
#
# def submenu_individualPiece_files_entries():
#     return {
#         "menu_displayed_text": [
#             "Submenu Individual Piece Files Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["FILE: Select new score", select_score_filePath, "<Allows you to select a new score>"],
#             ["SHOW: Show metadata (score)", show_score_metadata, "<Displays the metadata of the selected score>"],
#             ["PLAY: Play selected score (midi)", utility_playback_MIDI, "<Plays score as midi>"],
#             ["NAME: Change the names of the individual parts/voices", name_individualVoices, "<Allows you to rename the individual parts/voices>"],
#             ["NAME: Show names of individual parts/voices", show_names_individualVoices, "<Displays the names of the individual parts/voices>"],
#             ["EXPO: Export file", score_export, "<Saves a selection of notes as .xml/.midi/.ly/.pdf file>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
# # #### Untermenü Einzelwerk (zweite Ebene, statistische Analysen, Seite 1)
#
# def submenu_individualPiece_statisticalAnalyses_entries():
#     return {
#         "menu_displayed_text": [
#             "Submenu Individual Piece Statistical Analyses Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["STAT: Ambitus", range_analysis_textOutput, ""],
#             ["STAT: Ambitus (comparison)", range_comparison_textOutput, ""],
#             ["STAT: Interval types", intervalStructure_intervalTypes_textOutput, "<Attention: currently only consistently monodic melody lines are correctly analyzed>."],
#             ["STAT: Interval types and frequency", intervalStructure_intervalTypes_quantity_textOutput, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
#             ["STAT: Interval types and frequency (comparison)", intervalStructure_intervalTypes_comparison_textOutput, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
#             ["STAT: Number of intervals", intervalStructure_Intervalle_quantity_textOutput, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
#             ["STAT: Number of tones", notes_quantity_total_textOutput, "<Attention: currently only consistently monodic melody lines are correctly analyzed>"],
#             ["HIST: Sound events per pitch", predefinedVisualizations_HistogramPitchSpace, "<A histogram of the pitch space>"],
#             ["HIST: Sound events per pitch class", predefinedVisualizations_HistogramPitchClass, "<A pitch class histogram>"],
#             ["HIST: Sound events per tone durations", predefinedVisualizations_HistogramQuarterLength, "<A histogram of the pitch lengths>"],
#             ["BARS: Pitches over time (pitch lengths)", predefinedVisualizations_HorizontalBarPitchSpaceOffset, "<A graph of events sorted by pitch space over time>"],
#             ["BARS: Pitch classes over time (pitch durations)", predefinedVisualizations_HorizontalBarPitchClassOffset, "<A graph of events sorted by pitch space over time>"],
#             ["HIST: Tone starting frequency on types of metrical positions", meter_metricWeight_textOutput, "<Metric weight; Explanations: https://analyse.hfm-weimar.de/doku.php?id=basics1>"],
#             ["MORE: Further graphs", open_submenu_individualPiece_statisticalAnalyses_visualizations, "<Two-dimensional frequency distributions/scatter diagrams>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
# # ##### Untermenü Einzelwerk (dritte Ebene, statistische Analysen, Seite 2)
#
# def submenu_individualPiece_statisticalAnalyses_visualizations_entries():
#     return {
#         "menu_displayed_text": [
#             "Submenu Individual Piece Statistical Analyses Visualizations Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["SCTR: Pitch over durations", predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength, "<A scatter diagram of the sound events, sorted by pitch over durations>"],
#             ["BARS: Number of pitches over durations (3D)", predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength, "<A 3D histogram of pitch and duration>"],
#             ["SCTR: Pitch classes over durations", predefinedVisualizations_ScatterWeightedPitchClassQuarterLength, "<A scatter diagram of the sound events, sorted by pitch class, over the durations>"],
#             ["SCTR: Pitch classes over time (cues)", predefinedVisualizations_ScatterPitchClassOffset, "<A scatter plot of pitch class and offset>"],
#             ["SCTR: Dynamics over pitches", predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol, "<A scatter plot of the dynamics used by each pitch class>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
# # #### Untermenü Einzelwerk (zweite Ebene, Darstellungen)
#
# def submenu_individualPiece_visualizations_entries():
#     return {
#         "menu_displayed_text": [
#             "Submenu Individual Piece Visualizations Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["SHOW: Show sheet music selection (MuseScore)", visualizations_MuseScore, "<Opens MuseScore and displays the selected scores>"],
#             ["SHOW: Sheet music selection (chord connections)", visualizations_chordConnections, "<Saves a selection of scores, shown as chord connections>"],
#             ["SHOW: Sheet music selection (figured bass)", visualization_chordConnections_figuredBass, "<Saves a selection of scores, shown as chord connections with figured bass>"],
#             ["SHOW: Sheet music selection (chord-scale system)", visualization_chordConnections_romanNumerals, "<Saves a score selection, shown as chord connections with numbering>"],
#             ["SHOW: Pianorolls", predefinedVisualizations_HorizontalBarPitchSpaceOffset, "<A graph of events sorted by pitch space over time>"],
#             ["SHOW: Voice progression (line plot)", melody_melodicDevelopment_visualization_lineGraph, "<Prone to error: Only works with consistently monodic parts>"],
#             ["SHOW: Dolan", predefinedVisualizations_Dolan, "<Change in volume over time>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
# # #### Untermenü Einzelwerk (zweite Ebene, Mustersuche)
#
# def submenu_individualPiece_patternSearch_entries():
#     return {
#         "menu_displayed_text": [
#             "Submenu Individual Piece Pattern Search Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["SEAR: Pattern search (without rhythmic values)", patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm, "<Search for a sequence of notes (without rhythmic values)>"],
#             ["SEAR: Pattern search (without rhythmic values/transposed)", patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm, "<Search for a sequence of notes and all of its transpositions (without rhythmic values)>"],
#             ["SEAR: Pattern search (with rhythmic values)", patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm, "<Search for a sequence of notes (with rhythmic values)>"],
#             ["SEAR: Pattern search (with rhythmic values/transposed)", patternSearch_menuStructure_toneSequence_withTransposition_withRhythm, "<Search for a sequence of notes and all of its transpositions (with rhythmic values)>"],
#             ["SEAR: Pattern search (only rhythm)", patternSearch_menuStructure_withRhythm_withoutPitch, "<Search for a specific rhythm>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
# # #### Untermenü Einzelwerk (zweite Ebene, Einstellungen)
#
# def submenu_individualPiece_settings_entries():
#     return {
#         "menu_displayed_text": [
#             "Submenu Individual Piece Settings Header",
#             "Please make a selection from the options below by entering the entry index number:",
#             ["Menu item", "<Explanation>"],
#             "Which menu item should be executed? (<No. of menu item>): "
#         ],
#         "menu_entries": [
#             ["ENVT: Environment file (path)", environmentFile_path, "<Outputs the path of the environment file (if available)>"],
#             ["ENVT: Show settings", show_environmentFile_settings, "<Display the settings in the environment file>"],
#             ["ENVT: Reconfigure settings", environmentFile_settings_reconfigure, "<Reconfiguration of the environment file>"],
#             ["LANG: Change config.LANGUAGE", change_LANGUAGE, "<Change the output language of the program>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }

def some_function():
    print("This is some function")

    input("<To continue, please press Enter>")


def another_submenu_func():
    print("This is another submenu")

    input("<To continue, please press Enter>")


def some_other_function():
    print("This is some other function")

    input("<To continue, please press Enter>")
