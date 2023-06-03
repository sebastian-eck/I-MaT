# # Text

# ## Headers

# In[1]:


def text_headers(identifier):
    dict_de = {
        "range_analysis_textOutput": ["Notenauswahl", "Ambitus"],
        "range_comparison_textOutput": ["Notenauswahl", "Ambitus"],
        "intervalStructure_intervalTypes_textOutput": [
            "Notenauswahl",
            "Anzahl der Intervalltypen",
            "Intervalltypen",
        ],
        "intervalStructure_intervalTypes_quantity_textOutput": [
            "Notenauswahl",
            "Intervall",
            "Vorkommen",
        ],
        "intervalStructure_intervalTypes_comparison_textOutput": [
            "Notenauswahl",
            "Intervall",
            "Vorkommen",
            "Differenz zur anderen Notenauswahl (+/-)",
        ],
        "intervalStructure_Intervalle_quantity_textOutput": [
            "Notenauswahl",
            "Anzahl Intervalle",
        ],
        "meter_metricWeight_textOutput": [
            "Kennung",
            "Metrisches Gewicht (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "meter_pitchClass_metricPosition_textOutput": [
            "Kennung",
            "Tonhoehe (x-Achse)",
            "Metrisches Gewicht (y-Achse)",
            "Haeufigkeit (z-Achse)",
        ],
        "notes_notesQuantity_total_textOutput": ["Kennung", "Anzahl Töne"],
        "notes_notesQuantity_pitches_textOutput": [
            "Kennung",
            "Tonhoehen",
            "Pitch",
        ],
        "predefinedVisualizations_HistogramPitchSpace": [
            "Kennung",
            "Tonstufe (Midi)",
            "Tonstufenname (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "predefinedVisualizations_HistogramPitchClass": [
            "Kennung",
            "Tonklasse (Midi)",
            "Tonklassenname (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "predefinedVisualizations_HistogramQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "predefinedVisualizations_HorizontalBarPitchSpaceOffset": [
            "Kennung",
            "Tonstufe (Midi)",
            "Tonstufenname (y-Achse)",
            "Offset (x-Achse)",
            "Dargestellte Tonlaenge",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Tonstufe (Midi)",
            "Tonstufenname (y-Achse)",
            "Haeufigkeit",
        ],
        "predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Tonstufe (Midi)",
            "Tonstufenname (y-Achse)",
            "Haeufigkeit (z-Achse)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchClassQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Tonklasse (Midi)",
            "Tonklassenname (y-Achse)",
            "Haeufigkeit",
        ],
        "predefinedVisualizations_ScatterPitchClassOffset": [
            "Kennung",
            "Tonklasse",
            "Tonklassenname (y-Achse)",
            "Offset (x-Achse)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol": [
            "Kennung",
            "Tonstufe (Midi)",
            "Tonstufenname (x-Achse)",
            "Dynamik (y-Achse)",
            "Haeufigkeit",
        ],
        "predefinedVisualizations_HorizontalBarPitchClassOffset": [
            "Kennung",
            "Tonklasse (Midi)",
            "Tonklassenname (y-Achse)",
            "Offset (x-Achse)",
            "Dargestellte Tonlaenge",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote)",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote",
        ],
        "patternSearch_menuStructure_rhythm_withoutPitch": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote",
        ],
        "show_names_individualVoices": ["Nr.", "Name der Stimme"],
        "helpers_name_individualVoices": ["Nr.", "Name der Stimme"],
        "show_score_metadata": ["Nr.", "Metadata", "Wert"],
    }

    dict_en = {
        "range_analysis_textOutput": ["Notenauswahl", "Ambitus"],
        "range_comparison_textOutput": ["Note selection", "Ambitus"],
        "intervalStructure_intervalTypes_textOutput": [
            "Note selection",
            "Number of interval types",
            "Interval types",
        ],
        "intervalStructure_intervalTypes_quantity_textOutput": [
            "Note selection",
            "Interval",
            "Frequency",
        ],
        "intervalStructure_intervalTypes_comparison_textOutput": [
            "Note selection",
            "Interval",
            "Frequency",
            "Difference to other note selection (+/-)",
        ],
        "intervalStructure_Intervalle_quantity_textOutput": [
            "Note selection",
            "Number of intervals",
        ],
        "meter_metricWeight_textOutput": [
            "Identifier",
            "Metric weight (x-axis)",
            "Frequency (y-axis)",
        ],
        "meter_pitchClass_metricPosition_textOutput": [
            "Identifier",
            "Pitch (x-axis)",
            "Metric weight (y-axis)",
            "Frequency (z-axis)",
        ],
        "notes_notesQuantity_total_textOutput": ["Identifier", "Number of tones"],
        "notes_notesQuantity_pitches_textOutput": [
            "Identifier",
            "Pitch",
            "Pitch",
        ],
        "predefinedVisualizations_HistogramPitchSpace": [
            "Identifier",
            "Pitch (midi)",
            "Pitch name (x-axis)",
            "Frequency (y-axis)",
        ],
        "predefinedVisualizations_HistogramPitchClass": [
            "Identifier",
            "Tone class (Midi)",
            "Tone class name (x-axis)",
            "Frequency (y-axis)",
        ],
        "predefinedVisualizations_HistogramQuarterLength": [
            "Identifier",
            "Rhythm value (quarter = 1.0)",
            "Rhythm value name (x-axis)",
            "Frequency (y-axis)",
        ],
        "predefinedVisualizations_HorizontalBarPitchSpaceOffset": [
            "Identifier",
            "Pitch (midi)",
            "Pitch name (y-axis)",
            "Offset (x-axis)",
            "Displayed length",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength": [
            "Identifier",
            "Rhythm value (quarter = 1.0)",
            "Rhythm value name (x-axis)",
            "Pitch (midi)",
            "Pitch name (y-axis)",
            "Frequency",
        ],
        "predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength": [
            "Identifier",
            "Rhythm value (quarter = 1.0)",
            "Rhythm value name (x-axis)",
            "Pitch (midi)",
            "Pitch name (y-axis)",
            "Frequency (z-axis)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchClassQuarterLength": [
            "Identifier",
            "rhythm value (quarter = 1.0)",
            "rhythm value name (x-axis)",
            "pitch class (midi)",
            "pitch class name (y-axis)",
            "frequency",
        ],
        "predefinedVisualizations_ScatterPitchClassOffset": [
            "Identifier",
            "pitch class",
            "pitch class name (y-axis)",
            "offset (x-axis)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol": [
            "Identifier",
            "Pitch (midi)",
            "Pitch name (x-axis)",
            "Dynamics (y-axis)",
            "Frequency",
        ],
        "predefinedVisualizations_HorizontalBarPitchClassOffset": [
            "Identifier",
            "Tone class (Midi)",
            "Tone class name (y-axis)",
            "Offset (x-axis)",
            "Displayed pitch length",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "patternSearch_menuStructure_rhythm_withoutPitch": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "show_names_individualVoices": ["No.", "Part name"],
        "helpers_name_individualVoices": ["No.", "Part name"],
        "show_score_metadata": ["No.", "Metadata", "Value"],
    }

    if LANGUAGE == "DE":
        return dict_de[identifier]

    elif LANGUAGE == "EN":
        return dict_en[identifier]


# ## Environment

# ### Create

# In[ ]:


def text_environmentFile_createNewFile(environmentFile_path):
    text_de = (
        "KEINE ENVIRONMENT-DATEI VORHANDEN\n\n"
        "Erwartete Datei: "
        + str(environmentFile_path)
        + "\n\nEs wurde keine Environment-Datei gefunden. Das Erstellen dieser Datei ist zur korrekten Ausführung des Programs notwendig.\n\nMöchten Sie jetzt eine neue Environment-Datei erstellen? (ja/nein): "
    )

    text_en = (
        "NO ENVIRONMENT-DATEI FOUND\n\n"
        "Expected File: "
        + str(environmentFile_path)
        + "\n\nNo environment file was found. The creation of this file is necessary for the correct execution of the program.\n\nDo you want to create a new environment file now? (yes/no): "
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### New file created

# In[ ]:


def text_environmentFile_createNewFile_created(environmentFile_path):
    text_de = (
        "Es wurde eine neue Environment-Datei in folgendem Verzeichnis erstellt:\n\n"
        + str(environmentFile_path)
        + '\n\nFalls Sie die Datei im Explorer/Finder nicht sehen können, müssen Sie die Option "ausgeblendete Dateien anzeigen" aktivieren:\n\nWINDOWS: Explorer > Ansicht > Ein-/ausblenden > Ausgeblendete Elemente\n\nMAC: Im Finder Tastenkombination "Befehlstaste (cmd/command) + Umschalttaste + Punkt"'
    )

    text_en = (
        "A new environment file has been created in the following directory:\n\n"
        + str(environmentFile_path)
        + '\n\nIf you cannot see the file in Explorer / Finder, you have to activate the option "View hidden files":\n\nWINDOWS: View > Show/hide > Hidden items\n\nMAC: In the Finder key combination "Command key (cmd / command) + Shift key + period"'
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### No file created

# In[ ]:


def text_environmentFile_createNewFile_noFileCreated():
    text_de = (
        "Wenn Sie die Environment-Datei nicht erstellen, können Sie das Programm zwar verwenden, aber keine Notendateien in Ihrem Noteneditor anzeigen lassen oder Notendateien aus dem Internet herunterladen.\n\n"
        'Um die environment-Datei nachträglich zu erstellen, öffnen Sie "SETT: Einstellungen > Environment: Einstellungen neu konfigurieren\n'
        "Es wird dringend geraten, die environments-Datei zu erstellen und zu konfigurieren."
    )

    text_en = (
        "If you do not create the Environment file, you can use the program, but you cannot view score files in your Score Editor or download score files from the Internet.\n\n"
        'To create the Environment file later, open "SETT: Settings > Environment: Reconfigure Settings.\n\n'
        "It is strongly advised to create and configure the environments file."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Reconfigure

# #### Ask delete or not (input)

# In[ ]:


def text_environmentFile_reconfigure_askDelete():
    text_de = "Möchten Sie die Environment-Datei löschen? (ja(nein): "

    text_en = "Do you want to delete the Environment file? (yes/no): "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Deleted

# In[ ]:


def text_environmentFile_reconfigure_deleted():
    text_de = "Die Environment-Datei wurde erfolgreich gelöscht."

    text_en = "The Environment file was deleted successfully."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Not deleted

# In[ ]:


def text_environmentFile_reconfigure_notDeleted():
    text_de = "Die Environment-Datei wurde nicht gelöscht."

    text_en = "The Environment file was not deleted."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Show Environment path

# In[ ]:


def text_environmentFile_showPath(environmentFile_path):
    text_de = (
        "Der Pfad der Environmentdatei lautet: " + str(environmentFile_path) + "\n\n"
        'Falls Sie die Datei nicht sehen können, müssen Sie die Option "ausgeblendete Dateien anzeigen" aktivieren:\n\n'
        "WINDOWS: Explorer > Ansicht > Ein-/ausblenden > Ausgeblendete Elemente\n\n"
        'MAC: Im Finder Tastenkombination "Befehlstaste (cmd/command) + Umschalttaste + Punkt"'
    )

    text_en = (
        "The path of the environment file is: " + str(environmentFile_path) + "\n\n"
        'If you cannot see the file, you have to activate the option "Show hidden files":\n\n'
        "WINDOWS: Explorer > View > Show / hide > Hidden items\n\n"
        'MAC: In the Finder key combination "Command key (cmd / command) + Shift key + period"'
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Musecore

# #### Path

# In[ ]:


def text_environmentFile_configure_musescorePath():
    text_de = (
        "Bitte geben Sie den Pfad zu Ihrer MuseScore3.exe (Windows) bzw. MuseScore3.app (Mac) - Datei an.\n\n"
        "Unter Windows finden Sie diese üblicherweise im Ordner: C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe\n\n"
        "Unter Mac finden Sie diese üblicherweise im Ordner: Applications\\MuseScore3.app\n\n"
        'WINDOWS: Ziehen Sie hierzu die Datei "MuseScore3.exe" einfach aus dem Ordner in das Terminal und drücken Sie "Eingabe".\n\n'
        'MAC: Klicken Sie mit Rechtsklick auf "MuseScore3.app" und wählen Sie "MuseScore3.app als Pfadname kopieren" aus.\n\n'
        'Fügen Sie den Link nachfolgend mit "command + v" ein.\n\n'
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )

    text_en = (
        "Please enter the path to your MuseScore3.exe (Windows) or MuseScore3.app (Mac) file.\n\n"
        "Under Windows you will usually find this in the folder: C: \\ Program Files \\ MuseScore 3 \\ bin \\ MuseScore3.exe\n\n"
        "On Mac you can usually find this in the folder: Applications \\ MuseScore3.app\n\n"
        'WINDOWS: To do this, simply drag the "MuseScore3.exe" file from the folder into the terminal and press "Enter".\n\n'
        'MAC: Right click on "MuseScore3.app" and select "Copy MuseScore3.app as path name".\n\n'
        'Insert the link below with "command + v".\n\n'
        "Be careful not to put any spaces at the end of the path."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Scratch folder (working directory)

# #### Path

# In[ ]:


def text_environmentFile_configure_scratchPath():
    text_de = (
        "Bitte geben Sie den Pfad zu dem Ordner an, in dem Ihre von music21 exportierten Dateien gespeichert werden sollen.\n\n"
        'WINDOWS: Ziehen Sie hierzu einfach das Icon des gewünschten Ordners in das Terminal und drücken Sie "Eingabe".\n\n'
        'MAC: Klicken Sie mit Rechtsklick auf den gewünschten Ordner und wählen Sie "<Ordner-Name> als Pfadname kopieren" aus.\n\n'
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

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Exception

# #### Modules

# In[2]:


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

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### General

# In[3]:


def text_exception_general(exception_text, function_name):
    tb = sys.exc_info()[2]

    text_de = (
        "Bei der Ausführung des Programms wurde ein Fehler festgestellt:\n\n\Fehler in Zeile: "
        + str(tb.tb_lineno)
        + "\n\nFehlercode: "
        + str(exception_text)
        + "\n\nIn Funktion: "
        + str(function_name)
        + "\n\nSollte das Problem weiterhin bestehen, wenden Sie sich bitte an den Projekt-Support.\n\nSupport: analyse@hfm-weimar.de"
    )

    text_en = (
        "An error was encountered while executing the program:\n\n\Error in line: "
        + str(tb.tb_lineno)
        + "\n\nError code: "
        + str(exception_text)
        + "\n\nIn function: "
        + str(function_name)
        + "\n\nIf the problem persists, please contact project support.\n\nSupport: analyse@hfm-weimar.de"
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## General

# ### Title

# In[ ]:


def text_general_title():
    text_de = (
        "\nI-MaT - Interaktives Musikanalyse Tool, (2.2, 01.2022)\n\n"
        'Fellowship-Projekt "Computergestützte Musikanalyse"\n\n\n'
        "Fellowship für Innovationen in der digitalen Hochschullehre\n\n"
        "----------------------------------------------------------------------\n"
    )

    text_en = (
        "\nI-MaT - Interactive music analysis tool, (2.2, 01.2022)\n\n"
        'Fellowship project "Computer-assisted Music Analysis"\n\n\n'
        "Fellowship for innovations in digital university teaching\n\n"
        "----------------------------------------------------------------------\n"
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Correct Entry

# In[ ]:


def text_general_checkEntry():
    text_de = "Ist die Eingabe korrekt? (ja/nein): "

    text_en = "Is the entry correct? (yes/no): "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Proceed (input)

# In[5]:


def text_general_proceed():
    text_de = "<Um fortzufahren, bitte Eingabe drücken>"

    text_en = "<To continue, please press Enter>"

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Restricted yes/no (input)

# In[6]:


def text_general_input_RestrictedToYesAndNo():
    text_de = (
        "<Eingabe beschränkt auf ja/nein (alternativ: 1/0). Bitte erneut eingeben.>"
    )

    text_en = "<Input restricted to yes/no (alternatively: 1/0). Please re-enter.>"

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Restricted numbers (input)

# In[ ]:


def text_general_input_restrictedToNumbers(input_text):
    text_de = (
        "Fehler: '"
        + input_text
        + "' - Eingabe beschränkt auf Zahlen. Bitte erneut eingeben."
    )

    text_en = "Error: '" + input_text + "' - Input restricted to numbers. Please re-enter."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Close MuseScore3 to continue

# In[7]:


def text_general_close_museScore3():
    text_de = (
        "Hinweis 1: um fortzufahren, bitte MuseScore schließen.\n\n"
        "Hinweis 2: zum Exportieren der Datei als PDF in MuseScore bitte '> Datei > Export...' verwenden.\n\n"
        "WICHTIG: Ladezeit variiert mit Größe der importierten Datei."
    )

    text_en = (
        "Note 1: Please close MuseScore to continue.\n\n"
        "Note 2: to export the file as PDF in MuseScore please use '> File > Export ...'.\n\n"
        "IMPORTANT: Loading time varies with the size of the imported file."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Close player to continue

# In[ ]:


def text_general_close_audioPlayer():
    text_de = "Hinweis: um fortzufahren, bitte den Audio-Player schließen."

    text_en = "Note: please close the audio player to continue."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Enter new path/URL (input)

# In[ ]:


def text_general_enter_newPath():
    text_de = "Geben Sie den Pfad/die URL ein: "

    text_en = "Enter Path/URL: "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Show entered Path

# In[3]:


def text_general_show_enteredPath(enteredPath):
    text_de = 'Folgender Pfad/Url wurde eingegeben: "' + str(enteredPath) + '"'

    text_en = 'The following path/URL was entered: "' + str(enteredPath) + '"'

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Informations

# In[ ]:


def text_general_projectDescription():
    text_de = (
        "Lehrveranstaltungen zur musikalischen Analyse sind an Universitäten und Musikhochschulen ein fester Bestandteil\n"
        "sowohl der musikwissenschaftlichen Studiengänge als auch der Ausbildung von Musiklehrer*innen und Musiker*innen.\n"
        "Ziel des Fellowship-Projektes ist es, unter Rückgriff auf verschiedene computerbasierte Analyse-Tools mehrer\n"
        "flexibel einsetzbare Unterrichtsmodule zur Musikanalyse zu konzipieren, zu erproben, zu evaluieren und zu vermitteln.\n"
        "Die Unterrichtsmodule widmen sich u.a. der computerbasierten Annotation und Visualisierung von Notentexten und\n"
        "Audiodateien, der statistischen Analyse von Musikkorpora, der Suche nach musikalischen Mustern (Melodien, Rhythmen usw.)\n"
        "Sie sollen herkömmliche Analysekurse ergänzen, wurden bereits in mehreren Lehrveranstaltungen an der HfM Weimar\n"
        "erprobt und evaluiert und werden über diese Internetplattform einem breiteren Interessentenkreis kostenfrei zur\n"
        "Verfügung gestellt. Computer können als Hilfsmittel der Analyse von Notentexten und Musikaufnahmen eingesetzt werden.\n\n"
        "Mit Computerprogrammen können schnell und verlässlich\n\n"
        " - musikalische Abläufe und Strukturen visualisiert,\n"
        " - musikalische Merkmale der betreffenden Stücke (z.B. Häufigkeiten von Tonhöhen) statistisch beschrieben\n"
        " - und nach bestimmten Mustern (z.B. melodischen Motiven) durchsucht werden.\n\n"
        "Dadurch werden herkömmliche Analyseansätze erweitert und neue Perspektiven der musikalischen Analyse in\n"
        "Musikwissenschaft und Musiktheorie eröffnet und erkundet. Zum einen können mit den Computer-Tools gezielt\n"
        "analytischen Fragestellungen weiterverfolgt werden, zum anderen ermöglicht ein spielerischer Umgang mit den\n"
        "Tools und Notendateien ein Entdecken von unerwarteten Zusammenhängen - was dann zu neuen analytischen \n"
        "Fragestellungen führen kann.\n\n"
        "Im Rahmen des Projektes werden Unterrichtmodule und Tutorials (<https://analyse.hfm-weimar.de/doku.php?id=tutorials>\n"
        "bereitgestellt, die anhand von musikanalytischen Fragestellungen in verschiedene Möglichkeiten der computergestützten\n"
        "Analyse von Noten- bzw. Audio-Dateien einführen. Jede Unterrichtsmodule setzt sich aus einem Grundlagen-Modul (Basics)\n"
        "sowie einer Spezialisierung (Advanced) zusammen. Die Unterrichtseinheiten können im Selbststudium oder innerhalb von\n"
        "Lehrveranstaltungen eingesetzt werden. Die Dauer der beiden Unterrichtsmodule beträgt jeweils ca. drei 90-minütige\n"
        "Sitzungen mit zusätzlichen Vorbereitungen, Hausaufgaben und optionalen Vertiefungen.\n\n"
        "Alle in den Unterrichtsmodule verwendete Software (<https://analyse.hfm-weimar.de/doku.php?id=installation>) ist frei\n"
        "zugänglich und lizenzfrei nutzbar. Damit folgt das Projekt dem Prinzip des Open Access, des offenen Zugangs zu\n"
        "öffentlich geförderten Projektergebnissen und der Unabhängigkeit von kommerziell orientierten IT-Konzernen.\n\n"
        "Weitere Informationen zu den Zielsetzungen, Mitarbeiter*innen, Veröffentlichungen des Projekts usw. finden Sie\n"
        "unter 'Das Projekt' (<https://analyse.hfm-weimar.de/doku.php?id=forschung>).\n\n"
        "Das Projekt Computergestützte Musikanalyse in der digitalen Hochschullehre ist am Institut für Musikwissenschaft\n"
        "Weimar-Jena der Hochschule für Musik Franz Liszt Weimar angesiedelt. Es wird gefördert vom Thüringer Ministerium\n"
        "für Wirtschaft, Wissenschaft und Digitalen Wandel und dem Stifterverband. Das Projekt versteht sich als Beitrag\n"
        "zur Computational Musicology bzw. Digital Musicology innerhalb der Digital Humanties.\n\n"
        "Das Projekt befindet sich derzeit in der Testphase. Rückmeldungen sind erwünscht: analyse@hfm-weimar.de\n\n"
        "Impressum:\n\n"
        "Hochschule für Musik Franz Liszt Weimar\n"
        "Institut für Musikwissenschaft Weimar | Jena\n"
        "Hochschulzentrum am Horn\n"
        "Carl-Alexander-Platz 1\n"
        "99425 Weimar\n\n"
    )

    text_en = (
        "Courses on musical analysis are an integral part of both musicology courses and the training of music teachers\n"
        "and musicians at universities and conservatories. The goal of the fellowship project is to design, test, evaluate,\n"
        "and teach several flexibly applicable teaching modules on music analysis, with recourse to various computer-based\n"
        "analysis tools. The teaching modules are dedicated to computer-based annotation and visualization of musical texts\n"
        "and audio files, statistical analysis of music corpora, and search for musical patterns (melodies, rhythms etc.).\n"
        "They are intended to complement conventional analysis courses, have been and evaluated within several coursesat the HfM\n"
        "Weimar, and will are publicly available to a wider circle of interested parties via this Internet platform.\n\n"
        "Computers can be used as aids in the analysis of musical texts and recordings.\n\n"
        "Computer programs can be used to quickly and reliably\n\n"
        " - visualize musical sequences and structures,\n"
        " - statistically describe musical characteristics of the pieces in question (e.g. frequencies of pitches)\n"
        " - and searched for specific patterns (e.g. melodic motifs).\n\n"
        "This extends conventional approaches to analysis and opens up and explores new perspectives of musical analysis\n"
        "in musicology and music theory. On the one hand, the computer tools can be used to pursue specific analytical questions,\n"
        "and on the other hand, a playful approach to the tools and note files enables the discovery of unexpected\n"
        "relationships - which can then lead to new analytical questions.\n\n"
        "The Teaching modules and tutorials (<https://analyse.hfm-weimar.de/doku.php?id=en:tutorials>) are provided that\n"
        "introduce various possibilities of computer-assisted analysis of sheet music or audio files on the basis of\n"
        "music-analytical issues. Each teaching unit consists of a basic module(Basics Sheet Music or Basics Audio)\n"
        "and a specialization (Advanced). The teaching units can be used in self-study or within courses. The duration\n"
        "of the teaching units is approximately three sessions of 90-minutes, with additional preparation, homework\n"
        "and optional specializations.\n\n"
        "All software (<https://analyse.hfm-weimar.de/doku.php?id=en:installation>) used in the teaching units is freely\n"
        "accessible and license-free. Thus, the project follows the principle of open access - open access to publicly\n"
        "funded project results and independence from commercially oriented IT corporations.\n\n"
        "The project Computergestützte Musikanalyse in der digitalen Hochschullehre (computer-aided music analysis\n"
        "within digital higher education) is located at the Institute of Musicology Weimar-Jena of the Franz Liszt University\n"
        "of Music Weimar. It is funded by the Thuringian Ministry for Economy, Science and Digital Change and the Stifterverband.\n"
        "The project sees itself as a contribution to Computational Musicology or Digital Musicology within Digital Humanities.\n\n"
        "Further information about the project's objectives, staff etc. can be found on\n\n"
        " -> 'The project' (<https://analyse.hfm-weimar.de/doku.php?id=en:research>).\n\n"
        "The project is currently in the test phase. Feedback is welcome: analyse@hfm-weimar.de\n\n"
        "Imprint:\n\n"
        "University of Music Franz Liszt Weimar\n"
        "Institute for Musicology Weimar | Jena\n"
        "University Center at the Horn\n"
        "Carl-Alexander-Platz 1\n"
        "99425 Weimar\n\n"
    )

    try:
        if LANGUAGE == "DE":
            clear_screen()

            print(text_de)

        elif LANGUAGE == "EN":
            clear_screen()

            print(text_en)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")


# ### Choose Key

# In[ ]:


def text_general_chooseKey():
    text_de = "Wählen Sie im nachfolgenden Auswahlmenü die Tonart des ausgewählten Notenabschnittes aus."

    text_en = "Please select the key of the selected score section in the following selection menu."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Diagram export unavailable

# In[ ]:


def text_general_exportToDiagrammUnavailable():
    text_de = "Für dieses Tool ist ein Datenexport als Grafikdiagramm nicht vorgesehen."

    text_en = "Data export as a graphic is not intended for this tool."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### No results

# In[ ]:


def text_general_noResults():
    text_de = "Fehler: Die Auswertung der Notendatei lieferte keine Ergebnisse."

    text_en = "Error: The analysis of the score file did not produce any results."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Display

# ### Show score selection (input)

# In[ ]:


def text_display_showScoreSelection():
    text_de = "Möchten Sie den ausgewählten/eingegebenen Notentext anzeigen lassen? (ja/nein): "

    text_en = "Would you like to display the selected/entered music text? (yes/no): "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Export

# ### Filename

# In[8]:


def text_export_fileName():
    text_de = "Unter welchem Namen soll die Datei gespeichert werden? Dateiname: "

    text_en = "Under what name should the file be saved? Filename: "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Terminate

# In[9]:


def text_general_terminateProgram():
    text_de = "<Um das Programm zu beenden, bitte Eingabe drücken>"

    text_en = "<To terminate the program, please press Enter>"

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Save

# In[10]:


def text_general_exportSuccessful(path, name, extension):
    text_de = (
        "Die Datei wurde erfolgreich gespeichert.\n\n"
        "Speicherort: " + str(path) + "\n\n"
        "Dateiname: " + str(name) + str(extension)
    )

    text_en = (
        "The file was saved successfully.\n\n"
        "Location: " + str(path) + "\n\n"
        "Filename: " + str(name) + str(extension)
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Images

# In[11]:


def text_general_exportGraph(path):
    text_de = (
        "Die Datei wurde erfolgreich gespeichert.\n\n"
        "Speicherort: " + str(path) + "\n\n"
        "Um fortfahren zu können, müssen Sie eventuell die sich soeben geöffneten Grafikansichten schließen."
    )

    text_en = (
        "The file was saved successfully.\n\n"
        "Location: " + str(path) + "\n\n"
        "In order to be able to continue, you may have to close the graphic views that have just opened."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ##### Name

# In[ ]:


def text_general_exportGraphName():
    text_de = (
        "Bitte wählen Sie einen Titel für das zu exportierende Grafikdiagramm aus: "
    )

    text_en = "Please select a title for the graphic diagram to be exported: "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Pattern search

# ### Show pattern selection

# In[ ]:


def text_patternSearch_showPatternSelection(selection):
    text_de = "Auswahl (englische Tonnamen): " + str(selection)

    text_en = "Selection: " + str(selection)

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Delete selection

# In[ ]:


def text_patternSearch_deleteSelection():
    text_de = "Die Eingabe wurde gelöscht. Bitte geben Sie die Suchmuster erneut ein."

    text_en = "The entry has been deleted. Please re-enter the search pattern."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Patterns found

# In[1]:


def text_patternSearch_patternsFound(result_quantity):
    text_de = "Das eingegebene Suchmuster wurde genau " + \
        str(result_quantity) + "-mal gefunden."

    text_en = "The search pattern entered was found exactly " + \
        str(result_quantity) + " times."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Include rests

# In[ ]:


def text_patternSearch_includeRests():
    text_de = (
        "Sollen Muster über Pausen hinweg gesucht werden?\n\n"
        "[ja = Pausen werden bei der Mustersuche ignoniert] (ja/nein): "
    )

    text_en = (
        "Should patterns be searched across rests?\n\n"
        "[yes = rests are ignored in the pattern search] (yes/no): "
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### enter custom rhythm

# In[ ]:


def text_patternSearch_enter_customRhythm():
    text_de = (
        "Bitte geben Sie nachfolgend einen selbstgewählten Rhythmuswert ein.\n\n"
        "Hinweis 1: 1.0 = Viertelnote; 2.0 = Halbe Note etc.\n\n"
        "Komplexe Rhythmen, z.B. Triolen/Quintolen, können als Brüche eingegeben werden: z.B. 1/3 oder 1/5\n\n"
        "Siehe hierzu: https://web.mit.edu/music21/doc/usersGuide/usersGuide_19_duration2.html\n\n"
        "Hinweis 2: Es sind nur Zahlen, z.B. '1.0', '1' oder '1/3' zulässig.\n\n"
        "Eingabe: "
    )

    text_en = (
        "Please enter a custom rhythm value below.\n\n"
        "Note 1: 1.0 = quarter note; 2.0 = half note etc.\n\n"
        "Complex rhythms, e.g. triplets/quintuplets, can be entered as fractions: e.g. 1/3 or 1/5\n\n"
        "See also: https://web.mit.edu/music21/doc/usersGuide/usersGuide_19_duration2.html\n\n"
        "Note 2: Only numbers, e.g. '1.0', '1' or '1/3' are permitted.\n\n"
        "Input: "
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Menu

# ### Selection

# #### Headers

# In[ ]:


def text_menu_selection_header():
    text_de = "Bitte treffen Sie eine Auswahl:"

    text_en = "Please select:"

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Input

# In[ ]:


def text_menu_selection_input():
    text_de = "Welcher Menüpunkt soll ausgeführt werden? (<Nr. des Menüpunkts>): "

    text_en = "Which menu item should be executed? (<No. of menu item>): "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Repeat

# In[ ]:


def text_menu_selection_repeat():
    text_de = "Möchten Sie das Tool mit einer anderen Notenauswahl wiederholen? 'nein' => Hauptmenü (ja/nein): "

    text_en = "Would you like to repeat the tool with a different score selection? 'no' => main menu (yes/no): "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### No previous selection

# In[ ]:


def text_menu_selection_noPreviousSelection():
    text_de = (
        "Es liegt noch keine Notenauswahl vor, auf die zurückgegriffen werden kann.\n\n"
        "Bitte wählen Sie aus Menüpunkt 1 oder 2."
    )

    text_en = (
        "There is not yet a selection of notes that can be used.\n\n"
        "Please choose from menu item 1 or 2."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Headers

# In[5]:


def text_menu_headers(identifier):
    dict_de = {
        "open_mainmenu_individualPiece": "-- Hauptmenü Einzelwerk --",
        "open_submenu_individualPiece_files": "-- Untermenü Einzelwerk (Files) --",
        "open_submenu_individualPiece_statisticalAnalyses": "-- Untermenü Einzelwerk (statistische Analysen) --",
        "open_submenu_individualPiece_statisticalAnalyses_visualizations": "-- Untermenü Einzelwerk (statistische Analysen - Darstellungen zweidimensionaler Häufigkeitsverteilungen) --",
        "open_submenu_individualPiece_visualizations": "-- Untermenü Einzelwerk (Darstellungen) --",
        "open_submenu_individualPiece_patternSearch": "-- Untermenü Einzelwerk (Mustersuche) --",
        "open_submenu_individualPiece_settings": "-- Untermenü Einzelwerk (Einstellungen) --ACHTUNG: Erstellen Sie vor der Bearbeitung der Environment-Datei eine Sicherungskopie!",
        "open_startmenu": "-- Startmenü --",
        "show_environmentFile_settings": "Ihre Environment-Datei 'music21-settings' ist wie folgt definiert:",
        "open_submenu_patternSearch": "Bitte geben Sie hier das zur Mustersuche verwendete Noten-/Rhythmusmuster (1.0 = Viertelnote) ein:",
        "select_score_filePath": "-- Auswahl einer Notendatei zur weiteren Analyse --",
        "select_score_completeOrIndividualVoice": "-- Auswahl der gesamten Partitur oder einer Einzelstimme --",
        "select_bars": "-- Auswahl der Takte --",
        "show_names_individualVoices": "-- Allgemeine Informationen (Stimmennamen) --",
        "show_score_metadata": "-- Allgemeine Informationen (Metadaten) --",
        "show_resultslist": "-- Ergebnisse --",
        "helpers_name_individualVoices": "-- Konfiguration: Stimmnamen --",
    }

    dict_en = {
        "open_mainmenu_individualPiece": "-- main menu individual piece --",
        "open_submenu_individualPiece_files": "-- Submenu individual piece (Files) --",
        "open_submenu_individualPiece_statisticalAnalyses": "-- Submenu individual piece (statistical analysis) --",
        "open_submenu_individualPiece_statisticalAnalyses_visualizations": "-- Submenu individual piece (statistical analyzes - representations of two-dimensional frequency distributions) --",
        "open_submenu_individualPiece_visualizations": "-- Submenu individual piece (Visualisations) --",
        "open_submenu_individualPiece_patternSearch": "-- Submenu individual piece (Pattern search) --",
        "open_submenu_individualPiece_settings": "-- Submenu individual piece (Settings) --ATTENTION: Make a backup copy before editing the environment file!",
        "open_startmenu": "-- Start menu --",
        "show_environmentFile_settings": "Your environment file 'music21-settings' is defined as follows:",
        "open_submenu_patternSearch": "Please enter the note / rhythm pattern (1.0 = quarter) used for the pattern search here.",
        "select_score_filePath": "-- Selection of a score file for further analysis --",
        "select_score_completeOrIndividualVoice": "-- Selection of the entire score or a single part --",
        "select_bars": "-- Selection of bars --",
        "show_names_individualVoices": "-- General information (part names) --",
        "show_score_metadata": "-- General information (Metadata) --",
        "show_resultslist": "-- Results --",
        "helpers_name_individualVoices": "-- Configuration: part names --",
    }

    if LANGUAGE == "DE":
        return dict_de[identifier]

    elif LANGUAGE == "EN":
        return dict_en[identifier]


# ### Exception

# #### Selection out of range

# In[ ]:


def text_menu_exception_selectionOutOfRange(max_value):
    text_de = (
        "Der eingegebene Wert muss eine Zahl zwischen 1 und "
        + str(max_value)
        + " sein."
    )

    text_en = (
        "The entered value must be a number between 1 and " +
        str(max_value) + "."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Description

# #### Without Explenation

# In[ ]:


def text_menu_headers_withoutExplenation():
    list_de = ["Nr.", "Menüpunkt"]

    list_en = ["No.", "Menu item"]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### With Explenation

# In[ ]:


def text_menu_headers_withExplenation():
    list_de = ["Nr.", "Menüpunkt", "<Erläuterung>"]

    list_en = ["No.", "Menu item", "<Explanation>"]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ## Score

# ### Selection

# In[ ]:


def text_score_selection():
    text_de = (
        "Bitte wählen Sie eine Notendatei aus, die sie in das Programm laden möchten. Verwendet Sie falls möglich eine .xml-Datei.\n\n"
        "NOTENDATENBANK:\n\n"
        "Die Notendatenbank umfasst mehrere Tausend nach Komponisten geordnete Notendateien, die für eigene Analyseprojekte,\n"
        "insbesondere für Korpusanalysen, verwendet werden können. Die Noten stammen aus einer Reihe von im Internet frei verfügbaren\n"
        "Online-Datenbanken sowie weiteren Forschungsdatenbanken, vgl. Liste der Datenbanken. Alle Dateien können unter Beachtung der\n"
        "Creative-Commons-Lizenzierung verwendet werden. Alle Notendateien wurden ins MusicXML-Format konvertiert.\n\n"
        "Achtung: Die Qualität der einzelnen MusicXML-Dateien wurde nicht überprüft und kann daher stark variieren; Fehler sind nicht ausgeschlossen.\n\n"
        'Notendatenbank: "<https://analyse.hfm-weimar.de/doku.php?id=komponisten">\n\n'
        "SUBKORPUS DER NOTENDATENBANK:\n\n"
        "Der Subkorpus der Notendatenbank entspricht einem (subjekt geprägten) chronologischen Gang durch die europäische Musikgeschichte\n"
        "anhand verschiedener Komponisten und Kompositionen (s. Inhaltsverzeichnis rechts).\n"
        "Dabei wurden vier verschiedene Gattungen berücksichtigt:\n\n"
        " - Vokalsatz,\n"
        " - Piano solo,\n"
        " - Streichquartett und Sinfonie.\n\n"
        "Alle MusicXML-Dateien wurden auf ihre Qualität und auf mögliche Fehler geprüft. In dieser Auswahl sind alle Noten enthalten,\n"
        "die in den Modulen zur Notenanalyse und den entsprechenden Aufgaben verwendet werden.\n\n"
        "Subkorpus der Notendatenbank: <https://analyse.hfm-weimar.de/doku.php?id=notenauswahl#subkorpus_der_notendatenbank>\n\n"
        "Kopieren Sie sich die URL der gewünschten Datei (Rechtsklick > Link kopieren) und fügen Sie diesen nachfolgend ein.\n\n"
        "Alternativ können Sie auch eine auf Ihrem Rechner lokal gespeicherte Datei öffnen. Ziehen Sie diese einfach per Drag & Drop\n"
        "in das Fenster des Terminals.\n\n"
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )
    text_en = (
        "Please select a note file that you want to load into the program. Use an .xml file if possible.\n\n"
        "SHEET MUSIC DATABASE:\n\n"
        "The sheet music database includes several thousand sheet music files listed by composer name, which can be used for\n"
        "your own analysis projects, especially for corpus analysis. The scores come from a number of online databases freely\n"
        "available on the Internet as well as other research databases, cf. list of databases. All files can be used in\n"
        "compliance with Creative Commons licensing.\n\n"
        "Attention: The quality of the individual MusicXML files have not been checked and can therefore vary greatly; errors are not excluded.\n\n"
        "Sheet Music Database: <https://analyse.hfm-weimar.de/doku.php?id=en:datenbank>\n\n"
        "SUBCORPUS OF THE SHEET MUSIC DATABASE:\n\n"
        "This subcorpus of the sheet music database corresponds to a (subjective) chronological walk through European music history\n"
        "on the basis of various composers and compositions (see table of contents on the right).\n"
        "Four different genres were considered:\n\n"
        " - Vocal,\n"
        " - Piano solo,\n"
        " - String quartet and Symphony.\n\n"
        "All MusicXML-files were checked for quality and possible errors. This selection contains all scores used in\n"
        "the two modules for score analysis and the corresponding tasks.\n\n"
        "Subcorpus of the sheet music database: <https://analyse.hfm-weimar.de/doku.php?id=en:notenauswahl>\n\n"
        "Copy the URL of the desired file (right click > copy link) and paste it below.\n\n"
        "Alternatively, you can also open a file saved locally on your computer. Simply drag and drop the file into the terminal window.\n\n"
        "Be careful not to put any spaces at the end of the path."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Successful

# In[ ]:


def text_score_selectionSuccessful(time):
    text_de = (
        "Datei erfolgreich eingelesen.\n\n"
        "Zum Öffnen benötigte Zeit: " + str(time) + "s"
    )

    text_en = (
        "File successfully loaded. \n\n" "Time required to open: " +
        str(time) + "s"
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Exception

# In[ ]:


def text_score_selectionException():
    text_de = (
        "Geben Sie den Pfad/die URL erneut ein und achten Sie auf die richtige Schreibweise.\n\n"
        "Falls Sie die URL nicht öffnen können, speichern Sie die Datei Lokal (Rechtsklick > Ziel speichern unter..) und öffnen Sie die heruntergeladene Datei lokal über deren Pfad.\n\n"
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )

    text_en = (
        "Re-enter the path / URL and make sure that the spelling is correct.\n\n"
        "If you cannot open the URL, save the file locally (right click > Save target as ..) and open the downloaded file locally using its path.\n\n"
        "Be careful not to put any spaces at the end of the path."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Bars

# ### Selection start (input)

# In[ ]:


def text_score_barsSelectionStart(number_of_bars, selected_score):
    text_de = (
        "Anzahl Takte: " + str(number_of_bars) + " Takte\n\n"
        "Notenauswahl: " + str(selected_score) + "\n\n"
        "Taktauswahl ab Takt: [Nr. des Taktes] "
    )

    text_en = (
        "Number of bars: " + str(number_of_bars) + " bars\n\n"
        "Score selection: " + str(selected_score) + "\n\n"
        "Selection starting from bar: [No. of the bar] "
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Selection send (input)

# In[ ]:


def text_score_barsSelectionEnd(number_of_bars, selected_score, bars_selection_start):
    text_de = (
        "Anzahl Takte: " + str(number_of_bars) + " Takte\n\n"
        "Notenauswahl: " + str(selected_score) + "\n\n"
        "Taktauswahl ab Takt: " + str(bars_selection_start) + "\n\n"
        "Taktauswahl bis einschließlich Takt: "
    )

    text_en = (
        "Number of bars: " + str(number_of_bars) + " bars\n\n"
        "Score selection: " + str(selected_score) + "\n\n"
        "Selection starting from bar: " + str(bars_selection_start) + "\n\n"
        "Selection endling including bar: "
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Exception

# #### Not a number

# In[ ]:


def text_score_bars_exception_notNumber():
    text_de = "Bitte eine positive Zahl ohne Buchstaben/Sonderzeichen eingeben."

    text_en = "Please enter a positive number without letters/special characters."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Out of range

# In[ ]:


def text_score_bars_exception_outOfRange(start, end):
    text_de = (
        "Der eingegebene Wert muss zwischen "
        + str(start)
        + " und "
        + str(end)
        + "liegen."
    )

    text_en = (
        "The entered value must be between " +
        str(start) + " and " + str(end) + "."
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Metadata

# ### Part Names

# In[4]:


def text_metadata_partsNames():
    text_de = "Namen der Einzelstimmen:"

    text_en = "Names of the individual parts/voices:"

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Give name

# In[ ]:


def text_metadata_partsNames_chooseName(parts_quantity, part_number):
    text_de = (
        "Die Partitur enthält " + str(parts_quantity) + " Stimmen.\n\n"
        "Bitte ordnen Sie den Einzelstimmen eindeutige Bezeichnungen zu (z.B. Violine I, Violine II etc.).\n\n"
        "Über diese Namen greifen Sie bei Verwendung der nachfolgenden Tools direkt auf die jeweiligen Einzelstimmen zu.\n\n"
        "Beginnen Sie bitte bei der höchsten Stimme im Notensystem. Es folgt dann jeweils die im Notensystem direkt darunterliegende.\n\n"
        "Benenne Stimme " + str(part_number) + ": "
    )

    text_en = (
        "The score contains " + str(parts_quantity) + " parts.\n\n"
        "Please assign unique names to the individual parts/voices (e.g. violin I, violin II, etc.).\n\n"
        "You can use these names to access the individual parts/voices directly when using the following tools.\n\n"
        "Please start with the highest voice/part in the staff. This is followed by the one directly below.\n\n"
        "Name part " + str(part_number) + ": "
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ##### Declined

# In[ ]:


def text_metadata_partsNames_chooseName_notUnique():
    text_de = "Name bereits vergeben. Wählen Sie einen eindeutigen Namen."

    text_en = "Name already given. Choose a unique name."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Check entered name

# In[ ]:


def text_metadata_partsNames_checkEnteredName(
    parts_quantity, part_number, name_entered
):
    text_de = (
        "Die Partitur enthält " + str(parts_quantity) + " Stimmen.\n\n"
        "Bitte ordnen Sie den Einzelstimmen eindeutige Bezeichnungen zu (z.B. Violine I, Violine II etc.).\n\n"
        "Über diese Namen greifen Sie bei Verwendung der nachfolgenden Tools direkt auf die jeweiligen Einzelstimmen zu.\n\n"
        "Beginnen Sie bitte bei der höchsten Stimme im Notensystem. Es folgt dann jeweils die im Notensystem direkt darunterliegende.\n\n"
        "Stimme " + str(part_number) + ": " + str(name_entered)
    )

    text_en = (
        "The score contains " + str(parts_quantity) + " parts.\n\n"
        "Please assign unique names to the individual parts/voices (e.g. violin I, violin II, etc.).\n\n"
        "You can use these names to access the individual parts/voices directly when using the following tools.\n\n"
        "Please start with the highest voice/part in the score. This is followed by the one directly below.\n\n"
        "Part " + str(part_number) + ": " + str(name_entered)
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Available Metadata

# In[ ]:


def text_metadata_availableMetadata(number):
    text_de = "Anzahl enthaltener Metadaten: " + str(number)

    text_en = "Number of metadata contained: " + str(number)

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### No metadata

# In[ ]:


def text_metadata_availableMetadata_noMetadataAvailable():
    text_de = "Die ausgewählte Notendatei enthält keine Metadaten!"

    text_en = "The selected scores do not contain any metadata!"

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ## Analysis

# ### Score selection

# In[ ]:


def text_analysis_scoreSelection():
    list_de = [
        "Wählen Sie bitte im nachfolgenden Menü die zu analysierenden Noten aus (Notendatei 1).",
        "Wählen Sie bitte im nachfolgenden Menü die zu analysierenden Noten aus (Notendatei 2)",
    ]

    list_en = [
        "Please select the scores to be analyzed in the following menu (scores file 1).",
        "Please select the scores to be analyzed in the following menu (scores file 2).",
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ### measures

# In[ ]:


def text_analysis_measures():
    text_de = "T. "

    text_en = "Meas. "

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# ### Notes

# #### Intervals

# In[ ]:


def text_analysis_notes_intervals():
    text_de = "Hinweis 1: Auf- und absteigende Intervalle werden gesondert gezählt.\nHinweis 2: Intervalle, zwischen denen Pausen stehen werden nicht mitgezählt."

    text_en = "Note 1: ascending and descending intervals are counted separately. Note 2: Intervals between which there are rests are not counted."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Function: Melodik_Melodieverlauf_visualization_lineGraph

# In[6]:


def text_analysis_notes_melody_melodicProgression_visualization_lineGraph():
    text_de = (
        "Hinweis 1: Auswahl auf einzelne Taktausschnitte der vollständigen Partitur beschränkt.\n\n"
        "Hinweis 2: Die ausgewählten Abschnitte müssen in allen Einzelstimmen durchgängig einstimmig sein!\n\n"
        "Hinweis 3: Die Taktauswahl muss mindestens zwei Takte umfassen!"
    )

    text_en = (
        "Note 1: Selection limited to individual bar excerpts from the full score.\n\n"
        "Note 2: The selected sections must be consistently monodic in all individual parts/voices!\n\n"
        "Note 3: The measure selection must include at least two measures!"
    )

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# #### Function: text_analysis_notes_predefinedVisualizations_Dolan

# In[ ]:


def text_analysis_notes_predefinedVisualizations_Dolan():
    text_de = "Hinweis: Bei manchen Notendateien gelten die Dynamikbezeichnungen einer Stimme für die komplette Partitur."

    text_en = "Note: With some sheet music files, the dynamics of a part apply to the entire score."

    if LANGUAGE == "DE":
        return text_de

    elif LANGUAGE == "EN":
        return text_en


# # Initialization

# ## Importing required modules

# In[12]:

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

    Input = input(text_general_terminateProgram())
    print("")


# ## Environment File

# ### Check

# In[13]:


def check_environmentFile():
    try:
        us = environment.UserSettings()

        environmentFile_path = us.getSettingsPath()

        if os.path.exists(environmentFile_path) == False:
            loopDone = False

            while not loopDone:
                clear_screen()

                input_text = input(text_environmentFile_createNewFile(environmentFile_path))
                print("")

                if Rueckgabe_Wahrheitswert_ja_1(input_text):
                    clear_screen()

                    try:
                        us.create()

                        us["autoDownload"] = "allow"

                        print(
                            text_environmentFile_createNewFile_created(
                                us.getSettingsPath()
                            )
                        )
                        print()

                        input_text = input(text_general_proceed())
                        print("")

                        clear_screen()

                        EnvironmentFile_enterPath_MuseScore3()

                        environmentFile_enterPath_scratchFolder()

                        loopDone = True

                    except Exception as e:
                        print(text_exception_general(
                            e, sys._getframe().f_code.co_name))
                        print("")

                        loopDone = True

                        input_text = input(text_general_proceed())
                        print("")

                elif Rueckgabe_Wahrheitswert_nein_0(input_text):
                    clear_screen()

                    print(text_environmentFile_createNewFile_noFileCreated())
                    print("")

                    loopDone = True

                    input_text = input(text_general_proceed())
                    print("")

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loopDone = False

                    input_text = input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input_text = input(text_general_proceed())
        print("")

    clear_screen()


# ### Path input MuseScore3

# In[14]:


def EnvironmentFile_enterPath_MuseScore3():
    loopDone = False

    while not loopDone:
        clear_screen()

        try:
            print(text_environmentFile_configure_musescorePath())
            print("")

            MuseScore3_Pfad_Input = str(input(text_general_enter_newPath()))
            print("")

            MuseScore3_Pfad = MuseScore3_Pfad_Input.replace('"', "")

            print(text_general_show_enteredPath(MuseScore3_Pfad))
            print("")

            loop2Done = False

            while not loop2Done:
                Input = input(text_general_checkEntry())
                print("")

                if Rueckgabe_Wahrheitswert_ja_1(Input):
                    loopDone = True
                    loop2Done = True

                    us["musescoreDirectPNGPath"] = MuseScore3_Pfad

                    us["musicxmlPath"] = MuseScore3_Pfad

                    print("\n")

                    clear_screen()

                elif Rueckgabe_Wahrheitswert_nein_0(Input):
                    loopDone = False
                    loop2Done = True

                    clear_screen()

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop2Done = False

                    Input = input(text_general_proceed())
                    print("")

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")

            loopDone = False

    clear_screen()


# ### Path input Scratch folder

# In[15]:


def environmentFile_enterPath_scratchFolder():
    loopDone = False

    while not loopDone:
        clear_screen()

        try:
            print(text_environmentFile_configure_scratchPath())
            print("")

            Scratch_Ordner_Pfad_Input = str(
                input(text_general_enter_newPath()))
            print("")

            Scratch_Ordner_Pfad = Scratch_Ordner_Pfad_Input.replace('"', "")

            print(text_general_show_enteredPath(Scratch_Ordner_Pfad))
            print("")

            loop2Done = False

            while not loop2Done:
                Input = input(text_general_checkEntry())
                print("")

                if Rueckgabe_Wahrheitswert_ja_1(Input):
                    loopDone = True
                    loop2Done = True

                    us["directoryScratch"] = Scratch_Ordner_Pfad

                    clear_screen()

                elif Rueckgabe_Wahrheitswert_nein_0(Input):
                    loopDone = False
                    loop2Done = True

                    clear_screen()

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop2Done = False

                    Input = input(text_general_proceed())
                    print("")

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")

            loopDone = False

    clear_screen()


# ## Constants


# ### Language

global LANGUAGE

LANGUAGE = "EN"

# ### Environment File Settings

# In[16]:


us = environment.UserSettings()

EnvironmentFile_settings = [
    ["autoDownload", "autoDownload", str(us["autoDownload"])],
    ["braillePath", "braillePath", str(us["braillePath"])],
    ["debug", "debug", str(us["debug"])],
    ["directoryScratch", "directoryScratch", str(us["directoryScratch"])],
    ["graphicsPath", "graphicsPath", str(us["graphicsPath"])],
    ["ipythonShowFormat", "ipythonShowFormat", str(us["ipythonShowFormat"])],
    ["lilypondBackend", "lilypondBackend", str(us["lilypondBackend"])],
    ["lilypondFormat", "lilypondFormat", str(us["lilypondFormat"])],
    ["lilypondPath", "lilypondPath", str(us["lilypondPath"])],
    ["lilypondVersion", "lilypondVersion", str(us["lilypondVersion"])],
    ["localCorporaSettings", "localCorporaSettings", str(us["localCorporaSettings"])],
    ["localCorpusPath", "localCorpusPath", str(us["localCorpusPath"])],
    ["localCorpusSettings", "localCorpusSettings", str(us["localCorpusSettings"])],
    ["manualCoreCorpusPath", "manualCoreCorpusPath", str(us["manualCoreCorpusPath"])],
    ["midiPath", "midiPath", str(us["midiPath"])],
    ["musescoreDirectPNGPath", "musescoreDirectPNGPath", str(us["musescoreDirectPNGPath"])],
    ["musicxmlPath", "musicxmlPath", str(us["musicxmlPath"])],
    ["pdfPath", "pdfPath", str(us["pdfPath"])],
    ["showFormat", "showFormat", str(us["showFormat"])],
    ["vectorPath", "vectorPath", str(us["vectorPath"])],
    ["warnings", "warnings", str(us["warnings"])],
    ["writeFormat", "writeFormat", str(us["writeFormat"])],
]


# # Helper Programs

# ## Without User Input

# ### Playing back a music file (MIDI)

# In[17]:


def helper_playback_MIDI():
    selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    print(text_general_close_audioPlayer())
    print("")

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore.show("midi")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")

    # --- Oberhalb: Code des Tools ---

    # --- Nachfolgend: Fragt den User, ob das Tool mit einer neuen Notenauswahl wiederholt werden soll

    Menue_Frage_Tool_Wiederholen(helper_playback_MIDI)


# ### Erhalte Key zu Value

# In[18]:


def Erhalte_Key_zu_Value(val, dictionary):
    try:
        for key, value in dictionary.items():
            if val == value:
                return key

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Sortieren eines Dictionaries nach Größe der Values (aufsteigend)

# In[19]:


# Quelle: Example- Counting Numbers in a List, https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637


def count(num_list):
    try:
        count_dict = {}

        for num in num_list:
            count_dict[num] = num_list.count(num)

        return dict(sorted(count_dict.items(), key=lambda x: x[1]))

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Ausgabe eines Textes in gleichlangen Zeilen

# In[20]:


def gleichmaessige_textOutput(Input_Text, Input_Teiler):
    try:
        n = 0

        while (n + Input_Teiler) < len(Input_Text) + 1:
            Position_letztes_Leerzeichen = Input_Text.rfind(
                " ", n, n + Input_Teiler)

            if Position_letztes_Leerzeichen > 0:
                print(Input_Text[n:Position_letztes_Leerzeichen])

                n = Position_letztes_Leerzeichen + 1

            else:
                print(
                    "Error: select larger line length; Line length is smaller than longest word."
                )

                break

        if len(Input_Text[n: len(Input_Text)]) < Input_Teiler:
            print(Input_Text[n: len(Input_Text)])

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Bildschirm leeren

# In[21]:


def clear_screen():
    try:
        if name == "nt":
            _ = system("cls")

        # for mac and linux(here, os.name is 'posix')

        else:
            _ = system("clear")

        print(text_general_title())

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_terminateProgram())
        print("")

        terminateProgram()


# ### Environment

# #### Pfad

# In[9]:


def environmentFile_path():
    clear_screen()

    try:
        us = environment.UserSettings()

        print(text_environmentFile_showPath(us.getSettingsPath()))
        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")


# #### Einstellungen Anzeigen

# In[23]:


def show_environmentFile_settings():
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        us = environment.UserSettings()

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(EnvironmentFile_settings, 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input_Menueauswahl = input(text_general_proceed())
    print("")

    clear_screen()


# #### Einstellungen (Neukonfiguration)

# In[1]:


def EnvironmentFile_settings_reconfigure():
    try:
        us = environment.UserSettings()

        environmentFile_path = us.getSettingsPath()

        if os.path.exists(environmentFile_path):
            loopDone = False

            while not loopDone:
                clear_screen()

                print(text_environmentFile_showPath(environmentFile_path))
                print("")

                Input = input(text_environmentFile_reconfigure_askDelete())
                print("")

                if Rueckgabe_Wahrheitswert_ja_1(Input):
                    os.remove(environmentFile_path)

                    print(text_environmentFile_reconfigure_deleted())
                    print("")

                    Input = input(text_general_proceed())
                    print("")

                    clear_screen()

                    us.create()

                    us["autoDownload"] = "allow"

                    print(
                        text_environmentFile_createNewFile_created(
                            us.getSettingsPath())
                    )
                    print("")

                    Input = input(text_general_proceed())
                    print("")

                    clear_screen()

                    EnvironmentFile_enterPath_MuseScore3()

                    environmentFile_enterPath_scratchFolder()

                    loopDone = True

                elif Rueckgabe_Wahrheitswert_nein_0(Input):
                    loopDone = True

                    print(text_environmentFile_reconfigure_notDeleted())
                    print()

                    Input = input(text_general_proceed())
                    print("")

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    Input = input(text_general_proceed())
                    print("")

                    loopDone = False

        else:
            loopDone = False

            while not loopDone:
                clear_screen()

                Input = input(text_environmentFile_createNewFile(us.getSettingsPath()))
                print("")

                if Rueckgabe_Wahrheitswert_ja_1(Input):
                    us.create()

                    us["autoDownload"] = "allow"

                    print(
                        text_environmentFile_createNewFile_created(
                            us.getSettingsPath())
                    )
                    print("")

                    Input = input(text_general_proceed())
                    print("")

                    clear_screen()

                    EnvironmentFile_enterPath_MuseScore3()

                    environmentFile_enterPath_scratchFolder()

                    loopDone = True

                elif Rueckgabe_Wahrheitswert_nein_0(Input):
                    print(text_environmentFile_createNewFile_noFileCreated())
                    print("")

                    Input = input(text_general_proceed())
                    print("")

                    loopDone = True

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loopDone = False

                    Input = input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Rückgabe Wahrheitswert

# #### ja / 1

# In[25]:


def Rueckgabe_Wahrheitswert_ja_1(Input):
    if Input == "ja" or Input == "1" or Input == "yes":
        return True

    else:
        return False


# #### nein / 0

# In[26]:


def Rueckgabe_Wahrheitswert_nein_0(Input):
    if Input == "nein" or Input == "0" or Input == "no":
        return True

    else:
        return False


# #### is number

# In[ ]:


def Rueckgabe_Wahrheitswert_is_number(Input):
    try:
        float(Input)

        return True

    except:
        try:
            m, n = map(float, Input.split("/"))

            return True

        except:
            return False


# ### Programm beenden

# In[27]:


def terminateProgram():
    exit()


# ### CSV-Export

# In[28]:


def export_as_csv(
    data,
    columns,
    save_at,
    do_print=False,
    do_return_pd=False,
    sep=";",
    index=False,
    header=True,
):
    # data = [[Zeile1 Spalte1, Zeile1 Spalte2], [Zeile2 Spalte1, Zeile2 Spalte2] ...]

    try:
        """
        data (list): nd array as list
        columns (list): list of column header in strings
        save_at (str) : path the csv to be saved
        """

        pd_data = pd.DataFrame(data, columns=columns)
        pd_data.to_csv(save_at, sep=";", index=index, header=header)
        if do_print:
            display(HTML(pd_data.to_html(index=False)))
        if do_return_pd:
            return pd_data

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Liste als String

# In[31]:


def Liste_als_String(Liste):
    try:
        string = " ".join(
            [
                str(item)
                .replace("'", "")
                .replace(" ", "")
                .replace(",", ": ")
                .replace("[", "")
                .replace("]", "")
                for item in Liste
            ]
        )

        return string

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## Mit Input

# ### Auswahl des Pfades/der URL einer Notendatei

# In[32]:


def select_score_filePath():
    try:
        # Erstellen einer globalen Variabel 'Partitur', auf die von jeder Stelle im Programm aus zugegriffen werden kann.

        global Partitur

        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        # Ausgabe eines Auswahlmenüs, das den Benutzer zwischen einer "Beispiel-Datei" und einer "Eigenen Auswahl" auswählen lässt (s. .

        Auswahl = open_submenu_Daten_mit_Info(
            menue_entries_score_selection())

        if Auswahl == "Beispiel-Datei":
            Partitur = converter.parse(
                "https://analyse.hfm-weimar.de/database/02/PrJode_Jos0602_COM_1-5_MissaLhomm_002_00066.xml"
            )

        else:
            loopDone = False

            while not loopDone:
                clear_screen()

                print(menu_header)
                print("")

                print(text_score_selection())
                print("")

                NotenDatei_Pfad_Input = input(text_general_enter_newPath())
                print("")

                try:
                    loop2Done = False

                    while not loop2Done:
                        clear_screen()

                        print(menu_header)
                        print("")

                        print(text_score_selection())
                        print("")

                        NotenDatei_Pfad = NotenDatei_Pfad_Input.replace(
                            '"', "")

                        print(text_general_show_enteredPath(NotenDatei_Pfad))
                        print("")

                        Input = input(text_general_checkEntry())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            start = time.time()

                            try:
                                Partitur = converter.parse(NotenDatei_Pfad)

                                print(
                                    text_score_selectionSuccessful(
                                        time.time() - start)
                                )
                                print("")

                                Input = input(text_general_proceed())
                                print("")

                                loopDone = True
                                loop2Done = True

                                clear_screen()

                            except Exception as e:
                                print(
                                    text_exception_general(
                                        e, sys._getframe().f_code.co_name
                                    )
                                )
                                print("")

                                print(text_score_selectionException())
                                print("")

                                Input = input(text_general_proceed())
                                print("")

                                loopDone = False
                                loop2Done = True

                                clear_screen()

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone = False
                            loop2Done = True

                            clear_screen()

                            print(menu_header)
                            print("")

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop2Done = False

                            Input = input(text_general_proceed())
                            print("")

                except Exception as e:
                    print(text_exception_general(
                        e, sys._getframe().f_code.co_name))
                    print("")

                    Input = input(text_general_proceed())
                    print("")

        show_score_metadata()

        helpers_name_individualVoices()

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Menüeinträge

# In[ ]:


def menue_entries_score_selection():
    list_de = [
        [
            "Notenauswahl: Beispiel-Datei",
            "Beispiel-Datei",
            "<Datei: Josquin des Prez (1450/55-1521): Missa L'homme arme sexti toni - Kyrie (Online-Datenbank)",
        ],
        [
            "Notenauswahl: Eigene Auswahl",
            "Eigene Auswahl",
            "<Auswahl einer lokal gespeicherten Datei (Pfad)/einer Datei aus der Online-Datenbank (URL)>",
        ],
    ]

    list_en = [
        [
            "Note selection: example file",
            "Beispiel-Datei",
            "<File: Josquin des Prez (1450/55-1521): Missa L'homme arme sexti toni - Kyrie (online database)",
        ],
        [
            "Note selection: custom selection ",
            "Eigene Auswahl",
            "<Selection of a locally saved file (path)/a file from the online database (URL)>",
        ],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ### Benennen der Einzelstimmen

# In[33]:


def helpers_name_individualVoices():
    global Verzeichnis_Einzelstimmen

    global Verzeichnis_Partitur_und_Einzelstimmen

    try:
        Stimmen_Namen = ["none"] * len(Partitur.parts)
        Stimmen_Data = ["none"] * len(Partitur.parts)

        n = 0

        while n < len(Partitur.parts):
            Stimmen_Data[n] = Partitur.parts[n]

            n = n + 1

        Auswahl = open_submenu_Daten_mit_Info(
            modul_navigation_Benennung_Einzelstimmen()
        )

        if Auswahl == "Darstellung_MuseScore":
            print(text_general_close_museScore3())
            print()

            Partitur.show()

            helpers_name_individualVoices()

        elif Auswahl == "benutzerdefiniert":
            loop1Done = False

            while not loop1Done:
                n = 0

                while n < len(Partitur.parts):
                    clear_screen()

                    menu_header = text_menu_headers(sys._getframe().f_code.co_name)

                    print(menu_header)
                    print("")

                    Input_Stimmen_Namen = input(
                        text_metadata_partsNames_chooseName(
                            len(Partitur.parts), n + 1)
                    )
                    print("")

                    if not Input_Stimmen_Namen in Stimmen_Namen:
                        loop2Done = False

                        while not loop2Done:
                            clear_screen()

                            menu_header = text_menu_headers(
                                sys._getframe().f_code.co_name)

                            print(menu_header)
                            print("")

                            print(
                                text_metadata_partsNames_checkEnteredName(
                                    len(Partitur.parts), n +
                                    1, Input_Stimmen_Namen
                                )
                            )
                            print("")

                            Input = input(text_general_checkEntry())
                            print("")

                            if Rueckgabe_Wahrheitswert_ja_1(Input):
                                Stimmen_Namen[n] = Input_Stimmen_Namen

                                n = n + 1

                                loop2Done = True

                            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                                loop2Done = True

                            else:
                                print(text_general_input_RestrictedToYesAndNo())
                                print("")

                                Input = input(text_general_proceed())
                                print("")

                    else:
                        print(text_metadata_partsNames_chooseName_notUnique())

                        Input = input(text_general_proceed())
                        print("")

                loop2Done = False

                while not loop2Done:
                    clear_screen()

                    menu_header = text_menu_headers(sys._getframe().f_code.co_name)

                    print(menu_header)
                    print("")

                    print(text_metadata_partsNames())
                    print("")

                    menu_header = text_headers(sys._getframe().f_code.co_name)

                    print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

                    Index = 1

                    for i in Stimmen_Namen:
                        print("{:<4} {:<65}".format(Index, i))

                        Index += 1

                    print("")

                    Input = input(text_general_checkEntry())
                    print("")

                    if Rueckgabe_Wahrheitswert_ja_1(Input):
                        clear_screen()

                        loop1Done = True
                        loop2Done = True

                    elif Rueckgabe_Wahrheitswert_nein_0(Input):
                        loop1Done = False
                        loop2Done = True

                        Stimmen_Namen = ["none"] * len(Partitur.parts)

                        clear_screen()

                    else:
                        print(text_general_input_RestrictedToYesAndNo())
                        print("")

                        loop2Done = False

                        Input = input(text_general_proceed())
                        print("")

            # Erstellen eines Dictionarys mit den Namen der Instrumente als 'keys' und den zugehörigen Music21-Pfaden als 'values':

            keys = Stimmen_Namen

            vals = Stimmen_Data

            # Zusammenführen der Listen in ein Dictionary

            Verzeichnis_Einzelstimmen = dict(zip(keys, vals))

            keys.insert(0, "Partitur")

            vals.insert(0, Partitur)

            Verzeichnis_Partitur_und_Einzelstimmen = dict(zip(keys, vals))

            clear_screen()

        elif Auswahl == "generisch":
            if LANGUAGE == "DE":
                n = 0

                while n < len(Partitur.parts):
                    Stimmen_Namen[n] = "Stimme " + str(n + 1)

                    n = n + 1

            elif LANGUAGE == "EN":
                n = 0

                while n < len(Partitur.parts):
                    Stimmen_Namen[n] = "Part " + str(n + 1)

                    n = n + 1

            clear_screen()

            menu_header = text_menu_headers(sys._getframe().f_code.co_name)

            print(menu_header)
            print("")

            print(text_metadata_partsNames())
            print("")

            menu_header = text_headers(sys._getframe().f_code.co_name)

            print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

            Index = 1

            for i in Stimmen_Namen:
                print("{:<4} {:<65}".format(Index, i))

                Index += 1

            print("")

            Input = input(text_general_proceed())
            print("")

            # Erstellen eines Dictionarys mit den Namen der Instrumente als 'keys' und den zugehörigen Music21-Pfaden als 'values':

            keys = Stimmen_Namen

            vals = Stimmen_Data

            # Zusammenführen der Listen in ein Dictionary

            Verzeichnis_Einzelstimmen = dict(zip(keys, vals))

            keys.insert(0, "Partitur")

            vals.insert(0, Partitur)

            Verzeichnis_Partitur_und_Einzelstimmen = dict(zip(keys, vals))

            clear_screen()

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Auswahl Noten

# In[34]:


def select_score_completeOrIndividualVoice():
    global Noten

    global Input_Takte_Anfang

    global Input_Takte_Ende

    global previously_selectedScore

    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        while True:
            clear_screen()

            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_selectedScore())

            if Auswahl == "Komplett":
                # global Noten

                Noten = Partitur

                # global Input_Takte_Anfang

                Input_Takte_Anfang = "1"

                # lobal Input_Takte_Ende

                Anzahl_Takte = len(
                    Partitur.parts[0].getElementsByClass("Measure"))

                Input_Takte_Ende = Anzahl_Takte

                # global previously_selectedScore

                previously_selectedScore = Noten

                return Noten

            elif Auswahl == "Neue_Auswahl":
                # global Noten

                Noten = Menue_Frage_Auswahl_Partitur_oder_Einzelstimme()

                Takte_aus_Noten = select_bars(Noten)

                # global previously_selectedScore

                previously_selectedScore = Takte_aus_Noten

                return Takte_aus_Noten

            elif Auswahl == "Wiederhole_Auswahl":
                clear_screen()

                try:
                    previously_selectedScore

                    return previously_selectedScore

                except:
                    print(text_menu_selection_noPreviousSelection())
                    print("")

                    Input = input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Auswahl Partitur oder Einzelstimme

# In[35]:


def Menue_Frage_Auswahl_Partitur_oder_Einzelstimme():
    try:
        clear_screen()

        global Noten

        Noten = open_submenu_Daten(
            list(Verzeichnis_Partitur_und_Einzelstimmen.items())
        )

        return Noten

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Auswahl Takte

# In[36]:


def select_bars(Noten):
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        Anzahl_Takte = len(Partitur.parts[0].getElementsByClass("Measure"))

        loopDone = False

        while not loopDone:
            clear_screen()

            print(menu_header)
            print("")

            global Input_Takte_Anfang

            Input_Takte_Anfang = input(
                text_score_barsSelectionStart(
                    Anzahl_Takte,
                    Erhalte_Key_zu_Value(
                        Noten, Verzeichnis_Partitur_und_Einzelstimmen),
                )
            )
            print("")

            if str.isdigit(Input_Takte_Anfang):
                Auswahl_Takte_Anfang = int(Input_Takte_Anfang)

                if Auswahl_Takte_Anfang >= 1 and Auswahl_Takte_Anfang <= Anzahl_Takte:
                    loopDone = True

                else:
                    print(text_menu_exception_selectionOutOfRange(Anzahl_Takte))
                    print("")

            else:
                print(text_score_bars_exception_notNumber())
                print("")

        loopDone = False

        while not loopDone:
            clear_screen()

            print(menu_header)
            print("")

            global Input_Takte_Ende

            Input_Takte_Ende = input(
                text_score_barsSelectionEnd(
                    Anzahl_Takte,
                    Erhalte_Key_zu_Value(
                        Noten, Verzeichnis_Partitur_und_Einzelstimmen),
                    Auswahl_Takte_Anfang,
                )
            )
            print("")

            if str.isdigit(Input_Takte_Ende):
                Auswahl_Takte_Ende = int(Input_Takte_Ende)

                if (
                    Auswahl_Takte_Ende >= Auswahl_Takte_Anfang
                    and Auswahl_Takte_Ende <= Anzahl_Takte
                ):
                    loopDone = True

                else:
                    print(
                        text_score_bars_exception_outOfRange(
                            Auswahl_Takte_Anfang, Anzahl_Takte
                        )
                    )
                    print("")

            else:
                print(text_score_bars_exception_notNumber())
                print("")

        return Noten.measures(Auswahl_Takte_Anfang, Auswahl_Takte_Ende)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Wiederholen des Tools mit anderer Notenauswahl

# In[37]:


def Menue_Frage_Tool_Wiederholen(Tool):
    try:
        while True:
            clear_screen()

            Input = input(text_menu_selection_repeat())
            print("")

            if Rueckgabe_Wahrheitswert_ja_1(Input):
                clear_screen()

                Tool()

                break

            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                Input = input(text_general_proceed())
                print("")

                loopDone = False

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Noten Export

# In[38]:


def Noten_speichern():
    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        us = environment.UserSettings()

        Noten_Speichern_Pfad = us["directoryScratch"]

        while True:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_Konvertierung())

            if Auswahl == "XML":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore.write("xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "XML_Akkord":
                selectedScore = select_score_completeOrIndividualVoice()

                selectedScore_chordConnection = selectedScore.chordify()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "XML_Akkord_Generalbass":
                selectedScore = select_score_completeOrIndividualVoice()

                selectedScore_chordConnection = selectedScore.chordify()

                for (
                    item
                ) in selectedScore_chordConnection.recurse().getElementsByClass(
                    "Chord"
                ):
                    item.closedPosition(forceOctave=4, inPlace=True)

                    item.annotateIntervals()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "XML_Akkord_Stufen":
                selectedScore = select_score_completeOrIndividualVoice()

                clear_screen()

                print(text_general_chooseKey())
                print("")

                Input = input(text_general_proceed())
                print("")

                Tonart = open_submenu_Daten(keys_list())

                selectedScore_chordConnection = selectedScore.chordify()

                for (
                    item
                ) in selectedScore_chordConnection.recurse().getElementsByClass(
                    "Chord"
                ):
                    rn = roman.romanNumeralFromChord(item, key.Key(Tonart))

                    item.addLyric(str(rn.figure))

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "MIDI":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".midi"
                )

                mf = selectedScore.write("midi", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".midi"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "TXT_music21":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".txt"
                )

                mf = selectedScore.write("txt", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".txt"))
                print()

                Input = input(text_general_proceed())

            elif Auswahl == "TXT_music21_textline":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".txt"
                )

                mf = selectedScore.write("textline", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".txt"))
                print()

                Input = input(text_general_proceed())

            elif Auswahl == "TXT_BRAILLE":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".txt"
                )

                mf = selectedScore.write("braille", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".txt"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "LILY":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".ly"
                )

                mf = selectedScore.write("lily", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".ly"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "PDF":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName().replace(" ", "_"))
                print("")

                Pfad_Dateiname = str(Noten_Speichern_Pfad) + \
                    "\\" + str(Dateiname)

                mf = selectedScore.write("lily.pdf", fp=str(Pfad_Dateiname))

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".pdf"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "PNG":
                selectedScore = select_score_completeOrIndividualVoice()

                Dateiname = input(text_export_fileName().replace(" ", "_"))
                print("")

                Pfad_Dateiname = str(Noten_Speichern_Pfad) + \
                    "\\" + str(Dateiname)

                mf = selectedScore.write("lily.png", fp=str(Pfad_Dateiname))

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".png"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Darstellung

# #### MuseScore

# In[39]:


def Darstellung_MuseScore():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

        print(text_general_close_museScore3())
        print()

        # --- Unterhalb: Code des Tools ---

        selectedScore.show()

        # --- Oberhalb: Code des Tools ---

        # --- Nachfolgend: Fragt den User, ob das Tool mit einer neuen Notenauswahl wiederholt werden soll

        Menue_Frage_Tool_Wiederholen(Darstellung_MuseScore)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Notenauswahl als Akkordverbindungen speichern (im 'scratch-Ordner')

# In[40]:


def Darstellung_Akkordverbindungen():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore_chordConnection = selectedScore.chordify()

        us = environment.UserSettings()

        Noten_Speichern_Pfad = us["directoryScratch"]

        while True:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_transformierter_Notentext()
            )

            if Auswahl == "Darstellung_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif Auswahl == "Noten_speichern":
                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Repeat":
                Darstellung_Akkordverbindungen()

                break

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Notenauswahl als Akkordverbindungen mit Generalbassbezifferung speichern (im 'scratch-Ordner')

# In[41]:


def Darstellung_Akkordverbindungen_Generalbass():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore_chordConnection = selectedScore.chordify()

        for item in selectedScore_chordConnection.recurse().getElementsByClass(
            "Chord"
        ):
            item.closedPosition(forceOctave=4, inPlace=True)

            item.annotateIntervals()

        us = environment.UserSettings()

        Noten_Speichern_Pfad = us["directoryScratch"]

        while True:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_transformierter_Notentext()
            )

            if Auswahl == "Darstellung_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif Auswahl == "Noten_speichern":
                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Repeat":
                Darstellung_Akkordverbindungen_Generalbass()

                break

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Notenauswahl als Akkordverbindungen mit Stufenbezifferung speichern (im 'scratch-Ordner')

# In[42]:


def Darstellung_Akkordverbindungen_Stufenbezifferung():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        clear_screen()

        print(text_general_chooseKey())
        print("")

        Input = input(text_general_proceed())
        print("")

        Tonart = open_submenu_Daten(keys_list())

        selectedScore_chordConnection = selectedScore.chordify()

        for item in selectedScore_chordConnection.recurse().getElementsByClass(
            "Chord"
        ):
            rn = roman.romanNumeralFromChord(item, key.Key(Tonart))

            item.addLyric(str(rn.figure))

        us = environment.UserSettings()

        Noten_Speichern_Pfad = us["directoryScratch"]

        while True:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_transformierter_Notentext()
            )

            if Auswahl == "Darstellung_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif Auswahl == "Noten_speichern":
                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Repeat":
                Darstellung_Akkordverbindungen_Stufenbezifferung()

                break

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Change language

# In[ ]:


def change_language():
    global LANGUAGE

    if LANGUAGE == "DE":
        LANGUAGE = "EN"

    elif LANGUAGE == "EN":
        LANGUAGE = "DE"


# # Programme: Metadaten

# ## Anzeige der Namen der Einzelstimmen

# In[43]:


def show_names_individualVoices():
    try:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_metadata_partsNames())
        print("")

        menu_header = text_headers(sys._getframe().f_code.co_name)

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        Index = 1

        for i in Verzeichnis_Einzelstimmen.keys():
            print("{:<4} {:<65}".format(Index, i))

            Index += 1

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")


# ## Anzeige der Metadaten einer Notendatei

# In[44]:


def show_score_metadata():
    try:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        loopDone = False

        while not loopDone:
            if len(Partitur.metadata.all()) > 0:
                print(text_metadata_availableMetadata(
                    len(Partitur.metadata.all())))
                print("")

                menu_header = text_headers(sys._getframe().f_code.co_name)

                print("{:<4} {:<30} {:<30}\n".format(
                    menu_header[0], menu_header[1], menu_header[2]))

                Index = 1

                for k, v in dict(Partitur.metadata.all()).items():
                    print("{:<4} {:<30} {:<30}".format(Index, k, v))

                    Index += 1

            else:
                print(text_metadata_availableMetadata_noMetadataAvailable())
                print("")

            loopDone = True

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")


# # Programme: musikalische Parameter

# ## Menüstrukturen

# ### Ohne Grafikexport

# In[ ]:


def Menuestrukturen_Musikalische_Parameter_ohne_Grafikexport(
    function_name, menu_header, Data, notes
):
    try:
        clear_screen()

        show_resultslist(menu_header, Data)
        print("")

        if notes != "":
            print(notes)
            print("")

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                function_name()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                print(text_general_exportToDiagrammUnavailable())
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## Ambitus

# ### Analyse

# In[45]:


def range_Analyse(selectedScore):
    try:
        selectedScore_stripTies = selectedScore.stripTies()

        ambitusAnalyzer = analysis.discrete.Ambitus()

        Ambitus = ambitusAnalyzer.getSolution(selectedScore_stripTies).name

        return Ambitus

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Textausgabe

# In[46]:


def range_analysis_textOutput():
    clear_screen()

    try:
        selectedScore = select_score_completeOrIndividualVoice()

        # --- Unterhalb: Code des Tools ---

        Ambitus = range_Analyse(selectedScore)

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = [[score_label, Ambitus]]

        Menuestrukturen_Musikalische_Parameter_ohne_Grafikexport(
            range_analysis_textOutput, menu_header, Data, notes=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Vergleich

# #### Textausgabe

# In[47]:


def range_comparison_textOutput():
    clear_screen()

    try:
        print(text_analysis_scoreSelection()[0])
        print("")

        Input = input(text_general_proceed())
        print("")

        selectedScore1 = select_score_completeOrIndividualVoice()

        selectedScore1_Name = Noten

        Input_Takte_Anfang_Noten1 = Input_Takte_Anfang

        Input_Takte_Ende_Noten1 = Input_Takte_Ende

        print(text_analysis_scoreSelection()[1])
        print("")

        Input = input(text_general_proceed())
        print("")

        selectedScore2 = select_score_completeOrIndividualVoice()

        selectedScore2_Name = Noten

        Input_Takte_Anfang_Noten2 = Input_Takte_Anfang

        Input_Takte_Ende_Noten2 = Input_Takte_Ende

        range_Noten1 = range_Analyse(selectedScore1)

        range_Noten2 = range_Analyse(selectedScore2)

        Kennung1 = (
            Erhalte_Key_zu_Value(
                selectedScore1_Name, Verzeichnis_Partitur_und_Einzelstimmen
            )
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang_Noten1)
            + "-"
            + str(Input_Takte_Ende_Noten1)
        )

        Kennung2 = (
            Erhalte_Key_zu_Value(
                selectedScore2_Name, Verzeichnis_Partitur_und_Einzelstimmen
            )
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang_Noten2)
            + "-"
            + str(Input_Takte_Ende_Noten2)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = [[Kennung1, range_Noten1], [Kennung2, range_Noten2]]

        Menuestrukturen_Musikalische_Parameter_ohne_Grafikexport(
            range_comparison_textOutput, menu_header, Data, notes=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## Artikulation

# ## Dynamik

# ## Formaler Ablauf (Strukturen)

# ## Harmonik

# ## Intervallstruktur

# ### Intervalltypen (Anzahl)

# In[48]:


def intervalStructure_intervalTypes_quantity(selectedScore):
    try:
        selectedScore_stripTies = selectedScore.stripTies()

        IntervallAnalyzer = analysis.discrete.MelodicIntervalDiversity()

        Intervalltypen_und_quantity = IntervallAnalyzer.countMelodicIntervals(
            selectedScore_stripTies,
            found=None,
            ignoreDirection=False,
            ignoreUnison=False,
        )

        Intervalltypen_quantity = len(Intervalltypen_und_quantity)

        # gibt die Anzahl der vorhandenen Intervalltypen als Integer zurück

        return Intervalltypen_quantity

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Intervalltypen (Unique Intervals)

# In[49]:


def intervalStructure_intervalTypes_UniqueIntervals(selectedScore):
    try:
        selectedScore_stripTies = selectedScore.stripTies()

        IntervallAnalyzer = analysis.discrete.MelodicIntervalDiversity()

        Intervalltypen_und_quantity = IntervallAnalyzer.countMelodicIntervals(
            selectedScore_stripTies,
            found=None,
            ignoreDirection=False,
            ignoreUnison=False,
        )

        Intervalltypen = list(Intervalltypen_und_quantity.keys())

        # gibt die Anzahl der vorhandenen Intervalltypen als Integer zurück

        return Intervalltypen

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# #### Textausgabe

# In[50]:


def intervalStructure_intervalTypes_textOutput():
    clear_screen()

    try:
        selectedScore = select_score_completeOrIndividualVoice()

        # --- Unterhalb: Code des Tools ---

        Intervalltypen_quantity = intervalStructure_intervalTypes_quantity(
            selectedScore)

        Intervalltypen = str(
            intervalStructure_intervalTypes_UniqueIntervals(selectedScore)
        )

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = [[score_label, Intervalltypen_quantity, Intervalltypen]]

        Menuestrukturen_Musikalische_Parameter_ohne_Grafikexport(
            intervalStructure_intervalTypes_textOutput,
            menu_header,
            Data,
            notes=text_analysis_notes_intervals(),
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Intervalltypen (Anzahl)

# #### Textausgabe

# In[51]:


def intervalStructure_intervalTypes_quantity_textOutput():
    clear_screen()

    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        intList = analysis.segmentByRests.Segmenter.getIntervalList(
            selectedScore_stripTies
        )

        Intervalle = count([x.directedName for x in intList])

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Intervalle_Liste = []

        for x, y in Intervalle.items():
            Intervalle_Liste.append([score_label, x, y])

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Intervalle_Liste

        clear_screen()

        show_resultslist(menu_header, Data)
        print("")

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                intervalStructure_intervalTypes_quantity_textOutput()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                print(text_general_exportGraph(Noten_Speichern_Pfad))
                print()

                names = []
                values = []

                for datensatz in Data:
                    names.append(datensatz[1])
                    values.append(datensatz[2])

                plt.bar(names, values)
                plt.ylabel("Frequency")
                plt.xlabel("Interval types")
                plt.title("Interval types and corresponding frequency")

                plt.show()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Intervalltypen (Vergleich)

# #### Textausgabe

# In[52]:


def intervalStructure_intervalTypes_comparison_textOutput():
    clear_screen()

    try:
        print(text_analysis_scoreSelection()[0])
        print("")

        Input = input(text_general_proceed())
        print("")

        selectedScore1 = select_score_completeOrIndividualVoice()

        selectedScore1_stripTies = selectedScore1.stripTies()

        selectedScore1_Name = Noten

        Input_Takte_Anfang_Noten1 = Input_Takte_Anfang

        Input_Takte_Ende_Noten1 = Input_Takte_Ende

        print(text_analysis_scoreSelection()[1])
        print("")

        Input = input(text_general_proceed())
        print("")

        selectedScore2 = select_score_completeOrIndividualVoice()

        selectedScore2_stripTies = selectedScore2.stripTies()

        selectedScore2_Name = Noten

        Input_Takte_Anfang_Noten2 = Input_Takte_Anfang

        Input_Takte_Ende_Noten2 = Input_Takte_Ende

        Liste_alle_Intervalle_Noten1 = (
            analysis.segmentByRests.Segmenter.getIntervalList(
                selectedScore1_stripTies)
        )

        a = count([x.directedName for x in Liste_alle_Intervalle_Noten1])

        Liste_alle_Intervalle_Noten2 = (
            analysis.segmentByRests.Segmenter.getIntervalList(
                selectedScore2_stripTies)
        )

        b = count([x.directedName for x in Liste_alle_Intervalle_Noten2])

        selectedScore1_Bezeichnung = Erhalte_Key_zu_Value(
            selectedScore1_Name, Verzeichnis_Partitur_und_Einzelstimmen
        )

        Kennung1 = (
            selectedScore1_Bezeichnung
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang_Noten1)
            + "-"
            + str(Input_Takte_Ende_Noten1)
        )

        selectedScore2_Bezeichnung = Erhalte_Key_zu_Value(
            selectedScore2_Name, Verzeichnis_Partitur_und_Einzelstimmen
        )

        Kennung2 = (
            selectedScore2_Bezeichnung
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang_Noten2)
            + "-"
            + str(Input_Takte_Ende_Noten2)
        )

        Intervalle_comparison_Liste = []

        for i in a.keys():
            if i in b.keys():
                Differenz = a[i] - b[i]

                if Differenz < 0:
                    Intervalle_comparison_Liste.append(
                        [Kennung1, i, a[i], str(Differenz)]
                    )

                else:
                    Intervalle_comparison_Liste.append(
                        [Kennung1, i, a[i], str(Differenz)]
                    )

            else:
                Intervalle_comparison_Liste.append([Kennung1, i, a[i], a[i]])

        for i in b.keys():
            if i in a.keys():
                Differenz = b[i] - a[i]

                if Differenz < 0:
                    Intervalle_comparison_Liste.append(
                        [Kennung2, i, b[i], str(Differenz)]
                    )

                else:
                    Intervalle_comparison_Liste.append(
                        [Kennung2, i, b[i], str(Differenz)]
                    )

            else:
                Intervalle_comparison_Liste.append([Kennung2, i, b[i], b[i]])

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Intervalle_comparison_Liste

        clear_screen()

        show_resultslist(menu_header, Data)
        print("")

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                intervalStructure_intervalTypes_comparison_textOutput()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                print(text_general_exportGraph(Noten_Speichern_Pfad))
                print()

                interval_1 = []
                frequency_1 = []
                difference_1 = []

                interval_2 = []
                frequency_2 = []
                difference_2 = []

                for datensatz in Data:
                    if datensatz[0] == Kennung1:
                        interval_1.append(datensatz[1])
                        frequency_1.append(int(datensatz[2]))
                        difference_1.append(int(datensatz[3]))

                for datensatz in Data:
                    if datensatz[0] == Kennung2:
                        interval_2.append(datensatz[1])
                        frequency_2.append(int(datensatz[2]))
                        difference_2.append(int(datensatz[3]))

                fig, axs1 = plt.subplots(2, 1)
                axs1[0].bar(interval_1, frequency_1)
                axs1[0].set_title(Kennung1)
                axs1[0].set(xlabel="Interval types", ylabel="Frequency")

                axs1[1].bar(interval_1, difference_1)
                axs1[1].set(
                    xlabel="Interval types", ylabel="Difference to other note selection"
                )

                fig.tight_layout()

                plt.show()

                fig, axs2 = plt.subplots(2, 1)

                axs2[0].set_title(Kennung2)
                axs2[0].bar(interval_2, frequency_2)
                axs2[0].set(xlabel="Interval types", ylabel="Frequency")

                axs2[1].bar(interval_2, difference_2)
                axs2[1].set(
                    xlabel="Interval types", ylabel="Difference to other note selection"
                )

                fig.tight_layout()

                plt.show()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Intervalle Anzahl

# #### Textausgabe

# In[53]:


def intervalStructure_Intervalle_quantity_textOutput():
    clear_screen()

    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        intList = analysis.segmentByRests.Segmenter.getIntervalList(
            selectedScore_stripTies
        )

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = [[score_label, len(intList)]]

        Menuestrukturen_Musikalische_Parameter_ohne_Grafikexport(
            intervalStructure_Intervalle_quantity_textOutput,
            menu_header,
            Data,
            notes=text_analysis_notes_intervals(),
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## Klang

# ## Melodik

# ### Melodieverlauf

# #### Darstellung

# ##### Liniendiagramm

# In[54]:


def Melodik_Melodieverlauf_visualization_lineGraph():
    clear_screen()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    print(text_analysis_notes_melody_melodicProgression_visualization_lineGraph())
    print("")

    Input = input(text_general_proceed())
    print("")

    # --- Unterhalb: Code des Tools ---

    try:
        fig = plt.figure()
        subplot = fig.add_subplot(1, 1, 1)

        Auswahl = select_bars(Partitur)

        for i in range(len(Auswahl.parts)):
            top = Auswahl.parts[i].flat.notes
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

    Input = input(text_general_proceed())
    print("")

    Menue_Frage_Tool_Wiederholen(
        Melodik_Melodieverlauf_visualization_lineGraph)


# ## Metrum

# ### Metrisches Gewicht

# In[55]:


def meter_metricWeight_textOutput():
    clear_screen()

    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        n_list, n_beat_strength = [], []

        l_bs = []

        for n in selectedScore_stripTies.flat.notes:
            c_n = str(n)

            n_list.append(c_n.replace(
                "<music21.note.Note ", "").replace(">", ""))

            n_beat_strength.append(float(n.beatStrength))

        pd_bs = pd.DataFrame(
            np.array([n_list, n_beat_strength]).T, columns=[
                "Notes", "Beat_Strength"]
        )

        n_uni = pd_bs["Notes"].unique()

        bs_uni = pd_bs["Beat_Strength"].unique()

        bs_int_indi = []

        for c_bs_uni in bs_uni:
            l = len(pd_bs.loc[(pd_bs["Beat_Strength"] == c_bs_uni)])

            bs_int_indi.append([score_label, c_bs_uni, l])

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = bs_int_indi

        show_resultslist(menu_header, Data)

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                meter_metricWeight_textOutput()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data,
                    columns=menu_header,
                    save_at=Pfad_Dateiname,
                    do_print=False,
                    do_return_pd=True,
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                print(text_general_exportGraph(Noten_Speichern_Pfad))
                print()

                Pfad_Dateiname = str(Noten_Speichern_Pfad) + \
                    "\\" + "Temp" + ".csv"

                pd_bs_indi_data = export_as_csv(
                    data=Data,
                    columns=menu_header,
                    save_at=Pfad_Dateiname,
                    do_print=False,
                    do_return_pd=True,
                )

                np_bs_indi_data = pd_bs_indi_data.to_numpy()
                fig2 = plt.figure()
                ax2 = fig2.add_subplot(111)
                ax2.bar(
                    np_bs_indi_data[:, 1],
                    np_bs_indi_data[:, 2],
                    width=0.5,
                    color="darkslateblue",
                    alpha=0.8,
                )
                ax2.set_title("Metric weight")
                ax2.set_xlabel("Metric position")
                ax2.set_ylabel("Frequency")

                plt.show()

                os.remove(Pfad_Dateiname)

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Tonklassen auf metrischen Positionen (-- entfernt --)

# def meter_pitchClass_metricPosition_textOutput():
#
#     clear_screen()
#
#     try:
#
#         selectedScore = select_score_completeOrIndividualVoice()
#
#         selectedScore_stripTies = selectedScore.stripTies()
#
#         # --- Unterhalb: Code des Tools ---
#
#         selectedScore_name = str(Erhalte_Key_zu_Value(Noten,Verzeichnis_Partitur_und_Einzelstimmen))
#
#         score_label = selectedScore_name + ', ' + text_analysis_measures() + str(Input_Takte_Anfang) + '-' + str(Input_Takte_Ende)
#
#         n_list, n_beat_strength = [],[]
#
#         l_bs = []
#
#         for n in selectedScore_stripTies.flat.notes:
#
#             c_n = str(n)
#
#             n_list.append(c_n.replace('<music21.note.Note ','').replace('>',''))
#
#             n_beat_strength.append(float(n.beatStrength))
#
#         pd_bs = pd.DataFrame(np.array([n_list, n_beat_strength]).T, columns=['Notes', 'Beat_Strength'])
#
#         n_uni = pd_bs['Notes'].unique()
#
#         bs_uni = pd_bs['Beat_Strength'].unique()
#
#         n_uni_int_dict = dict(zip(n_uni, np.arange(len(n_uni))))
#
#         bs_uni_int_dict = dict(zip(bs_uni, np.arange(len(bs_uni))))
#
#         for c_n_uni in n_uni:
#
#             for c_bs_uni in bs_uni:
#
#                 l = len(pd_bs.loc[(pd_bs['Notes']==c_n_uni) & (pd_bs['Beat_Strength']==c_bs_uni)])
#
#                 l_bs.append([score_label, c_n_uni, c_bs_uni, l])
#
#         menu_header = text_headers(sys._getframe().f_code.co_name)
#
#         Data = l_bs
#
#         show_resultslist(menu_header, Data)
#
#         while True:
#
#             Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())
#
#             if Auswahl == 'Repeat':
#
#                 meter_pitchClass_metricPosition_textOutput()
#
#                 break
#
#             elif Auswahl == 'Export_CSV':
#
#                 us = environment.UserSettings()
#
#                 Noten_Speichern_Pfad = us['directoryScratch']
#
#                 Dateiname = input(text_export_fileName())
#                 print('')
#
#                 Pfad_Dateiname = str(Noten_Speichern_Pfad)+'\\'+str(Dateiname)+'.csv'
#
#                 export_as_csv(data=Data,
#
#                               columns=menu_header,
#
#                               save_at=Pfad_Dateiname,
#
#                               do_print=False)
#
#                 print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
#                 print('')
#
#                 Input = input(text_general_proceed())
#                 print('')
#
#             elif Auswahl == 'Export_Grafik':
#
#                 us = environment.UserSettings()
#
#                 Noten_Speichern_Pfad = us['directoryScratch']
#
#                 print(text_general_exportGraph(Noten_Speichern_Pfad))
#                 print()
#
#                 Pfad_Dateiname = str(Noten_Speichern_Pfad)+'\\'+'Temp'+'.csv'
#
#                 pd_bs_data = export_as_csv(data=Data,
#
#                                            columns=menu_header,
#
#                                            save_at=Pfad_Dateiname,
#
#                                            do_print=True, do_return_pd=True)
#
#                 np_bs_data = pd_bs_data.to_numpy()
#
#                 plt_bs_data = np.zeros(np.shape(pd_bs_data))
#
#                 for i in range(np.shape(np_bs_data)[0]):
#
#                     plt_bs_data[i][0] = n_uni_int_dict[np_bs_data[i][1]]
#                     plt_bs_data[i][1] = bs_uni_int_dict[np_bs_data[i][2]]
#                     plt_bs_data[i][2] = np_bs_data[i][3]
#
#
#                 from mpl_toolkits.mplot3d import Axes3D
#                 import matplotlib.pyplot as plt
#                 import matplotlib.cm as cm
#
#                 fig = plt.figure()
#                 ax1 = fig.add_subplot(111, projection='3d')
#                 numele= np.shape(np_bs_data)[0]
#
#                 x = plt_bs_data[:,0]
#                 y = plt_bs_data[:,1]
#                 z = np.zeros(numele)
#
#                 dx = 0.5 * np.ones(numele)
#                 dy = 0.3 * np.ones(numele)
#                 dz = plt_bs_data[:,2]
#
#
#                 cmap = cm.get_cmap('jet') # Get desired colormap
#                 max_height = np.max(dz)   # get range of colorbars
#                 min_height = np.min(dz)
#                 rgba = [cmap((k-min_height)/max_height) for k in dz]
#
#                 ax1.set_xticks(np.arange(len(n_uni)))
#                 ax1.set_yticks(np.arange(len(bs_uni)))
#
#
#                 ax1.bar3d(x, y, z, dx, dy, dz, color=rgba, zsort='average')
#
#                 ax1.set_xticklabels(list(n_uni))
#                 ax1.set_yticklabels([str(i) for i in bs_uni])
#                 ax1.set_xlabel('Tonhoehe')
#                 ax1.set_ylabel('Metrisches Gewicht')
#                 ax1.set_zlabel('Haeufigkeit')
#
#                 plt.show()
#
#                 os.remove(Pfad_Dateiname)
#
#                 Input = input(text_general_proceed())
#                 print('')
#
#             elif Auswahl == 'Back':
#
#                 break
#
#     except Exception as e:
#
#         print(text_exception_general(e,sys._getframe().f_code.co_name))
#         print('')
#
#         Input = input(text_general_proceed())
#         print('')

# ## Rhythmik

# ## Satztechnik (Aufbau, Struktur der Mehrstimmigkeit)

# ## Takt

# ## Tempo

# ## Tonmaterial

# ### Töne Anzahl (gesamt)

# #### Textausgabe

# In[56]:


def notes_notesQuantity_total_textOutput():
    clear_screen()

    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        # --- Unterhalb: Code des Tools ---

        Anzahl_Noten = len(
            selectedScore_stripTies.flat.getElementsByClass("Note"))

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = [[score_label, Anzahl_Noten]]

        Menuestrukturen_Musikalische_Parameter_ohne_Grafikexport(
            notes_notesQuantity_total_textOutput, menu_header, Data, notes=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Töne Anzahl (Tonhöhen)

# #### Textausgabe (-- entfernt --)

# def notes_notesQuantity_pitches_textOutput():
#
#     clear_screen()
#
#     try:
#
#         selectedScore = select_score_completeOrIndividualVoice()
#
#         selectedScore_stripTies = selectedScore.stripTies()
#
#         selectedScore_name = str(Erhalte_Key_zu_Value(Noten,Verzeichnis_Partitur_und_Einzelstimmen))
#
#         score_label = selectedScore_name + ', ' + text_analysis_measures() + str(Input_Takte_Anfang) + '-' + str(Input_Takte_Ende)
#
#         nameOctaveCount = analysis.pitchAnalysis.pitchAttributeCount(selectedScore_stripTies, 'nameWithOctave')
#
#         notes_nameOctaveCount = [[score_label, i, nameOctaveCount[i]]for i in sorted(nameOctaveCount)]
#
#         menu_header = text_headers(sys._getframe().f_code.co_name)
#
#         Data = notes_nameOctaveCount
#
#         show_resultslist(menu_header, Data)
#
#         while True:
#
#             Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())
#
#             if Auswahl == 'Repeat':
#
#                 notes_notesQuantity_pitches_textOutput()
#
#                 break
#
#             elif Auswahl == 'Export_CSV':
#
#                 us = environment.UserSettings()
#
#                 Noten_Speichern_Pfad = us['directoryScratch']
#
#                 Dateiname = input(text_export_fileName())
#                 print('')
#
#                 Pfad_Dateiname = str(Noten_Speichern_Pfad)+'\\'+str(Dateiname)+'.csv'
#
#                 export_as_csv(data=Data,
#
#                               columns=menu_header,
#
#                               save_at=Pfad_Dateiname,
#
#                               do_print=False)
#
#                 print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
#                 print('')
#
#                 Input = input(text_general_proceed())
#                 print('')
#
#             elif Auswahl == 'Export_Grafik':
#
#                 print(text_general_exportToDiagrammUnavailable())
#
#                 Input = input(text_general_proceed())
#                 print('')
#
#             elif Auswahl == 'Back':
#
#                 break
#
#     except Exception as e:
#
#         print(text_exception_general(e,sys._getframe().f_code.co_name))
#         print('')
#
#         Input = input(text_general_proceed())
#         print('')

# # Vordefinierte Darstellungen

# ## Menüstrukturen

# ### Mit Grafikexport

# In[ ]:


def Menuestrukturen_vordefinierte_visualizations(
    function_name, menu_header, Data, Graph, notes
):
    try:
        clear_screen()

        show_resultslist(menu_header, Data)
        print("")

        if notes != "":
            print(notes)
            print("")

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                function_name()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                print(text_general_exportGraph(Noten_Speichern_Pfad))
                print()

                Graph.doneAction = None
                Graph.run()

                plt.show()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## HistogramPitchSpace

#

# In[57]:


def predefinedVisualizations_HistogramPitchSpace():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.HistogramPitchSpace

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [score_label, item[0], pitch.Pitch(
                    item[0]).nameWithOctave, item[1]]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_HistogramPitchSpace,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## HistogramPitchClass

# In[58]:


def predefinedVisualizations_HistogramPitchClass():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.HistogramPitchClass

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [score_label, item[0], pitch.Pitch(
                    item[0]).nameWithOctave, item[1]]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_HistogramPitchClass,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## HistogramQuarterLength

# In[1]:


def predefinedVisualizations_HistogramQuarterLength():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.HistogramQuarterLength

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [
                    score_label,
                    item[0],
                    duration.Duration(quarterLength=float(item[0])).fullName,
                    item[1],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_HistogramQuarterLength,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## HorizontalBarPitchSpaceOffset (Pianorollendarstellung)

# In[60]:


def predefinedVisualizations_HorizontalBarPitchSpaceOffset():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.HorizontalBarPitchSpaceOffset

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        Liste_Einsaetze = []

        for x in Graph.data:
            x[0] = x[0].replace("♭", "-").replace("♯", "#")

            octave = ""

            if any(chr.isdigit() for chr in str(x[0])):
                for c in x[0]:
                    if c.isdigit():
                        number = c

            if not any(chr.isdigit() for chr in str(x[0])):
                octave = number

            if len(x) != 0:
                for y in x:
                    if type(y) == list and len(y) != 0:
                        for z in y:
                            if type(z) == tuple:
                                if "B#/D--/C" in x[0] or "B##/D-/C#" in x[0]:
                                    x[0] = x[0].replace("/D", octave + "/D")

                                    x[0] = x[0].replace(
                                        "/C", str(int(octave) + 1) + "/C"
                                    )

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    Liste_Einsaetze.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                elif "B#/C/D--" in x[0] or "B##/C#/D-" in x[0]:
                                    x[0] = x[0].replace("/C", octave + "/C")

                                    x[0] = x[0].replace(
                                        "/D", str(int(octave) + 1) + "/D"
                                    )

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    Liste_Einsaetze.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                elif "B#/D--" in x[0] or "B##/D-" in x[0]:
                                    x[0] = x[0].replace("/", octave + "/")

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    Liste_Einsaetze.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                elif (
                                    "B-/C--" in x[0]
                                    or "B/C-" in x[0]
                                    or "B#/C" in x[0]
                                    or "B##/C#" in x[0]
                                ):
                                    x[0] = x[0].replace("/", octave + "/")

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    Liste_Einsaetze.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                else:
                                    if any(chr.isdigit() for chr in str(x[0])):
                                        if "/" in x[0]:
                                            n = x[0].rfind("/")

                                            Liste_Einsaetze.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0][n + 1:])
                                                    ).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

                                        else:
                                            Liste_Einsaetze.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0])).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

                                    else:
                                        if "/" in x[0]:
                                            x[0] = x[0].replace(
                                                "/", octave + "/")

                                            x[0] = x[0] + str(octave)

                                            n = x[0].rfind("/")

                                            Liste_Einsaetze.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0][n + 1:])
                                                    ).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

                                        else:
                                            x[0] = x[0] + str(octave)

                                            Liste_Einsaetze.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0])).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Liste_Einsaetze

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                predefinedVisualizations_HorizontalBarPitchSpaceOffset()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                print(text_general_exportGraph(Noten_Speichern_Pfad))
                print()

                Graph.doneAction = None
                Graph.run()

                plt.show()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## ScatterWeightedPitchSpaceQuarterLength

# In[61]:


def predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.ScatterWeightedPitchSpaceQuarterLength

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        ax = graph.axis.QuarterLengthAxis(Graph)

        Verzeichnis_Tondauern = {}

        for item in ax.ticks():
            Verzeichnis_Tondauern.update({item[0]: item[1]})

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [
                    score_label,
                    Verzeichnis_Tondauern[item[0]],
                    duration.Duration(
                        quarterLength=float(Verzeichnis_Tondauern[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## Plot3DBarsPitchSpaceQuarterLength

# In[62]:


def predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.Plot3DBarsPitchSpaceQuarterLength

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        ax = graph.axis.QuarterLengthAxis(Graph)

        Verzeichnis_Tondauern = {}

        for item in ax.ticks():
            Verzeichnis_Tondauern.update({item[0]: item[1]})

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [
                    score_label,
                    Verzeichnis_Tondauern[item[0]],
                    duration.Duration(
                        quarterLength=float(Verzeichnis_Tondauern[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## ScatterWeightedPitchClassQuarterLength

# In[63]:


def predefinedVisualizations_ScatterWeightedPitchClassQuarterLength():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.ScatterWeightedPitchClassQuarterLength

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        ax = graph.axis.QuarterLengthAxis(Graph)

        Verzeichnis_Tondauern = {}

        for item in ax.ticks():
            Verzeichnis_Tondauern.update({item[0]: item[1]})

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [
                    score_label,
                    Verzeichnis_Tondauern[item[0]],
                    duration.Duration(
                        quarterLength=float(Verzeichnis_Tondauern[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_ScatterWeightedPitchClassQuarterLength,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## ScatterPitchClassOffset

# In[64]:


def predefinedVisualizations_ScatterPitchClassOffset():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.ScatterPitchClassOffset

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [score_label, item[1], pitch.Pitch(
                    item[1]).nameWithOctave, item[0]]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_ScatterPitchClassOffset,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## ScatterWeightedPitchSpaceDynamicSymbol

# In[65]:


def predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.ScatterWeightedPitchSpaceDynamicSymbol

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        ax = graph.axis.DynamicsAxis(Graph)

        Verzeichnis_Dynamiken = {}

        for item in ax.ticks():
            Verzeichnis_Dynamiken.update({item[0]: item[1].replace("$", "")})

        Werte_Liste = []

        for item in Graph.data:
            Werte_Liste.append(
                [
                    score_label,
                    item[0],
                    pitch.Pitch(item[0]).nameWithOctave,
                    Verzeichnis_Dynamiken[item[1]],
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Werte_Liste

        Menuestrukturen_vordefinierte_visualizations(
            predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol,
            menu_header,
            Data,
            Graph,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## HorizontalBarPitchClassOffset

# In[66]:


def predefinedVisualizations_HorizontalBarPitchClassOffset():
    try:
        selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = selectedScore.stripTies()

        selectedScore_name = str(
            Erhalte_Key_zu_Value(Noten, Verzeichnis_Partitur_und_Einzelstimmen)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(Input_Takte_Anfang)
            + "-"
            + str(Input_Takte_Ende)
        )

        Auswahl_Graph = graph.plot.HorizontalBarPitchClassOffset

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.extractData()

        Liste_Einsaetze = []

        for x in Graph.data:
            x[0] = x[0].replace("♭", "-").replace("♯", "#")

            if len(x) != 0:
                for y in x:
                    if type(y) == list and len(y) != 0:
                        for z in y:
                            if type(z) == tuple:
                                if "/" in x[0]:
                                    n = x[0].rfind("/")

                                    Liste_Einsaetze.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).pitchClass,
                                            str(x[0]),
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                else:
                                    Liste_Einsaetze.append(
                                        [
                                            score_label,
                                            pitch.Pitch(str(x[0])).pitchClass,
                                            str(x[0]),
                                            z[0],
                                            z[1],
                                        ]
                                    )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Liste_Einsaetze

        while True:
            Auswahl = open_submenu_Daten_mit_Info(Modul_Navigation())

            if Auswahl == "Repeat":
                predefinedVisualizations_HorizontalBarPitchClassOffset()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Grafik":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                print(text_general_exportGraph(Noten_Speichern_Pfad))
                print()

                Graph.doneAction = None
                Graph.run()

                plt.show()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ## Dolan

# In[67]:


def predefinedVisualizations_Dolan():
    clear_screen()

    # --- Unterhalb: Code des Tools ---

    selectedScore = select_score_completeOrIndividualVoice()

    selectedScore_stripTies = selectedScore.stripTies()

    print(text_analysis_notes_predefinedVisualizations_Dolan())
    print("")

    try:
        Auswahl_Graph = graph.plot.Dolan

        Graph = Auswahl_Graph(selectedScore_stripTies)

        Graph.doneAction = None
        Graph.run()

        plt.show()

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")

    # --- Oberhalb: Code des Tools ---

    Menue_Frage_Tool_Wiederholen(predefinedVisualizations_Dolan)


# # Mustersuche

# ## Menüstrukturen

# In[68]:


def open_submenu_patternSearch(Liste):
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_patternSearch_showPatternSelection(Suchpattern))
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplenation()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(Liste, 1):
            print("{:<4} {:<65}".format(index, item[0]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if 0 <= Input_Menueauswahl_Int < len(Liste):
                clear_screen()

                return Liste[Input_Menueauswahl_Int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(Liste)))
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(Liste)))
            print("")

            Input = input(text_general_proceed())
            print("")


# ## Suchroutinen

# ### Tonfolge ohne Transposition/ohne Rhythmus

# In[69]:


def patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm():
    try:
        music = deepcopy(Partitur.stripTies(inPlace=True))

        StreamMot = patternSearch_enter_search_pattern_without_rhythm()

        while True:
            clear_screen()

            Input = input(text_patternSearch_includeRests())
            print("")

            if Rueckgabe_Wahrheitswert_ja_1(Input):
                full_piece_stream = music.recurse().notes

                break

            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                full_piece_stream = music.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                Input = input(text_general_proceed())
                print("")

        p_full_piece = search.noteNameSearch(full_piece_stream, StreamMot)

        print(text_patternSearch_patternsFound(len(p_full_piece)))
        print("")

        Input = input(text_general_proceed())
        print("")

        Muster_Liste = []

        Zaehler = 1

        for Position in p_full_piece:
            startingNote = full_piece_stream[Position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            Muster_Liste.append(
                [
                    Zaehler,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    Liste_als_String(Suchpattern),
                ]
            )

            Zaehler += 1

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Muster_Liste

        show_resultslist(menu_header, Data)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")

    while True:
        try:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_patternSearch())

            if Auswahl == "Repeat":
                patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Notentext":
                for found in p_full_piece:
                    for ffound in range(len(StreamMot)):
                        full_piece_stream[found + ffound].lyric = "*"
                        full_piece_stream[found + ffound].style.color = "red"

                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = music.write("xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")


# ### Tonfolge mit Transposition/ohne Rhythmus

# In[70]:


def patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm():
    try:
        music = deepcopy(Partitur.stripTies(inPlace=True))

        StreamMot = patternSearch_enter_search_pattern_without_rhythm()

        while True:
            clear_screen()

            Input = input(text_patternSearch_includeRests())
            print("")

            if Rueckgabe_Wahrheitswert_ja_1(Input):
                s = music.recurse().notes

                break

            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                s = music.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                Input = input(text_general_proceed())
                print("")

        def pitchClassEqual(n1, n2):
            if not hasattr(n1, "pitch"):
                return False
            if not hasattr(n2, "pitch"):
                return False
            if n1.pitch.pitchClass == n2.pitch.pitchClass:
                return True
            else:
                return False

        results = []
        zähler = 1
        Durchlauf = 1

        # Die Ergebnisse müssen in einer extra Liste ("results") eingetragen werden.
        # Der "zähler" vereinfacht das Aufzählen der Töne, wenn man diese nacheinander zeigen will.

        Muster_Liste = []

        for egal in range(12):  # Suche 12 Mal
            s_len = [StreamMot.notes[i].name for i in range(
                len(StreamMot.notes))]
            p = search.streamSearchBase(
                s, StreamMot, algorithm=pitchClassEqual)
            for notePosition in p:
                startingNote = s[notePosition]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                results.append(notePosition)

                Muster_Liste.append(
                    [
                        zähler,
                        startingNote,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        Liste_als_String(s_len),
                    ]
                )

                zähler += 1

            [n.transpose(1, inPlace=True) for n in StreamMot]

            Durchlauf += 1

        print(text_patternSearch_patternsFound(len(results)))
        print("")

        Input = input(text_general_proceed())
        print("")

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Muster_Liste

        show_resultslist(menu_header, Data)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")

    while True:
        try:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_patternSearch())

            if Auswahl == "Repeat":
                patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Notentext":
                for found in results:
                    for ffound in range(len(StreamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = music.write("xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")


# ### Tonfolge ohne Transposition/mit Rhythmus

# In[71]:


def patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm():
    try:
        music = deepcopy(Partitur.stripTies(inPlace=True))

        StreamMot = patternSearch_enter_search_pattern_with_rhythm()

        while True:
            clear_screen()

            Input = input(text_patternSearch_includeRests())
            print("")

            if Rueckgabe_Wahrheitswert_ja_1(Input):
                s = music.recurse().notes

                break

            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                s = music.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                Input = input(text_general_proceed())
                print("")

        # Die Suche wird nun mit dem Befehl 'search.noteNameRhythmicSearch' erstellt.

        p = search.noteNameRhythmicSearch(s, StreamMot)

        print(text_patternSearch_patternsFound(len(p)))
        print("")

        Input = input(text_general_proceed())
        print("")

        zähler = 1

        Muster_Liste = []

        for Position in p:
            startingNote = s[Position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            Muster_Liste.append(
                [
                    zähler,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    Liste_als_String(Suchpattern),
                ]
            )

            zähler += 1

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Muster_Liste

        show_resultslist(menu_header, Data)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")

    while True:
        try:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_patternSearch())

            if Auswahl == "Repeat":
                patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Notentext":
                for found in p:
                    for ffound in range(len(StreamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = music.write("xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")


# ### Tonfolge mit Transposition/mit Rhythmus

# In[72]:


def patternSearch_menuStructure_toneSequence_withTransposition_withRhythm():
    try:
        music = deepcopy(Partitur.stripTies(inPlace=True))

        StreamMot = patternSearch_enter_search_pattern_with_rhythm()

        while True:
            clear_screen()

            Input = input(text_patternSearch_includeRests())
            print("")

            if Rueckgabe_Wahrheitswert_ja_1(Input):
                s = music.recurse().notes

                break

            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                s = music.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                Input = input(text_general_proceed())
                print("")

        results = []
        zähler = 1
        Durchlauf = 1

        # Die Ergebnisse müssen in einer extra Liste ("results") eingetragen werden.
        # Der "zähler" vereinfacht das Aufzählen der Töne, wenn man diese nacheinander zeigen will.

        Muster_Liste = []

        for egal in range(12):  # Suche 12 Mal
            s_len = [StreamMot.notes[i].name for i in range(
                len(StreamMot.notes))]
            p = search.noteNameRhythmicSearch(s, StreamMot)
            for notePosition in p:
                startingNote = s[notePosition]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                results.append(notePosition)

                Muster_Liste.append(
                    [
                        zähler,
                        startingNote,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        Liste_als_String(s_len),
                    ]
                )

                zähler += 1

            [n.transpose(1, inPlace=True) for n in StreamMot]

            Durchlauf += 1

        print(text_patternSearch_patternsFound(len(results)))
        print("")

        Input = input(text_general_proceed())
        print("")

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Muster_Liste

        show_resultslist(menu_header, Data)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")

    while True:
        try:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_patternSearch())

            if Auswahl == "Repeat":
                patternSearch_menuStructure_toneSequence_withTransposition_withRhythm()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Notentext":
                for found in results:
                    for ffound in range(len(StreamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = music.write("xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")


# ### Rhythmus ohne Tonhöhen

# In[ ]:


def patternSearch_menuStructure_rhythm_withoutPitch():
    try:
        music = deepcopy(Partitur.stripTies(inPlace=True))

        StreamMot = patternSearch_enter_search_pattern_only_rhythm()

        while True:
            clear_screen()

            Input = input(text_patternSearch_includeRests())
            print("")

            if Rueckgabe_Wahrheitswert_ja_1(Input):
                s = music.recurse().notes

                break

            elif Rueckgabe_Wahrheitswert_nein_0(Input):
                s = music.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                Input = input(text_general_proceed())
                print("")

        # Die Suche wird nun mit dem Befehl 'search.noteNameRhythmicSearch' erstellt.

        p = search.rhythmicSearch(s, StreamMot)

        print(text_patternSearch_patternsFound(len(p)))
        print("")

        Input = input(text_general_proceed())
        print("")

        zähler = 1

        Muster_Liste = []

        for Position in p:
            startingNote = s[Position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            Muster_Liste.append(
                [
                    zähler,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    Liste_als_String(Suchpattern),
                ]
            )

            zähler += 1

        menu_header = text_headers(sys._getframe().f_code.co_name)

        Data = Muster_Liste

        show_resultslist(menu_header, Data)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")

    while True:
        try:
            Auswahl = open_submenu_Daten_mit_Info(
                modul_navigation_patternSearch())

            if Auswahl == "Repeat":
                patternSearch_menuStructure_rhythm_withoutPitch()

                break

            elif Auswahl == "Export_CSV":
                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".csv"
                )

                export_as_csv(
                    data=Data, columns=menu_header, save_at=Pfad_Dateiname, do_print=False
                )

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".csv"))
                print()

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Export_Notentext":
                for found in p:
                    for ffound in range(len(StreamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                Noten_Speichern_Pfad = us["directoryScratch"]

                Dateiname = input(text_export_fileName())
                print("")

                Pfad_Dateiname = (
                    str(Noten_Speichern_Pfad) + "\\" + str(Dateiname) + ".xml"
                )

                mf = music.write("xml", fp=Pfad_Dateiname)

                print(text_general_exportSuccessful(Noten_Speichern_Pfad, Dateiname, ".xml"))
                print("")

                Input = input(text_general_proceed())
                print("")

            elif Auswahl == "Back":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            Input = input(text_general_proceed())
            print("")


# ## Menüeinträge

# ### Tonauswahl

# In[7]:


def key_selection_menu_entries():
    list_de = [
        ["‾‾‾‾  -   Ces", "C-"],
        ["C         C", "C"],
        ["____  ♯   Cis", "C#"],
        ["‾‾‾‾  -   Des", "D-"],
        ["D         D", "D"],
        ["____  ♯   Dis", "D#"],
        ["‾‾‾‾  -   Es", "E-"],
        ["E         E", "E"],
        ["____  ♯   Eis", "E#"],
        ["‾‾‾‾  -   Fes", "F-"],
        ["F         F", "F"],
        ["____  ♯   Fis", "F#"],
        ["‾‾‾‾  -   Ges", "G-"],
        ["G         G", "G"],
        ["____  ♯   Gis", "G#"],
        ["‾‾‾‾  -   As", "A-"],
        ["A         A", "A"],
        ["____  ♯   Ais", "A#"],
        ["‾‾‾‾  -   B", "B-"],
        ["H         H", "B"],
        ["____  ♯   His", "B#"],
        ["BACK: Zuletzt eingegebene Note entfernen", "remove"],
        ["DONE: Eingabe beenden", "complete"],
    ]

    list_en = [
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

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ### Rhythmusauswahl

# In[74]:


def rhythm_selection_menu_entries():
    list_de = [
        ["[0.125]   32-tel-Note", 0.125],
        ["[0.25]    16-tel-Note", 0.25],
        ["[0.375]   16-tel-Note + Punktierung", 0.375],
        ["[1/3]     8-tel-Triole", "1/3"],
        ["[0.5]     8-tel-Note", 0.5],
        ["[0.75]    8-tel-Note + Punktierung", 0.75],
        ["[2/3]     4-tel-Triole", "2/3"],
        ["[1.0]     4-tel-Note", 1.0],
        ["[1.5]     4-tel-Note + Punktierung", 1.5],
        ["[4/3]     Halbe-Triole", "4/3"],
        ["[2.0]     Halbe-Note", 2.0],
        ["[3.0]     Halbe-Note + Punktierung", 3.0],
        ["[8/3]     Ganze-Triole", "8/3"],
        ["[4.0]     Ganze-Note", 4.0],
        ["[6.0]     Ganze-Note + Punktierung", 6.0],
        ["[16/3]    Doppelganze-Triole", "16/3"],
        ["[8.0]     Doppelganze-Note", 8.0],
        ["[12.0]    Doppelganze-Note + Punktierung", 12.0],
        ["[x.xx]    Selbstgewählten Notenwert eingeben", "custom"],
        ["BACK:     Zuletzt eingegebene Note entfernen", "remove"],
    ]

    list_en = [
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
        ["[x.xx]    Enter custom rhythm", "custom"],
        ["BACK:     Remove the last note entered", "remove"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ### Rhythmusauswahl (only rhythm)

# In[ ]:


def rhythm_selection_menu_entries_only_rhythm():
    list_de = [
        ["[0.125]   32-tel-Note", 0.125],
        ["[0.25]    16-tel-Note", 0.25],
        ["[0.375]   16-tel-Note + Punktierung", 0.375],
        ["[1/3]     8-tel-Triole", "1/3"],
        ["[0.5]     8-tel-Note", 0.5],
        ["[0.75]    8-tel-Note + Punktierung", 0.75],
        ["[2/3]     4-tel-Triole", "2/3"],
        ["[1.0]     4-tel-Note", 1.0],
        ["[1.5]     4-tel-Note + Punktierung", 1.5],
        ["[4/3]     Halbe-Triole", "4/3"],
        ["[2.0]     Halbe-Note", 2.0],
        ["[3.0]     Halbe-Note + Punktierung", 3.0],
        ["[8/3]     Ganze-Triole", "8/3"],
        ["[4.0]     Ganze-Note", 4.0],
        ["[6.0]     Ganze-Note + Punktierung", 6.0],
        ["[16/3]    Doppelganze-Triole", "16/3"],
        ["[8.0]     Doppelganze-Note", 8.0],
        ["[12.0]    Doppelganze-Note + Punktierung", 12.0],
        ["[x.xx]    Selbstgewählten Notenwert eingeben", "custom"],
        ["BACK:     Zuletzt eingegebenen Notenwert entfernen", "remove"],
        ["DONE:     Eingabe beenden", "complete"],
    ]

    list_en = [
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
        ["[x.xx]    Enter custom rhythm", "custom"],
        ["BACK:     Remove the last rhythm entered", "remove"],
        ["DONE:     Finish input", "complete"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ## Enter search pattern

# ### With rhythm

# In[ ]:


def patternSearch_enter_search_pattern_with_rhythm():
    try:
        global Suchpattern

        loopDone1 = False

        while not loopDone1:
            StreamMot = stream.Stream()

            Suchpattern = []

            loopDone2 = False

            while not loopDone2:
                Tonauswahl = open_submenu_patternSearch(
                    key_selection_menu_entries())

                clear_screen()

                if Tonauswahl == "remove":
                    if len(Suchpattern) > 0:
                        Suchpattern.pop()

                elif Tonauswahl == "complete":
                    for Tonhoehe, Rhythmus in Suchpattern:
                        if "/" in Rhythmus:
                            num, den = map(float, Rhythmus.split("/"))

                            StreamMot.append(
                                note.Note(
                                    Tonhoehe, quarterLength=float(num / den))
                            )

                        else:
                            StreamMot.append(
                                note.Note(
                                    Tonhoehe, quarterLength=float(Rhythmus))
                            )

                    loopDone3 = False

                    while not loopDone3:
                        clear_screen()

                        Input = input(text_display_showScoreSelection())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            print(text_general_close_museScore3())
                            print()

                            StreamMot.show()

                            loopDone3 = True

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())

                    loopDone3 = False

                    while not loopDone3:
                        clear_screen()

                        print(text_patternSearch_showPatternSelection(Suchpattern))
                        print("")

                        Input = input(text_general_checkEntry())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            loopDone1 = True
                            loopDone2 = True
                            loopDone3 = True

                            clear_screen()

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone1 = False
                            loopDone2 = True
                            loopDone3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            Input = input(text_general_proceed())
                            print("")

                            clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            Input = input(text_general_proceed())
                            print("")

                else:
                    Rhythmusauswahl = open_submenu_patternSearch(
                        rhythm_selection_menu_entries()
                    )

                    if Rhythmusauswahl == "remove":
                        if len(Suchpattern) > 0:
                            Suchpattern.pop()

                    elif Rhythmusauswahl == "custom":
                        loopDone4 = True

                        while loopDone4:
                            clear_screen()

                            Rhythmuseingabe = input(
                                text_patternSearch_enter_customRhythm()
                            )
                            print("")

                            if Rueckgabe_Wahrheitswert_is_number(Rhythmuseingabe):
                                Suchpattern.append(
                                    [Tonauswahl, str(Rhythmuseingabe)])

                                loopDone4 = False

                            else:
                                print(text_general_input_restrictedToNumbers(
                                    Rhythmuseingabe))
                                print("")

                                Input = input(text_general_proceed())
                                print("")

                    else:
                        Suchpattern.append([Tonauswahl, str(Rhythmusauswahl)])

        clear_screen()

        return StreamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Without rhythm

#

# In[ ]:


def patternSearch_enter_search_pattern_without_rhythm():
    try:
        global Suchpattern

        loopDone1 = False

        while not loopDone1:
            StreamMot = stream.Stream()

            Suchpattern = []

            loopDone2 = False

            while not loopDone2:
                Tonauswahl = open_submenu_patternSearch(
                    key_selection_menu_entries())

                clear_screen()

                if Tonauswahl == "remove":
                    if len(Suchpattern) > 0:
                        Suchpattern.pop()

                elif Tonauswahl == "complete":
                    for Tonhoehe in Suchpattern:
                        StreamMot.append(note.Note(Tonhoehe))

                    loopDone3 = False

                    while not loopDone3:
                        clear_screen()

                        Input = input(text_display_showScoreSelection())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            print(text_general_close_museScore3())
                            print()

                            StreamMot.show()

                            loopDone3 = True

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                    loopDone3 = False

                    while not loopDone3:
                        clear_screen()

                        print(text_patternSearch_showPatternSelection(Suchpattern))
                        print("")

                        Input = input(text_general_checkEntry())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            loopDone1 = True
                            loopDone2 = True
                            loopDone3 = True

                            clear_screen()

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone1 = False
                            loopDone2 = True
                            loopDone3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            Input = input(text_general_proceed())
                            print("")

                            clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            Input = input(text_general_proceed())
                            print("")

                else:
                    Suchpattern.append(Tonauswahl)

        clear_screen()

        return StreamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# ### Only rhythm

# In[ ]:


def patternSearch_enter_search_pattern_only_rhythm():
    try:
        global Suchpattern

        loopDone1 = False

        while not loopDone1:
            StreamMot = stream.Stream()

            Suchpattern = []

            loopDone2 = False

            while not loopDone2:
                Rhythmusauswahl = open_submenu_patternSearch(
                    rhythm_selection_menu_entries_only_rhythm()
                )

                clear_screen()

                if Rhythmusauswahl == "remove":
                    if len(Suchpattern) > 0:
                        Suchpattern.pop()

                elif Rhythmusauswahl == "custom":
                    loopDone4 = True

                    while loopDone4:
                        clear_screen()

                        Rhythmuseingabe = input(
                            text_patternSearch_enter_customRhythm()
                        )
                        print("")

                        if Rueckgabe_Wahrheitswert_is_number(Rhythmuseingabe):
                            Suchpattern.append(str(Rhythmuseingabe))

                            loopDone4 = False

                        else:
                            print(text_general_input_restrictedToNumbers(
                                Rhythmuseingabe))
                            print("")

                            Input = input(text_general_proceed())
                            print("")

                elif Rhythmusauswahl == "complete":
                    for Rhythmus in Suchpattern:
                        if "/" in Rhythmus:
                            num, den = map(float, Rhythmus.split("/"))

                            StreamMot.append(
                                note.Note("G", quarterLength=float(num / den))
                            )

                        else:
                            StreamMot.append(
                                note.Note("G", quarterLength=float(Rhythmus))
                            )

                    loopDone3 = False

                    while not loopDone3:
                        clear_screen()

                        Input = input(text_display_showScoreSelection())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            print(text_general_close_museScore3())
                            print()

                            StreamMot.show()

                            loopDone3 = True

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                    loopDone3 = False

                    while not loopDone3:
                        clear_screen()

                        print(text_patternSearch_showPatternSelection(Suchpattern))
                        print("")

                        Input = input(text_general_checkEntry())
                        print("")

                        if Rueckgabe_Wahrheitswert_ja_1(Input):
                            loopDone1 = True
                            loopDone2 = True
                            loopDone3 = True

                            clear_screen()

                        elif Rueckgabe_Wahrheitswert_nein_0(Input):
                            loopDone1 = False
                            loopDone2 = True
                            loopDone3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            Input = input(text_general_proceed())
                            print("")

                            clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            Input = input(text_general_proceed())
                            print("")

                else:
                    Suchpattern.append(str(Rhythmusauswahl))

        clear_screen()

        return StreamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        Input = input(text_general_proceed())
        print("")


# # Programme: Zeichenorientierte Benutzerschnittstelle (CLI)

# ## Einzelwerk

# ### Menüstrukturen

# #### Hauptmenü Einzelwerk (erste Ebene)

# In[75]:


def open_mainmenu_individualPiece():
    select_score_filePath()

    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(Eintraege_Hauptmenue_Einzelwerk(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if 0 <= Input_Menueauswahl_Int < len(Eintraege_Hauptmenue_Einzelwerk()):
                clear_screen()

                Eintraege_Hauptmenue_Einzelwerk()[Input_Menueauswahl_Int][1]()

                clear_screen()

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Hauptmenue_Einzelwerk())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Hauptmenue_Einzelwerk())
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, File)

# In[76]:


def open_submenu_individualPiece_files():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(Eintraege_Untermenue_Einzelwerk_files(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if (
                0
                <= Input_Menueauswahl_Int
                < len(Eintraege_Untermenue_Einzelwerk_files())
            ):
                clear_screen()

                if (
                    Eintraege_Untermenue_Einzelwerk_files()[
                        Input_Menueauswahl_Int][1]
                    != "nothing"
                ):
                    Eintraege_Untermenue_Einzelwerk_files()[
                        Input_Menueauswahl_Int][1]()

                clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Untermenue_Einzelwerk_files())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Untermenue_Einzelwerk_files())
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, statistische Analysen)

# In[77]:


def open_submenu_individualPiece_statisticalAnalyses():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            Eintraege_Untermenue_Einzelwerk_statisticalAnalyses(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if (
                0
                <= Input_Menueauswahl_Int
                < len(Eintraege_Untermenue_Einzelwerk_statisticalAnalyses())
            ):
                clear_screen()

                if (
                    Eintraege_Untermenue_Einzelwerk_statisticalAnalyses()[
                        Input_Menueauswahl_Int
                    ][1]
                    != "nothing"
                ):
                    Eintraege_Untermenue_Einzelwerk_statisticalAnalyses()[
                        Input_Menueauswahl_Int
                    ][1]()

                clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Untermenue_Einzelwerk_statisticalAnalyses())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Untermenue_Einzelwerk_statisticalAnalyses())
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# ##### Untermenü Einzelwerk (dritte Ebene, statistische Analysen, zweidimensionale Häufigkeitsverteilungen/Streudiagramme)

# In[78]:


def open_submenu_individualPiece_statisticalAnalyses_visualizations():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if (
                0
                <= Input_Menueauswahl_Int
                < len(
                    Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations()
                )
            ):
                clear_screen()

                if (
                    Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations()[
                        Input_Menueauswahl_Int
                    ][
                        1
                    ]
                    != "nothing"
                ):
                    Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations()[
                        Input_Menueauswahl_Int
                    ][
                        1
                    ]()

                clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(
                            Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations()
                        )
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(
                        Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations()
                    )
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, Darstellungen)

# In[79]:


def open_submenu_individualPiece_visualizations():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            Eintraege_Untermenue_Einzelwerk_visualizations(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        clear_screen()

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if (
                0
                <= Input_Menueauswahl_Int
                < len(Eintraege_Untermenue_Einzelwerk_visualizations())
            ):
                clear_screen()

                if (
                    Eintraege_Untermenue_Einzelwerk_visualizations()[
                        Input_Menueauswahl_Int
                    ][1]
                    != "nothing"
                ):
                    Eintraege_Untermenue_Einzelwerk_visualizations()[
                        Input_Menueauswahl_Int
                    ][1]()

                clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Untermenue_Einzelwerk_visualizations())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Untermenue_Einzelwerk_visualizations())
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, Mustersuche)

# In[80]:


def open_submenu_individualPiece_patternSearch():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(Eintraege_Untermenue_Einzelwerk_patternSearch(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        clear_screen()

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if (
                0
                <= Input_Menueauswahl_Int
                < len(Eintraege_Untermenue_Einzelwerk_patternSearch())
            ):
                clear_screen()

                if (
                    Eintraege_Untermenue_Einzelwerk_patternSearch()[
                        Input_Menueauswahl_Int
                    ][1]
                    != "nothing"
                ):
                    Eintraege_Untermenue_Einzelwerk_patternSearch()[
                        Input_Menueauswahl_Int
                    ][1]()

                clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Untermenue_Einzelwerk_patternSearch())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Untermenue_Einzelwerk_patternSearch())
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, Einstellungen)

# In[81]:


def open_submenu_individualPiece_settings():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            Eintraege_Untermenue_Einzelwerk_settings(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        clear_screen()

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if (
                0
                <= Input_Menueauswahl_Int
                < len(Eintraege_Untermenue_Einzelwerk_settings())
            ):
                clear_screen()

                if (
                    Eintraege_Untermenue_Einzelwerk_settings()[
                        Input_Menueauswahl_Int
                    ][1]
                    != "nothing"
                ):
                    Eintraege_Untermenue_Einzelwerk_settings()[
                        Input_Menueauswahl_Int
                    ][1]()

                clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Untermenue_Einzelwerk_settings())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Untermenue_Einzelwerk_settings())
                )
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# ### Menüeinträge

# #### Hauptmenü Einzelwerk (erste Ebene)

# In[82]:


def Eintraege_Hauptmenue_Einzelwerk():
    list_de = [
        [
            "FILE: Menüauswahl",
            open_submenu_individualPiece_files,
            "<Grundlegende Funktionen>",
        ],
        [
            "TOOL: Menüauswahl (statistische Analysen)",
            open_submenu_individualPiece_statisticalAnalyses,
            "<Auswahl verschiedener statistischer Analyse-Tools>",
        ],
        [
            "TOOL: Menüauswahl (Darstellung)",
            open_submenu_individualPiece_visualizations,
            "<Auswahl verschiedener Darstellungs-Tools>",
        ],
        [
            "TOOL: Menüauswahl (Mustersuche)",
            open_submenu_individualPiece_patternSearch,
            "<Auswahl verschiedener Tools zur Mustersuche>",
        ],
        [
            "SETT: Einstellungen",
            open_submenu_individualPiece_settings,
            "<Einstellungen in der music21 environment-Datei/Spracheinstellungen>",
        ],
        [
            "HELP: Projektübersicht",
            text_general_projectDescription,
            '<Informationen über das Projekt "Computergestützte Musikanalyse">',
        ],
        ["EXIT: Programm beenden", terminateProgram, "<Beendet das Python-Skript>"],
    ]

    list_en = [
        [
            "FILE: Menu selection",
            open_submenu_individualPiece_files,
            "<Basic functions>",
        ],
        [
            "TOOL: Menu selection (statistical analysis)",
            open_submenu_individualPiece_statisticalAnalyses,
            "<Selection of various statistical analysis tools>",
        ],
        [
            "TOOL: Menu selection (visualisation)",
            open_submenu_individualPiece_visualizations,
            "<Selection of different visualisation tools>",
        ],
        [
            "TOOL: Menu selection (pattern search)",
            open_submenu_individualPiece_patternSearch,
            "<Selection of different tools for pattern search>",
        ],
        [
            "SETT: Settings",
            open_submenu_individualPiece_settings,
            "<Settings in the music21 environment file/language settings>",
        ],
        [
            "HELP: Project overview",
            text_general_projectDescription,
            '<Information about the project "Computer-Aided Music Analysis">',
        ],
        ["EXIT: Exit program", terminateProgram, "<Exits the Python script>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Untermenü Einzelwerk (zweite Ebene, File)

# In[83]:


def Eintraege_Untermenue_Einzelwerk_files():
    list_de = [
        [
            "FILE: Neue Notendatei auswählen",
            select_score_filePath,
            "<Ermöglicht die Auswahl einer neuen Notendatei>",
        ],
        [
            "SHOW: Meta-Daten anzeigen (Partitur)",
            show_score_metadata,
            "<Zeigt die Meta-Daten der ausgewählten Notendatei an>",
        ],
        [
            "PLAY: Notendatei wiedergeben (Midi)",
            helper_playback_MIDI,
            "<Gibt Notendatei als Midi wieder>",
        ],
        [
            "NAME: Namen der Einzelstimmen ändern",
            helpers_name_individualVoices,
            "<Ermöglicht das erneute Umbenennen der Einzelstimmen>",
        ],
        [
            "NAME: Namen der Einzelstimmen anzeigen",
            show_names_individualVoices,
            "<Zeigt die selbst vergebenen Namen der Einzelstimmen an>",
        ],
        [
            "EXPO: Datei exportieren",
            Noten_speichern,
            "<Speichert eine Notenauswahl als .xml-/.midi-/.ly-/.pdf-Datei>",
        ],
        ["BACK: Zurück ins Hauptmenü", "nothing", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "FILE: Select new score",
            select_score_filePath,
            "<Allows you to select a new score>",
        ],
        [
            "SHOW: Show metadata (score)",
            show_score_metadata,
            "<Displays the metadata of the selected score>",
        ],
        ["PLAY: Play selected score (midi)",
         helper_playback_MIDI, "<Plays score as midi>"],
        [
            "NAME: Change the names of the individual parts/voices",
            helpers_name_individualVoices,
            "<Allows you to rename the individual parts/voices>",
        ],
        [
            "NAME: Show names of individual parts/voices",
            show_names_individualVoices,
            "<Displays the names of the individual parts/voices>",
        ],
        [
            "EXPO: Export file",
            Noten_speichern,
            "<Saves a selection of notes as .xml/.midi/.ly/.pdf file>",
        ],
        ["BACK: Back to the main menu", "nothing", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Untermenü Einzelwerk (zweite Ebene, statistische Analysen)

# In[84]:


def Eintraege_Untermenue_Einzelwerk_statisticalAnalyses():
    list_de = [
        ["STAT: Ambitus", range_analysis_textOutput, ""],
        ["STAT: Ambitus (Vergleich)", range_comparison_textOutput, ""],
        [
            "STAT: Intervalltypen",
            intervalStructure_intervalTypes_textOutput,
            "<Achtung: derzeit werden nur konsequent einstimmige Melodielinien korrekt analysiert>.",
        ],
        [
            "STAT: Intervalltypen und -anzahl",
            intervalStructure_intervalTypes_quantity_textOutput,
            "<Achtung: derzeit werden nur konsequent einstimmige Melodielinien korrekt analysiert>",
        ],
        [
            "STAT: Intervalltypen und -anzahl (Vergleich)",
            intervalStructure_intervalTypes_comparison_textOutput,
            "<Achtung: derzeit werden nur konsequent einstimmige Melodielinien korrekt analysiert>",
        ],
        [
            "STAT: Anzahl Intervalle",
            intervalStructure_Intervalle_quantity_textOutput,
            "<Achtung: derzeit werden nur konsequent einstimmige Melodielinien korrekt analysiert>",
        ],
        [
            "STAT: Anzahl Töne",
            notes_notesQuantity_total_textOutput,
            "<Achtung: derzeit werden nur konsequent einstimmige Melodielinien korrekt analysiert>",
        ],
        [
            "HIST: Klangereignisse über Tonhöhen",
            predefinedVisualizations_HistogramPitchSpace,
            "<Ein Histogramm des Tonhöhenraums>",
        ],
        [
            "HIST: Klangereignisse über Tonhöhenklassen",
            predefinedVisualizations_HistogramPitchClass,
            "<Ein Histogramm der Tonhöhenklasse>",
        ],
        [
            "HIST: Klangereignisse über Tonlängen",
            predefinedVisualizations_HistogramQuarterLength,
            "<Ein Histogramm der Tonlängen>",
        ],
        [
            "BARS: Tonhöhen über Zeit (Tonlängen)",
            predefinedVisualizations_HorizontalBarPitchSpaceOffset,
            "<Ein Diagramm der Ereignisse, sortiert nach Tonhöhenraum über die Zeit>",
        ],
        [
            "BARS: Tonhöhenklassen über Zeit (Tonlängen)",
            predefinedVisualizations_HorizontalBarPitchClassOffset,
            "<Ein Diagramm der Ereignisse, sortiert nach Tonhöhenraum über die Zeit>",
        ],
        [
            "HIST: Tonanfangshäufigkeit auf metrischen Akzentstufen",
            meter_metricWeight_textOutput,
            "<Metrisches Gewicht; Hinweise unter: https://analyse.hfm-weimar.de/doku.php?id=basics1>",
        ],
        [
            "MORE: Weitere Darstellungen",
            open_submenu_individualPiece_statisticalAnalyses_visualizations,
            "<Zweidimensionale Häufigkeitsverteilungen/Streudiagramme>",
        ],
        ["BACK: Zurück ins Hauptmenü", "nothing", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        ["STAT: Ambitus", range_analysis_textOutput, ""],
        ["STAT: Ambitus (comparison)", range_comparison_textOutput, ""],
        [
            "STAT: Interval types",
            intervalStructure_intervalTypes_textOutput,
            "<Attention: currently only consistently monodic melody lines are correctly analyzed>.",
        ],
        [
            "STAT: Interval types and frequency",
            intervalStructure_intervalTypes_quantity_textOutput,
            "<Attention: currently only consistently monodic melody lines are correctly analyzed>",
        ],
        [
            "STAT: Interval types and frequency (comparison)",
            intervalStructure_intervalTypes_comparison_textOutput,
            "<Attention: currently only consistently monodic melody lines are correctly analyzed>",
        ],
        [
            "STAT: Number of intervals",
            intervalStructure_Intervalle_quantity_textOutput,
            "<Attention: currently only consistently monodic melody lines are correctly analyzed>",
        ],
        [
            "STAT: Number of tones",
            notes_notesQuantity_total_textOutput,
            "<Attention: currently only consistently monodic melody lines are correctly analyzed>",
        ],
        [
            "HIST: Sound events per pitch",
            predefinedVisualizations_HistogramPitchSpace,
            "<A histogram of the pitch space>",
        ],
        [
            "HIST: Sound events per pitch class",
            predefinedVisualizations_HistogramPitchClass,
            "<A pitch class histogram>",
        ],
        [
            "HIST: Sound events per tone durations",
            predefinedVisualizations_HistogramQuarterLength,
            "<A histogram of the pitch lengths>",
        ],
        [
            "BARS: Pitches over time (pitch lengths)",
            predefinedVisualizations_HorizontalBarPitchSpaceOffset,
            "<A graph of events sorted by pitch space over time>",
        ],
        [
            "BARS: Pitch classes over time (pitch durations)",
            predefinedVisualizations_HorizontalBarPitchClassOffset,
            "<A graph of events sorted by pitch space over time>",
        ],
        [
            "HIST: Tone starting frequency on types of metrical positions",
            meter_metricWeight_textOutput,
            "<Metric weight; Explanations: https://analyse.hfm-weimar.de/doku.php?id=basics1>",
        ],
        [
            "MORE: Further graphs",
            open_submenu_individualPiece_statisticalAnalyses_visualizations,
            "<Two-dimensional frequency distributions/scatter diagrams>",
        ],
        ["BACK: Back to the main menu", "nothing", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ##### Untermenü Einzelwerk (dritte Ebene, statistische Analysen, Darstellungen)

# In[85]:


def Eintraege_Untermenue_Einzelwerk_statisticalAnalyses_visualizations():
    list_de = [
        [
            "SCTR: Tonhöhen über Tonlängen",
            predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength,
            "<Ein Streudiagramm der Klangereignisse, sortiert nach Tonhöhe, über die Tonlängen>",
        ],
        [
            "BARS: Anzahl Tonhöhen über Tonlängen (3D)",
            predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength,
            "<Ein 3D-Histogramm von Tonhöhe und Tonlängen>",
        ],
        [
            "SCTR: Tonhöhenklassen über Tonlängen",
            predefinedVisualizations_ScatterWeightedPitchClassQuarterLength,
            "<Ein Streudiagramm der Klangereignisse, sortiert nach Tonhöhenklasse, über die Tonlängen>",
        ],
        [
            "SCTR: Tonhöhenklassen über Zeit (Einsätze)",
            predefinedVisualizations_ScatterPitchClassOffset,
            "<Ein Streudiagramm von Tonhöhenklasse und Offset>",
        ],
        [
            "SCTR: Dynamiken über Tonhöhen",
            predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol,
            "<Ein Streudiagramm der Dynamik, die vom Tonhöhenraum verwendet wird>",
        ],
        ["BACK: Zurück ins Hauptmenü", "nothing", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "SCTR: Pitch over durations ",
            predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength,
            "<A scatter diagram of the sound events, sorted by pitch over durations >",
        ],
        [
            "BARS: Number of pitches over durations (3D)",
            predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength,
            "<A 3D histogram of pitch and duration>",
        ],
        [
            "SCTR: Pitch classes over durations",
            predefinedVisualizations_ScatterWeightedPitchClassQuarterLength,
            "<A scatter diagram of the sound events, sorted by pitch class, over the durations>",
        ],
        [
            "SCTR: Pitch classes over time (cues)",
            predefinedVisualizations_ScatterPitchClassOffset,
            "<A scatter plot of pitch class and offset>",
        ],
        [
            "SCTR: Dynamics over pitches",
            predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol,
            "<A scatter plot of the dynamics used by each pitch class>",
        ],
        ["BACK: Back to the main menu", "nothing", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Untermenü Einzelwerk (zweite Ebene, Darstellungen)

# In[86]:


def Eintraege_Untermenue_Einzelwerk_visualizations():
    list_de = [
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            Darstellung_MuseScore,
            "<Öffnet MuseScore und zeigt den Notentext an>",
        ],
        [
            "SHOW: Notenauswahl (Akkordverbindungen)",
            Darstellung_Akkordverbindungen,
            "<Speichert eine Notenauswahl, dargestellt als Akkordverbindungen>",
        ],
        [
            "SHOW: Notenauswahl (Generalbass)",
            Darstellung_Akkordverbindungen_Generalbass,
            "<Speichert eine Notenauswahl, dargestellt als Akkordverbindungen mit Generalbassbezifferung>",
        ],
        [
            "SHOW: Notenauswahl (Stufenbezifferung)",
            Darstellung_Akkordverbindungen_Stufenbezifferung,
            "<Speichert eine Notenauswahl, dargestellt als Akkordverbindungen mit Stufenbezifferung>",
        ],
        [
            "SHOW: Pianorollendarstellung",
            predefinedVisualizations_HorizontalBarPitchSpaceOffset,
            "<Ein Diagramm der Ereignisse, sortiert nach Tonhöhenraum über die Zeit>",
        ],
        [
            "SHOW: Linien: Stimmenverlauf",
            Melodik_Melodieverlauf_visualization_lineGraph,
            "<Fehleranfällig: Funktioniert nur bei durchgehend einstimmigen Einzelstimmen>",
        ],
        [
            "SHOW: Dolan",
            predefinedVisualizations_Dolan,
            "<Lautstärkeänderung über die Zeit>",
        ],
        ["BACK: Zurück ins Hauptmenü", "nothing", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "SHOW: Show sheet music selection (MuseScore)",
            Darstellung_MuseScore,
            "<Opens MuseScore and displays the selected scores>",
        ],
        [
            "SHOW: Sheet music selection (chord connections)",
            Darstellung_Akkordverbindungen,
            "<Saves a selection of scores, shown as chord connections>",
        ],
        [
            "SHOW: Sheet music selection (figured bass)",
            Darstellung_Akkordverbindungen_Generalbass,
            "<Saves a selection of scores, shown as chord connections with figured bass>",
        ],
        [
            "SHOW: Sheet music selection (chord-scale system)",
            Darstellung_Akkordverbindungen_Stufenbezifferung,
            "<Saves a score selection, shown as chord connections with numbering>",
        ],
        [
            "SHOW: Pianorolls",
            predefinedVisualizations_HorizontalBarPitchSpaceOffset,
            "<A graph of events sorted by pitch space over time>",
        ],
        [
            "SHOW: Voice progression (line plot)",
            Melodik_Melodieverlauf_visualization_lineGraph,
            "<Prone to error: Only works with consistently monodic parts>",
        ],
        [
            "SHOW: Dolan",
            predefinedVisualizations_Dolan,
            "<Change in volume over time>",
        ],
        ["BACK: Back to the main menu", "nothing", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Untermenü Einzelwerk (zweite Ebene, Mustersuche)

# In[87]:


def Eintraege_Untermenue_Einzelwerk_patternSearch():
    list_de = [
        [
            "SEAR: Mustersuche (ohne Rhythmus)",
            patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm,
            "<Suche einer unrhythmisierten Tonfolge>",
        ],
        [
            "SEAR: Mustersuche (ohne Rhythmus/transponiert)",
            patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm,
            "<Suche einer unrhythmisierten Tonfolge und sämtlicher Transpositionen>",
        ],
        [
            "SEAR: Mustersuche (mit Rhythmus)",
            patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm,
            "<Suche einer rhythmisierten Tonfolge>",
        ],
        [
            "SEAR: Mustersuche (mit Rhythmus/transponiert)",
            patternSearch_menuStructure_toneSequence_withTransposition_withRhythm,
            "<Suche einer rhythmisierten Tonfolge und sämtlicher Transpositionen>",
        ],
        [
            "SEAR: Mustersuche (nur Rhythms)",
            patternSearch_menuStructure_rhythm_withoutPitch,
            "<Suche einer Rhythmusfolge ohne Tonhöhen>",
        ],
        ["BACK: Zurück ins Hauptmenü", "nothing", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "SEAR: Pattern search (without rhythmic values)",
            patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm,
            "<Search for a sequence of notes (without rhythmic values)>",
        ],
        [
            "SEAR: Pattern search (without rhythmic values/transposed)",
            patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm,
            "<Search for a sequence of notes and all of its transpositions (without rhythmic values)>",
        ],
        [
            "SEAR: Pattern search (with rhythmic values)",
            patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm,
            "<Search for a sequence of notes (with rhythmic values)>",
        ],
        [
            "SEAR: Pattern search (with rhythmic values/transposed)",
            patternSearch_menuStructure_toneSequence_withTransposition_withRhythm,
            "<Search for a sequence of notes and all of its transpositions (with rhythmic values)>",
        ],
        [
            "SEAR: Pattern search (only rhythm)",
            patternSearch_menuStructure_rhythm_withoutPitch,
            "<Search for a specific rhythm>",
        ],
        ["BACK: Back to the main menu", "nothing", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Untermenü Einzelwerk (zweite Ebene, Einstellungen)

# In[88]:


def Eintraege_Untermenue_Einzelwerk_settings():
    list_de = [
        [
            "ENVT: Environment-Datei (Pfad)",
            environmentFile_path,
            "<Gibt den Pfad der environment-Datei aus (falls vorhanden)>",
        ],
        [
            "ENVT: Einstellungen anzeigen",
            show_environmentFile_settings,
            "<Anzeigen der Einstellungen in der Environment-Datei>",
        ],
        [
            "ENVT: Einstellungen neu konfigurieren",
            EnvironmentFile_settings_reconfigure,
            "<Neukonfiguaration der Environment-Datei>",
        ],
        [
            "LANG: Change language to ENGLISH",
            change_language,
            "<Change the output language of the program to German>",
        ],
        ["BACK: Zurück ins Hauptmenü", "nothing", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "ENVT: Environment file (path)",
            environmentFile_path,
            "<Outputs the path of the environment file (if available)>",
        ],
        [
            "ENVT: Show settings",
            show_environmentFile_settings,
            "<Display the settings in the environment file>",
        ],
        [
            "ENVT: Reconfigure settings",
            EnvironmentFile_settings_reconfigure,
            "<Reconfiguration of the environment file>",
        ],
        [
            "LANG: Ändere Ausgabesprache auf DEUTSCH",
            change_language,
            "<Ändert die Ausgabesprache des Programms auf Deutsch>",
        ],
        ["BACK: Back to the main menu", "nothing", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ## Startmenü

# ### Menüstrukturen

# In[89]:


def open_startmenu():
    while True:
        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(Eintraege_Startmenue(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        clear_screen()

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if 0 <= Input_Menueauswahl_Int < len(Eintraege_Startmenue()):
                clear_screen()

                Eintraege_Startmenue()[Input_Menueauswahl_Int][1]()

                clear_screen()

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(Eintraege_Startmenue())
                    )
                )
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(Eintraege_Startmenue()))
            )
            print("")

            Input = input(text_general_proceed())
            print("")


# ### Menüeinträge

# In[90]:


def Eintraege_Startmenue():
    list_de = [
        [
            "PROG: Analyse eines einzelnen Werkes",
            open_mainmenu_individualPiece,
            "<Analyse eines einzelnen Werkes>",
        ],
        [
            "SETT: Einstellungen",
            open_submenu_individualPiece_settings,
            "<Einstellungen in der music21 environment-Datei>",
        ],
        [
            "HELP: Projektübersicht",
            text_general_projectDescription,
            '<Informationen über das Projekt "Computergestützte Musikanalyse">',
        ],
        [
            "LANG: Change language to ENGLISH",
            change_language,
            "<Change the output language of the program to German>",
        ],
        ["EXIT: Programm beenden", terminateProgram, "<Beendet das Python-Skript>"],
    ]

    list_en = [
        [
            "PROG: Analysis of a single piece of music",
            open_mainmenu_individualPiece,
            "<Analysis of a single piece of music>",
        ],
        [
            "SETT: Settings",
            open_submenu_individualPiece_settings,
            "<View the settings in the music21 environment file>",
        ],
        [
            "HELP: Project overview",
            text_general_projectDescription,
            '<Information about the project "Computer-Aided Music Analysis">',
        ],
        [
            "LANG: Ändere Ausgabesprache auf DEUTSCH",
            change_language,
            "<Ändert die Ausgabesprache des Programms auf Deutsch>",
        ],
        ["EXIT: Exit programm", terminateProgram, "<Exits the Python script>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ## Allgemein

# ### Auswahlmenü

# #### Auswahl Eintrag aus Liste (Rückgabe der Listeneinträge)

# Stellt den Inhalt eines Arrays (= Liste) als Liste mit Indices dar. Zurückgegeben wird nicht der Inhalt der Liste, sondern die aus der Liste ausgewählte Nummer.

# In[91]:


def open_submenu_Rueckgabe_IndexausListe(Liste):
    while True:
        clear_screen()

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplenation()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(Liste, 1):
            print("{:<4} {:<65}".format(index, item))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if 0 <= Input_Menueauswahl_Int < len(Liste):
                clear_screen()

                # Rückgabe der ausgewählten Nummer

                return Input_Menueauswahl_Int

            else:
                print(text_menu_exception_selectionOutOfRange(len(Liste)))
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(Liste)))
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Daten ohne 'Erläuterung'

# In[92]:


def open_submenu_Daten(Liste):
    while True:
        clear_screen()

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplenation()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(Liste, 1):
            print("{:<4} {:<65}".format(index, item[0]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if 0 <= Input_Menueauswahl_Int < len(Liste):
                clear_screen()

                return Liste[Input_Menueauswahl_Int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(Liste)))
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(Liste)))
            print("")

            Input = input(text_general_proceed())
            print("")


# #### Daten mit 'Erläuterung'

# In[93]:


def open_submenu_Daten_mit_Info(Liste):
    while True:
        clear_screen()

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplenation()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(Liste, 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        Input_Menueauswahl = input(text_menu_selection_input())
        print("")

        if str.isdigit(Input_Menueauswahl):
            Input_Menueauswahl_Int = int(Input_Menueauswahl) - 1

            if 0 <= Input_Menueauswahl_Int < len(Liste):
                clear_screen()

                return Liste[Input_Menueauswahl_Int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(Liste)))
                print("")

                Input = input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(Liste)))
            print("")

            Input = input(text_general_proceed())
            print("")


# #### show_resultslist

# In[94]:


def show_resultslist(Beschreibung, Daten):
    try:
        # Beschreibung = ['Beschreibung1', 'Beschreibung2', ...]

        clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("\n")

        if len(Daten) == 0:
            print(text_general_noResults())
            print("")

        else:
            menu_header = ""

            # converts every item in List to a string

            m = 0

            n = 0

            for item in Daten:
                m = Daten.index(item)

                for Inhalt in item:
                    n = item.index(Inhalt)

                    Daten[m][n] = str(Inhalt)

            Beschreibung_und_Daten = [Beschreibung] + Daten

            max_lengths_dict = {}

            n = 0

            while n < len(Beschreibung):
                max_lengths_dict[n] = 0

                n = n + 1

            for item in Beschreibung_und_Daten:
                for Inhalt in item:
                    if len(Inhalt) >= max_lengths_dict[item.index(Inhalt)]:
                        max_lengths_dict[item.index(Inhalt)] = len(Inhalt)

            for item in Beschreibung:
                menu_header = (
                    menu_header
                    + f"{item:<{max_lengths_dict[Beschreibung.index(item)] + 7}s}"
                )

            print(menu_header)
            print("\n")

            for item in Daten:
                Daten_String = ""

                for Inhalt in item:
                    Daten_String = (
                        Daten_String
                        + f"{Inhalt:<{max_lengths_dict[item.index(Inhalt)] + 7}s}"
                    )

                print(Daten_String)
                print("")

            print("\n")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    Input = input(text_general_proceed())
    print("")


# ### Menüeinträge

# #### Tonarten

# In[2]:


def keys_list():
    list_de = [
        ["C-Dur", "C"],
        ["G-Dur", "G"],
        ["D-Dur", "D"],
        ["A-Dur", "A"],
        ["E-Dur", "E"],
        ["H-Dur", "B"],
        ["Fis-Dur", "F#"],
        ["Cis-Dur", "C#"],
        ["Gis-Dur", "G#"],
        ["Dis-Dur", "D#"],
        ["Ais-Dur", "A#"],
        ["Eis-Dur", "E#"],
        ["His-Dur", "B#"],
        ["F-Dur", "F"],
        ["B-Dur", "B-"],
        ["Es-Dur", "E-"],
        ["As-Dur", "A-"],
        ["Des-Dur", "D-"],
        ["Ges-Dur", "G-"],
        ["Ces-Dur", "C-"],
        ["Fes-Dur", "F-"],
        ["C-Moll", "c"],
        ["G-Moll", "g"],
        ["D-Moll", "d"],
        ["A-Moll", "a"],
        ["E-Moll", "e"],
        ["H-Moll", "b"],
        ["Fis-Moll", "f#"],
        ["Cis-Moll", "c#"],
        ["Gis-Moll", "g#"],
        ["Dis-Moll", "d#"],
        ["Ais-Moll", "a#"],
        ["Eis-Moll", "e#"],
        ["His-Moll", "b#"],
        ["F-Moll", "f"],
        ["B-Moll", "b-"],
        ["Es-Moll", "e-"],
        ["As-Moll", "a-"],
        ["Des-Moll", "d-"],
        ["Ges-Moll", "g-"],
        ["Ces-Moll", "c-"],
        ["Fes-Moll", "f-"],
    ]

    list_en = [
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

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Environment-Einstellungen

# In[96]:


us = environment.UserSettings()

EnvironmentFile_settings = [
    ["autoDownload", "autoDownload", str(us["autoDownload"])],
    ["braillePath", "braillePath", str(us["braillePath"])],
    ["debug", "debug", str(us["debug"])],
    ["directoryScratch", "directoryScratch", str(us["directoryScratch"])],
    ["graphicsPath", "graphicsPath", str(us["graphicsPath"])],
    ["ipythonShowFormat", "ipythonShowFormat", str(us["ipythonShowFormat"])],
    ["lilypondBackend", "lilypondBackend", str(us["lilypondBackend"])],
    ["lilypondFormat", "lilypondFormat", str(us["lilypondFormat"])],
    ["lilypondPath", "lilypondPath", str(us["lilypondPath"])],
    ["lilypondVersion", "lilypondVersion", str(us["lilypondVersion"])],
    ["localCorporaSettings", "localCorporaSettings", str(us["localCorporaSettings"])],
    ["localCorpusPath", "localCorpusPath", str(us["localCorpusPath"])],
    ["localCorpusSettings", "localCorpusSettings", str(us["localCorpusSettings"])],
    ["manualCoreCorpusPath", "manualCoreCorpusPath", str(us["manualCoreCorpusPath"])],
    ["midiPath", "midiPath", str(us["midiPath"])],
    ["musescoreDirectPNGPath", "musescoreDirectPNGPath", str(us["musescoreDirectPNGPath"])],
    ["musicxmlPath", "musicxmlPath", str(us["musicxmlPath"])],
    ["pdfPath", "pdfPath", str(us["pdfPath"])],
    ["showFormat", "showFormat", str(us["showFormat"])],
    ["vectorPath", "vectorPath", str(us["vectorPath"])],
    ["warnings", "warnings", str(us["warnings"])],
    ["writeFormat", "writeFormat", str(us["writeFormat"])],
]


# #### Modul-Navigation

# In[97]:


def Modul_Navigation():
    list_de = [
        [
            "REPT: Neue Notenauswahl",
            "Repeat",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "EXPT: Ergebnisse als CSV-Datei exportieren",
            "Export_CSV",
            "<Exportiert und speichert die Ergebnisse als CSV-Datei>",
        ],
        [
            "GRPH: Ergebnisse als Grafik anzeigen",
            "Export_Grafik",
            "<Exportiert und speichert die Ergebnisse als Grafik>",
        ],
        ["BACK: Zurück ins Hauptmenü", "Back", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New score selection",
            "Repeat",
            "<Repeat the tool with new score selection>",
        ],
        [
            "EXPT: Export results as CSV file",
            "Export_CSV",
            "<Exports and saves the results as CSV file>",
        ],
        [
            "GRPH: Display results as graphic",
            "Export_Grafik",
            "<Exports and saves the results as graphic>",
        ],
        ["BACK: Back to the main menu", "Back", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (Mustersuche)

# In[98]:


def modul_navigation_patternSearch():
    list_de = [
        [
            "REPT: Neue Suchmusterauswahl",
            "Repeat",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "EXPT: Ergebnisse als CSV-Datei exportieren",
            "Export_CSV",
            "<Exportiert und speichert die Ergebnisse als CSV-Datei>",
        ],
        [
            "GRPH: Ergebnisse als XML-Datei exportieren",
            "Export_Notentext",
            "<Exportiert und speichert die Ergebnisse farblich markiert als XML-Datei>",
        ],
        ["BACK: Zurück ins Hauptmenü", "Back", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New search pattern selection", "Repeat", "<Repeat the tool with new score selection>",
        ],
        [
            "EXPT: Export results as CSV file",
            "Export_CSV",
            "<Exports and saves the results as CSV file>",
        ],
        [
            "GRPH: Export results as XML file",
            "Export_Notentext",
            "<Exports and saves the results highlighted in a xml file>",
        ],
        ["BACK: Back to the main menu", "Back", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (selectedScore)

# In[99]:


def modul_navigation_selectedScore():
    list_de = [
        [
            "Notenauswahl: vollständige Partitur",
            "Komplett",
            "<Auswahl der gesamten Partitur>",
        ],
        [
            "Notenauswahl: Taktausschnitt (Stimme/Partitur)",
            "Neue_Auswahl",
            "<Taktauswahl aus der Partitur oder einer Einzelstimme>",
        ],
        [
            "Notenauswahl: vorherige Auswahl wiederholen",
            "Wiederhole_Auswahl",
            "<Wiederholung der letzten Notenauswahl>",
        ],
    ]

    list_en = [
        [
            "Score selection: complete score",
            "Komplett",
            "<Selection of the entire score>",
        ],
        [
            "Score selection: bar excerpt (part / score)",
            "Neue_Auswahl",
            "<bar selection from the score or a single part>",
        ],
        [
            "Score selection: repeat previous selection",
            "Wiederhole_Auswahl",
            "<Repeat last score selection>",
        ],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (Benennung Einzelstimmen)

# In[100]:


def modul_navigation_Benennung_Einzelstimmen():
    list_de = [
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            "Darstellung_MuseScore",
            "<Öffnet MuseScore und zeigt die Notenauswahl an>",
        ],
        [
            "NAME: generische Stimmenbezeichnungen",
            "generisch",
            "<Vergabe generischer Stimmenbezeichnungen (Stimme 1, Stimme 2 etc.)>",
        ],
        [
            "NAME: selbstgewählte Stimmenbezeichnungen",
            "benutzerdefiniert",
            "<Vergabe selbstgewählter Stimmenbezeichnungen>",
        ],
    ]

    list_en = [
        [
            "SHOW: Show score selection (MuseScore)",
            "Darstellung_MuseScore",
            "<Opens MuseScore and displays the selected score>",
        ],
        [
            "NAME: generic voice/part designations",
            "generisch",
            "<Assignment of generic voice/part designations (Part 1, Part 2 etc.)>",
        ],
        [
            "NAME: self-selected voice/part designations",
            "benutzerdefiniert",
            "<assignment of self-selected voice/part designations>",
        ],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (transformierter Notentext)

# In[101]:


def modul_navigation_transformierter_Notentext():
    list_de = [
        [
            "REPT: Neue Notenauswahl",
            "Repeat",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            "Darstellung_MuseScore",
            "<Öffnet MuseScore und zeigt den transformierten Notentext an>",
        ],
        [
            "SAVE: Datei speichern",
            "Noten_speichern",
            '<Speichert den transformierten Notentext als .xml-Datei im "scratch-Ordner" von music21>',
        ],
        ["BACK: Zurück ins Hauptmenü", "Back", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New score selection",
            "Repeat",
            "<Repeat the tool with new score selection>",
        ],
        [
            "SHOW: Show score selection (MuseScore)",
            "Darstellung_MuseScore",
            "<Opens MuseScore and shows the transformed note text>",
        ],
        [
            "SAVE: Save file",
            "Noten_speichern",
            '<Saves the transformed music text as an .xml file in the "scratch folder" of music21>',
        ],
        ["BACK: Back to the main menu", "Back", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (Konvertierung)

# In[102]:


def modul_navigation_Konvertierung():
    list_de = [
        [
            "XML : Konvertierung nach .xml",
            "XML",
            "<Konvertiert die Datei ins .xml-Format>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_Akkord",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen)>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_Akkord_Generalbass",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen + Generalbass>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_Akkord_Stufen",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen + Stufenbezifferung)>",
        ],
        [
            "MIDI: Konvertierung nach .midi",
            "MIDI",
            "<Konvertiert die Datei ins .midi-Format>",
        ],
        [
            "BRLL: Konvertierung nach .txt (music21)",
            "TXT_music21",
            "<Exportiert die Notenauswahl im music21-Format als .txt-Datei>",
        ],
        [
            "BRLL: Konvertierung nach .txt (music21/textline)",
            "TXT_music21_textline",
            "<Exportiert die Notenauswahl im music21-Format als .txt-Datei (textline)>",
        ],
        [
            "BRLL: Konvertierung nach .txt (Braille)",
            "TXT_BRAILLE",
            "<Speichert die Datei im .txt-Braille-Format>",
        ],
        [
            "LILY: Konvertierung nach .ly (LilyPond)",
            "LILY",
            "<Konvertiert die Datei ins .ly-Format>",
        ],
        [
            "PDF : Als PDF exportieren",
            "PDF",
            "<Speichert die Datei im .pdf-Format. Setzt eine Installation von Lilypond voraus!>",
        ],
        [
            "PNG : Als PNG exportieren",
            "PNG",
            "<Speichert die Datei im .png-Format. Setzt eine Installation von Lilypond voraus!>",
        ],
        ["BACK: Zurück ins Hauptmenü", "Back", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        ["XML : Conversion to .xml", "XML", "<Converts the file to .xml format>"],
        [
            "XML : conversion to .xml",
            "XML_Akkord",
            "<Converts the file to .xml format (transformation to chord connections)>",
        ],
        [
            "XML : conversion to .xml",
            "XML_Akkord_Generalbass",
            "<Converts the file to .xml format (transformation to chord connections + figured bass>",
        ],
        [
            "XML : conversion to .xml",
            "XML_Akkord_Stufen",
            "<Converts the file to .xml format (transformation to chord connections + numbering of levels)>",
        ],
        ["MIDI: Conversion to .midi", "MIDI",
            "<Converts the file to .midi format>"],
        [
            "BRLL: Conversion to .txt (music21)",
            "TXT_music21",
            "<Exports the note selection in music21 format as a .txt file>",
        ],
        [
            "BRLL: Conversion to .txt (music21 / textline)",
            "TXT_music21_textline",
            "<Exports the sheet music selection in music21 format as a .txt file (textline)>",
        ],
        [
            "BRLL: Conversion to .txt (Braille)",
            "TXT_BRAILLE",
            "<Saves the file in .txt Braille format>",
        ],
        [
            "LILY: Conversion to .ly (LilyPond)",
            "LILY",
            "<Converts the file to .ly format>",
        ],
        [
            "PDF : Export as PDF",
            "PDF",
            "<Saves the file in .pdf format. Requires an installation of Lilypond!> ",
        ],
        [
            "PNG : Export as PNG",
            "PNG",
            "<Saves the file in .png format. Requires an installation of Lilypond!> ",
        ],
        ["BACK: Back to the main menu", "Back", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ## Ausgabe eines Textes zur Beschreibung des Projektes

# In[4]:


def Start_Ausgabe_Text():
    clear_screen()

    text = (
        "Funding period: one year; Start: January 1, 2021\n\n"
        "Funded by the Stifterverband together with the Thuringian Ministry of Economics,\n"
        "Science and Digital Society as part of the fellowship program for innovations in digital university teaching.\n\n"
        "-- Project team --\n\n\n"
        "-- Project management  --\n\n"
        "{:<50} {}\n\n".format(
            "Prof. Dr. Martin Pfleiderer", "<martin.pfleiderer@hfm-weimar.de>"
        ),
        "Institute for Musicology Weimar-Jena - University of Music FRANZ LISZT Weimar\n\n",
        "-- Scientific Assistants --\n\n",
        "{:<50} {}\n".format("Egor Polyakov", "<egor.polyakov@hfm-weimar.de>"),
        "{:<50} {}\n\n".format("Christon-Ragavan Nadar", ""),
        "-- Student staff --\n\n",
        "{:<50} {}\n".format("Sebastian Oliver Eck",
                             "<sebastian.eck@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Juan Sebastián Paez Medina",
                             "<juan.sebastian.paez.medina@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Andres Romero Varon",
                             "<andres.romero.varon@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Esther Johanna Barta", ""),
        "{:<50} {}\n\n".format("Clarissa Henriette Mühlhausen", ""),
        "-- Program code --\n\n",
        "{:<50} {}\n\n".format("Sebastian Oliver Eck",
                               "<sebastian.eck@hfm.uni-weimar.de>"),
        "-- Search routines --\n\n",
        "{:<50} {}\n".format("Sebastian Oliver Eck",
                             "<sebastian.eck@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Juan Sebastián Paez Medina",
                             "<juan.sebastian.paez.medina@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Andres Romero Varon",
                             "<andres.romero.varon@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Egor Polyakov", "<egor.polyakov@hfm-weimar.de>"),
        "{:<50} {}\n\n".format("Christon-Ragavan Nadar", ""),
        "Using Music21 (MIT, Massachusetts, Cambridge, USA): [https://web.mit.edu/music21/]\n\n",
        "<Please use the program in full screen mode if possible>\n\n"
    )

    print("".join(text))
    Input = input(text_general_proceed())

    clear_screen()


# ## Start der zeichenorientierten Benutzerschnittstelle (CLI)

# ### Prüfen der EnvironmentDatei

# In[8]:


check_environmentFile()


# ### Ausgabe der Projektbeschreibung

# In[9]:


Start_Ausgabe_Text()


# ### Öffnen des Startmenüs

# In[ ]:


open_startmenu()
