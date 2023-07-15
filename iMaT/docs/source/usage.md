# Usage

## Download and Installation

To use the Interactive Music Analysis Tool (I-MaT), follow these steps:

1. **Install Anaconda or Miniconda**: Download and install Anaconda or Miniconda on your system.
   - For installation instructions, refer to the [installation guide](https://analyse.hfm-weimar.de/doku.php?id=en:jupyter-anaconda).
   - Make sure to include the current version of the HfM environment (`hfm_x.x.x.yml`). You can download it from [here](https://analyse.hfm-weimar.de/scripts/hfm_1.1.2.yml) (right click: save link as..).
   - Additionally, install [MuseScore](https://musescore.org/en).

2. **Download the I-MaT program**:
   - Right-click on the [Download link](https://analyse.hfm-weimar.de/jupyter/I-MaT-InteraktivesMusikanalyse-Tool.py) for the Python script.
   - Select "Save link as" to download the file.
   - Save the file on your desktop (for both Windows and Mac).

## Starting the Program

Follow these steps to start the I-MaT program:

1. **Open the Anaconda Prompt**:

   - On Windows:
     - Go to the Start menu.
     - Navigate to "Anaconda 3 (64-bit)".
     - Choose either "Anaconda Powershell Prompt (anaconda3)" or "Anaconda Prompt (anaconda3)".
     
   - On Mac:
     - Locate the Anaconda Powershell Prompt or Anaconda Prompt in the Finder.

2. **Activate the project-specific Python environment**:

   - In the Anaconda Prompt, you will see a line starting with `(base) C:\Users\Username>`.
   - Enter the following command and press Enter:
     ```
     conda activate hfm_1.x.x
     ```
     Note: Replace `1.x.x` with the actual version number.

3. **Start the program**:

   - In the Anaconda Prompt, type `python`.
   - Drag and drop the 'I-MaT - Interaktives Musikanalyse-Tool.py' file into the prompt window.
   - Press Enter to start the program.

Example command with the program file saved on the desktop (Windows):

```
(hfm_1.x.x) C:\Users\Username>python "C:\Users\Username\Desktop\I-MaT - Interaktives Musikanalyse-Tool.py"
```

The I-MaT program will start running after a few seconds.

## Troubleshooting

If you encounter any issues, follow these steps:

1. Check if the project-specific Python environment is installed correctly:
- Open the Anaconda Prompt.
- Enter the command `conda info --envs` and press Enter.
- Make sure the desired version (`hfm_1.x.x`) is listed in the output.

2. If the version is missing, install the project-specific Python environment by referring to the installation instructions:
- [Windows](https://analyse.hfm-weimar.de/doku.php?id=en:installation_windows)
- [Mac](https://analyse.hfm-weimar.de/doku.php?id=en:installation_mac)
- [Linux](https://analyse.hfm-weimar.de/doku.php?id=en:installation_linux)
- Follow the instructions provided under "2. Project-specific Python environment".