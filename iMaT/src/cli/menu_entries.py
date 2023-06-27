from src.analysis.functions import analysis_advanced_calculate_activity_rate, \
    analysis_advanced_compare_pitches_and_pitch_classes_per_duration, analysis_ambitus, \
    analysis_number_of_intervals_per_type, analysis_number_of_intervals_per_type_with_direction, \
    analysis_number_of_notes, analysis_number_of_pitch_classes_per_metrical_position, \
    analysis_number_of_pitch_classes_per_offset, analysis_number_of_pitch_classes_per_tone_duration, \
    analysis_number_of_pitches_per_metrical_position, analysis_number_of_pitches_per_offset, \
    analysis_number_of_pitches_per_tone_duration, analysis_number_of_rests, analysis_number_of_rests_per_rest_duration, \
    analysis_number_of_sound_events_per_metrical_position, analysis_number_of_sound_events_per_pitch, \
    analysis_number_of_sound_events_per_pitch_class, analysis_number_of_sound_events_per_tone_duration
from src.analysis.main import analysis_workflow_single_piece
from src.conversion.main import convert_multiple_files_filetype
from src.m21_environment.main import display_environment_file, set_user_preferences
from src.pattern_search.functions import pattern_search_only_rhythm, \
    pattern_search_with_transposition_with_rhythm, \
    pattern_search_with_transposition_without_rhythm, \
    pattern_search_without_transposition_with_rhythm, pattern_search_without_transposition_without_rhythm
from src.pattern_search.main import pattern_search_workflow_single_piece
from src.routines.routines_display import generic_display_workflow
from src.score_selection.main import score_selection
from src.tokenization.main import corpus_tokenization
from src.tokenization.tokenization_refine_results.tokenization_absolute_duration import \
    corpus_tokenization_refine_data_absolute_duration
from src.tokenization.tokenization_refine_results.tokenization_calculate_pitch_intervals import \
    tokenization_calculate_pitch_intervals
from src.tokenization.tokenization_refine_results.tokenization_remove_prefixes import \
    corpus_tokenization_remove_prefixes
from src.tokenization.tokenization_refine_results.tokenization_tokens_to_txt import export_csv_columns_to_txt_file
from src.utils.various import change_part_names, show_metadata, show_part_names
from src.visualizations.m21_integrated import play_midi_score, show_chord_connections, show_chord_scale_system, \
    show_figured_bass, show_key_analysis, show_musescore, show_pianoroll, show_voice_progression, show_volume_change


def start_menu_entries():
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
            ["TOKE: Tokenisation of multiple music files", tokenization_mainmenu_entries, "<Tokenisation of multiple music file wihthin one folder>"],
            ["CONF: Update Software Paths and Preferences", submenu_individualPiece_settings_entries, "<Update or redefine paths to essential software and user preferences>"],
        ]
    }


def tokenization_mainmenu_entries():
    return {
        "menu_displayed_text": [
            "Tokenization Menu Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["TOKN: Tokenize a folder of midi files", corpus_tokenization, "<Tokenize sheet music using the midiTok library>"],
            ["RFNE: Refine tokenization results", tokenization_submenu_entries_refine_data, "<Prepare tokenization data (CSV) for further processing>"],
            ["CALC: Add columns by performing calculations", tokenization_submenu_entries_calculations, "<Perform calculations on existing data and safe those in new columns>"],
            ["EXTR: Extract Columns to TXT", export_csv_columns_to_txt_file, "<Extract specified columns from the dataset and save to a TXT file>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
        ],
    }


def tokenization_submenu_entries_refine_data():
    return {
        "menu_displayed_text": [
            "Tokenization Menu - Refine Data",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "Explanation"],
        ],
        "menu_entries": [
            ["REFN: Refine data (remove string prefixes)", corpus_tokenization_remove_prefixes, "<Remove redundant string prefices from entries>"],
            ["REFN: Refine data (Duration: a.b.c -> float)", corpus_tokenization_refine_data_absolute_duration, "<Convert the Duration value (a.b.c) to another equal representation (-> a + b/c [= float])>"],
            ["BACK: Return to the last menu", 'back', "<Return to the parent menu>"],
        ]
    }


def tokenization_submenu_entries_calculations():
    return {
        "menu_displayed_text": [
            "Tokenization Menu - Enhance Data",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "Explanation"],
        ],
        "menu_entries": [
            ["CALC: Calculate intervals between pitch values", tokenization_calculate_pitch_intervals, "<Add new column 'Pitch PitchDifferenceToNextPitch'>"],
            ["BACK: Return to the last menu", 'back', "<Return to the parent menu>"],
        ]
    }


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


def submenu_individualPiece_files_entries():
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


