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
        "notes_quantity_total_textOutput": ["Kennung", "Anzahl Töne"],
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
        "patternSearch_menuStructure_withRhythm_withoutPitch": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote",
        ],
        "show_names_individualVoices": ["Nr.", "Name der Stimme"],
        "name_individualVoices": ["Nr.", "Name der Stimme"],
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
        "notes_quantity_total_textOutput": ["Identifier", "Number of tones"],
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
        "patternSearch_menuStructure_withRhythm_withoutPitch": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "show_names_individualVoices": ["No.", "Part name"],
        "name_individualVoices": ["No.", "Part name"],
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
        "\nI-MaT - Interaktives Musikanalyse previousTool, (2.2, 01.2022)\n\n"
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
            utility_clear_screen()

            print(text_de)

        elif LANGUAGE == "EN":
            utility_clear_screen()

            print(text_en)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
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
    text_de = "Für dieses previousTool ist ein Datenexport als Grafikdiagramm nicht vorgesehen."

    text_en = "data_values export as a graphic is not intended for this tool."

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
    text_de = "Unter welchem Namen soll die Datei gespeichert werden? filename: "

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
        "filename: " + str(name) + str(extension)
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
    text_de = "Möchten Sie das previousTool mit einer anderen Notenauswahl wiederholen? 'nein' => Hauptmenü (ja/nein): "

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
        "name_individualVoices": "-- Konfiguration: Stimmnamen --",
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
        "name_individualVoices": "-- Configuration: part names --",
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

# #### Without Explanation

# In[ ]:


def text_menu_headers_withoutExplanationsColumn():
    list_de = ["Nr.", "Menüpunkt"]

    list_en = ["No.", "Menu item"]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### With Explanation

# In[ ]:


def text_menu_headers_withExplanationsColumn():
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


def text_score_selectFirstMeasure(number_of_bars, selected_score):
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


def text_score_selectLastMeasure(number_of_bars, selected_score, bars_selection_start):
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


def text_metadata_availableMetadata_none():
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

    user_input = input(text_general_terminateProgram())
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
                utility_clear_screen()

                input_text = input(text_environmentFile_createNewFile(environmentFile_path))
                print("")

                if utility_userInput_isAffirmative(input_text):
                    utility_clear_screen()

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

                        utility_clear_screen()

                        environmentFile_enterPath_MuseScore3()

                        environmentFile_enterPath_scratchFolder()

                        loopDone = True

                    except Exception as e:
                        print(text_exception_general(
                            e, sys._getframe().f_code.co_name))
                        print("")

                        loopDone = True

                        input_text = input(text_general_proceed())
                        print("")

                elif utility_userInput_isNegative(input_text):
                    utility_clear_screen()

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

    utility_clear_screen()


# ### Path input MuseScore3

# In[14]:


def environmentFile_enterPath_MuseScore3():
    loopDone = False

    while not loopDone:
        utility_clear_screen()

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
                user_input = input(text_general_checkEntry())
                print("")

                if utility_userInput_isAffirmative(user_input):
                    loopDone = True
                    loop2Done = True

                    us["musescoreDirectPNGPath"] = MuseScore3_Pfad

                    us["musicxmlPath"] = MuseScore3_Pfad

                    print("\n")

                    utility_clear_screen()

                elif utility_userInput_isNegative(user_input):
                    loopDone = False
                    loop2Done = True

                    utility_clear_screen()

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop2Done = False

                    input(text_general_proceed())
                    print("")

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")

            loopDone = False

    utility_clear_screen()


# ### Path input Scratch folder

# In[15]:


def environmentFile_enterPath_scratchFolder():
    loopDone = False

    while not loopDone:
        utility_clear_screen()

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
                user_input = input(text_general_checkEntry())
                print("")

                if utility_userInput_isAffirmative(user_input):
                    loopDone = True
                    loop2Done = True

                    us["directoryScratch"] = Scratch_Ordner_Pfad

                    utility_clear_screen()

                elif utility_userInput_isNegative(user_input):
                    loopDone = False
                    loop2Done = True

                    utility_clear_screen()

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loop2Done = False

                    input(text_general_proceed())
                    print("")

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")

            loopDone = False

    utility_clear_screen()


# ## Constants


# ### Language

global LANGUAGE

LANGUAGE = "EN"

# ### Environment File Settings

# In[16]:


us = environment.UserSettings()

