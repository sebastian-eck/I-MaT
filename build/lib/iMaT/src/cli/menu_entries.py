"""
cli.menu_entries.py
===================

This module provides functionalities to construct the entries for various menus used within the command-line interface (CLI) of the Interactive Music Analysis Tool (I-MaT).

This module is responsible for constructing the menu entries for different sections of the command line interface (CLI)
of the Interactive Music Analysis Tool (I-MaT). The menus are used to navigate through the CLI, and the functions
in this module return the entries for each menu in a structured format.

Functions
---------
- `mainmenu_environment_settings_entries`: Returns the menu entries for the main environment settings menu.
- `mainmenu_single_musical_piece_entries`: Returns the menu entries for the single musical piece menu.
- `mainmenu_tokenization_entries`: Returns the menu entries for the tokenization menu.
- `start_menu_entries`: Returns the menu entries for the start menu.
- `submenu_single_musical_piece_basic_functions_entries`: Returns the menu entries for the basic functions submenu.
- `submenu_single_musical_piece_pattern_search_entries`: Returns the menu entries for the pattern search submenu.
- `submenu_single_musical_piece_statistical_analysis_page1_entries`: Returns the menu entries for the first page of the statistical analysis submenu.
- `submenu_single_musical_piece_statistical_analysis_page2_entries`: Returns the menu entries for the second page of the statistical analysis submenu.
- `submenu_single_musical_piece_visualizations_entries`: Returns the menu entries for the visualizations submenu.
- `submenu_tokenization_calculations_entries`: Returns the menu entries for the calculations submenu in tokenization.
- `submenu_tokenization_refine_data_entries`: Returns the menu entries for the refine data submenu in tokenization.

Each function returns a dictionary representing the menu entries for a specific menu. The dictionary includes the
menu text to be displayed, the function to be executed when the menu entry is selected, and other relevant information.

These functions allow for easy modification of the menu structure and contents, providing flexibility in the design
and functionality of the CLI. The module aids in ensuring that the command-line interface remains user-friendly
and intuitive, providing clear navigation and straightforward access to the tool's functionalities.
"""
from iMaT.src.analysis.functions import analysis_advanced_calculate_activity_rate, \
    analysis_advanced_compare_pitches_and_pitch_classes_per_duration, analysis_ambitus, \
    analysis_number_of_intervals_per_type, analysis_number_of_intervals_per_type_with_direction, \
    analysis_number_of_notes, analysis_number_of_pitch_classes_per_metrical_position, \
    analysis_number_of_pitch_classes_per_offset, analysis_number_of_pitch_classes_per_tone_duration, \
    analysis_number_of_pitches_per_metrical_position, analysis_number_of_pitches_per_offset, \
    analysis_number_of_pitches_per_tone_duration, analysis_number_of_rests, analysis_number_of_rests_per_rest_duration, \
    analysis_number_of_sound_events_per_metrical_position, analysis_number_of_sound_events_per_pitch, \
    analysis_number_of_sound_events_per_pitch_class, analysis_number_of_sound_events_per_tone_duration
from iMaT.src.analysis.main import analysis_workflow_single_musical_piece
from iMaT.src.conversion.main import convert_multiple_files_filetype
from iMaT.src.m21_environment.main import display_environment_file, set_user_preferences
from iMaT.src.pattern_search.functions import pattern_search_only_rhythm, \
    pattern_search_with_transposition_with_rhythm, \
    pattern_search_with_transposition_without_rhythm, \
    pattern_search_without_transposition_with_rhythm, pattern_search_without_transposition_without_rhythm
from iMaT.src.pattern_search.main import pattern_search_workflow_single_musical_piece
from iMaT.src.visualizations.main import generic_display_workflow
from iMaT.src.score_selection.main import score_selection
from iMaT.src.tokenization.main import tokenization_tokenize_folder_midi_files
from iMaT.src.tokenization.refine_results.absolute_duration import \
    corpus_tokenization_refine_data_absolute_duration
from iMaT.src.tokenization.refine_results.calculate_pitch_intervals import \
    tokenization_calculate_pitch_intervals
