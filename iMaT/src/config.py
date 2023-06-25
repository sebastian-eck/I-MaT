LANGUAGE = "EN"

global_selectedScore = None

global_input_firstMeasure = None

global_input_lastMeasure = None

global_previously_selectedScore = None

global_catalogue_individualParts = None

global_catalogue_completeScoreWithIndividualParts = None

global_score = None

global_searchPattern = None

global_score_path_input = None

global_score_path = None

global_example_score_path = "https://analyse.hfm-weimar.de/database/02/PrJode_Jos0602_COM_1-5_MissaLhomm_002_00066.xml"

global_selected_score = None

example_scores_dict = {
    "example_score_1": ["Example score 1: Dufay, Guillaume (1397-1474): Missa L'homme arme - Kyrie",
                        "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_1-5_MissaLhomm_002_00956.xml",
                        "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
    "example_score_2": ["Example score 2: Dufay, Guillaume (1397-1474): Missa L'homme arme - Gloria",
                        "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_2-5_MissaLhomm_002_00957.xml",
                        "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
    "example_score_3": ["Example score 3: Dufay, Guillaume (1397-1474): Missa L'homme arme - Credo",
                        "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_3-5_MissaLhomm_002_00958.xml",
                        "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
    "example_score_4": ["Example score 4: Dufay, Guillaume (1397-1474): Missa L'homme arme - Sanctus",
                        "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_3-5_MissaLhomm_002_00958.xml",
                        "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"],
    "example_score_5": ["Example score 5: Dufay, Guillaume (1397-1474): Missa L'homme arme - Agnus Dei",
                        "https://analyse.hfm-weimar.de/database/02/DuGui_Duf1004_COM_3-5_MissaLhomm_002_00958.xml",
                        "<Subcorpus (Projekt: Computergestützte Musikanalyse)>"]
}


keys_list = [
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