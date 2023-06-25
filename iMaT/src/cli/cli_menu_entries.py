# --------------------------------------
# # Menüeinträge
from src.analysis.analysis import analysis_advanced_calculate_activity_rate, \
    analysis_advanced_compare_pitches_and_pitch_classes_per_duration, analysis_ambitus, \
    analysis_number_of_intervals_per_type, analysis_number_of_intervals_per_type_with_direction, \
    analysis_number_of_notes, analysis_number_of_pitch_classes_per_metrical_position, \
    analysis_number_of_pitch_classes_per_offset, analysis_number_of_pitch_classes_per_tone_duration, \
    analysis_number_of_pitches_per_metrical_position, analysis_number_of_pitches_per_offset, \
    analysis_number_of_pitches_per_tone_duration, analysis_number_of_rests, analysis_number_of_rests_per_rest_duration, \
    analysis_number_of_sound_events_per_metrical_position, analysis_number_of_sound_events_per_pitch, \
    analysis_number_of_sound_events_per_pitch_class, analysis_number_of_sound_events_per_tone_duration
from src.conversion.conversion_file_type import convert_multiple_files_filetype
from src.pattern_search.pattern_search import pattern_search_only_rhythm, pattern_search_with_transposition_with_rhythm, \
    pattern_search_with_transposition_without_rhythm, \
    pattern_search_without_transposition_with_rhythm, pattern_search_without_transposition_without_rhythm
from src.routines.routines_analysis import generic_analysis_workflow_single
from src.routines.routines_configure_m21_environment import display_environment_file, set_user_preferences
from src.routines.routines_display import generic_display_workflow
from src.routines.routines_pattern_search import generic_analysis_pattern_search
from src.routines.routines_score_selection import score_selection
from src.tokenization.tokenization import corpus_tokenization
from src.tokenization.tokenization_calculate import corpus_tokenization_calculate_pitch_intervals
from src.tokenization.tokenization_clean_data import corpus_tokenization_refine_data_remove_prefixes
from src.tokenization.tokenization_refine_data import corpus_tokenization_refine_data_absolute_duration
from src.utils.utils import change_part_names, show_metadata, show_part_names
from src.visualizations.visualizations_general import play_midi_score, show_chord_connections, show_chord_scale_system, \
    show_figured_bass, show_key_analysis, show_musescore, show_pianoroll, show_voice_progression, show_volume_change


# ## Startmenü (erste Ebene)

def startmenu_entries():
    return {
        "menu_displayed_text": [
            "Start Menu Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"]
        ],
        "menu_entries": [
            ["PROG: Analysis of one sheet music file", mainmenu_individualPiece_entries, "<Analysis of a single piece of music>"],
            ["CONV: Conversion of multiple music files", convert_multiple_files_filetype, "<Conversion of multiple music file wihthin one folder>"],
            ["TOKE: Tokenisation of multiple music files", tokenization_menu, "<Tokenisation of multiple music file wihthin one folder>"],
            ["CONF: Update Software Paths and Preferences", set_user_preferences, "<Update or redefine paths to essential software and user preferences>"],
        ]
    }


# ### Tokenisation of a sheet music file

def tokenization_menu():
    return {
        "menu_displayed_text": [
            "Tokenization Menu Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["TOKN: Tokenize a folder of midi files", corpus_tokenization, "<Tokenize sheet music using the midiTok library>"],
            ["RFNE: Refine tokenization results", tokenization_submenu_refine_data, "<Prepare tokenization data (CSV) for further processing>"],
            ["CALC: Add columns by performing calculations", tokenization_submenu_calculations, "<Perform calculations on existing data and safe those in new columns>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
        ],
    }


def tokenization_submenu_refine_data():
    return {
        "menu_displayed_text": [
            "Tokenization Menu - Enhance Data",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "Explanation"],
        ],
        "menu_entries": [
            ["REFN: Refine data (remove string prefixes)", corpus_tokenization_refine_data_remove_prefixes, "<Remove redundant string prefices from entries>"],
            ["REFN: Refine data (Duration: a.b.c -> float)", corpus_tokenization_refine_data_absolute_duration, "<Convert the Duration value (a.b.c) to another equal representation (-> a + b/c [= float])>"],
            ["BACK: Return to the last menu", 'back', "<Return to the parent menu>"],
        ]
    }

def tokenization_submenu_calculations():
    return {
        "menu_displayed_text": [
            "Tokenization Menu - Enhance Data",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "Explanation"],
        ],
        "menu_entries": [
            ["CALC: Calculate intervals between pitch values", corpus_tokenization_calculate_pitch_intervals, "<Add new column 'Pitch PitchDifferenceToNextPitch'>"],
            ["BACK: Return to the last menu", 'back', "<Return to the parent menu>"],
        ]
    }


