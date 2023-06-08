import sys

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_proceed
from i_mat.src.cli.cli_score_selection import select_bars
from i_mat.src.cli.cli_text_output import text_analysis_notes_melody_melodicProgression_visualization_lineGraph
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_with_userInput import menu_askUser_repeatPreviousTool
from i_mat.src.utils.utils_without_userInput import utility_clear_screen


def melody_melodicDevelopment_visualization_lineGraph():
    utility_clear_screen()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    print(text_analysis_notes_melody_melodicProgression_visualization_lineGraph())
    print("")

    input(text_general_proceed())
    print("")

    # --- Unterhalb: Code des Tools ---

    try:
        fig = plt.figure()
        subplot = fig.add_subplot(1, 1, 1)

        user_selection = select_bars(config.global_score)

        for i in range(len(user_selection.parts)):
            top = user_selection.parts[i].flat.notes
            y = [n.pitch.ps for n in top]
            x = [n.offset + n.quarterLength / 2.0 for n in top]

            tick = interpolate.splrep(x, y, s=0)
            xnew = np.arange(0, max(x), 0.01)
            ynew = interpolate.splev(xnew, tick, der=0)

            subplot.plot(xnew, ynew)
            subplot.spines["top"].set_color("none")
            subplot.spines["right"].set_color("none")

        plt.show()

    # --- Oberhalb: Code des Tools ---

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    menu_askUser_repeatPreviousTool(
        melody_melodicDevelopment_visualization_lineGraph)