from iMaT.src.tokenization.refine_results.remove_prefixes import \
    corpus_tokenization_refine_data_remove_prefixes
from iMaT.src.tokenization.refine_results.tokens_to_txt import tokenization_export_csv_columns_to_txt_file
from iMaT.src.utils.misc import change_part_names, show_metadata, show_part_names
from iMaT.src.visualizations.m21_integrated import play_midi_score, show_chord_connections, show_chord_scale_system, \
    show_figured_bass, show_key_analysis, show_musescore, show_pianoroll, show_voice_progression, show_volume_change


def start_menu_entries():
    """
    Entry point for the program, allowing navigation through various functionalities.

    Level: Root

    This function defines the top level menu of the application.
    It provides options to either analyze a single sheet music file,
    convert multiple music files, tokenize multiple music files, or
    update the software paths and preferences.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["PROG: Analysis of one sheet music file", mainmenu_single_musical_piece_entries, "<Analysis of a single piece of music>"],
            ["CONV: Conversion of multiple music files", convert_multiple_files_filetype, "<Conversion of multiple music file wihthin one folder>"],
            ["TOKE: Tokenisation of multiple music files", mainmenu_tokenization_entries, "<Tokenisation of multiple music file wihthin one folder>"],
            ["CONF: Update Software Paths and Preferences", mainmenu_environment_settings_entries, "<Update or redefine paths to essential software and user preferences>"],
        ]
    }


def mainmenu_single_musical_piece_entries():
    """
    Menu dedicated to operations and analyses related to a single piece of music.

    Level: First Child (Parent: start_menu_entries)

    This function defines the second level menu that is specific to
    analyzing a single piece of music. It provides options to access
    basic functions, statistical analysis tools, visualization tools,
    and pattern search tools.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Individual Piece",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["FILE: Access Basic Functions", submenu_single_musical_piece_basic_functions_entries, "<Access basic functions such as file selection, display metadata, etc.>"],
            ["TOOL: Statistical Analysis Tools", submenu_single_musical_piece_statistical_analysis_page1_entries, "<Choose from various statistical analysis tools>"],
            ["TOOL: Visualization Tools", submenu_single_musical_piece_visualizations_entries, "<Choose from different visualization tools>"],
            ["TOOL: Pattern Search Tools", submenu_single_musical_piece_pattern_search_entries, "<Choose from different tools for pattern search>"],
            ["BACK: Return to Previous Menu", 'back', "<Go back to the previous menu."],
        ]
    }


