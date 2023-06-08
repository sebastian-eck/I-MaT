import ast
import re
from os import path

import music21
from music21 import converter
import pandas as pd
from miditok import CPWord, MIDILike, MuMIDI, Octuple, OctupleMono, REMI, REMIPlus, Structured
from miditoolkit import MidiFile


def extract_tokens(tokens_string):

    # Cut away the beginning of the string "[TokSequence(tokens=["
    start_index = tokens_string.index('=[') + 2
    trimmed_string = tokens_string[start_index:]

    # Cut away everything after the first appearing "]"
    end_index = trimmed_string.index(']')  # Find the index of the first appearing "]"
    trimmed_string = trimmed_string[:end_index]

    # Extract strings using regular expression
    search_pattern = r"'([^']*)'"
    token_list = re.findall(search_pattern, trimmed_string)

    return token_list

def extract_tokens_nested_list(tokens_string):

    # Cut away everything before the string "[TokSequence(tokens=["
    start_index = tokens_string.index('=[') + 2
    trimmed_string = tokens_string[start_index:]

    # Cut away everything after the the string ", ids="
    end_index = trimmed_string.index('], ids=')  # Find the index of the first appearing "]"
    trimmed_string = trimmed_string[:end_index]

    search_pattern = r'\[([^\[\]]*?)\]'
    matched_lists = re.findall(search_pattern, trimmed_string)

    token_lists = [ast.literal_eval(list) for list in matched_lists]

    return token_lists



# 1: REMI


# Creates the tokenizer and loads a MIDI
tokenizer = REMI()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "01_token_REMI.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)

# 2: REMIPlus


# Creates the tokenizer and loads a MIDI
tokenizer = REMIPlus()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "02_token_REMIPlus.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 3: MIDILike


# Creates the tokenizer and loads a MIDI
tokenizer = MIDILike()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "03_token_MIDILike.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 4: TSD


# Creates the tokenizer and loads a MIDI
tokenizer = REMIPlus()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "04_token_TSD.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 5: Structured


# Creates the tokenizer and loads a MIDI
tokenizer = Structured()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "05_token_Structured.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 6: CPWord


# Creates the tokenizer and loads a MIDI
tokenizer = CPWord()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "06_token_CPWord.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)

extract_tokens_nested_list(tokens_string)

# 7: Octuple


# Creates the tokenizer and loads a MIDI
tokenizer = Octuple()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "07_token_Octuple.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)


# 8: Octuple Mono


# Creates the tokenizer and loads a MIDI
tokenizer = OctupleMono()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "08_token_Octuple Mono.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)


# 9: MuMIDI

# Saves the token object as a string
tokens_string = str(tokens)


# Creates the tokenizer and loads a MIDI
tokenizer = MuMIDI()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "09_token_MuMIDI.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)





# Directory for saving the tokenized Midi-Files
file_folder = r"C:\Users\sebas\OneDrive\Dokumente\01_Dokumente Studium, Seminare, Vorlesungen\03_Waseda University\03_SoSe 2023\07_Introduction to Digital Humanities 01\Abschlussprojekt\02_Tokenization\01_Test Tokens"

# source MidiFile
midi = MidiFile(r'C:\Users\sebas\OneDrive\Dokumente\01_Dokumente Studium, Seminare, Vorlesungen\03_Waseda University\03_SoSe 2023\07_Introduction to Digital Humanities 01\Abschlussprojekt\01_Database\Test Track.mid')


def extract_tokens(tokens_string):

    # Cut away the beginning of the string "[TokSequence(tokens=["
    start_index = tokens_string.index('=[') + 2
    trimmed_string = tokens_string[start_index:]

    # Cut away everything after the first appearing "]"
    end_index = trimmed_string.index(']')  # Find the index of the first appearing "]"
    trimmed_string = trimmed_string[:end_index]

    # Extract strings using regular expression
    search_pattern = r"'([^']*)'"
    token_list = re.findall(search_pattern, trimmed_string)

    return token_list

def extract_tokens_nested_list(tokens_string):

    # Cut away everything before the string "[TokSequence(tokens=["
    start_index = tokens_string.index('=[') + 2
    trimmed_string = tokens_string[start_index:]

    # Cut away everything after the the string ", ids="
    end_index = trimmed_string.index('], ids=')  # Find the index of the first appearing "]"
    trimmed_string = trimmed_string[:end_index]

    search_pattern = r'\[([^\[\]]*?)\]'
    matched_lists = re.findall(search_pattern, trimmed_string)

    token_lists = [ast.literal_eval(list) for list in matched_lists]

    return token_lists

# 1: REMI

additional_tokens_REMI = {

    'Chord': False,
    'Program': True,
    'Rest': False,
    'Tempo': False,
    'TimeSignature': True

}

# Creates the tokenizer and loads a MIDI
tokenizer = REMI()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "01_token_REMI.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)

# 2: REMIPlus


# Creates the tokenizer and loads a MIDI
tokenizer = REMIPlus()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "02_token_REMIPlus.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 3: MIDILike


