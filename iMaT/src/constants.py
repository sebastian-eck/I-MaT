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

TITLE_TEXT = (
    '\nI-MaT - Interactive Music Analysis Tool, v3.0, (2023). Project: "Computer-Assisted Music Analysis"\n\n'
    'Department of Musicology Weimar-Jena, University of Music Franz Liszt Weimar, Germany\n\n'
    'MIT License, Copyright (c) 2023 S.O. Eck.\n\n'
    '----------------------------------------------------------------------\n'
)