environmentFile_settings = [
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


# # Utility Programs

# ## Without User Input

# ### Playing back a music file (MIDI)

# In[17]:


def utility_playback_MIDI():
    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    print(text_general_close_audioPlayer())
    print("")

    # --- Unterhalb: Code des Tools ---

    try:
        temporary_selectedScore.show("midi")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    # --- Oberhalb: Code des Tools ---

    # --- Nachfolgend: Fragt den User, ob das previousTool mit einer neuen Notenauswahl wiederholt werden soll

    menu_askUser_repeatPreviousTool(utility_playback_MIDI)


# ### Erhalte Key zu Value

# In[18]:


def utility_getKeyToValue(val, dictionary):
    try:
        for key, value in dictionary.items():
            if val == value:
                return key

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Sortieren eines Dictionaries nach Größe der Values (aufsteigend)

# In[19]:


# Quelle: Example- Counting Numbers in a List, https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637


def utility_count(num_list):
    try:
        count_dict = {}

        for num in num_list:
            count_dict[num] = num_list.count(num)

        return dict(sorted(count_dict.items(), key=lambda x: x[1]))

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Bildschirm leeren

# In[21]:


def utility_clear_screen():
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

        user_input = input(text_general_terminateProgram())
        print("")

        utility_terminateProgram()


# ### Rückgabe Wahrheitswert

# #### ja / 1

# In[25]:


def utility_userInput_isAffirmative(user_input):
    if user_input == "ja" or user_input == "1" or user_input == "yes":
        return True

    else:
        return False


# #### nein / 0

# In[26]:


def utility_userInput_isNegative(user_input):
    if user_input == "nein" or user_input == "0" or user_input == "no":
        return True

    else:
        return False


# #### is number

# In[ ]:


def utility_userInput_isNumber(user_input):
    try:
        float(user_input)

        return True

    except:
        try:
            m, n = map(float, user_input.split("/"))

            return True

        except:
            return False


# ### Programm beenden

# In[27]:


def utility_terminateProgram():
    exit()


# ### CSV-Export

# In[28]:


def utility_export_as_csv(
    data,
    columns,
    save_at,
    do_print=False,
    do_return_pd=False,
    sep=";",
    index=False,
    header=True,
):
    # data = [[row1 column1, row1 column2], [row2 column1, row2 column2] ...]

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

        input(text_general_proceed())
        print("")


# ### Liste als String

# In[31]:


def utility_listToString(received_list):
    try:
        string = " ".join(
            [
                str(item)
                .replace("'", "")
                .replace(" ", "")
                .replace(",", ": ")
                .replace("[", "")
                .replace("]", "")
                for item in received_list
            ]
        )

        return string

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Environment

# #### Pfad

# In[9]:


def environmentFile_path():
    utility_clear_screen()

    try:
        us = environment.UserSettings()

        print(text_environmentFile_showPath(us.getSettingsPath()))
        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


# #### Einstellungen Anzeigen

# In[23]:


def show_environmentFile_settings():
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        us = environment.UserSettings()

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(environmentFile_settings, 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    utility_clear_screen()


# #### Einstellungen (Neukonfiguration)

# In[1]:


def environmentFile_settings_reconfigure():
    try:
        us = environment.UserSettings()

        environmentFile_path = us.getSettingsPath()

        if os.path.exists(environmentFile_path):
            loopDone = False

            while not loopDone:
                utility_clear_screen()

                print(text_environmentFile_showPath(environmentFile_path))
                print("")

                user_input = input(text_environmentFile_reconfigure_askDelete())
                print("")

                if utility_userInput_isAffirmative(user_input):
                    os.remove(environmentFile_path)

                    print(text_environmentFile_reconfigure_deleted())
                    print("")

                    user_input = input(text_general_proceed())
                    print("")

                    utility_clear_screen()

                    us.create()

                    us["autoDownload"] = "allow"

                    print(
                        text_environmentFile_createNewFile_created(
                            us.getSettingsPath())
                    )
                    print("")

                    user_input = input(text_general_proceed())
                    print("")

                    utility_clear_screen()

                    environmentFile_enterPath_MuseScore3()

                    environmentFile_enterPath_scratchFolder()

                    loopDone = True

                elif utility_userInput_isNegative(user_input):
                    loopDone = True

                    print(text_environmentFile_reconfigure_notDeleted())
                    print()

                    user_input = input(text_general_proceed())
                    print("")

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    user_input = input(text_general_proceed())
                    print("")

                    loopDone = False

        else:
            loopDone = False

            while not loopDone:
                utility_clear_screen()

                user_input = input(text_environmentFile_createNewFile(us.getSettingsPath()))
                print("")

                if utility_userInput_isAffirmative(user_input):
                    us.create()

                    us["autoDownload"] = "allow"

                    print(
                        text_environmentFile_createNewFile_created(
                            us.getSettingsPath())
                    )
                    print("")

                    user_input = input(text_general_proceed())
                    print("")

                    utility_clear_screen()

                    environmentFile_enterPath_MuseScore3()

                    environmentFile_enterPath_scratchFolder()

                    loopDone = True

                elif utility_userInput_isNegative(user_input):
                    print(text_environmentFile_createNewFile_noFileCreated())
                    print("")

                    user_input = input(text_general_proceed())
                    print("")

                    loopDone = True

                else:
                    print(text_general_input_RestrictedToYesAndNo())
                    print("")

                    loopDone = False

                    user_input = input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        user_input = input(text_general_proceed())
        print("")


# ## Mit Input

# ### Auswahl des Pfades/der URL einer Notendatei

# In[32]:


def select_score_filePath():
    try:
        # Erstellen einer globalen Variabel 'Partitur', auf die von jeder Stelle im Programm aus zugegriffen werden kann.

        global global_score

        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        # Ausgabe eines Auswahlmenüs, das den Benutzer zwischen einer "Beispiel-Datei" und einer "Eigenen Auswahl" auswählen lässt (s. .

        user_selection = open_submenu_data_withExplanationsColumn(
            menue_entries_score_selection())

        if user_selection == "Beispiel-Datei":
            global_score = converter.parse(
                "https://analyse.hfm-weimar.de/database/02/PrJode_Jos0602_COM_1-5_MissaLhomm_002_00066.xml"
            )

        else:
            loopDone = False

            while not loopDone:
                utility_clear_screen()

                print(menu_header)
                print("")

                print(text_score_selection())
                print("")

                global_score_path_input = input(text_general_enter_newPath())
                print("")

                try:
                    loop2Done = False

                    while not loop2Done:
                        utility_clear_screen()

                        print(menu_header)
                        print("")

                        print(text_score_selection())
                        print("")

                        global_score_path = global_score_path_input.replace(
                            '"', "")

                        print(text_general_show_enteredPath(global_score_path))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            start = time.time()

                            try:
                                global_score = converter.parse(global_score_path)

                                print(
                                    text_score_selectionSuccessful(
                                        time.time() - start)
                                )
                                print("")

                                user_input = input(text_general_proceed())
                                print("")

                                loopDone = True
                                loop2Done = True

                                utility_clear_screen()

                            except Exception as e:
                                print(
                                    text_exception_general(
                                        e, sys._getframe().f_code.co_name
                                    )
                                )
                                print("")

                                print(text_score_selectionException())
                                print("")

                                user_input = input(text_general_proceed())
                                print("")

                                loopDone = False
                                loop2Done = True

                                utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loopDone = False
                            loop2Done = True

                            utility_clear_screen()

                            print(menu_header)
                            print("")

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop2Done = False

                            user_input = input(text_general_proceed())
                            print("")

                except Exception as e:
                    print(text_exception_general(
                        e, sys._getframe().f_code.co_name))
                    print("")

                    user_input = input(text_general_proceed())
                    print("")

        show_score_metadata()

        name_individualVoices()

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        user_input = input(text_general_proceed())
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


def name_individualVoices():
    global global_catalogue_individualParts

    global global_catalogue_completeScoreWithIndividualParts

    try:
        parts_names = ["none"] * len(global_score.parts)
        parts_data = ["none"] * len(global_score.parts)

        n = 0

        while n < len(global_score.parts):
            parts_data[n] = global_score.parts[n]

            n = n + 1

        user_selection = open_submenu_data_withExplanationsColumn(
            module_navigation_name_individualVoices()
        )

        if user_selection == "visualizations_MuseScore":
            print(text_general_close_museScore3())
            print()

            global_score.show()

            name_individualVoices()

        elif user_selection == "customDesignations":
            loop1Done = False

            while not loop1Done:
                n = 0

                while n < len(global_score.parts):
                    utility_clear_screen()

                    menu_header = text_menu_headers(sys._getframe().f_code.co_name)

                    print(menu_header)
                    print("")

                    Input_Stimmen_Namen = input(
                        text_metadata_partsNames_chooseName(
                            len(global_score.parts), n + 1)
                    )
                    print("")

                    if not Input_Stimmen_Namen in parts_names:
                        loop2Done = False

                        while not loop2Done:
                            utility_clear_screen()

                            menu_header = text_menu_headers(
                                sys._getframe().f_code.co_name)

                            print(menu_header)
                            print("")

                            print(
                                text_metadata_partsNames_checkEnteredName(
                                    len(global_score.parts), n +
                                    1, Input_Stimmen_Namen
                                )
                            )
                            print("")

                            user_input = input(text_general_checkEntry())
                            print("")

                            if utility_userInput_isAffirmative(user_input):
                                parts_names[n] = Input_Stimmen_Namen

                                n = n + 1

                                loop2Done = True

                            elif utility_userInput_isNegative(user_input):
                                loop2Done = True

                            else:
                                print(text_general_input_RestrictedToYesAndNo())
                                print("")

                                input(text_general_proceed())
                                print("")

                    else:
                        print(text_metadata_partsNames_chooseName_notUnique())

                        input(text_general_proceed())
                        print("")

                loop2Done = False

                while not loop2Done:
                    utility_clear_screen()

                    menu_header = text_menu_headers(sys._getframe().f_code.co_name)

                    print(menu_header)
                    print("")

                    print(text_metadata_partsNames())
                    print("")

                    menu_header = text_headers(sys._getframe().f_code.co_name)

                    print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

                    Index = 1

                    for i in parts_names:
                        print("{:<4} {:<65}".format(Index, i))

                        Index += 1

                    print("")

                    user_input = input(text_general_checkEntry())
                    print("")

                    if utility_userInput_isAffirmative(user_input):
                        utility_clear_screen()

                        loop1Done = True
                        loop2Done = True

                    elif utility_userInput_isNegative(user_input):
                        loop1Done = False
                        loop2Done = True

                        parts_names = ["none"] * len(global_score.parts)

                        utility_clear_screen()

                    else:
                        print(text_general_input_RestrictedToYesAndNo())
                        print("")

                        loop2Done = False

                        input(text_general_proceed())
                        print("")

            # Erstellen eines Dictionarys mit den Namen der Instrumente als 'keys' und den zugehörigen Music21-Pfaden als 'values':

            keys = parts_names

            vals = parts_data

            # Zusammenführen der Listen in ein Dictionary

            global_catalogue_individualParts = dict(zip(keys, vals))

            keys.insert(0, "Score")

            vals.insert(0, global_score)

            global_catalogue_completeScoreWithIndividualParts = dict(zip(keys, vals))

            utility_clear_screen()

        elif user_selection == "genericDesignations":
            if LANGUAGE == "DE":
                n = 0

                while n < len(global_score.parts):
                    parts_names[n] = "Stimme " + str(n + 1)

                    n = n + 1

            elif LANGUAGE == "EN":
                n = 0

                while n < len(global_score.parts):
                    parts_names[n] = "Part " + str(n + 1)

                    n = n + 1

            utility_clear_screen()

            menu_header = text_menu_headers(sys._getframe().f_code.co_name)

            print(menu_header)
            print("")

            print(text_metadata_partsNames())
            print("")

            menu_header = text_headers(sys._getframe().f_code.co_name)

            print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

            Index = 1

            for i in parts_names:
                print("{:<4} {:<65}".format(Index, i))

                Index += 1

            print("")

            input(text_general_proceed())
            print("")

            # Erstellen eines Dictionarys mit den Namen der Instrumente als 'keys' und den zugehörigen Music21-Pfaden als 'values':

            keys = parts_names

            vals = parts_data

            # Zusammenführen der Listen in ein Dictionary

            global_catalogue_individualParts = dict(zip(keys, vals))

            keys.insert(0, "Score")

            vals.insert(0, global_score)

            global_catalogue_completeScoreWithIndividualParts = dict(zip(keys, vals))

            utility_clear_screen()

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Auswahl Noten

# In[34]:


def select_score_completeOrIndividualVoice():
    global global_selectedScore

    global global_input_firstMeasure

    global global_input_lastMeasure

    global global_previously_selectedScore

    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        while True:
            utility_clear_screen()

            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_selectedScore())

            if user_selection == "completeScore":
                
                global_selectedScore = global_score
 
                global_input_firstMeasure = "1"

                number_of_measures = len(
                    global_score.parts[0].getElementsByClass("Measure"))

                global_input_lastMeasure = number_of_measures

                global_previously_selectedScore = global_selectedScore

                return global_selectedScore

            elif user_selection == "newSelection":

                global_selectedScore = menu_askUser_selectCompleteScoreOrIndividualPart()

                selected_measures = select_bars(global_selectedScore)

                global_previously_selectedScore = selected_measures

                return selected_measures

            elif user_selection == "repeatPreviousSelection":
                utility_clear_screen()

                try:
                    global_previously_selectedScore

                    return global_previously_selectedScore

                except:
                    print(text_menu_selection_noPreviousSelection())
                    print("")

                    input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Auswahl Partitur oder Einzelstimme

# In[35]:


def menu_askUser_selectCompleteScoreOrIndividualPart():
    try:
        utility_clear_screen()

        global global_selectedScore

        global_selectedScore = open_submenu_data_withoutExplanationsColumn(
            list(global_catalogue_completeScoreWithIndividualParts.items())
        )

        return global_selectedScore

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Auswahl Takte

# In[36]:


def select_bars(Noten):
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        number_of_measures = len(global_score.parts[0].getElementsByClass("Measure"))

        loopDone = False

        while not loopDone:
            utility_clear_screen()

            print(menu_header)
            print("")

            global global_input_firstMeasure

            global_input_firstMeasure = input(
                text_score_selectFirstMeasure(
                    number_of_measures,
                    utility_getKeyToValue(
                        Noten, global_catalogue_completeScoreWithIndividualParts),
                )
            )
            print("")

            if str.isdigit(global_input_firstMeasure):
                selected_firstMeasure = int(global_input_firstMeasure)

                if selected_firstMeasure >= 1 and selected_firstMeasure <= number_of_measures:
                    loopDone = True

                else:
                    print(text_menu_exception_selectionOutOfRange(number_of_measures))
                    print("")

            else:
                print(text_score_bars_exception_notNumber())
                print("")

        loopDone = False

        while not loopDone:
            utility_clear_screen()

            print(menu_header)
            print("")

            global global_input_lastMeasure

            global_input_lastMeasure = input(
                text_score_selectLastMeasure(
                    number_of_measures,
                    utility_getKeyToValue(
                        Noten, global_catalogue_completeScoreWithIndividualParts),
                    selected_firstMeasure,
                )
            )
            print("")

            if str.isdigit(global_input_lastMeasure):
                selected_last_measure = int(global_input_lastMeasure)

                if (
                    selected_last_measure >= selected_firstMeasure
                    and selected_last_measure <= number_of_measures
                ):
                    loopDone = True

                else:
                    print(
                        text_score_bars_exception_outOfRange(
                            selected_firstMeasure, number_of_measures
                        )
                    )
                    print("")

            else:
                print(text_score_bars_exception_notNumber())
                print("")

        return Noten.measures(selected_firstMeasure, selected_last_measure)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Wiederholen des Tools mit anderer Notenauswahl

# In[37]:


def menu_askUser_repeatPreviousTool(previousTool):
    try:
        while True:
            utility_clear_screen()

            user_input = input(text_menu_selection_repeat())
            print("")

            if utility_userInput_isAffirmative(user_input):
                utility_clear_screen()

                previousTool()

                break

            elif utility_userInput_isNegative(user_input):
                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

                loopDone = False

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Noten Export

# In[38]:


def score_export():
    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_conversion())

            if user_selection == "XML":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = temporary_selectedScore.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "XML_chords":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                selectedScore_chordConnection = temporary_selectedScore.chordify()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "XML_chords_figuredBass":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                selectedScore_chordConnection = temporary_selectedScore.chordify()

                for (
                    item
                ) in selectedScore_chordConnection.recurse().getElementsByClass(
                    "Chord"
                ):
                    item.closedPosition(forceOctave=4, inPlace=True)

                    item.annotateIntervals()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "XML_chords_romanNumerals":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                utility_clear_screen()

                print(text_general_chooseKey())
                print("")

                input(text_general_proceed())
                print("")

                Tonart = open_submenu_data_withoutExplanationsColumn(keys_list())

                selectedScore_chordConnection = temporary_selectedScore.chordify()

                for (
                    item
                ) in selectedScore_chordConnection.recurse().getElementsByClass(
                    "Chord"
                ):
                    rn = roman.romanNumeralFromChord(item, key.Key(Tonart))

                    item.addLyric(str(rn.figure))

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "MIDI":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".midi"
                )

                mf = temporary_selectedScore.write("midi", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".midi"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "TXT_music21":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".txt"
                )

                mf = temporary_selectedScore.write("txt", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".txt"))
                print()

                input(text_general_proceed())

            elif user_selection == "TXT_music21_textline":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".txt"
                )

                mf = temporary_selectedScore.write("textline", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".txt"))
                print()

                input(text_general_proceed())

            elif user_selection == "TXT_braille":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".txt"
                )

                mf = temporary_selectedScore.write("braille", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".txt"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "lilypond":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".ly"
                )

                mf = temporary_selectedScore.write("lily", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".ly"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "PDF":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName().replace(" ", "_"))
                print("")

                path_and_filename = str(score_export_path) + \
                    "\\" + str(filename)

                mf = temporary_selectedScore.write("lily.pdf", fp=str(path_and_filename))

                print(text_general_exportSuccessful(score_export_path, filename, ".pdf"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "PNG":
                temporary_selectedScore = select_score_completeOrIndividualVoice()

                filename = input(text_export_fileName().replace(" ", "_"))
                print("")

                path_and_filename = str(score_export_path) + \
                    "\\" + str(filename)

                mf = temporary_selectedScore.write("lily.png", fp=str(path_and_filename))

                print(text_general_exportSuccessful(score_export_path, filename, ".png"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Darstellung

# #### MuseScore

# In[39]:


def visualizations_MuseScore():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

        print(text_general_close_museScore3())
        print()

        # --- Unterhalb: Code des Tools ---

        temporary_selectedScore.show()

        # --- Oberhalb: Code des Tools ---

        # --- Nachfolgend: Fragt den User, ob das previousTool mit einer neuen Notenauswahl wiederholt werden soll

        menu_askUser_repeatPreviousTool(visualizations_MuseScore)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Notenauswahl als Akkordverbindungen speichern (im 'scratch-Ordner')

# In[40]:


def visualizations_chordConnections():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore_chordConnection = temporary_selectedScore.chordify()

        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_transformedScores()
            )

            if user_selection == "visualizations_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif user_selection == "save_file":
                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "repeatSelection":
                visualizations_chordConnections()

                break

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Notenauswahl als Akkordverbindungen mit Generalbassbezifferung speichern (im 'scratch-Ordner')

# In[41]:


def visualization_chordConnections_figuredBass():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        selectedScore_chordConnection = temporary_selectedScore.chordify()

        for item in selectedScore_chordConnection.recurse().getElementsByClass(
            "Chord"
        ):
            item.closedPosition(forceOctave=4, inPlace=True)

            item.annotateIntervals()

        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_transformedScores()
            )

            if user_selection == "visualizations_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif user_selection == "save_file":
                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "repeatSelection":
                visualization_chordConnections_figuredBass()

                break

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Notenauswahl als Akkordverbindungen mit Stufenbezifferung speichern (im 'scratch-Ordner')

# In[42]:


def visualization_chordConnections_romanNumerals():
    # --- Nachfolgend: Fragt den User, welche Noten ausgewählt werden sollen

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    # --- Nachfolgend: Hinweise zu Bedienung, eingeschränkter Kompatibilität des Tools

    # --- Unterhalb: Code des Tools ---

    try:
        utility_clear_screen()

        print(text_general_chooseKey())
        print("")

        input(text_general_proceed())
        print("")

        Tonart = open_submenu_data_withoutExplanationsColumn(keys_list())

        selectedScore_chordConnection = temporary_selectedScore.chordify()

        for item in selectedScore_chordConnection.recurse().getElementsByClass(
            "Chord"
        ):
            rn = roman.romanNumeralFromChord(item, key.Key(Tonart))

            item.addLyric(str(rn.figure))

        us = environment.UserSettings()

        score_export_path = us["directoryScratch"]

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_transformedScores()
            )

            if user_selection == "visualizations_MuseScore":
                print(text_general_close_museScore3())
                print()

                selectedScore_chordConnection.show()

            elif user_selection == "save_file":
                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = selectedScore_chordConnection.write(
                    "xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "repeatSelection":
                visualization_chordConnections_romanNumerals()

                break

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
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
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_metadata_partsNames())
        print("")

        menu_header = text_headers(sys._getframe().f_code.co_name)

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        Index = 1

        for i in global_catalogue_individualParts.keys():
            print("{:<4} {:<65}".format(Index, i))

            Index += 1

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


# ## Anzeige der Metadaten einer Notendatei

# In[44]:


def show_score_metadata():
    try:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        loopDone = False

        while not loopDone:
            if len(global_score.metadata.all()) > 0:
                print(text_metadata_availableMetadata(
                    len(global_score.metadata.all())))
                print("")

                menu_header = text_headers(sys._getframe().f_code.co_name)

                print("{:<4} {:<30} {:<30}\n".format(
                    menu_header[0], menu_header[1], menu_header[2]))

                Index = 1

                for k, v in dict(global_score.metadata.all()).items():
                    print("{:<4} {:<30} {:<30}".format(Index, k, v))

                    Index += 1

            else:
                print(text_metadata_availableMetadata_none())
                print("")

            loopDone = True

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


# # Programme: musikalische Parameter

# ## Menüstrukturen

# ### Ohne Grafikexport

# In[ ]:


def menuStructure_musicalParameters_withoutGraphicsExport(
    function_name, menu_header, data_values, explanations
):
    try:
        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        if explanations != "":
            print(explanations)
            print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                function_name()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                print(text_general_exportToDiagrammUnavailable())
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## Ambitus

# ### Analyse

# In[45]:


def analyze_range(temporary_selectedScore):
    try:
        selectedScore_stripTies = temporary_selectedScore.stripTies()

        rangeAnalyzer = analysis.discrete.Ambitus()

        range = rangeAnalyzer.getSolution(selectedScore_stripTies).name

        return range

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Textausgabe

# In[46]:


def range_analysis_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        # --- Unterhalb: Code des Tools ---

        range = analyze_range(temporary_selectedScore)

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = [[score_label, range]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            range_analysis_textOutput, menu_header, data_values, explanations=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Vergleich

# #### Textausgabe

# In[47]:


def range_comparison_textOutput():
    utility_clear_screen()

    try:
        print(text_analysis_scoreSelection()[0])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore1 = select_score_completeOrIndividualVoice()

        selectedScore1_name = global_selectedScore

        input_bars_start_selectedScore1 = global_input_firstMeasure

        input_bars_end_selectedScore1 = global_input_lastMeasure

        print(text_analysis_scoreSelection()[1])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore2 = select_score_completeOrIndividualVoice()

        selectedScore2_name = global_selectedScore

        input_bars_start_selectedScore2 = global_input_firstMeasure

        input_bars_end_selectedScore2 = global_input_lastMeasure

        range_Noten1 = analyze_range(selectedScore1)

        range_Noten2 = analyze_range(selectedScore2)

        score_label1 = (
            utility_getKeyToValue(
                selectedScore1_name, global_catalogue_completeScoreWithIndividualParts
            )
            + ", "
            + text_analysis_measures()
            + str(input_bars_start_selectedScore1)
            + "-"
            + str(input_bars_end_selectedScore1)
        )

        score_label2 = (
            utility_getKeyToValue(
                selectedScore2_name, global_catalogue_completeScoreWithIndividualParts
            )
            + ", "
            + text_analysis_measures()
            + str(input_bars_start_selectedScore2)
            + "-"
            + str(input_bars_end_selectedScore2)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = [[score_label1, range_Noten1], [score_label2, range_Noten2]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            range_comparison_textOutput, menu_header, data_values, explanations=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## Artikulation

# ## Dynamik

# ## Formaler Ablauf (Strukturen)

# ## Harmonik

# ## Intervallstruktur

# ### Intervalltypen (Anzahl)

# In[48]:


def intervalStructure_intervalTypes_quantity(temporary_selectedScore):
    try:
        selectedScore_stripTies = temporary_selectedScore.stripTies()

        intervalAnalyzer = analysis.discrete.MelodicIntervalDiversity()

        intervals_typesAndQuantity = intervalAnalyzer.countMelodicIntervals(
            selectedScore_stripTies,
            found=None,
            ignoreDirection=False,
            ignoreUnison=False,
        )

        intervalTypes_quantity = len(intervals_typesAndQuantity)

        # gibt die Anzahl der vorhandenen Intervalltypen als Integer zurück

        return intervalTypes_quantity

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Intervalltypen (Unique Intervals)

# In[49]:


def intervalStructure_intervalTypes_UniqueIntervals(temporary_selectedScore):
    try:
        selectedScore_stripTies = temporary_selectedScore.stripTies()

        intervalAnalyzer = analysis.discrete.MelodicIntervalDiversity()

        intervals_typesAndQuantity = intervalAnalyzer.countMelodicIntervals(
            selectedScore_stripTies,
            found=None,
            ignoreDirection=False,
            ignoreUnison=False,
        )

        intervals_types = list(intervals_typesAndQuantity.keys())

        # gibt die Anzahl der vorhandenen Intervalltypen als Integer zurück

        return intervals_types

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# #### Textausgabe

# In[50]:


def intervalStructure_intervalTypes_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        # --- Unterhalb: Code des Tools ---

        intervalTypes_quantity = intervalStructure_intervalTypes_quantity(
            temporary_selectedScore)

        intervals_types = str(
            intervalStructure_intervalTypes_UniqueIntervals(temporary_selectedScore)
        )

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = [[score_label, intervalTypes_quantity, intervals_types]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            intervalStructure_intervalTypes_textOutput,
            menu_header,
            data_values,
            explanations=text_analysis_notes_intervals(),
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Intervalltypen (Anzahl)

# #### Textausgabe

# In[51]:


def intervalStructure_intervalTypes_quantity_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        intList = analysis.segmentByRests.Segmenter.getIntervalList(
            selectedScore_stripTies
        )

        intervals = utility_count([x.directedName for x in intList])

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        intervals_list = []

        for x, y in intervals.items():
            intervals_list.append([score_label, x, y])

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = intervals_list

        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                intervalStructure_intervalTypes_quantity_textOutput()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                names = []
                values = []

                for datensatz in data_values:
                    names.append(datensatz[1])
                    values.append(datensatz[2])

                plt.bar(names, values)
                plt.ylabel("Frequency")
                plt.xlabel("Interval types")
                plt.title("Interval types and corresponding frequency")

                plt.show()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Intervalltypen (Vergleich)

# #### Textausgabe

# In[52]:


def intervalStructure_intervalTypes_comparison_textOutput():
    utility_clear_screen()

    try:
        print(text_analysis_scoreSelection()[0])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore1 = select_score_completeOrIndividualVoice()

        selectedScore1_stripTies = selectedScore1.stripTies()

        selectedScore1_name = global_selectedScore

        input_bars_start_selectedScore1 = global_input_firstMeasure

        input_bars_end_selectedScore1 = global_input_lastMeasure

        print(text_analysis_scoreSelection()[1])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore2 = select_score_completeOrIndividualVoice()

        selectedScore2_stripTies = selectedScore2.stripTies()

        selectedScore2_name = global_selectedScore

        input_bars_start_selectedScore2 = global_input_firstMeasure

        input_bars_end_selectedScore2 = global_input_lastMeasure

        allIntervals_list_selectedScore1 = (
            analysis.segmentByRests.Segmenter.getIntervalList(
                selectedScore1_stripTies)
        )

        a = utility_count([x.directedName for x in allIntervals_list_selectedScore1])

        allIntervals_list_selectedScore2 = (
            analysis.segmentByRests.Segmenter.getIntervalList(
                selectedScore2_stripTies)
        )

        b = utility_count([x.directedName for x in allIntervals_list_selectedScore2])

        selectedScore1_name = utility_getKeyToValue(
            selectedScore1_name, global_catalogue_completeScoreWithIndividualParts
        )

        score_label1 = (
            selectedScore1_name
            + ", "
            + text_analysis_measures()
            + str(input_bars_start_selectedScore1)
            + "-"
            + str(input_bars_end_selectedScore1)
        )

        selectedScore2_name = utility_getKeyToValue(
            selectedScore2_name, global_catalogue_completeScoreWithIndividualParts
        )

        score_label2 = (
            selectedScore2_name
            + ", "
            + text_analysis_measures()
            + str(input_bars_start_selectedScore2)
            + "-"
            + str(input_bars_end_selectedScore2)
        )

        intervals_comparison_list = []

        for i in a.keys():
            if i in b.keys():
                difference = a[i] - b[i]

                if difference < 0:
                    intervals_comparison_list.append(
                        [score_label1, i, a[i], str(difference)]
                    )

                else:
                    intervals_comparison_list.append(
                        [score_label1, i, a[i], str(difference)]
                    )

            else:
                intervals_comparison_list.append([score_label1, i, a[i], a[i]])

        for i in b.keys():
            if i in a.keys():
                difference = b[i] - a[i]

                if difference < 0:
                    intervals_comparison_list.append(
                        [score_label2, i, b[i], str(difference)]
                    )

                else:
                    intervals_comparison_list.append(
                        [score_label2, i, b[i], str(difference)]
                    )

            else:
                intervals_comparison_list.append([score_label2, i, b[i], b[i]])

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = intervals_comparison_list

        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                intervalStructure_intervalTypes_comparison_textOutput()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                interval_1 = []
                frequency_1 = []
                difference_1 = []

                interval_2 = []
                frequency_2 = []
                difference_2 = []

                for dataset in data_values:
                    if dataset[0] == score_label1:
                        interval_1.append(dataset[1])
                        frequency_1.append(int(dataset[2]))
                        difference_1.append(int(dataset[3]))

                for dataset in data_values:
                    if dataset[0] == score_label2:
                        interval_2.append(dataset[1])
                        frequency_2.append(int(dataset[2]))
                        difference_2.append(int(dataset[3]))

                fig, axs1 = plt.subplots(2, 1)
                axs1[0].bar(interval_1, frequency_1)
                axs1[0].set_title(score_label1)
                axs1[0].set(xlabel="Interval types", ylabel="Frequency")

                axs1[1].bar(interval_1, difference_1)
                axs1[1].set(
                    xlabel="Interval types", ylabel="Difference to other note selection"
                )

                fig.tight_layout()

                plt.show()

                fig, axs2 = plt.subplots(2, 1)

                axs2[0].set_title(score_label2)
                axs2[0].bar(interval_2, frequency_2)
                axs2[0].set(xlabel="Interval types", ylabel="Frequency")

                axs2[1].bar(interval_2, difference_2)
                axs2[1].set(
                    xlabel="Interval types", ylabel="Difference to other note selection"
                )

                fig.tight_layout()

                plt.show()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Intervalle Anzahl

# #### Textausgabe

# In[53]:


def intervalStructure_Intervalle_quantity_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        intList = analysis.segmentByRests.Segmenter.getIntervalList(
            selectedScore_stripTies
        )

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = [[score_label, len(intList)]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            intervalStructure_Intervalle_quantity_textOutput,
            menu_header,
            data_values,
            explanations=text_analysis_notes_intervals(),
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## Klang

# ## Melodik

# ### Melodieverlauf

# #### Darstellung

# ##### Liniendiagramm

# In[54]:


def Melodik_Melodieverlauf_visualization_lineGraph():
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

        user_selection = select_bars(global_score)

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
        Melodik_Melodieverlauf_visualization_lineGraph)


# ## Metrum

# ### Metrisches Gewicht

# In[55]:


def meter_metricWeight_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
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

        data_values = bs_int_indi

        show_resultslist(menu_header, data_values)

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                meter_metricWeight_textOutput()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values,
                    columns=menu_header,
                    save_at=path_and_filename,
                    do_print=False,
                    do_return_pd=True,
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                path_and_filename = str(score_export_path) + \
                    "\\" + "Temp" + ".csv"

                pd_bs_indi_data = utility_export_as_csv(
                    data=data_values,
                    columns=menu_header,
                    save_at=path_and_filename,
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

                os.remove(path_and_filename)

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Tonklassen auf metrischen Positionen (-- entfernt --)

# def meter_pitchClass_metricPosition_textOutput():
#
#     utility_clear_screen()
#
#     try:
#
#         temporary_selectedScore = select_score_completeOrIndividualVoice()
#
#         selectedScore_stripTies = temporary_selectedScore.stripTies()
#
#         # --- Unterhalb: Code des Tools ---
#
#         selectedScore_name = str(utility_getKeyToValue(Noten,Verzeichnis_Partitur_und_Einzelstimmen))
#
#         score_label = selectedScore_name + ', ' + text_analysis_measures() + str(input_bars_start) + '-' + str(input_bars_end)
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
#         data_values = l_bs
#
#         show_resultslist(menu_header, data_values)
#
#         while True:
#
#             Auswahl = open_submenu_data_withExplanationsColumn(Modul_Navigation())
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
#                 score_export_path = us['directoryScratch']
#
#                 filename = input(text_export_fileName())
#                 print('')
#
#                 path_and_filename = str(score_export_path)+'\\'+str(filename)+'.csv'
#
#                 utility_export_as_csv(data=data_values,
#
#                               columns=menu_header,
#
#                               save_at=path_and_filename,
#
#                               do_print=False)
#
#                 print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
#                 print('')
#
#                 input(text_general_proceed())
#                 print('')
#
#             elif Auswahl == 'Export_Grafik':
#
#                 us = environment.UserSettings()
#
#                 score_export_path = us['directoryScratch']
#
#                 print(text_general_exportGraph(score_export_path))
#                 print()
#
#                 path_and_filename = str(score_export_path)+'\\'+'Temp'+'.csv'
#
#                 pd_bs_data = utility_export_as_csv(data=data_values,
#
#                                            columns=menu_header,
#
#                                            save_at=path_and_filename,
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
#                 os.remove(path_and_filename)
#
#                 input(text_general_proceed())
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
#         input(text_general_proceed())
#         print('')

# ## Rhythmik

# ## Satztechnik (Aufbau, Struktur der Mehrstimmigkeit)

# ## Takt

# ## Tempo

# ## Tonmaterial

# ### Töne Anzahl (gesamt)

# #### Textausgabe

# In[56]:


def notes_quantity_total_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        # --- Unterhalb: Code des Tools ---

        notes_amount = len(
            selectedScore_stripTies.flat.getElementsByClass("Note"))

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = [[score_label, notes_amount]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            notes_quantity_total_textOutput, menu_header, data_values, explanations=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Töne Anzahl (Tonhöhen)

# #### Textausgabe (-- entfernt --)

# def notes_notesQuantity_pitches_textOutput():
#
#     utility_clear_screen()
#
#     try:
#
#         temporary_selectedScore = select_score_completeOrIndividualVoice()
#
#         selectedScore_stripTies = temporary_selectedScore.stripTies()
#
#         selectedScore_name = str(utility_getKeyToValue(Noten,Verzeichnis_Partitur_und_Einzelstimmen))
#
#         score_label = selectedScore_name + ', ' + text_analysis_measures() + str(input_bars_start) + '-' + str(input_bars_end)
#
#         nameOctaveCount = analysis.pitchAnalysis.pitchAttributeCount(selectedScore_stripTies, 'nameWithOctave')
#
#         notes_nameOctaveCount = [[score_label, i, nameOctaveCount[i]]for i in sorted(nameOctaveCount)]
#
#         menu_header = text_headers(sys._getframe().f_code.co_name)
#
#         data_values = notes_nameOctaveCount
#
#         show_resultslist(menu_header, data_values)
#
#         while True:
#
#             Auswahl = open_submenu_data_withExplanationsColumn(Modul_Navigation())
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
#                 score_export_path = us['directoryScratch']
#
#                 filename = input(text_export_fileName())
#                 print('')
#
#                 path_and_filename = str(score_export_path)+'\\'+str(filename)+'.csv'
#
#                 utility_export_as_csv(data=data_values,
#
#                               columns=menu_header,
#
#                               save_at=path_and_filename,
#
#                               do_print=False)
#
#                 print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
#                 print('')
#
#                 input(text_general_proceed())
#                 print('')
#
#             elif Auswahl == 'Export_Grafik':
#
#                 print(text_general_exportToDiagrammUnavailable())
#
#                 input(text_general_proceed())
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
#         input(text_general_proceed())
#         print('')

# # Vordefinierte Darstellungen

# ## Menüstrukturen

# ### Mit Grafikexport

# In[ ]:


def menu_structures_predefined_visualizations(
    function_name, menu_header, data_values, graph_processed, notes
):
    try:
        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        if notes != "":
            print(notes)
            print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                function_name()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                graph_processed.doneAction = None
                graph_processed.run()

                plt.show()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## HistogramPitchSpace

#

# In[57]:


def predefinedVisualizations_HistogramPitchSpace():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.HistogramPitchSpace

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [score_label, item[0], pitch.Pitch(
                    item[0]).nameWithOctave, item[1]]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_HistogramPitchSpace,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## HistogramPitchClass

# In[58]:


def predefinedVisualizations_HistogramPitchClass():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.HistogramPitchClass

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [score_label, item[0], pitch.Pitch(
                    item[0]).nameWithOctave, item[1]]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_HistogramPitchClass,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## HistogramQuarterLength

# In[1]:


def predefinedVisualizations_HistogramQuarterLength():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.HistogramQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    item[0],
                    duration.Duration(quarterLength=float(item[0])).fullName,
                    item[1],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_HistogramQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## HorizontalBarPitchSpaceOffset (Pianorollendarstellung)

# In[60]:


def predefinedVisualizations_HorizontalBarPitchSpaceOffset():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.HorizontalBarPitchSpaceOffset

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        onsets_list = []

        for x in graph_processed.data:
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

                                    onsets_list.append(
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

                                    onsets_list.append(
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

                                    onsets_list.append(
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

                                    onsets_list.append(
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

                                            onsets_list.append(
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
                                            onsets_list.append(
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

                                            onsets_list.append(
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

                                            onsets_list.append(
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

        data_values = onsets_list

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                predefinedVisualizations_HorizontalBarPitchSpaceOffset()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                graph_processed.doneAction = None
                graph_processed.run()

                plt.show()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## ScatterWeightedPitchSpaceQuarterLength

# In[61]:


def predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.ScatterWeightedPitchSpaceQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.QuarterLengthAxis(graph_processed)

        toneDurations_dict = {}

        for item in ax.ticks():
            toneDurations_dict.update({item[0]: item[1]})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    toneDurations_dict[item[0]],
                    duration.Duration(
                        quarterLength=float(toneDurations_dict[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## Plot3DBarsPitchSpaceQuarterLength

# In[62]:


def predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.Plot3DBarsPitchSpaceQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.QuarterLengthAxis(graph_processed)

        toneDurations_dict = {}

        for item in ax.ticks():
            toneDurations_dict.update({item[0]: item[1]})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    toneDurations_dict[item[0]],
                    duration.Duration(
                        quarterLength=float(toneDurations_dict[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## ScatterWeightedPitchClassQuarterLength

# In[63]:


def predefinedVisualizations_ScatterWeightedPitchClassQuarterLength():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.ScatterWeightedPitchClassQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.QuarterLengthAxis(graph_processed)

        toneDurations_dict = {}

        for item in ax.ticks():
            toneDurations_dict.update({item[0]: item[1]})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    toneDurations_dict[item[0]],
                    duration.Duration(
                        quarterLength=float(toneDurations_dict[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterWeightedPitchClassQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## ScatterPitchClassOffset

# In[64]:


def predefinedVisualizations_ScatterPitchClassOffset():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.ScatterPitchClassOffset

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [score_label, item[1], pitch.Pitch(
                    item[1]).nameWithOctave, item[0]]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterPitchClassOffset,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## ScatterWeightedPitchSpaceDynamicSymbol

# In[65]:


def predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.ScatterWeightedPitchSpaceDynamicSymbol

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.DynamicsAxis(graph_processed)

        Verzeichnis_Dynamiken = {}

        for item in ax.ticks():
            Verzeichnis_Dynamiken.update({item[0]: item[1].replace("$", "")})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    item[0],
                    pitch.Pitch(item[0]).nameWithOctave,
                    Verzeichnis_Dynamiken[item[1]],
                    item[2],
                ]
            )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## HorizontalBarPitchClassOffset

# In[66]:


def predefinedVisualizations_HorizontalBarPitchClassOffset():
    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        selectedScore_name = str(
            utility_getKeyToValue(global_selectedScore, global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
            selectedScore_name
            + ", "
            + text_analysis_measures()
            + str(global_input_firstMeasure)
            + "-"
            + str(global_input_lastMeasure)
        )

        selectedGraph = graph.plot.HorizontalBarPitchClassOffset

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        onsets_list = []

        for x in graph_processed.data:
            x[0] = x[0].replace("♭", "-").replace("♯", "#")

            if len(x) != 0:
                for y in x:
                    if type(y) == list and len(y) != 0:
                        for z in y:
                            if type(z) == tuple:
                                if "/" in x[0]:
                                    n = x[0].rfind("/")

                                    onsets_list.append(
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
                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(str(x[0])).pitchClass,
                                            str(x[0]),
                                            z[0],
                                            z[1],
                                        ]
                                    )

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = onsets_list

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation())

            if user_selection == "repeatSelection":
                predefinedVisualizations_HorizontalBarPitchClassOffset()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                graph_processed.doneAction = None
                graph_processed.run()

                plt.show()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ## Dolan

# In[67]:


def predefinedVisualizations_Dolan():
    utility_clear_screen()

    # --- Unterhalb: Code des Tools ---

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    selectedScore_stripTies = temporary_selectedScore.stripTies()

    print(text_analysis_notes_predefinedVisualizations_Dolan())
    print("")

    try:
        selectedGraph = graph.plot.Dolan

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.doneAction = None
        graph_processed.run()

        plt.show()

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    # --- Oberhalb: Code des Tools ---

    menu_askUser_repeatPreviousTool(predefinedVisualizations_Dolan)


# # Mustersuche

# ## Menüstrukturen

# In[68]:


def open_submenu_patternSearch(received_list):
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_patternSearch_showPatternSelection(global_searchPattern))
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplanationsColumn()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(received_list, 1):
            print("{:<4} {:<65}".format(index, item[0]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(received_list):
                utility_clear_screen()

                return received_list[userInput_menuSelection_int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(received_list)))
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(received_list)))
            print("")

            input(text_general_proceed())
            print("")


# ## Suchroutinen

# ### Tonfolge ohne Transposition/ohne Rhythmus

# In[69]:


def patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm():
    try:
        score_deepCopy = deepcopy(global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withoutRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                full_piece_stream = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                full_piece_stream = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        p_full_piece = search.noteNameSearch(full_piece_stream, streamMot)

        print(text_patternSearch_patternsFound(len(p_full_piece)))
        print("")

        input(text_general_proceed())
        print("")

        searchPattern_list = []

        counter = 1

        for position in p_full_piece:
            startingNote = full_piece_stream[position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            searchPattern_list.append(
                [
                    counter,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    utility_listToString(global_searchPattern),
                ]
            )

            counter += 1

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in p_full_piece:
                    for ffound in range(len(streamMot)):
                        full_piece_stream[found + ffound].lyric = "*"
                        full_piece_stream[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


# ### Tonfolge mit Transposition/ohne Rhythmus

# In[70]:


def patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm():
    try:
        score_deepCopy = deepcopy(global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withoutRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
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
        counter = 1
        iteration = 1

        # Die Ergebnisse müssen in einer extra Liste ("results") eingetragen werden.
        # Der "zähler" vereinfacht das Aufzählen der Töne, wenn man diese nacheinander zeigen will.

        searchPattern_list = []

        for egal in range(12):  # Suche 12 Mal
            s_len = [streamMot.notes[i].name for i in range(
                len(streamMot.notes))]
            p = search.streamSearchBase(
                s, streamMot, algorithm=pitchClassEqual)
            for notePosition in p:
                startingNote = s[notePosition]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                results.append(notePosition)

                searchPattern_list.append(
                    [
                        counter,
                        startingNote,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        utility_listToString(s_len),
                    ]
                )

                counter += 1

            [n.transpose(1, inPlace=True) for n in streamMot]

            iteration += 1

        print(text_patternSearch_patternsFound(len(results)))
        print("")

        input(text_general_proceed())
        print("")

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in results:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


# ### Tonfolge ohne Transposition/mit Rhythmus

# In[71]:


def patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm():
    try:
        score_deepCopy = deepcopy(global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        # Die Suche wird nun mit dem Befehl 'search.noteNameRhythmicSearch' erstellt.

        p = search.noteNameRhythmicSearch(s, streamMot)

        print(text_patternSearch_patternsFound(len(p)))
        print("")

        input(text_general_proceed())
        print("")

        counter = 1

        searchPattern_list = []

        for position in p:
            startingNote = s[position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            searchPattern_list.append(
                [
                    counter,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    utility_listToString(global_searchPattern),
                ]
            )

            counter += 1

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in p:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


# ### Tonfolge mit Transposition/mit Rhythmus

# In[72]:


def patternSearch_menuStructure_toneSequence_withTransposition_withRhythm():
    try:
        score_deepCopy = deepcopy(global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        results = []
        counter = 1
        iteration = 1

        # Die Ergebnisse müssen in einer extra Liste ("results") eingetragen werden.
        # Der "zähler" vereinfacht das Aufzählen der Töne, wenn man diese nacheinander zeigen will.

        searchPattern_list = []

        for egal in range(12):  # Suche 12 Mal
            s_len = [streamMot.notes[i].name for i in range(
                len(streamMot.notes))]
            p = search.noteNameRhythmicSearch(s, streamMot)
            for notePosition in p:
                startingNote = s[notePosition]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                results.append(notePosition)

                searchPattern_list.append(
                    [
                        counter,
                        startingNote,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        utility_listToString(s_len),
                    ]
                )

                counter += 1

            [n.transpose(1, inPlace=True) for n in streamMot]

            iteration += 1

        print(text_patternSearch_patternsFound(len(results)))
        print("")

        input(text_general_proceed())
        print("")

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withTransposition_withRhythm()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in results:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


# ### Rhythmus ohne Tonhöhen

# In[ ]:


def patternSearch_menuStructure_withRhythm_withoutPitch():
    try:
        score_deepCopy = deepcopy(global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enter_search_pattern_only_rhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        # Die Suche wird nun mit dem Befehl 'search.noteNameRhythmicSearch' erstellt.

        p = search.rhythmicSearch(s, streamMot)

        print(text_patternSearch_patternsFound(len(p)))
        print("")

        input(text_general_proceed())
        print("")

        counter = 1

        searchPattern_list = []

        for position in p:
            startingNote = s[position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            searchPattern_list.append(
                [
                    counter,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    utility_listToString(global_searchPattern),
                ]
            )

            counter += 1

        menu_header = text_headers(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_withRhythm_withoutPitch()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in p:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                    str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


# ## Menüeinträge

# ### Tonauswahl

# In[7]:


def keySelection_menuEntries():
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


def rhythmSelection_menuEntries():
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


def rhythmSelection_menuEntries_onlyRhythm():
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


def patternSearch_enterSearchPattern_withRhythm():
    try:
        global global_searchPattern

        loopDone1 = False

        while not loopDone1:
            streamMot = stream.Stream()

            global_searchPattern = []

            loopDone2 = False

            while not loopDone2:
                searchPattern_toneSelection = open_submenu_patternSearch(
                    keySelection_menuEntries())

                utility_clear_screen()

                if searchPattern_toneSelection == "remove":
                    if len(global_searchPattern) > 0:
                        global_searchPattern.pop()

                elif searchPattern_toneSelection == "complete":
                    for Tonhoehe, Rhythmus in global_searchPattern:
                        if "/" in Rhythmus:
                            num, den = map(float, Rhythmus.split("/"))

                            streamMot.append(
                                note.Note(
                                    Tonhoehe, quarterLength=float(num / den))
                            )

                        else:
                            streamMot.append(
                                note.Note(
                                    Tonhoehe, quarterLength=float(Rhythmus))
                            )

                    loopDone3 = False

                    while not loopDone3:
                        utility_clear_screen()

                        user_input = input(text_display_showScoreSelection())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            print(text_general_close_museScore3())
                            print()

                            streamMot.show()

                            loopDone3 = True

                        elif utility_userInput_isNegative(user_input):
                            loopDone3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())

                    loopDone3 = False

                    while not loopDone3:
                        utility_clear_screen()

                        print(text_patternSearch_showPatternSelection(global_searchPattern))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            loopDone1 = True
                            loopDone2 = True
                            loopDone3 = True

                            utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loopDone1 = False
                            loopDone2 = True
                            loopDone3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            input(text_general_proceed())
                            print("")

                            utility_clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                else:
                    searchPattern_rhythmSelection = open_submenu_patternSearch(
                        rhythmSelection_menuEntries()
                    )

                    if searchPattern_rhythmSelection == "remove":
                        if len(global_searchPattern) > 0:
                            global_searchPattern.pop()

                    elif searchPattern_rhythmSelection == "custom":
                        loopDone4 = True

                        while loopDone4:
                            utility_clear_screen()

                            input_rhythm = input(
                                text_patternSearch_enter_customRhythm()
                            )
                            print("")

                            if utility_userInput_isNumber(input_rhythm):
                                global_searchPattern.append(
                                    [searchPattern_toneSelection, str(input_rhythm)])

                                loopDone4 = False

                            else:
                                print(text_general_input_restrictedToNumbers(
                                    input_rhythm))
                                print("")

                                input(text_general_proceed())
                                print("")

                    else:
                        global_searchPattern.append([searchPattern_toneSelection, str(searchPattern_rhythmSelection)])

        utility_clear_screen()

        return streamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Without rhythm

#

# In[ ]:


def patternSearch_enterSearchPattern_withoutRhythm():
    try:
        global global_searchPattern

        loopDone1 = False

        while not loopDone1:
            streamMot = stream.Stream()

            global_searchPattern = []

            loopDone2 = False

            while not loopDone2:
                searchPattern_toneSelection = open_submenu_patternSearch(
                    keySelection_menuEntries())

                utility_clear_screen()

                if searchPattern_toneSelection == "remove":
                    if len(global_searchPattern) > 0:
                        global_searchPattern.pop()

                elif searchPattern_toneSelection == "complete":
                    for Tonhoehe in global_searchPattern:
                        streamMot.append(note.Note(Tonhoehe))

                    loopDone3 = False

                    while not loopDone3:
                        utility_clear_screen()

                        user_input = input(text_display_showScoreSelection())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            print(text_general_close_museScore3())
                            print()

                            streamMot.show()

                            loopDone3 = True

                        elif utility_userInput_isNegative(user_input):
                            loopDone3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                    loopDone3 = False

                    while not loopDone3:
                        utility_clear_screen()

                        print(text_patternSearch_showPatternSelection(global_searchPattern))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            loopDone1 = True
                            loopDone2 = True
                            loopDone3 = True

                            utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loopDone1 = False
                            loopDone2 = True
                            loopDone3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            input(text_general_proceed())
                            print("")

                            utility_clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                else:
                    global_searchPattern.append(searchPattern_toneSelection)

        utility_clear_screen()

        return streamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# ### Only rhythm

# In[ ]:


def patternSearch_enter_search_pattern_only_rhythm():
    try:
        global global_searchPattern

        loopDone1 = False

        while not loopDone1:
            streamMot = stream.Stream()

            global_searchPattern = []

            loopDone2 = False

            while not loopDone2:
                searchPattern_rhythmSelection = open_submenu_patternSearch(
                    rhythmSelection_menuEntries_onlyRhythm()
                )

                utility_clear_screen()

                if searchPattern_rhythmSelection == "remove":
                    if len(global_searchPattern) > 0:
                        global_searchPattern.pop()

                elif searchPattern_rhythmSelection == "custom":
                    loopDone4 = True

                    while loopDone4:
                        utility_clear_screen()

                        Rhythmuseingabe = input(
                            text_patternSearch_enter_customRhythm()
                        )
                        print("")

                        if utility_userInput_isNumber(Rhythmuseingabe):
                            global_searchPattern.append(str(Rhythmuseingabe))

                            loopDone4 = False

                        else:
                            print(text_general_input_restrictedToNumbers(
                                Rhythmuseingabe))
                            print("")

                            input(text_general_proceed())
                            print("")

                elif searchPattern_rhythmSelection == "complete":
                    for rhythm in global_searchPattern:
                        if "/" in rhythm:
                            num, den = map(float, rhythm.split("/"))

                            streamMot.append(
                                note.Note("G", quarterLength=float(num / den))
                            )

                        else:
                            streamMot.append(
                                note.Note("G", quarterLength=float(rhythm))
                            )

                    loopDone3 = False

                    while not loopDone3:
                        utility_clear_screen()

                        user_input = input(text_display_showScoreSelection())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            print(text_general_close_museScore3())
                            print()

                            streamMot.show()

                            loopDone3 = True

                        elif utility_userInput_isNegative(user_input):
                            loopDone3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                    loopDone3 = False

                    while not loopDone3:
                        utility_clear_screen()

                        print(text_patternSearch_showPatternSelection(global_searchPattern))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            loopDone1 = True
                            loopDone2 = True
                            loopDone3 = True

                            utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loopDone1 = False
                            loopDone2 = True
                            loopDone3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            input(text_general_proceed())
                            print("")

                            utility_clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loopDone3 = False

                            input(text_general_proceed())
                            print("")

                else:
                    global_searchPattern.append(str(searchPattern_rhythmSelection))

        utility_clear_screen()

        return streamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


# # Programme: Zeichenorientierte Benutzerschnittstelle (CLI)

# ## Einzelwerk

# ### Menüstrukturen

# #### Hauptmenü Einzelwerk (erste Ebene)

# In[75]:


def open_mainmenu_individualPiece():
    select_score_filePath()

    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(mainmenu_individualPiece_entries(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(mainmenu_individualPiece_entries()):
                utility_clear_screen()

                mainmenu_individualPiece_entries()[userInput_menuSelection_int][1]()

                utility_clear_screen()

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(mainmenu_individualPiece_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(mainmenu_individualPiece_entries())
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, File)

# In[76]:


def open_submenu_individualPiece_files():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(submenu_individualPiece_files_entries(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if (
                0
                <= userInput_menuSelection_int
                < len(submenu_individualPiece_files_entries())
            ):
                utility_clear_screen()

                if (
                    submenu_individualPiece_files_entries()[
                        userInput_menuSelection_int][1]
                    != "nothing"
                ):
                    submenu_individualPiece_files_entries()[
                        userInput_menuSelection_int][1]()

                utility_clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(submenu_individualPiece_files_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(submenu_individualPiece_files_entries())
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, statistische Analysen)

# In[77]:


def open_submenu_individualPiece_statisticalAnalyses():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            submenu_individualPiece_statisticalAnalyses_entries(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if (
                0
                <= userInput_menuSelection_int
                < len(submenu_individualPiece_statisticalAnalyses_entries())
            ):
                utility_clear_screen()

                if (
                    submenu_individualPiece_statisticalAnalyses_entries()[
                        userInput_menuSelection_int
                    ][1]
                    != "nothing"
                ):
                    submenu_individualPiece_statisticalAnalyses_entries()[
                        userInput_menuSelection_int
                    ][1]()

                utility_clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(submenu_individualPiece_statisticalAnalyses_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(submenu_individualPiece_statisticalAnalyses_entries())
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# ##### Untermenü Einzelwerk (dritte Ebene, statistische Analysen, zweidimensionale Häufigkeitsverteilungen/Streudiagramme)

# In[78]:


def open_submenu_individualPiece_statisticalAnalyses_visualizations():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            submenu_individualPiece_statisticalAnalyses_visualizations_entries(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if (
                0
                <= userInput_menuSelection_int
                < len(
                    submenu_individualPiece_statisticalAnalyses_visualizations_entries()
                )
            ):
                utility_clear_screen()

                if (
                    submenu_individualPiece_statisticalAnalyses_visualizations_entries()[
                        userInput_menuSelection_int
                    ][
                        1
                    ]
                    != "nothing"
                ):
                    submenu_individualPiece_statisticalAnalyses_visualizations_entries()[
                        userInput_menuSelection_int
                    ][
                        1
                    ]()

                utility_clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(
                            submenu_individualPiece_statisticalAnalyses_visualizations_entries()
                        )
                    )
                )
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(
                        submenu_individualPiece_statisticalAnalyses_visualizations_entries()
                    )
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, Darstellungen)

# In[79]:


def open_submenu_individualPiece_visualizations():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            submenu_individualPiece_visualizations_entries(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        utility_clear_screen()

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if (
                0
                <= userInput_menuSelection_int
                < len(submenu_individualPiece_visualizations_entries())
            ):
                utility_clear_screen()

                if (
                    submenu_individualPiece_visualizations_entries()[
                        userInput_menuSelection_int
                    ][1]
                    != "nothing"
                ):
                    submenu_individualPiece_visualizations_entries()[
                        userInput_menuSelection_int
                    ][1]()

                utility_clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(submenu_individualPiece_visualizations_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(submenu_individualPiece_visualizations_entries())
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, Mustersuche)

# In[80]:


def open_submenu_individualPiece_patternSearch():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(submenu_individualPiece_patternSearch_entries(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        utility_clear_screen()

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if (
                0
                <= userInput_menuSelection_int
                < len(submenu_individualPiece_patternSearch_entries())
            ):
                utility_clear_screen()

                if (
                    submenu_individualPiece_patternSearch_entries()[
                        userInput_menuSelection_int
                    ][1]
                    != "nothing"
                ):
                    submenu_individualPiece_patternSearch_entries()[
                        userInput_menuSelection_int
                    ][1]()

                utility_clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(submenu_individualPiece_patternSearch_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(submenu_individualPiece_patternSearch_entries())
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# #### Untermenü Einzelwerk (zweite Ebene, Einstellungen)

# In[81]:


def open_submenu_individualPiece_settings():
    while True:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(
            submenu_individualPiece_settings(), 1
        ):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        utility_clear_screen()

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if (
                0
                <= userInput_menuSelection_int
                < len(submenu_individualPiece_settings())
            ):
                utility_clear_screen()

                if (
                    submenu_individualPiece_settings()[
                        userInput_menuSelection_int
                    ][1]
                    != "nothing"
                ):
                    submenu_individualPiece_settings()[
                        userInput_menuSelection_int
                    ][1]()

                utility_clear_screen()

                break

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(submenu_individualPiece_settings())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")
        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(submenu_individualPiece_settings())
                )
            )
            print("")

            input(text_general_proceed())
            print("")


# ### Menüeinträge

# #### Hauptmenü Einzelwerk (erste Ebene)

# In[82]:


def mainmenu_individualPiece_entries():
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
        ["EXIT: Programm beenden", utility_terminateProgram, "<Beendet das Python-Skript>"],
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
        ["EXIT: Exit program", utility_terminateProgram, "<Exits the Python script>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Untermenü Einzelwerk (zweite Ebene, File)

# In[83]:


def submenu_individualPiece_files_entries():
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
            utility_playback_MIDI,
            "<Gibt Notendatei als Midi wieder>",
        ],
        [
            "NAME: Namen der Einzelstimmen ändern",
            name_individualVoices,
            "<Ermöglicht das erneute Umbenennen der Einzelstimmen>",
        ],
        [
            "NAME: Namen der Einzelstimmen anzeigen",
            show_names_individualVoices,
            "<Zeigt die selbst vergebenen Namen der Einzelstimmen an>",
        ],
        [
            "EXPO: Datei exportieren",
            score_export,
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
         utility_playback_MIDI, "<Plays score as midi>"],
        [
            "NAME: Change the names of the individual parts/voices",
            name_individualVoices,
            "<Allows you to rename the individual parts/voices>",
        ],
        [
            "NAME: Show names of individual parts/voices",
            show_names_individualVoices,
            "<Displays the names of the individual parts/voices>",
        ],
        [
            "EXPO: Export file",
            score_export,
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


def submenu_individualPiece_statisticalAnalyses_entries():
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
            notes_quantity_total_textOutput,
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
            notes_quantity_total_textOutput,
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


def submenu_individualPiece_statisticalAnalyses_visualizations_entries():
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


def submenu_individualPiece_visualizations_entries():
    list_de = [
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            visualizations_MuseScore,
            "<Öffnet MuseScore und zeigt den Notentext an>",
        ],
        [
            "SHOW: Notenauswahl (Akkordverbindungen)",
            visualizations_chordConnections,
            "<Speichert eine Notenauswahl, dargestellt als Akkordverbindungen>",
        ],
        [
            "SHOW: Notenauswahl (Generalbass)",
            visualization_chordConnections_figuredBass,
            "<Speichert eine Notenauswahl, dargestellt als Akkordverbindungen mit Generalbassbezifferung>",
        ],
        [
            "SHOW: Notenauswahl (Stufenbezifferung)",
            visualization_chordConnections_romanNumerals,
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
            visualizations_MuseScore,
            "<Opens MuseScore and displays the selected scores>",
        ],
        [
            "SHOW: Sheet music selection (chord connections)",
            visualizations_chordConnections,
            "<Saves a selection of scores, shown as chord connections>",
        ],
        [
            "SHOW: Sheet music selection (figured bass)",
            visualization_chordConnections_figuredBass,
            "<Saves a selection of scores, shown as chord connections with figured bass>",
        ],
        [
            "SHOW: Sheet music selection (chord-scale system)",
            visualization_chordConnections_romanNumerals,
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


def submenu_individualPiece_patternSearch_entries():
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
            "SEAR: Mustersuche (nur Rhythmus)",
            patternSearch_menuStructure_withRhythm_withoutPitch,
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
            patternSearch_menuStructure_withRhythm_withoutPitch,
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


def submenu_individualPiece_settings():
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
            environmentFile_settings_reconfigure,
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
            environmentFile_settings_reconfigure,
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
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(startmenue_entries(), 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        utility_clear_screen()

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(startmenue_entries()):
                utility_clear_screen()

                startmenue_entries()[userInput_menuSelection_int][1]()

                utility_clear_screen()

            else:
                print(
                    text_menu_exception_selectionOutOfRange(
                        len(startmenue_entries())
                    )
                )
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(
                text_menu_exception_selectionOutOfRange(
                    len(startmenue_entries()))
            )
            print("")

            input(text_general_proceed())
            print("")


# ### Menüeinträge

# In[90]:


def startmenue_entries():
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
        ["EXIT: Programm beenden", utility_terminateProgram, "<Beendet das Python-Skript>"],
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
        ["EXIT: Exit programm", utility_terminateProgram, "<Exits the Python script>"],
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


def open_submenu_return_indexFromList(received_list):
    while True:
        utility_clear_screen()

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplanationsColumn()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(received_list, 1):
            print("{:<4} {:<65}".format(index, item))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(received_list):
                utility_clear_screen()

                # Rückgabe der ausgewählten Nummer

                return userInput_menuSelection_int

            else:
                print(text_menu_exception_selectionOutOfRange(len(received_list)))
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(received_list)))
            print("")

            input(text_general_proceed())
            print("")


# #### Daten ohne 'Erläuterung'

# In[92]:


def open_submenu_data_withoutExplanationsColumn(received_list):
    while True:
        utility_clear_screen()

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withoutExplanationsColumn()

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        for index, item in enumerate(received_list, 1):
            print("{:<4} {:<65}".format(index, item[0]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(received_list):
                utility_clear_screen()

                return received_list[userInput_menuSelection_int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(received_list)))
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(received_list)))
            print("")

            input(text_general_proceed())
            print("")


# #### Daten mit 'Erläuterung'

# In[93]:


def open_submenu_data_withExplanationsColumn(received_list):
    while True:
        utility_clear_screen()

        print(text_menu_selection_header())
        print("")

        menu_header = text_menu_headers_withExplanationsColumn()

        print("{:<4} {:<65} {}\n".format(menu_header[0], menu_header[1], menu_header[2]))

        for index, item in enumerate(received_list, 1):
            print("{:<4} {:<65} {}".format(index, item[0], item[2]))

        print("")

        userInput_menuSelection = input(text_menu_selection_input())
        print("")

        if str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(received_list):
                utility_clear_screen()

                return received_list[userInput_menuSelection_int][1]

            else:
                print(text_menu_exception_selectionOutOfRange(len(received_list)))
                print("")

                input(text_general_proceed())
                print("")

        else:
            print(text_menu_exception_selectionOutOfRange(len(received_list)))
            print("")

            input(text_general_proceed())
            print("")


# #### show_resultslist

# In[94]:


def show_resultslist(description, received_data):
    try:
        # Beschreibung = ['Beschreibung1', 'Beschreibung2', ...]

        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("\n")

        if len(received_data) == 0:
            print(text_general_noResults())
            print("")

        else:
            menu_header = ""

            # converts every item in List to a string

            m = 0

            n = 0

            for item in received_data:
                m = received_data.index(item)

                for content in item:
                    n = item.index(content)

                    received_data[m][n] = str(content)

            description_and_receivedData = [description] + received_data

            max_lengths_dict = {}

            n = 0

            while n < len(description):
                max_lengths_dict[n] = 0

                n = n + 1

            for item in description_and_receivedData:
                for content in item:
                    if len(content) >= max_lengths_dict[item.index(content)]:
                        max_lengths_dict[item.index(content)] = len(content)

            for item in description:
                menu_header = (
                    menu_header
                    + f"{item:<{max_lengths_dict[description.index(item)] + 7}s}"
                )

            print(menu_header)
            print("\n")

            for item in received_data:
                data_string = ""

                for content in item:
                    data_string = (
                        data_string
                        + f"{content:<{max_lengths_dict[item.index(content)] + 7}s}"
                    )

                print(data_string)
                print("")

            print("\n")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
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

environmentFile_settings = [
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


def module_navigation():
    list_de = [
        [
            "REPT: Neue Notenauswahl",
            "repeatSelection",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "EXPT: Ergebnisse als CSV-Datei exportieren",
            "export_CSV",
            "<Exportiert und speichert die Ergebnisse als CSV-Datei>",
        ],
        [
            "GRPH: Ergebnisse als Grafik anzeigen",
            "export_visualization",
            "<Exportiert und speichert die Ergebnisse als Grafik>",
        ],
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New score selection",
            "repeatSelection",
            "<Repeat the tool with new score selection>",
        ],
        [
            "EXPT: Export results as CSV file",
            "export_CSV",
            "<Exports and saves the results as CSV file>",
        ],
        [
            "GRPH: Display results as graphic",
            "export_visualization",
            "<Exports and saves the results as graphic>",
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (Mustersuche)

# In[98]:


def module_navigation_patternSearch():
    list_de = [
        [
            "REPT: Neue Suchmusterauswahl",
            "repeatSelection",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "EXPT: Ergebnisse als CSV-Datei exportieren",
            "export_CSV",
            "<Exportiert und speichert die Ergebnisse als CSV-Datei>",
        ],
        [
            "GRPH: Ergebnisse als XML-Datei exportieren",
            "Export_Notentext",
            "<Exportiert und speichert die Ergebnisse farblich markiert als XML-Datei>",
        ],
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New search pattern selection", "repeatSelection", "<Repeat the tool with new score selection>",
        ],
        [
            "EXPT: Export results as CSV file",
            "export_CSV",
            "<Exports and saves the results as CSV file>",
        ],
        [
            "GRPH: Export results as XML file",
            "Export_Notentext",
            "<Exports and saves the results highlighted in a xml file>",
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (temporary_selectedScore)

# In[99]:


def module_navigation_selectedScore():
    list_de = [
        [
            "Notenauswahl: vollständige Partitur",
            "completeScore",
            "<Auswahl der gesamten Partitur>",
        ],
        [
            "Notenauswahl: Taktausschnitt (Stimme/Partitur)",
            "newSelection",
            "<Taktauswahl aus der Partitur oder einer Einzelstimme>",
        ],
        [
            "Notenauswahl: vorherige Auswahl wiederholen",
            "repeatPreviousSelection",
            "<Wiederholung der letzten Notenauswahl>",
        ],
    ]

    list_en = [
        [
            "Score selection: complete score",
            "completeScore",
            "<Selection of the entire score>",
        ],
        [
            "Score selection: bar excerpt (part / score)",
            "newSelection",
            "<bar selection from the score or a single part>",
        ],
        [
            "Score selection: repeat previous selection",
            "repeatPreviousSelection",
            "<Repeat last score selection>",
        ],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (Benennung Einzelstimmen)

# In[100]:


def module_navigation_name_individualVoices():
    list_de = [
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            "visualizations_MuseScore",
            "<Öffnet MuseScore und zeigt die Notenauswahl an>",
        ],
        [
            "NAME: generische Stimmenbezeichnungen",
            "genericDesignations",
            "<Vergabe generischer Stimmenbezeichnungen (Stimme 1, Stimme 2 etc.)>",
        ],
        [
            "NAME: selbstgewählte Stimmenbezeichnungen",
            "customDesignations",
            "<Vergabe selbstgewählter Stimmenbezeichnungen>",
        ],
    ]

    list_en = [
        [
            "SHOW: Show score selection (MuseScore)",
            "visualizations_MuseScore",
            "<Opens MuseScore and displays the selected score>",
        ],
        [
            "NAME: generic voice/part designations",
            "genericDesignations",
            "<Assignment of generic voice/part designations (Part 1, Part 2 etc.)>",
        ],
        [
            "NAME: self-selected voice/part designations",
            "customDesignations",
            "<assignment of self-selected voice/part designations>",
        ],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (transformierter Notentext)

# In[101]:


def module_navigation_transformedScores():
    list_de = [
        [
            "REPT: Neue Notenauswahl",
            "repeatSelection",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            "visualizations_MuseScore",
            "<Öffnet MuseScore und zeigt den transformierten Notentext an>",
        ],
        [
            "SAVE: Datei speichern",
            "save_file",
            '<Speichert den transformierten Notentext als .xml-Datei im "scratch-Ordner" von music21>',
        ],
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New score selection",
            "repeatSelection",
            "<Repeat the tool with new score selection>",
        ],
        [
            "SHOW: Show score selection (MuseScore)",
            "visualizations_MuseScore",
            "<Opens MuseScore and shows the transformed note text>",
        ],
        [
            "SAVE: Save file",
            "save_file",
            '<Saves the transformed music text as an .xml file in the "scratch folder" of music21>',
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# #### Modul-Navigation (Konvertierung)

# In[102]:


def module_navigation_conversion():
    list_de = [
        [
            "XML : Konvertierung nach .xml",
            "XML",
            "<Konvertiert die Datei ins .xml-Format>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_chords",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen)>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_chords_figuredBass",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen + Generalbass>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_chords_romanNumerals",
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
            "TXT_braille",
            "<Speichert die Datei im .txt-Braille-Format>",
        ],
        [
            "LILY: Konvertierung nach .ly (LilyPond)",
            "lilypond",
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
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        ["XML : Conversion to .xml", "XML", "<Converts the file to .xml format>"],
        [
            "XML : conversion to .xml",
            "XML_chords",
            "<Converts the file to .xml format (transformation to chord connections)>",
        ],
        [
            "XML : conversion to .xml",
            "XML_chords_figuredBass",
            "<Converts the file to .xml format (transformation to chord connections + figured bass>",
        ],
        [
            "XML : conversion to .xml",
            "XML_chords_romanNumerals",
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
            "TXT_braille",
            "<Saves the file in .txt Braille format>",
        ],
        [
            "LILY: Conversion to .ly (LilyPond)",
            "lilypond",
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
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if LANGUAGE == "DE":
        return list_de

    elif LANGUAGE == "EN":
        return list_en


# ## Ausgabe eines Textes zur Beschreibung des Projektes

# In[4]:


def start_printText():
    utility_clear_screen()

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
    input(text_general_proceed())

    utility_clear_screen()


# ## Start der zeichenorientierten Benutzerschnittstelle (CLI)

# ### Prüfen der EnvironmentDatei

# In[8]:


check_environmentFile()


# ### Ausgabe der Projektbeschreibung

# In[9]:


start_printText()


# ### Öffnen des Startmenüs

# In[ ]:


open_startmenu()
