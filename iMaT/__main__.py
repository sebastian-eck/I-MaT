"""
__main__.py
===========

This is the entry point of the Interactive Music Analysis Tool (I-MaT) Command Line Interface (CLI) application.
The CLI app starts with a loading animation to simulate the time it takes to import the necessary modules.

The main function, start_imat_CLI(), first checks the existence of the environment file using
check_environmentFile() function. If the environment file exists, it then displays the start menu to the
user using display_menu_undirected() function.

When an error occurs during the execution, it is captured and displayed to the console for debugging.

The loading animation runs in a separate thread and stops once all the modules are imported.

This module should be run as the entry point of the I-MaT CLI application.
"""
import threading
from time import sleep

from tqdm import tqdm

from src.constants import TITLE_TEXT

print(TITLE_TEXT)


def animate_loading():
    """
    Creates a loading animation using the tqdm library. This function runs a for loop for 100 iterations,
    simulating computation time with a sleep function. The progress of these iterations is displayed to
    the console using tqdm, creating a loading bar animation.
    """
    for _ in tqdm(range(100), desc='Initializing the program...'):
        sleep(0.010)  # simulating computation time


# Start the loading animation in a separate thread
loading_thread = threading.Thread(target=animate_loading)
loading_thread.start()

# Importing modules
from src.cli.menu_constructors import display_menu_undirected
from src.cli.menu_entries import start_menu_entries
from src.m21_environment.main import check_environmentFile

# Once all modules are imported, stop the animation
loading_thread.do_run = False
loading_thread.join()


def start_imat_CLI():
    """
    Main function to start the Interactive Music Analysis Tool (I-MaT) Command Line Interface (CLI).
    First, it checks if the environment file exists using check_environmentFile function. If it exists,
    it displays the undirected menu to the user using display_menu_undirected function.

    If any exception occurs during the execution, it is caught and printed to the console.
    """
    try:
        check_environmentFile()
        display_menu_undirected(start_menu_entries)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    start_imat_CLI()