# ### Analysis of a single piece of music

# #### Hauptmenü Einzelwerk (zweite Ebene)

def mainmenu_individualPiece_entries():
    return {
        "menu_displayed_text": [
            "Main Menu: Manage Individual Piece",
            "Enter the index number of your chosen action:",
            "Input your choice (<Menu item number>): ",
            ["Menu Item", "<Explanation>"],
        ],
        "menu_entries": [
            ["FILE: Access Basic Functions", submenu_individualPiece_files_entries, "<Access basic functions such as file selection, display metadata, etc.>"],
            ["TOOL: Statistical Analysis Tools", submenu_individualPiece_statisticalAnalyses_entries, "<Choose from various statistical analysis tools>"],
            ["TOOL: Visualization Tools", submenu_individualPiece_visualizations_entries, "<Choose from different visualization tools>"],
            ["TOOL: Pattern Search Tools", submenu_individualPiece_patternSearch_entries, "<Choose from different tools for pattern search>"],
            ["BACK: Return to Previous Menu", 'back', "<Go back to the previous menu."],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, File)

def submenu_individualPiece_files_entries(selected_score=None):
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Files Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["FILE: Select Score", score_selection, "<Select a new music score file>"],
            ["META: Display Metadata", show_metadata, "<Display the metadata of the selected score>"],
            ["NAME: List Part Names", show_part_names, "<Show the names of individual parts or voices in the selected score>"],
            ["NAME: Rename Parts", change_part_names, "<Change the names of individual parts or voices in the selected score>"],
            ["BACK: Return to Previous Menu", 'back', "<Go back to the previous menu>"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, statistische Analysen, Seite 1)

def submenu_individualPiece_statisticalAnalyses_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Statistical Analyses Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["STAT: Ambitus", (generic_analysis_workflow_single, analysis_ambitus), "<Analyzes range of pitches>"],
            ["STAT: Number of Tones", (generic_analysis_workflow_single, analysis_number_of_notes), "<Attention: analyzes only monodic melody lines correctly>"],
            ["STAT: Number of Rests", (generic_analysis_workflow_single, analysis_number_of_rests), "<Counts total rests in piece>"],
            ["BARS: Rests per Duration", (generic_analysis_workflow_single, analysis_number_of_rests_per_rest_duration), "<Counts rests per specific duration>"],
            ["BARS: Interval Types Quantity", (generic_analysis_workflow_single, analysis_number_of_intervals_per_type), "<Attention: analyzes only intervals in monodic melody lines correctly>"],
            ["BARS: Interval Types Quantity (up/down)", (generic_analysis_workflow_single, analysis_number_of_intervals_per_type_with_direction), "<Attention: analyzes only intervals in monodic melody lines correctly>"],
            ["BARS: Sound Events per Pitch", (generic_analysis_workflow_single, analysis_number_of_sound_events_per_pitch), "<Counts sound events per specific pitch>"],
            ["BARS: Sound Events per Pitch Class", (generic_analysis_workflow_single, analysis_number_of_sound_events_per_pitch_class), "<Counts sound events per pitch class>"],
            ["BARS: Sound Events per Tone Duration", (generic_analysis_workflow_single, analysis_number_of_sound_events_per_tone_duration), "<Counts sound events per specific tone duration>"],
            ["BARS: Sound Events per Metrical Position", (generic_analysis_workflow_single, analysis_number_of_sound_events_per_metrical_position), "<Counts sound events per metrical position>"],
            ["MTRX: Pitches per Tone Duration", (generic_analysis_workflow_single, analysis_number_of_pitches_per_tone_duration), "<Analyzes pitch distribution across different tone durations>"],
            ["MTRX: Pitches per Metrical Position", (generic_analysis_workflow_single, analysis_number_of_pitches_per_metrical_position), "<Analyzes pitch distribution across metrical positions>"],
            ["MTRX: Pitches per Offset", (generic_analysis_workflow_single, analysis_number_of_pitches_per_offset), "<Analyzes pitch distribution across offsets>"],
            ["MTRX: Pitch Classes per Tone Duration", (generic_analysis_workflow_single, analysis_number_of_pitch_classes_per_tone_duration), "<Analyzes pitch class distribution across different tone durations>"],
            ["MTRX: Pitch Classes per Metrical Position", (generic_analysis_workflow_single, analysis_number_of_pitch_classes_per_metrical_position), "<Analyzes pitch class distribution across metrical positions>"],
            ["MTRX: Pitch Classes per Offset", (generic_analysis_workflow_single, analysis_number_of_pitch_classes_per_offset), "<Analyzes pitch class distribution across offsets>"],
            ["NEXT: Advanced Calculations", submenu_individualPiece_statistical_analysis_advanced_entries, "<Navigates to advanced calculations>"],
            ["BACK: Return to the Last Menu", 'back', "<Returns to the parent menu>"],
        ]
    }


