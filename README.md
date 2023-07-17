# An Introduction: The Interactive Music Analysis Tool (I-MaT)

The **Interactive Music Analysis Tool (I-MaT)**[^1] is a modular program designed for producing visualizations and statistical analyses of sheet music files. It is based on the **music21** python library ([GitHub repository](https://github.com/cuthbertLab/music21.git)), developed by the Massachusetts Institute of Technology (MIT),[^2] and was originally created as a subproject of the fellowship project Computer-assisted Music Analysis in Digital University Teaching ([Computergestützte Musikanalyse in der digitalen Hochschullehre, 2021, project report (PDF)](https://stifterverband.org/file/10986/download?token=tl9S2EL_)).[^3]

The project was located at the Department of Musicology Weimar-Jena at the Franz Liszt University of Music Weimar[^4] and was funded by the Thuringian Ministry for Economy, Science and Digital Change and the Deutscher Stifterverband.[^5]

A comprehensive documentation is available on: https://i-mat.readthedocs.io/en/latest/

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
I-MaT - Interactive Music Analysis Tool, v3.0, (2023). Project: "Computer-Assisted Music Analysis"

Department of Musicology Weimar-Jena, University of Music Franz Liszt Weimar, Germany

MIT License, Copyright (c) 2023 S.O. Eck.

----------------------------------------------------------------------

LOCATION: Start Menu

Please make a selection from the options below by entering the entry index number:

No.       Menu item                                           <Explanation>

1         PROG: Analysis of one sheet music file              <Analysis of a single piece of music>
2         CONV: Conversion of multiple music files            <Conversion of multiple music file wihthin one folder>
3         TOKE: Tokenisation of multiple music files          <Tokenisation of multiple music file wihthin one folder>
4         CONF: Update Software Paths and Preferences         <Update or redefine paths to essential software and user preferences>

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

- The main database[^14] comprises several thousand individual sheet music files (MusicXML).
- The subcorpus[^15] contains all scores used in the two teaching modules for score analysis[^16] and was carefully curated by student members of the project team.

### List of incorporated databases

The fellowship project uses several, under the Common Licence freely available online databases as sources for its own sheet music corpora. These include:

- The Classical Music Score Digitization Project (weblink no longer available).
- [Josquin Research Project, Standford University](http://jrp.stanford.edu).
- [Kern Scores](http://kern.ccarh.org/).
- [Tobi's Notenarchiv](http://www.tobis-notenarchiv.de/noten/index.htm).
- [Sethus Calvisius' cantional settings, edited by Dr. Franz Kaern-Biederstedt](https://analyse.hfm-weimar.de/doku.php?id=en:calvisius).
- [Music21 Corpus, MIT](https://web.mit.edu/music21/doc/about/referenceCorpus.html).

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
