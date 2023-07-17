"""
constants.py
============

This Python script contains a set of constants to be used in the Interactive Music Analysis Tool (I-MaT) application.

The constants defined in this module include a list of musical keys, a list of musical notes, a list of rhythmic values,
a dictionary mapping integers to pitch class names, a dictionary of example scores, and a title text for the
application.

The musical keys and notes are represented in two formats: full name and abbreviation. The rhythmic values are
represented as a float or a string (in case of triplets). The pitch class integers map to pitch class names according
to music theory.

The example scores dictionary contains information about example scores, including the title, URL, and subcorpus. The
title text for the application includes the name and version of the application, associated project and institution,
license information, and copyright statement.
"""

# CONSTANTS:

"""
TITLE_TEXT is a string that contains the title text for the application. It includes the name and version of the 
application, the associated project and institution, the license information, and the copyright statement. This text 
is used to display a title or header in the application's user interface.
"""

TITLE_TEXT = (
    '\nI-MaT - Interactive Music Analysis Tool, v3.0, (2023). Project: "Computer-Assisted Music Analysis"\n\n'
    'Department of Musicology Weimar-Jena, University of Music Franz Liszt Weimar, Germany\n\n'
    'MIT License, Copyright (c) 2023 S.O. Eck.\n\n'
    '----------------------------------------------------------------------\n'
)

"""
KEYS_LIST is a list of musical keys in the format ["Key-Name", "Abbreviation"]. It includes major and minor keys in
different pitches. This list is used to represent and validate keys that are input or output by the system. The
"Abbreviation" part of each list item is used for displaying or inputting keys in a compact way.
"""

KEYS_LIST = [
    ["C-Major", "C"],
    ["G-Major", "G"],
    ["D-Major", "D"],
    ["A-Major", "A"],
    ["E-Major", "E"],
    ["B-Major", "B"],
    ["F-sharp-Major", "F#"],
    ["C-sharp-Major", "C#"],
    ["G-sharp-Major", "G#"],
    ["D-sharp-Major", "D#"],
    ["A-sharp-Major", "A#"],
    ["E-sharp-Major", "E#"],
    ["B-sharp-Major", "B#"],
    ["F-Major", "F"],
    ["B-flat-Major", "B-"],
    ["E-flat-Major", "E-"],
    ["A-flat-Major", "A-"],
    ["D-flat-Major", "D-"],
    ["G-flat-Major", "G-"],
    ["C-flat-Major", "C-"],
    ["F-flat-Major", "F-"],
    ["C-Minor", "c"],
    ["G-Minor", "g"],
    ["D-Minor", "d"],
    ["A-Minor", "a"],
    ["E-Minor", "e"],
    ["B-Minor", "b"],
    ["F-sharp-Minor", "f#"],
    ["C-sharp-Minor", "c#"],
    ["G-sharp-Minor", "g#"],
    ["D-sharp-Minor", "d#"],
    ["A-sharp-Minor", "a#"],
    ["E-sharp-Minor", "e#"],
    ["H-sharp-Minor", "b#"],
    ["F-Minor", "f"],
    ["B-flat-Minor", "b-"],
    ["E-flat-Minor", "e-"],
    ["A-flat-Minor", "a-"],
    ["D-flat-Minor", "d-"],
    ["G-flat-Minor", "g-"],
    ["C-flat-Minor", "c-"],
    ["F-flat-Minor", "f-"],
]

"""
NOTES_LIST is a list of musical notes in the format ["Note-Name", "Abbreviation"]. It covers a variety of notes 
including flat ("-") and sharp ("#") versions. The last two entries in the list provide options to remove the last 
note entered or finish input. 
"""