# #### Untermenü Einzelwerk (dritte Ebene, Combinations)

def submenu_individualPiece_statistical_analysis_advanced_entries():
    return {
        "menu_displayed_text": [
            "Advanced Statistical Analyses Submenu",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["ADV: Activity Index", (generic_analysis_workflow_single, analysis_advanced_calculate_activity_rate), "<Calculates ratio of notes to rests [= Activity Index]>"],
            ["ADV: Pitches vs Pitch Classes/Dur.", (generic_analysis_workflow_single, analysis_advanced_compare_pitches_and_pitch_classes_per_duration), "<Compares pitch & pitch class counts per duration, including pitch to pitch class ratio>"],
            ["BACK: Return to Last Menu", 'back', "<Returns to previous menu>"],
        ]
    }

def submenu_individualPiece_visualizations_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Visualizations Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["PLAY: MIDI Playback", (generic_display_workflow, play_midi_score), "Play the selected score in MIDI format"],
            ["SHOW: Sheet Music in MuseScore", (generic_display_workflow, show_musescore), "Display the sheet music of the selected score in MuseScore"],
            ["SHOW: Chord Connections", (generic_display_workflow, show_chord_connections), "Display the chord connections of the selected score"],
            ["SHOW: Figured Bass", (generic_display_workflow, show_figured_bass), "Display the figured bass notation of the selected score"],
            ["SHOW: Chord-Scale System", (generic_display_workflow, show_chord_scale_system), "Display the chord-scale system of the selected score"],
            ["SHOW: Pianoroll View", (generic_display_workflow, show_pianoroll), "Display the pianoroll view of the selected score"],
            ["SHOW: Voice Progression (Line Plot)", (generic_display_workflow, show_voice_progression), "Display the voice progression of the selected score (Note: Only works with consistently monodic parts)"],
            ["SHOW: Volume Change Over Time", (generic_display_workflow, show_volume_change), "Display the change in volume over time for the selected score"],
            ["SHOW: Key Analysis", (generic_display_workflow, show_key_analysis), "Display the key analysis of the selected score in a color grid format"],
            ["BACK: Return to Previous Menu", 'back', "Return to the previous menu"],
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, Mustersuche)

def submenu_individualPiece_patternSearch_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Pattern Search",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["SEARCH: Pitch sequence", (generic_analysis_pattern_search, pattern_search_without_transposition_without_rhythm), "<Search for a sequence of pitches, ignoring rhythm>"],
            ["SEARCH: Pitch + transp.", (generic_analysis_pattern_search, pattern_search_with_transposition_without_rhythm), "<Search for a pitch sequence and its transpositions, ignoring rhythm>"],
            ["SEARCH: Pitch + rhythm", (generic_analysis_pattern_search, pattern_search_without_transposition_with_rhythm), "<Search for a sequence of pitches with rhythm>"],
            ["SEARCH: Pitch + rhythm + transp.", (generic_analysis_pattern_search, pattern_search_with_transposition_with_rhythm), "<Search for a pitch sequence with rhythm and its transpositions>"],
            ["SEARCH: Rhythm only", (generic_analysis_pattern_search, pattern_search_only_rhythm), "<Search for a rhythm pattern only>"],
            ["BACK: Return", 'back', "<Returns to the previous menu>"]
        ]
    }

# #### Untermenü Einzelwerk (dritte Ebene, Einstellungen)

def submenu_individualPiece_settings_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Settings",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["ENVT: Display Environment File", display_environment_file, "<Display the content of the current music21 environment file>"],
            ["CONF: Update Paths & Preferences", set_user_preferences, "<Update or redefine the paths to essential software and set user preferences>"],
            ["BACK: Return to Previous Menu", 'back', "<Return to the parent menu without making any changes>"],
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
#             ["TOOL: Menu selection (visualisation)", submenu_individualPiece_statistical_analysis_advanced_entries, "<Selection of different visualisation tools>"],
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
# def submenu_individualPiece_statistical_analysis_advanced_entries():
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


