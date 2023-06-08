import sys

import i_mat.config as config


def text_exception_modules(exception_text):
    tb = sys.exc_info()[2]

    text_de = (
            "Es fehlen Pakete auf Ihrem System. Bitte wenden Sie sich an einen Tutor (Fehlercode: MOD). Notwendig sind folgende Pakete:\n\n"
            "python==3.10.*\n"
            "numpy==1.20.*\n"
            "matplotlib==3.4.*\n"
            "pandas==1.2.*\n"
            "ipython==7.24.*\n"
            "scipy==1.6.*\n"
            "music21==6.7.*\n\n"
            "Fehler in Zeile: "
            + str(tb.tb_lineno)
            + " -> "
            + str(exception_text)
            + "\n\nSollte das Problem weiterhin bestehen, wenden Sie sich bitte an den Projekt-Support.\n\nSupport: analyse@hfm-weimar.de"
    )

    text_en = (
            "Packages are missing on your system. Please contact a tutor (error code: MOD). The following packages are required:\n\n"
            "python==3.10.*\n"
            "numpy==1.20.*\n"
            "matplotlib==3.4.*\n"
            "pandas==1.2.*\n"
            "ipython==7.24.*\n"
            "scipy==1.6.*\n"
            "music21==6.7.*\n\n"
            "Error in line: "
            + str(tb.tb_lineno)
            + " -> "
            + str(exception_text)
            + "\n\nIf the problem persists, please contact project support.\n\nSupport: analyse@hfm-weimar.de"
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_exception_general(exception_text, function_name):
    tb = sys.exc_info()[2]

    text_de = (
            "Bei der Ausführung des Programms wurde ein Fehler festgestellt:\n\nFehler in Zeile: "
            + str(tb.tb_lineno)
            + "\n\nFehlercode: "
            + str(exception_text)
            + "\n\nIn Funktion: "
            + str(function_name)
            + "\n\nSollte das Problem weiterhin bestehen, wenden Sie sich bitte an den Projekt-Support.\n\nSupport: analyse@hfm-weimar.de"
    )

    text_en = (
            "An error was encountered while executing the program:\n\nError in line: "
            + str(tb.tb_lineno)
            + "\n\nError code: "
            + str(exception_text)
            + "\n\nIn function: "
            + str(function_name)
            + "\n\nIf the problem persists, please contact project support.\n\nSupport: analyse@hfm-weimar.de"
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en
