# Interactive Music Analysis Tool (I-MaT)

The **Interactive Music Analysis Tool (I-MaT)**[^1] is a modular program designed for producing visualizations and statistical analyses of sheet music files. It is based on the **music21** python library ([GitHub repository](https://github.com/cuthbertLab/music21.git)), developed by the Massachusetts Institute of Technology (MIT),[^2] and was originally created as a sub-project of the fellowship project Computer-assisted Music Analysis in Digital University Teaching ([Computergestützte Musikanalyse in der digitalen Hochschullehre, 2021, project report (PDF)](https://stifterverband.org/file/10986/download?token=tl9S2EL_)).[^3]

The project was located at the Department of Musicology Weimar-Jena at the Franz Liszt University of Music Weimar[^4] and was funded by the Thuringian Ministry for Economy, Science and Digital Change and the Deutscher Stifterverband.[^5]

## Project Overview

The aim of the aforementioned project was to design, test, teach with and evaluate a comprehensive set of teaching modules for music analysis that make use of various computer-assisted, primarily quantitative analysis tools. The teaching modules were intended to complement conventional musicological and analysis courses and mainly focus on:

- "the computer-based annotation and visualization of sheet music texts and audio files,
- the statistical analysis of music corpora,
- the search for musical patterns (rhythms, melodies, harmony connections, etc.),
- and the comparison of interpretation"[^6]

Within the project "Computer-assisted Music Analysis [...]", three computerized approaches to music score analysis were utilized, namely music21,[^7] CAMAT,[^8] and I-MaT itself. Music21 is a Python library developed at MIT for symbolic music representation and processing. CAMAT ([GitHub repository](https://github.com/Christon-Ragavan/CAMAT)), on the other hand, is a Computer-Assisted Music Analysis Toolkit developed by Egor Poliakov[^9] and Christon R. Nadar[^10] within the fellowship project. CAMAT uses its own unique data structure, developed within the project to overcome certain design problems found within the music21 framework.[^11] Tutorials for musicological courses were prepared using music examples and code that can be executed as Jupyter Notebooks.[^12]

Both music21 and CAMAT require rudimentary knowledge of Python command syntax. In contrast, the Interactive Music Analysis Tool (I-MaT) is designed for users who have none to only limited knowledge of computer commands or programming languages as it utilizes a new and innovative approach to access and work with the music21 toolkit.

### I-MaT: Features and Accessibility

```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- Start menu --

Please select:

No.  Menu item                                                         <Explanation>

1    PROG: Analysis of a single piece of music                         <Analysis of a single piece of music>
2    SETT: Settings                                                    <View the settings in the music21 environment file>
3    HELP: Project overview                                            <Information about the project "Computer-Aided Music Analysis">
4    LANG: Ändere Ausgabesprache auf DEUTSCH                           <Ändert die Ausgabesprache des Programms auf Deutsch>
5    EXIT: Exit programm                                               <Exits the Python script>

Which menu item should be executed? (<No. of menu item>):
```

Figure 1: *I-Mat - Start menu*

I-MaT allows users to quickly obtain results by navigating through simple dialog windows and selecting methods and tools from predefined displayed options (*cf. figure 1*), shown in an easy-to-understand text-based command-line interface (CLI), i.e. the MS Windows Command shell (cmd) or PowerShell. Therefore, music21 commands on which the program is based are not visible to the user. Results such as visualizations, diagrams, transformed sheet music files, and CSV files can then be exported and displayed within I-MaT as well as in external programs such as MuseScore, matplotlib or PSPP, in which they can be further processed or analysed (*cf. figures 2-12*).

Moreover, the modular structure of I-MaT not only facilitates the addition of new analysis modules based on music21 or other libraries, but also enables easier maintenance and updates of the tool as new analysis methods and techniques become available over time. This makes I-MaT a flexible and therefore powerful tool that can cater to the needs of a diverse range of users, from novice music analysts to advanced researchers.

### Education and Training

I-MaT is an innovative tool for music analysis that can provide valuable support for music and musicology courses at both high school and university levels. Its user-friendly interface and modular design make it an ideal tool for students to quickly obtain results and explore various analytical approaches using computational methods, allowing them to gain a deeper understanding of the musical works they are studying. In addition to its analytical capabilities, I-MaT can serve as an effective didactic tool to introduce students to computer-assisted musicology and programming concepts in general, as well as music21 or other libraries used in the tool.

By using I-MaT, students can develop valuable analytical skills that will be useful not only in musicology but also in other areas of the humanities where data-driven methods are becoming increasingly important.

Lastly, I-MaT's modular structure enables collaborative work not only in the classroom but also bears the possibility to connect through platforms like GitHub, providing opportunities for its further development.

I-MaT should be seen as a contribution to Computational Musicology or Digital Musicology within the Digital Humanities.

Author: Sebastian Oliver Eck (Student Project Assistant - Institute for Musicology Weimar-Jena, Franz Liszt University of Music Weimar, Germany)

## Sheet Music Databases curated within the project

The fellowship project contains two larger databases:[^13]

- The main database[^14] comprises of several thousand individual sheet music files (MusicXML).
- The subcorpus[^15] contains all scores used in the two teaching modules for score analysis[^16] and was carefully curated by student members of the project team.

### List of incorporated databases (last accessed on: 2023-04-25)

The fellowship project uses several, under the Common Licence freely available online databases as sources for its own sheet music corpora. These include:

- The Classical Music Score Digitization Project (weblink not longer available).
- [Josquin Research Project, Standford University](http://jrp.stanford.edu).
- [Kern Scores](http://kern.ccarh.org/).
- [Tobi's Notenarchiv](http://www.tobis-notenarchiv.de/noten/index.htm).
- [Sethus Calvisius' cantional settings, edited by Dr. Franz Kaern-Biederstedt](https://analyse.hfm-weimar.de/doku.php?id=en:calvisius).
- [Music21 Corpus, MIT](https://web.mit.edu/music21/doc/about/referenceCorpus.html).

## Appendix: Figures

### General

```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- main menu individual piece --

Please select:

No.  Menu item                                                         <Explanation>

1    FILE: Menu selection                                              <Basic functions>
2    TOOL: Menu selection (statistical analysis)                       <Selection of various statistical analysis tools>      
3    TOOL: Menu selection (visualisation)                              <Selection of different visualisation tools>
4    TOOL: Menu selection (pattern search)                             <Selection of different tools for pattern search>      
5    SETT: Settings                                                    <Settings in the music21 environment file/language settings>
6    HELP: Project overview                                            <Information about the project "Computer-Aided Music Analysis">
7    EXIT: Exit program                                                <Exits the Python script>

Which menu item should be executed? (<No. of menu item>):
```


Figure 2:  *I-Mat - main menu*


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- Submenu individual piece (Files) --

Please select:

No.  Menu item                                                         <Explanation>

1    FILE: Select new score                                            <Allows you to select a new score>
2    SHOW: Show metadata (score)                                       <Displays the metadata of the selected score>
3    PLAY: Play selected score (midi)                                  <Plays score as midi>
4    NAME: Change the names of the individual voices                   <Allows you to rename the individual voices>
5    NAME: Show names of individual voices                             <Displays the names of the individual voices>
6    EXPO: Export file                                                 <Saves a selection of notes as .xml/.midi/.ly/.pdf file>
7    BACK: Back to the main menu                                       <Return to the main menu>

Which menu item should be executed? (<No. of menu item>): 
```


Figure 3:  *I-Mat - Submenu individual piece (Files)*


### Statistical Analysis


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- Submenu individual piece (statistical analysis) --

Please select:

No.  Menu item                                                         <Explanation>

1    STAT: Ambitus
2    STAT: Ambitus (comparison)
3    STAT: Interval types                                              <Attention: currently only consistently monodic melody lines are correctly analyzed>.
4    STAT: Interval types and frequency                                <Attention: currently only consistently monodic melody lines are correctly analyzed>
5    STAT: Interval types and frequency (comparison)                   <Attention: currently only consistently monodic melody lines are correctly analyzed>
6    STAT: Number of intervals                                         <Attention: currently only consistently monodic melody lines are correctly analyzed>
7    STAT: Number of tones                                             <Attention: currently only consistently monodic melody lines are correctly analyzed>
8    HIST: Sound events per pitch                                      <A histogram of the pitch space>
9    HIST: Sound events per pitch class                                <A pitch class histogram>
10   HIST: Sound events per tone durations                             <A histogram of the pitch lengths>
11   BARS: Pitches over time (pitch lengths)                           <A graph of events sorted by pitch space over time>    
12   BARS: Pitch classes over time (pitch durations)                   <A graph of events sorted by pitch space over time>    
13   HIST: Tone starting frequency on types of metrical positions      <Metric weight; Explanations: https://analyse.hfm-weimar.de/doku.php?id=basics1>
14   MORE: Further graphs                                              <Two-dimensional frequency distributions/scatter diagrams>
15   BACK: Back to the main menu                                       <Return to the main menu>

Which menu item should be executed? (<No. of menu item>):
```


Figure 4:  *I-Mat - Submenu individual piece (statistical analysis), page 1*


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- Results --


Identifier                 Rhythm value (quarter = 1.0)       Rhythm value name (x-axis)       Frequency (y-axis)


Partitur, Meas. 1-71       1.0                                Quarter                          142

Partitur, Meas. 1-71       2.0                                Half                             201

Partitur, Meas. 1-71       3.0                                Dotted Half                      36

Partitur, Meas. 1-71       4.0                                Whole                            153

Partitur, Meas. 1-71       6.0                                Dotted Whole                     29

Partitur, Meas. 1-71       8.0                                Breve                            50

Partitur, Meas. 1-71       12.0                               Dotted Breve                     30

Partitur, Meas. 1-71       14.0                               Double Dotted Breve              1

Partitur, Meas. 1-71       16.0                               Imperfect Longa                  10

Partitur, Meas. 1-71       24.0                               Perfect Longa                    1

Partitur, Meas. 1-71       32.0                               Imperfect Maxima                 3



<To continue, please press Enter>
```


Figure 5:  *I-Mat - statistical analyzes: 10  HIST: Sound events per tone durations (results)*


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

Please select:

No.  Menu item                                                         <Explanation>

1    REPT: New score selection                                         <Repeat the tool with new score selection>
2    EXPT: Export results as CSV file                                  <Exports and saves the results as CSV file>
3    GRPH: Display results as graphic                                  <Exports and saves the results as graphic> 
4    BACK: Back to the main menu                                       <Return to the main menu>

Which menu item should be executed? (<No. of menu item>):
```

Figure 6:  *I-Mat - statistical analyzes: 10  HIST: Sound events per tone durations (export menu)*


![Figure 7](https://user-images.githubusercontent.com/130949054/234640457-f6768147-4e48-4ec8-9bdc-c9ce5ba2ec75.PNG)


Figure 7:  *I-Mat - statistical analyzes: 10  HIST: Sound events per tone durations (3 GRPH: Display results as graphic)*


### Pattern Search


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- Submenu individual piece (Pattern search) --

Please select:

No.  Menu item                                                         <Explanation>

1    SEAR: Pattern search (without rhythmic values)                    <Search for a sequence of notes (without rhythmic values)>
2    SEAR: Pattern search (without rhythmic values/transposed)         <Search for a sequence of notes and all of its transpositions (without rhythmic values)>
3    SEAR: Pattern search (with rhythmic values)                       <Search for a sequence of notes (with rhythmic values)>
4    SEAR: Pattern search (with rhythmic values/transposed)            <Search for a sequence of notes and all of its transpositions (with rhythmic values)>   
5    SEAR: Pattern search (only rhythm)                                <Search for a specific rhythm>
6    BACK: Back to the main menu                                       <Return to the main menu>

Which menu item should be executed? (<No. of menu item>):
```

Figure 8: *I-Mat - Submenu individual piece (Pattern search)*


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

Please enter the note / rhythm pattern (1.0 = quarter) used for the pattern search here.

Selection: ['C', 'D', 'C']

Please select:

No.  Menu item

1    ‾‾‾‾  -   C-flat
2    C         C
3    ____  ♯   C-sharp
4    ‾‾‾‾  -   D-flat
5    D         D
6    ____  ♯   D-sharp
7    ‾‾‾‾  -   E-flat
8    E         E
9    ____  ♯   E-sharp
10   ‾‾‾‾  -   F-flat
11   F         F
12   ____  ♯   F-sharp
13   ‾‾‾‾  -   G-flat
14   G         G
15   ____  ♯   G-sharp
16   ‾‾‾‾  -   A-flat
17   A         A
18   ____  ♯   A-sharp
19   ‾‾‾‾  -   B-flat
20   B         B
21   ____  ♯   B-sharp
22   BACK: Remove the last note entered
23   DONE: Finish input

Which menu item should be executed? (<No. of menu item>):
```

Figure 9: *I-Mat - 2  SEAR: Pattern search (without rhythmic values/transposed) (search pattern input menu)*


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

-- Results --


No.       Pitch                       Measure       Beat       Voice          Search pattern       


1         <music21.note.Note C>       5             1.0        Superius       C D C

2         <music21.note.Note C>       62            1.0        Superius       C D C

3         <music21.note.Note C>       67            3.0        Superius       C D C

4         <music21.note.Note C>       33            2.0        Tenor          C D C

5         <music21.note.Note C>       16            2.0        Bassus         C D C

6         <music21.note.Note C>       53            1.0        Bassus         C D C

7         <music21.note.Note F>       3             2.5        Altus          F G F

8         <music21.note.Note F>       33            2.25       Altus          F G F

9         <music21.note.Note F>       52            1.0        Altus          F G F

10        <music21.note.Note F>       40            2.0        Bassus         F G F

11        <music21.note.Note G>       14            3.5        Superius       G A G

12        <music21.note.Note G>       36            2.0        Superius       G A G

13        <music21.note.Note G>       57            1.0        Superius       G A G

14        <music21.note.Note G>       57            3.0        Superius       G A G

15        <music21.note.Note G>       24            1.0        Altus          G A G

16        <music21.note.Note G>       47            2.5        Altus          G A G

17        <music21.note.Note G>       47            1.0        Tenor          G A G

18        <music21.note.Note G>       10            1.0        Bassus         G A G



<To continue, please press Enter>
```

Figure 10: *I-Mat - 2  SEAR: Pattern search (without rhythmic values/transposed) (results)*


```
I-MaT - Interactive music analysis tool, (2.2, 01.2022)

Fellowship project "Computer-assisted Music Analysis"


Fellowship for innovations in digital university teaching

----------------------------------------------------------------------

Please select:

No.  Menu item                                                         <Explanation>

1    REPT: New search pattern selection                                <Repeat the tool with new score selection>
2    EXPT: Export results as CSV file                                  <Exports and saves the results as CSV file>
3    GRPH: Export results as XML file                                  <Exports and saves the results highlighted in a xml file>
4    BACK: Back to the main menu                                       <Return to the main menu>

Which menu item should be executed? (<No. of menu item>):
```

Figure 11: *I-Mat - 2  SEAR: Pattern search (without rhythmic values/transposed) (export menu)*


![I-Mat - 2  SEAR Pattern search (without rhythmic values - transposed) (3  GRPH Export results as XML file)](https://user-images.githubusercontent.com/130949054/236673524-30fee5c7-0a66-4156-8b6b-fe24661aad18.png)


Figure 12: *I-Mat - 2  SEAR: Pattern search (without rhythmic values/transposed) (3  GRPH: Export results as XML file)*



## References

[^1]: Official project website: "Interactive Music Analysis Tool (I-MaT)", accessible at: https://analyse.hfm-weimar.de/doku.php?id=en:interaktive_musikanalyse (last accessed on: 2023-04-25).
[^2]: Official project website: "music11: a toolkit for computer-aided musicology", accessible at: http://web.mit.edu/music21/ (last accessed on: 2023-04-25).
[^3]: Official project website: "Computergestützte Musikanalyse in der digitalen Hochschullehre", accessible at: https://analyse.hfm-weimar.de/doku.php?id=en:start (last accessed on: 2023-04-25).
[^4]: University of Music Franz Liszt Weimar. Department of Musicology Weimar-Jena, https://www.hfm-weimar.de/en/department-of-musicology-weimar-jena/department-of-musicology-weimar-jena (last accessed on: 2023-04-25).
[^5]: Fellowships Hochschullehre "Deutscher Stifterverband": Fellows 2020, Prof. Dr. Martin Pfleiderer (Hochschule für Musik Franz Liszt Weimar, Institut für Musikwissenschaft Weimar-Jena); Fellowship für Innovationen in der digitalen Hochschullehre, Projekt: Computergestützte Musikanalyse, https://stifterverband.org/digital-lehrfellows-thueringen/2020/pfleiderer (last accessed on: 2023-04-25).
[^6]: Egor Poliakovand Christon R. Nada: "CAMAT: Computer Assisted Music Analysis Toolkit", DMRN+16: Digital Music Research Network, One-Day Workshop 2021; Queen Mary University London, Tue 21 Devember 2021, https://analyse.hfm-weimar.de/lib/exe/fetch.php?media=en:dmrn-16-proceedings_camat.pdf (last accessed on: 2023-04-25).
[^7]: Official project website: 1) "Module Basics: Sheet Music Analysis with music21", https://analyse.hfm-weimar.de/doku.php?id=en:basics1; 2) "Module Advanced Sheet Music Analysis with music21: Searching for Tone Sequences", https://analyse.hfm-weimar.de/doku.php?id=en:advanced1 (last accessed on: 2023-04-25).
[^8]: Official project website: 1) "Module Basics Sheet Music Analysis with CAMAT", https://analyse.hfm-weimar.de/doku.php?id=en:camat; 2) "Module Advanced: Sheet Music Analysis with CAMAT", https://analyse.hfm-weimar.de/doku.php?id=en:advanced_camat (last accessed on: 2023-04-25).
[^9]: Egor Poliakov (HMT Leipzig, Germany, egor.poliakov@hmt-leipzig.de).
[^10]: Christon R. Nadar (Semantic Music Technologies, Fraunhofer IDMT, Ilmenau, Germany).
[^11]: Cf. Egor Poliakovand Christon R. Nada (2021) (see footnote 6). For further information on the development of CAMAT, cf. Martin Pfleiderer, Egor Polyakov and Christon-Ragavan Nadar: Analyze! Development and integration of software-based tools for musicology music theory, in: Proceedings Innovation in Music 2022 Conference, edited by Jan-Olof Gullo, Russ Hepworth-Sawyer, Justin Paterson and Rob Toulson, Milton Park: Routledge 2023 (in print).
[^12]: Official project website: "Sheet Music Analysis", https://analyse.hfm-weimar.de/doku.php?id=en:noten (last accessed on: 2023-04-25).
[^13]: Official project website: "Sheet Music Database", https://analyse.hfm-weimar.de/doku.php?id=en:datenbank (last accessed on: 2023-04-25).
[^14]: Official project website: "Sheet Music Database. Main Database", https://analyse.hfm-weimar.de/doku.php?id=en:komponisten (last accessed on: 2023-04-25).
[^15]: Official project website: "Sheet Music Database. Subcorpus", https://analyse.hfm-weimar.de/doku.php?id=en:datenbank (last accessed on: 2023-04-25).
[^16]: Cf. footnotes 7 and 8.