def submenu_single_musical_piece_basic_functions_entries():
    """
    Submenu offering basic operations such as score selection and metadata display.

    Level: Second Child (Parent: mainmenu_single_musical_piece_entries)

    This function defines the third level menu for accessing basic
    functions of the program. It provides options such as selecting a
    music score, displaying metadata, listing part names, and renaming
    parts.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Individual Piece >> Access Basic Functions",
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


def submenu_single_musical_piece_statistical_analysis_page1_entries():
    """
    Submenu offering various statistical analyses for a single piece of music.

    Level: Second Child (Parent: mainmenu_single_musical_piece_entries)

    This function defines the third level menu for performing
    statistical analysis on a single piece of music. It provides
    options for analyzing different aspects of the piece, such as the
    number of tones, number of rests, etc.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Individual Piece >> Statistical Analysis Tools (Page 1)",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["STAT: Ambitus", (analysis_workflow_single_musical_piece, analysis_ambitus), "<Analyzes range of pitches>"],
            ["STAT: Number of Tones", (analysis_workflow_single_musical_piece, analysis_number_of_notes), "<Attention: analyzes only monodic melody lines correctly>"],
            ["STAT: Number of Rests", (analysis_workflow_single_musical_piece, analysis_number_of_rests), "<Counts total rests in piece>"],
            ["BARS: Rests per Duration", (analysis_workflow_single_musical_piece, analysis_number_of_rests_per_rest_duration), "<Counts rests per specific duration>"],
            ["BARS: Interval Types Quantity", (analysis_workflow_single_musical_piece, analysis_number_of_intervals_per_type), "<Attention: analyzes only intervals in monodic melody lines correctly>"],
            ["BARS: Interval Types Quantity (up/down)", (analysis_workflow_single_musical_piece, analysis_number_of_intervals_per_type_with_direction), "<Attention: analyzes only intervals in monodic melody lines correctly>"],
            ["BARS: Sound Events per Pitch", (analysis_workflow_single_musical_piece, analysis_number_of_sound_events_per_pitch), "<Counts sound events per specific pitch>"],
            ["BARS: Sound Events per Pitch Class", (analysis_workflow_single_musical_piece, analysis_number_of_sound_events_per_pitch_class), "<Counts sound events per pitch class>"],
            ["BARS: Sound Events per Tone Duration", (analysis_workflow_single_musical_piece, analysis_number_of_sound_events_per_tone_duration), "<Counts sound events per specific tone duration>"],
            ["BARS: Sound Events per Metrical Position", (analysis_workflow_single_musical_piece, analysis_number_of_sound_events_per_metrical_position), "<Counts sound events per metrical position>"],
            ["MTRX: Pitches per Tone Duration", (analysis_workflow_single_musical_piece, analysis_number_of_pitches_per_tone_duration), "<Analyzes pitch distribution across different tone durations>"],
            ["MTRX: Pitches per Metrical Position", (analysis_workflow_single_musical_piece, analysis_number_of_pitches_per_metrical_position), "<Analyzes pitch distribution across metrical positions>"],
            ["MTRX: Pitches per Offset", (analysis_workflow_single_musical_piece, analysis_number_of_pitches_per_offset), "<Analyzes pitch distribution across offsets>"],
            ["MTRX: Pitch Classes per Tone Duration", (analysis_workflow_single_musical_piece, analysis_number_of_pitch_classes_per_tone_duration), "<Analyzes pitch class distribution across different tone durations>"],
            ["MTRX: Pitch Classes per Metrical Position", (analysis_workflow_single_musical_piece, analysis_number_of_pitch_classes_per_metrical_position), "<Analyzes pitch class distribution across metrical positions>"],
            ["MTRX: Pitch Classes per Offset", (analysis_workflow_single_musical_piece, analysis_number_of_pitch_classes_per_offset), "<Analyzes pitch class distribution across offsets>"],
            ["NEXT: Advanced Calculations", submenu_single_musical_piece_statistical_analysis_page2_entries, "<Navigates to advanced calculations>"],
            ["BACK: Return to the Last Menu", 'back', "<Returns to the parent menu>"],
        ]
    }


def submenu_single_musical_piece_statistical_analysis_page2_entries():
    """
    Submenu dedicated to advanced statistical analyses for a single piece of music.

    Level: Third Child (Parent: submenu_single_musical_piece_statistical_analysis_page1_entries)

    This function defines the fourth level menu for performing
    advanced statistical calculations on a single piece of music.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Individual Piece >> Statistical Analysis Tools (Page 2)",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["ADV: Activity Index", (analysis_workflow_single_musical_piece, analysis_advanced_calculate_activity_rate), "<Calculates ratio of notes to rests [= Activity Index]>"],
            ["ADV: Pitches vs Pitch Classes/Dur.", (analysis_workflow_single_musical_piece, analysis_advanced_compare_pitches_and_pitch_classes_per_duration), "<Compares pitch & pitch class counts per duration, including pitch to pitch class ratio>"],
            ["BACK: Return to Last Menu", 'back', "<Returns to previous menu>"],
        ]
    }


def submenu_single_musical_piece_visualizations_entries():
    """
    Submenu offering various visualization tools for a single piece of music.

    Level: Second Child (Parent: mainmenu_single_musical_piece_entries)

    This function defines the third level menu for visualizing various
    aspects of a single piece of music.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Individual Piece >> Visualization Tools",
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


