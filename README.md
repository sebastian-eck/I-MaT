# The Interactive Music Analysis Tool (I-MaT)

I-MaT is an innovative tool designed to facilitate in-depth musical analysis through an easy-to-use interface. I-MaT offers a comprehensive set of functionalities allowing for the examination of musical pieces from a wide range of perspectives. The documentation (available on [readthedocs.io](https://i-mat.readthedocs.io/en/latest/)) serves as a comprehensive guide, aiming to provide you with insights into I-MaT's functionalities and its modular concept, and assist both first-time users and experienced researchers in using the tool effectively.

The sections contained within the documentation provide detailed information on how to use the Interactive Music Analysis Tool, from [downloading and the installation](https://i-mat.readthedocs.io/en/latest/getting_started.html), to [contribution and code extension](https://i-mat.readthedocs.io/en/latest/contribute.html), to its application in music analysis. Furthermore, you will find a detailed descriptions of I-MaT's [source code](https://i-mat.readthedocs.io/en/latest/module_files/src.html), explaining the different packages' and modules' content that make up the tool.

Through this documentation, I hope to provide you with the necessary knowledge to navigate I-MaT, explore its features, and conduct your own analyses by using my tool!

Start by installing the Interactive Music Analysis Tool (I-MaT):

    pip install imat

To run the tool, simply type the following command into your shell:

    imat

If that was too fast, don't worry.
You can find a detailed User Guide for how to install and start I-MaT in the [Getting Started with I-MaT](https://i-mat.readthedocs.io/en/latest/getting_started.html) section.

Please enjoy and let me know if you have any questions or suggestions on how to further improve I-MaT's functionalities!

Contact: imat.inquiries@gmail.com

# An Introduction to I-MaT

The Interactive Music Analysis Tool, I-MaT, (University of Music Franz Liszt Weimar, 2021a) is a modular program designed for producing visualizations, statistical analyses as well as tokenizations of textual music data. Its functionalities are built on various commonly used python libraries, such as music21 (Cuthbert, 2023a) and MidiTok (Fradet et al., 2021). I-MaT was developed as a sub-project within the fellowship project Computer-Assisted Music Analysis in Digital University Teaching (Pfleiderer, 2022; University of Music Franz Liszt Weimar, 2021c).

The fellowship project (2021) was located at the Institute for Musicology Weimar-Jena at the Franz Liszt University of Music Weimar, Germany.

## Project Overview

The aim of the fellowship project “Computer-Assisted Music Analysis […]” was to design, test, teach with and evaluate a comprehensive set of teaching modules for music analysis that make use of various computer-assisted, primarily quantitative analysis tools. The teaching modules were intended to complement conventional musicological and analysis courses and mainly focus on:

- “the computer-based annotation and visualization of sheet music texts and audio files,
- the statistical analysis of music corpora,
- the search for musical patterns (rhythms, melodies, harmony connections, etc.),
- and the comparison of interpretation” (Poliakov and Nadar, 2021a)

Within the project Computer-Assisted Music Analysis in Digital University Teaching, three computerized approaches to music score analysis were utilized, namely music21,  CAMAT,  and I-MaT (University of Music Franz Liszt Weimar, 2021d).

Music21 is a Python library created at the Massachusetts Institute of Technology (MIT), Cambridge for symbolic music representation and processing (Cuthbert, 2023b). CAMAT, on the other hand, is a Computer-Assisted Music Analysis Toolkit developed within the course of the fellowship project (Poliakov and Nadar, 2021b; Pfleiderer et al., 2023). CAMAT uses its own unique data structure to overcome certain design problems found within the music21 framework (Poliakov and Nadar, 2021a). Tutorials for musicological university level courses were prepared and their usability evaluated; the tutorials include music examples and code that can be executed as Jupyter Notebooks (University of Music Franz Liszt Weimar, 2021b).

## Objectives

As experienced during the fellowship project’s didactic test phase, working with Jupyter Notebooks and analyzing music with packages such as music21 or CAMAT proved challenging in particular for musicology students with none or only very limited knowledge of computer commands or programming languages.

As an initial response, I-MaT emerged as a pragmatic solution, aiding students in quickly obtaining meaningful analysis results. Motivated by the success and the evident impact it had on the learning process, the development and refinement of I-MaT continued independently following the conclusion of the aforementioned fellowship project at the end of 2021.

Since then, this research endeavor has been guided by two primary objectives:

1. The first objective was to design an easily accessible tool with a well-structured interface, further lowering the barrier for musicology students to engage with methods from digital musicology.
2. The second objective was to further refine and modularize I-MaT’s program code, to create a modular and flexible tool that could effortlessly be extended by either adding new functionalities offered by already integrated modules (such as music21 and MidiTok), or by incorporating new python packages related to digital musicology or other relevant fields, e.g., computational linguistics.

## I-MaT: Features and Accessibility

```
I-MaT - Interactive Music Analysis Tool, v3.2.1, (2023). Project: "Computer-Assisted Music Analysis"

Department of Musicology Weimar-Jena, University of Music Franz Liszt Weimar, Germany

MIT License, Copyright (c) 2023 S.O. Eck.

----------------------------------------------------------------------

LOCATION: Start Menu

Please make a selection from the options below by entering the entry index number:

No.       Menu item                                           <Explanation>

1         PROG: Analysis of one sheet music file              <Analysis of a single piece of music>
2         CONV: Conversion of multiple music files            <Conversion of multiple music files within one folder>
3         TOKE: Tokenisation of multiple music files          <Tokenisation of multiple music files within one folder>
4         CONF: Update Software Paths and Preferences         <Update or redefine paths to essential software and user preferences>

Which menu item should be executed? (<No. of menu item>):
```
Figure 1: The Interactive Music Analysis Tool (I-MaT) - Start Menu

Addressing the steep learning curve often encountered with Python-based music analysis tools like Music21 or CAMAT, the Interactive Music Analysis Tool (I-MaT) was designed specifically with user accessibility in mind. I-MaT utilizes a new and innovative approach to access, work with and implement various python libraries, such as, but not limited to, music21 or MidiTok for textual music analysis, within one unified, user friendly text-based command-line-interface (CLI).

I-MaT allows users to quickly obtain results by navigating through simple dynamic menu structures and selecting methods and tools from predefined options (see Figure 1). The tool uses an accessible and easily extendable text-based CLI, with the underlying Music21 and MidiTok commands remaining invisible to the user. While requiring minimal familiarity with command-line environments, the preference for a CLI over a GUI offers a compromise between user-friendliness and easy code extendibility.

This compromise was necessary to keep the barrier to entry as low as possible, and to encourage a broad usage and user-based participation in the tool's ongoing development via GitHub (Eck, 2023b). To further increase accessibility, I-MaT was distributed via Pypi.org (Eck, 2023c), allowing for an easy installation via integrated package-management systems such as the commonly used python pip installer. I-MaT’s source code is complemented by an extensive online documentation that offers guidance to both users as well as contributors (Eck, 2023a).

While virtually encompassing all the functionalities of the integrated python packages for music information retrieval/tokenization, i.e., music21/MidiTok, I-MaTs functionalities are currently limited to a representative, yet well-tested set of statistical analysis, export, visualization, transformation and musical data tokenization tools.

With all those benefits at hand, I-MaT is a very flexible and powerful tool that could cater to the needs of a diverse range of users, from novice music analysts to advanced researchers.

## Education and Training

In addition to its analytical capabilities, I-MaT serves as an effective didactic tool, further bridging the gap between musicology and the broader field of computer-assisted analysis and Music Information Retrieval (MIR).

I-MaT’s various functionalities could provide valuable support for music and musicology courses at both high school and university levels. Its user-friendly interface and simple installation make it an ideal tool for students to quickly obtain results and explore various analytical approaches using computational methods, allowing them to gain a deeper understanding of the musical works they are studying.

Furthermore, I-MaT’s modular design opens possibilities for launching educational projects centered around musicological programming, with the added advantage of seamlessly integrating their outcomes and functions into I-MaT through collaborative platforms like GitHub.

By using I-MaT, students can develop valuable analytical skills that are useful not only in musicology but also in other areas of the humanities where data-driven methods are becoming increasingly important.

The Interactive Music Analysis Tool, I-MaT, should be seen as a contribution to Computational Musicology or Digital Musicology within the Digital Humanities.

## Sheet Music Databases curated within the project

The fellowship project contains [two larger databases](https://analyse.hfm-weimar.de/doku.php?id=en:datenbank):

- The [main database](https://analyse.hfm-weimar.de/doku.php?id=en:komponisten) comprises several thousand individual sheet music files (.xml).
- The [subcorpus](https://analyse.hfm-weimar.de/doku.php?id=en:notenauswahl) contains all scores used in the two teaching modules for score analysis and was carefully curated by student members of the project team.

### List of incorporated databases

The fellowship project uses several, under the Common Licence freely available online databases as sources for its own sheet music corpora.

These include:

- The Classical Music Score Digitization Project (weblink no longer available).
- [Josquin Research Project, Standford University](http://jrp.stanford.edu).
- [Kern Scores](http://kern.ccarh.org/).
- [Tobi's Notenarchiv](http://www.tobis-notenarchiv.de/noten/index.htm).
- [Sethus Calvisius' cantional settings, edited by Dr. Franz Kaern-Biederstedt](https://analyse.hfm-weimar.de/doku.php?id=en:calvisius).
- [Music21 Corpus, MIT](https://web.mit.edu/music21/doc/about/referenceCorpus.html).

## References

- Cuthbert, M. S. A. (2023a). music21. A Toolkit for Computer-Aided Musicology. http://web.mit.edu/music21/ (accessed 19 July 2023).
- Cuthbert, M. S. A. (2023b). music21. GitHub Repository. https://github.com/cuthbertLab/music21 (accessed 19 July 2023).
- Eck, S. O. (2023a). Interactive Music Analysis Tool (I-MaT). Dokumentation. https://i-mat.readthedocs.io/en/latest/ (accessed 19 July 2023).
- Eck, S. O. (2023b). Interactive Music Analysis Tool (I-MaT). GitHub Repository. https://github.com/sebastian-eck/I-MaT (accessed 19 July 2023).
- Eck, S. O. (2023c). Interactive Music Analysis Tool (I-MaT). Pypi.org Distribution. https://pypi.org/project/imat/ (accessed 19 July 2023).
- Fradet, N., Briot, J.-P., Chhel, F., Seghrouchni, A. E. F. and Gutowski, N. (2021). MidiTok. A Python Package for MIDI File Tokenization. https://archives.ismir.net/ismir2021/latebreaking/000005.pdf (accessed 19 July 2023).
- Pfleiderer, M. (2022). Computergestützte Musikanalyse. Fellowship für Innovation in der digitalen Hochschullehre. Abschlussbericht. https://stifterverband.org/file/10986/download?token=tl9S2EL_.
- Pfleiderer, M., Poliakov, E. and Nadar, C. R. (2023). Analyze! Development and Integration of Software-Based Tools for Musicology Music Theory, Proceedings Innovation in Music 2022 Conference.
- Poliakov, E. and Nadar, C. R. (2021a). CAMAT. Computer Assisted Music Analysis Toolkit. https://analyse.hfm-weimar.de/lib/exe/fetch.php?media=en:dmrn-16-proceedings_camat.pdf (accessed 19 July 2023).
- Poliakov, E. and Nadar, C. R. (2021b). CAMAT. GitHub Repository. https://github.com/Christon-Ragavan/CAMAT (accessed 19 July 2023).
- University of Music Franz Liszt Weimar (2021a). Fellowship Project Computer-Assisted Music Analysis. Interactive Music Analysis Tool (I-MaT). https://analyse.hfm-weimar.de/doku.php?id=en:interaktive_musikanalyse (accessed 19 July 2023).
- University of Music Franz Liszt Weimar (2021b). Fellowship Project Computer-Assisted Music Analysis. Modules and Tutorials. https://analyse.hfm-weimar.de/doku.php?id=en:tutorials.
- University of Music Franz Liszt Weimar (2021c). Fellowship Project Computer-Assisted Music Analysis. Project-Wiki. https://analyse.hfm-weimar.de/doku.php?id=en:start (accessed 19 July 2023).
- University of Music Franz Liszt Weimar (2021d). Fellowship Project Computer-Assisted Music Analysis. Sheet Music Analysis. https://analyse.hfm-weimar.de/doku.php?id=en:noten (accessed 19 July 2023).