# Creates the tokenizer and loads a MIDI
tokenizer = MIDILike()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "03_token_MIDILike.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 4: TSD


# Creates the tokenizer and loads a MIDI
tokenizer = REMIPlus()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "04_token_TSD.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 5: Structured


# Creates the tokenizer and loads a MIDI
tokenizer = Structured()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "05_token_Structured.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)


# 6: CPWord


# Creates the tokenizer and loads a MIDI
tokenizer = CPWord()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "06_token_CPWord.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)

extract_tokens_nested_list(tokens_string)

# 7: Octuple


# Creates the tokenizer and loads a MIDI
tokenizer = Octuple()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "07_token_Octuple.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)


# 8: Octuple Mono


# Creates the tokenizer and loads a MIDI
tokenizer = OctupleMono()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "08_token_Octuple Mono.txt"

# Saves the token object as a string
tokens_string = str(tokens)

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)


# 9: MuMIDI

# Saves the token object as a string
tokens_string = str(tokens)


# Creates the tokenizer and loads a MIDI
tokenizer = MuMIDI()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# File Name
file_name_token = "09_token_MuMIDI.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens_nested_list(tokens_string)))

print("Data saved to", file_path)




# Creates the tokenizer and loads a MIDI
tokenizer = REMI()  # using the default parameters, read the documentation to customize your tokenizer

# Converts MIDI to tokens, and back to a MIDI
tokens = tokenizer(midi)  # calling it will automatically detect MIDIs, paths and tokens before the conversion

# Saves the token object as a string
tokens_string = str(tokens)

# File Name
file_name_token = "01_token_REMI.txt"

# Join the parts into a single path
file_path = path.join(file_folder, file_name_token)

# Opens the file in write mode
with open(file_path, "w") as file:
    # Writes the data to the file
    file.write(str(extract_tokens(tokens_string)))

print("Data saved to", file_path)




def select_sheet_music_file():
    # file_path = input("Enter the path of the sheet music file: ")
    file_path = r'C:\Users\sebas\OneDrive\Dokumente\01_Dokumente Studium, Seminare, Vorlesungen\03_Waseda University\03_SoSe 2023\07_Introduction to Digital Humanities 01\Abschlussprojekt\01_Database\Test Track.mid'

    if file_path.endswith(".mid"):
        return file_path
    else:
        try:
            allowed_formats = [".mid", ".xml", ".mxl", ".krn", ".abc", ".md", ".ly"]
            if any(file_path.endswith(ext) for ext in allowed_formats):

                parsed_score = parse_sheet_music_m21(file_path)

                return parsed_score
            else:
                print("Invalid file format. Please select a supported format.")
                return None
        except:
            print("Error occurred while parsing the file.")
            return None



        except:
            print("Invalid file format. Please select a MIDI file.")
            return None
# Directory for saving the tokenized Midi-Files
    file_folder = r"C:\Users\sebas\...\file.mid"

    if file_folder.endswith(".mid"):
        return file_folder
    else:
        # Parse the file with music21
        parsed_file = music21.converter.parse(file_folder)

        # Extract the file name without extension
        file_name = os.path.splitext(file_folder)[0]

        # Define the new path with ".mid" extension
        new_file_path = file_name + ".mid"

        # Export the parsed file to the new path
        parsed_file.write('midi', new_file_path)

        return new_file_path

def select_sheet_music_file():
    file_path = input("Enter the path of the sheet music file: ")

    if file_path.endswith(".mid"):
        return file_path




def select_path_for_export():

    # Directory for saving the tokenized Midi-Files
    file_folder = r"C:\Users\sebas\OneDrive\Dokumente\01_Dokumente Studium, Seminare, Vorlesungen\03_Waseda University\03_SoSe 2023\07_Introduction to Digital Humanities 01\Abschlussprojekt\02_Tokenization\01_Test Tokens"

    return file_folder


def parse_sheet_music_m21(file_path):

    score = music21.converter.parse(file_path)
    return score


def select_tokenizer():
    tokenizer_choice = input("Select the tokenizer to use (e.g., 'default', 'regex'): ")
    return tokenizer_choice


def tokenize_scores(score, tokenizer_choice):
    # tokenizer = Tokenizer(tokenizer_choice)
    tokenized_scores = tokenizer.tokenize(score)
    return tokenized_scores


def save_tokenized_scores(tokenized_scores):
    df = pd.DataFrame(tokenized_scores)
    df.to_csv("tokenized_scores.csv", index=False)
    print("Tokenized scores have been saved as 'tokenized_scores.csv'.")


def tokenizer_single_score():

    # Step 1: Select the path of the sheet music file

    sheet_music_file = select_sheet_music_file()

    # Step 2: Parse the scores using music21
    parsed_scores = parse_sheet_music_m21(sheet_music_file)

    # Step 3: Ask the user which tokenizer to use
    selected_tokenizer = select_tokenizer()

    # Step 4: Tokenize the scores using miditok
    tokenized_scores = tokenize_scores(parsed_scores, selected_tokenizer)

    # Step 5: Save the tokenized scores in a pandas DataFrame and CSV file
    save_tokenized_scores(tokenized_scores)