def submenu_single_musical_piece_pattern_search_entries():
    """
    Submenu for various pattern search tools in a single piece of music.

    Level: Second Child (Parent: mainmenu_single_musical_piece_entries)

    This function defines the third level menu for performing pattern
    searches on a single piece of music.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Individual Piece >> Pattern Search Tools",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["SEARCH: Pitch sequence", (pattern_search_workflow_single_musical_piece, pattern_search_without_transposition_without_rhythm), "<Search for a sequence of pitches, ignoring rhythm>"],
            ["SEARCH: Pitch + transp.", (pattern_search_workflow_single_musical_piece, pattern_search_with_transposition_without_rhythm), "<Search for a pitch sequence and its transpositions, ignoring rhythm>"],
            ["SEARCH: Pitch + rhythm", (pattern_search_workflow_single_musical_piece, pattern_search_without_transposition_with_rhythm), "<Search for a sequence of pitches with rhythm>"],
            ["SEARCH: Pitch + rhythm + transp.", (pattern_search_workflow_single_musical_piece, pattern_search_with_transposition_with_rhythm), "<Search for a pitch sequence with rhythm and its transpositions>"],
            ["SEARCH: Rhythm only", (pattern_search_workflow_single_musical_piece, pattern_search_only_rhythm), "<Search for a rhythm pattern only>"],
            ["BACK: Return", 'back', "<Returns to the previous menu>"]
        ]
    }


def mainmenu_tokenization_entries():
    """
    Main menu for operations related to music tokenization.

    Level: First Child (Parent: start_menu_entries)

    This function defines the second level menu for tokenization
    operations. It provides options to tokenize a folder of midi files,
    refine tokenization results, perform calculations on tokens, and
    extract token data to a TXT file.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Tokenization",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["TOKN: Tokenize a folder of midi files", tokenization_tokenize_folder_midi_files, "<Tokenize sheet music using the midiTok library>"],
            ["RFNE: Refine tokenization results", submenu_tokenization_refine_data_entries, "<Prepare tokenization data (CSV) for further processing>"],
            ["CALC: Add columns by performing calculations", submenu_tokenization_calculations_entries, "<Perform calculations on existing data and safe those in new columns>"],
            ["EXTR: Extract Columns to TXT", tokenization_export_csv_columns_to_txt_file, "<Extract specified columns from the dataset and save to a TXT file>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
        ],
    }


def submenu_tokenization_refine_data_entries():
    """
    Submenu for refining tokenized data.

    Level: Second Child (Parent: mainmenu_tokenization_entries)

    This function defines the third level menu for refining
    tokenization results. It provides options to remove string prefixes
    and convert duration values to a different format.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Tokenization >> Refine Data",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["REFN: Refine data (remove string prefixes)", corpus_tokenization_refine_data_remove_prefixes, "<Remove redundant string prefices from entries>"],
            ["REFN: Refine data (Duration: a.b.c -> float)", corpus_tokenization_refine_data_absolute_duration, "<Convert the Duration value (a.b.c) to another equal representation (-> a + b/c [= float])>"],
            ["BACK: Return to the last menu", 'back', "<Return to the parent menu>"],
        ]
    }


def submenu_tokenization_calculations_entries():
    """
    Submenu for conducting various calculations on tokenized data.

    Level: Second Child (Parent: mainmenu_tokenization_entries)

    This function defines the third level menu for performing
    calculations on tokens. It provides an option to calculate intervals
    between pitch values.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Tokenization >> Calculate on Tokens",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["CALC: Calculate intervals between pitch values", tokenization_calculate_pitch_intervals, "<Add new column 'Pitch PitchDifferenceToNextPitch'>"],
            ["BACK: Return to the last menu", 'back', "<Return to the parent menu>"],
        ]
    }


def mainmenu_environment_settings_entries():
    """
    Menu for managing software paths and user preferences.

    Level: First Child (Parent: start_menu_entries)

    This function defines the second level menu for updating software
    paths and preferences. It provides options to display the
    environment file and to update paths and preferences.
    """
    return {
        "menu_displayed_text": [
            "LOCATION: Start Menu >> Main Menu: Update Software Paths and Preferences",
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