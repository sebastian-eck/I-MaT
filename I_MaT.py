from i_mat.src.cli.cli_general_display import text_general_terminateProgram
from i_mat.src.cli.cli_start import open_startmenu
from i_mat.src.cli.cli_text_output import start_printText
from i_mat.src.utils.utils_error_handling import text_exception_modules
from i_mat.src.utils.utils_m21_environment import check_environmentFile

try:

    import os
    from os import system, name
    from copy import deepcopy
    import sys
    import time

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    from IPython.display import HTML, display
    from scipy import interpolate

    from music21 import graph
    from music21 import environment
    from music21 import converter
    from music21 import roman
    from music21 import key
    from music21 import analysis
    from music21 import pitch
    from music21 import duration
    from music21 import search
    from music21 import note
    from music21 import stream

except Exception as e:
    print(text_exception_modules(e))

    user_input = input(text_general_terminateProgram())
    print("")




check_environmentFile()

start_printText()

open_startmenu()





