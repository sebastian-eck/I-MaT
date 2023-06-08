from i_mat import config as config


def text_environmentFile_createNewFile(received_environmentFile_path):
    text_de = (
            "KEINE ENVIRONMENT-DATEI VORHANDEN\n\n"
            "Erwartete Datei: "
            + str(received_environmentFile_path)
            + "\n\nEs wurde keine Environment-Datei gefunden. Das Erstellen dieser Datei ist zur korrekten Ausführung "
              "des Programs notwendig.\n\nMöchten Sie jetzt eine neue Environment-Datei erstellen? (ja/nein):"
    )

    text_en = (
            "NO ENVIRONMENT-DATEI FOUND\n\n"
            "Expected File: "
            + str(received_environmentFile_path)
            + "\n\nNo environment file was found. The creation of this file is necessary for the correct execution of "
              "the program.\n\nDo you want to create a new environment file now? (yes/no):"
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_createNewFile_created(received_environmentFile_path):
    text_de = (
            "Es wurde eine neue Environment-Datei in folgendem Verzeichnis erstellt:\n\n"
            + str(received_environmentFile_path)
            + '\n\nFalls Sie die Datei im Explorer/Finder nicht sehen können, müssen Sie die Option "ausgeblendete '
              'Dateien anzeigen" aktivieren:\n\nWINDOWS: Explorer > Ansicht > Ein-/ausblenden > Ausgeblendete '
              'Elemente\n\nMAC: Im Finder Tastenkombination "Befehlstaste (cmd/command) + Umschalttaste + Punkt"'
    )

    text_en = (
            "A new environment file has been created in the following directory:\n\n"
            + str(received_environmentFile_path)
            + '\n\nIf you cannot see the file in Explorer / Finder, you have to activate the option "View hidden '
              'files":\n\nWINDOWS: View > Show/hide > Hidden items\n\nMAC: In the Finder key combination "Command key '
              '(cmd / command) + Shift key + period"'
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_createNewFile_noFileCreated():
    text_de = (
        "Wenn Sie die Environment-Datei nicht erstellen, können Sie das Programm zwar verwenden, aber keine "
        "Notendateien in Ihrem Noteneditor anzeigen lassen oder Notendateien aus dem Internet herunterladen.\n\n"
        'Um die environment-Datei nachträglich zu erstellen, öffnen Sie "SETT: Einstellungen > Environment: '
        'Einstellungen neu konfigurieren\n'
        "Es wird dringend geraten, die environments-Datei zu erstellen und zu konfigurieren."
    )

    text_en = (
        "If you do not create the Environment file, you can use the program, but you cannot view score files in your "
        "Score Editor or download score files from the Internet.\n\n"
        'To create the Environment file later, open "SETT: Settings > Environment: Reconfigure Settings.\n\n'
        "It is strongly advised to create and configure the environments file."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_reconfigure_askDelete():
    text_de = "Möchten Sie die Environment-Datei löschen? (ja(nein): "

    text_en = "Do you want to delete the Environment file? (yes/no): "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_reconfigure_deleted():
    text_de = "Die Environment-Datei wurde erfolgreich gelöscht."

    text_en = "The Environment file was deleted successfully."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_reconfigure_notDeleted():
    text_de = "Die Environment-Datei wurde nicht gelöscht."

    text_en = "The Environment file was not deleted."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_showPath(received_environmentFile_path):
    text_de = (
            "Der Pfad der Environment-Datei lautet: " + str(received_environmentFile_path) + "\n\n"
            'Falls Sie die Datei nicht sehen können, müssen Sie die Option "ausgeblendete Dateien anzeigen" '
                                                                                             'aktivieren:\n\n'
            "WINDOWS: Explorer > Ansicht > Ein-/ausblenden > Ausgeblendete Elemente\n\n"
            'MAC: Im Finder Tastenkombination "Befehlstaste (cmd/command) + Umschalttaste + Punkt"'
    )

    text_en = (
            "The path of the environment file is: " + str(received_environmentFile_path) + "\n\n"
            'If you cannot see the file, you have to activate the option "Show hidden files":\n\n'
            "WINDOWS: Explorer > View > Show / hide > Hidden items\n\n"
            'MAC: In the Finder key combination "Command key (cmd / command) + Shift key + period"'
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_configure_musescorePath():
    text_de = (
        "Bitte geben Sie den Pfad zu Ihrer MuseScore3.exe (Windows) bzw. MuseScore3.app (Mac) - Datei an.\n\n"
        "Unter Windows finden Sie diese üblicherweise im Ordner: C:\\Program Files\\MuseScore "
        "3\\bin\\MuseScore3.exe\n\n"
        "Unter Mac finden Sie diese üblicherweise im Ordner: Applications\\MuseScore3.app\n\n"
        'WINDOWS: Ziehen Sie hierzu die Datei "MuseScore3.exe" einfach aus dem Ordner in das Terminal und drücken Sie '
        '"Eingabe".\n\n'
        'MAC: Klicken Sie mit Rechtsklick auf "MuseScore3.app" und wählen Sie "MuseScore3.app als Pfadname kopieren" '
        'aus.\n\n'
        'Fügen Sie den Link nachfolgend mit "command + v" ein.\n\n'
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )

    text_en = (
        "Please enter the path to your MuseScore3.exe (Windows) or MuseScore3.app (Mac) file.\n\n"
        "Under Windows you will usually find this in the folder: C: \\ Program Files \\ MuseScore 3 \\ bin \\ "
        "MuseScore3.exe\n\n"
        "On Mac you can usually find this in the folder: Applications \\ MuseScore3.app\n\n"
        'WINDOWS: To do this, simply drag the "MuseScore3.exe" file from the folder into the terminal and press '
        '"Enter".\n\n'
        'MAC: Right click on "MuseScore3.app" and select "Copy MuseScore3.app as path name".\n\n'
        'Insert the link below with "command + v".\n\n'
        "Be careful not to put any spaces at the end of the path."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_environmentFile_configure_scratchPath():
    text_de = (
        "Bitte geben Sie den Pfad zu dem Ordner an, in dem Ihre von music21 exportierten Dateien gespeichert werden "
        "sollen.\n\n"
        'WINDOWS: Ziehen Sie hierzu einfach das Icon des gewünschten Ordners in das Terminal und drücken Sie '
        '"Eingabe".\n\n'
        'MAC: Klicken Sie mit Rechtsklick auf den gewünschten Ordner und wählen Sie "<Ordner-Name> als Pfadname '
        'kopieren" aus.\n\n'
        'Fügen Sie den Pfad des gewünschten Ordners nachfolgend mit "command + v" ein.\n\n'
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )

    text_en = (
        "Please enter the path to the folder in which your files exported by music21 should be saved.\n\n"
        'WINDOWS: To do this, simply drag the icon of the desired folder into the terminal and press "Enter".\n\n'
        'MAC: Right-click on the desired folder and select "Copy <folder name> as path name".\n\n'
        'Then insert the path of the desired folder with "command + v".\n\n'
        "Be careful not to put any spaces at the end of the path."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en