def submenu_individualPiece_statisticalAnalyses_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Statistical Analyses Header",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["STAT: Ambitus", (analysis_workflow_single_piece, analysis_ambitus), "<Analyzes range of pitches>"],
            ["STAT: Number of Tones", (analysis_workflow_single_piece, analysis_number_of_notes), "<Attention: analyzes only monodic melody lines correctly>"],
            ["STAT: Number of Rests", (analysis_workflow_single_piece, analysis_number_of_rests), "<Counts total rests in piece>"],
            ["BARS: Rests per Duration", (analysis_workflow_single_piece, analysis_number_of_rests_per_rest_duration), "<Counts rests per specific duration>"],
            ["BARS: Interval Types Quantity", (analysis_workflow_single_piece, analysis_number_of_intervals_per_type), "<Attention: analyzes only intervals in monodic melody lines correctly>"],
            ["BARS: Interval Types Quantity (up/down)", (analysis_workflow_single_piece, analysis_number_of_intervals_per_type_with_direction), "<Attention: analyzes only intervals in monodic melody lines correctly>"],
            ["BARS: Sound Events per Pitch", (analysis_workflow_single_piece, analysis_number_of_sound_events_per_pitch), "<Counts sound events per specific pitch>"],
            ["BARS: Sound Events per Pitch Class", (analysis_workflow_single_piece, analysis_number_of_sound_events_per_pitch_class), "<Counts sound events per pitch class>"],
            ["BARS: Sound Events per Tone Duration", (analysis_workflow_single_piece, analysis_number_of_sound_events_per_tone_duration), "<Counts sound events per specific tone duration>"],
            ["BARS: Sound Events per Metrical Position", (analysis_workflow_single_piece, analysis_number_of_sound_events_per_metrical_position), "<Counts sound events per metrical position>"],
            ["MTRX: Pitches per Tone Duration", (analysis_workflow_single_piece, analysis_number_of_pitches_per_tone_duration), "<Analyzes pitch distribution across different tone durations>"],
            ["MTRX: Pitches per Metrical Position", (analysis_workflow_single_piece, analysis_number_of_pitches_per_metrical_position), "<Analyzes pitch distribution across metrical positions>"],
            ["MTRX: Pitches per Offset", (analysis_workflow_single_piece, analysis_number_of_pitches_per_offset), "<Analyzes pitch distribution across offsets>"],
            ["MTRX: Pitch Classes per Tone Duration", (analysis_workflow_single_piece, analysis_number_of_pitch_classes_per_tone_duration), "<Analyzes pitch class distribution across different tone durations>"],
            ["MTRX: Pitch Classes per Metrical Position", (analysis_workflow_single_piece, analysis_number_of_pitch_classes_per_metrical_position), "<Analyzes pitch class distribution across metrical positions>"],
            ["MTRX: Pitch Classes per Offset", (analysis_workflow_single_piece, analysis_number_of_pitch_classes_per_offset), "<Analyzes pitch class distribution across offsets>"],
            ["NEXT: Advanced Calculations", submenu_individualPiece_statistical_analysis_advanced_entries, "<Navigates to advanced calculations>"],
            ["BACK: Return to the Last Menu", 'back', "<Returns to the parent menu>"],
        ]
    }


def submenu_individualPiece_statistical_analysis_advanced_entries():
    return {
        "menu_displayed_text": [
            "Advanced Statistical Analyses Submenu",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["ADV: Activity Index", (analysis_workflow_single_piece, analysis_advanced_calculate_activity_rate), "<Calculates ratio of notes to rests [= Activity Index]>"],
            ["ADV: Pitches vs Pitch Classes/Dur.", (analysis_workflow_single_piece, analysis_advanced_compare_pitches_and_pitch_classes_per_duration), "<Compares pitch & pitch class counts per duration, including pitch to pitch class ratio>"],
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


def submenu_individualPiece_patternSearch_entries():
    return {
        "menu_displayed_text": [
            "Submenu Individual Piece Pattern Search",
            "Please make a selection from the options below by entering the entry index number:",
            "Which menu item should be executed? (<No. of menu item>): ",
            ["Menu item", "<Explanation>"],
        ],
        "menu_entries": [
            ["SEARCH: Pitch sequence", (pattern_search_workflow_single_piece, pattern_search_without_transposition_without_rhythm), "<Search for a sequence of pitches, ignoring rhythm>"],
            ["SEARCH: Pitch + transp.", (pattern_search_workflow_single_piece, pattern_search_with_transposition_without_rhythm), "<Search for a pitch sequence and its transpositions, ignoring rhythm>"],
            ["SEARCH: Pitch + rhythm", (pattern_search_workflow_single_piece, pattern_search_without_transposition_with_rhythm), "<Search for a sequence of pitches with rhythm>"],
            ["SEARCH: Pitch + rhythm + transp.", (pattern_search_workflow_single_piece, pattern_search_with_transposition_with_rhythm), "<Search for a pitch sequence with rhythm and its transpositions>"],
            ["SEARCH: Rhythm only", (pattern_search_workflow_single_piece, pattern_search_only_rhythm), "<Search for a rhythm pattern only>"],
            ["BACK: Return", 'back', "<Returns to the previous menu>"]
        ]
    }


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