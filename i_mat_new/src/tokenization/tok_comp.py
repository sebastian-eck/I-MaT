import miditok

from miditok import REMI
from miditok import REMIPlus
from miditok import MIDILike
from miditok import TSD
from miditok import Structured
from miditok import CPWord
from miditok import Octuple
from miditok import OctupleMono
from miditok import MuMIDI

from miditok.utils import get_midi_programs
from miditoolkit import MidiFile
from pathlib import Path

import re
import ast

from os import path


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