NOTES_LIST = [
    ["‾‾‾‾  -   C-flat", "C-"],
    ["C         C", "C"],
    ["____  ♯   C-sharp", "C#"],
    ["‾‾‾‾  -   D-flat", "D-"],
    ["D         D", "D"],
    ["____  ♯   D-sharp", "D#"],
    ["‾‾‾‾  -   E-flat", "E-"],
    ["E         E", "E"],
    ["____  ♯   E-sharp", "E#"],
    ["‾‾‾‾  -   F-flat", "F-"],
    ["F         F", "F"],
    ["____  ♯   F-sharp", "F#"],
    ["‾‾‾‾  -   G-flat", "G-"],
    ["G         G", "G"],
    ["____  ♯   G-sharp", "G#"],
    ["‾‾‾‾  -   A-flat", "A-"],
    ["A         A", "A"],
    ["____  ♯   A-sharp", "A#"],
    ["‾‾‾‾  -   B-flat", "B-"],
    ["B         B", "B"],
    ["____  ♯   B-sharp", "B#"],
    ["BACK: Remove the last note entered", "remove"],
    ["DONE: Finish input", "complete"],
]

"""
RHYTHMIC_VALUES_LIST represents rhythmic values of musical notes. Each entry contains a display string and the 
corresponding rhythmic value. The rhythmic value is represented either as a float or as a string, in case of triplets. 
The list entries cover note values from thirty-second notes to double whole notes, including dotted and triplet versions.
"""

RHYTHMIC_VALUES_LIST = [
    ["[0.125]   Thirty-second note", 0.125],
    ["[0.25]    Sixteenth note", 0.25],
    ["[0.375]   Sixteenth note (dotted)", 0.375],
    ["[1/3]     Eighth note triplet", "1/3"],
    ["[0.5]     Eighth note", 0.5],
    ["[0.75]    Eighth note (dotted)", 0.75],
    ["[2/3]     Quarter note triplet", "2/3"],
    ["[1.0]     Quarter note", 1.0],
    ["[1.5]     Quarter note (dotted)", 1.5],
    ["[4/3]     Half note triplet", "4/3"],
    ["[2.0]     Half note", 2.0],
    ["[3.0]     Half note (dotted)", 3.0],
    ["[8/3]     Whole note triplet", "8/3"],
    ["[4.0]     Whole note", 4.0],
    ["[6.0]     Whole note (dotted)", 6.0],
    ["[16/3]    Double whole triplet", "16/3"],
    ["[8.0]     Double whole note", 8.0],
    ["[12.0]    Double whole note (dotted)", 12.0],
    ["BACK:     Remove the last note entered", "remove"],
    ["DONE:     Finish input", "complete"]
]

"""
PITCH_CLASS_NAMES is a dictionary that maps integers to pitch class names. In music theory, pitch classes are the set 
of all pitches that are integer multiples of the octave. This constant is useful for converting pitch class integers 
into human-readable names.
"""

PITCH_CLASS_NAMES = {
    0: "C",
    1: "C#/Db",
    2: "D",
    3: "D#/Eb",
    4: "E",
    5: "F",
    6: "F#/Gb",
    7: "G",
    8: "G#/Ab",
    9: "A",
    10: "A#/Bb",
    11: "B"
}

"""
EXAMPLE_SCORES_DICT is a dictionary containing data about example scores. Each entry includes the title of the score, 
the URL where the score can be found, and the subcorpus the score belongs to. This dictionary is used to provide users 
with a selection of example scores for analysis.
"""

EXAMPLE_SCORES_DICT = \
    {
        "example_score_1": [
            "Example score 1: Dufay, Guillaume (1397-1474): Missa L'homme arme - Kyrie",
            "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_1-5_MissaLhomm_002_00956.xml",
            "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
        "example_score_2": [
            "Example score 2: Dufay, Guillaume (1397-1474): Missa L'homme arme - Gloria",
            "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_2-5_MissaLhomm_002_00957.xml",
            "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
        "example_score_3": [
            "Example score 3: Dufay, Guillaume (1397-1474): Missa L'homme arme - Credo",
            "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_3-5_MissaLhomm_002_00958.xml",
            "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
        "example_score_4": [
            "Example score 4: Dufay, Guillaume (1397-1474): Missa L'homme arme - Sanctus",
            "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_3-5_MissaLhomm_002_00958.xml",
            "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
        "example_score_5": [
            "Example score 5: Dufay, Guillaume (1397-1474): Missa L'homme arme - Agnus Dei",
            "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_3-5_MissaLhomm_002_00958.xml",
            "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"]
    }