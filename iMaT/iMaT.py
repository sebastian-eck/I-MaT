import threading
from time import sleep
from tqdm import tqdm

from src.constants import TITLE_TEXT

print(TITLE_TEXT)

# It looks like it, but it is not a fake loading screen! It keeps the user busy while everything gets set up. Trust me.

def animate_loading():
    for _ in tqdm(range(64), desc='Initializing the program...'):
        sleep(0.015)  # simulating computation time

# Start the loading animation in a separate thread
loading_thread = threading.Thread(target=animate_loading)
loading_thread.start()

# Import your modules here
from src.cli.menu_constructors import display_menu_undirected
from src.cli.menu_entries import start_menu_entries
from src.m21_environment.main import check_environmentFile

# Once all modules are imported, stop the animation
loading_thread.do_run = False
loading_thread.join()

def main():
    try:
        check_environmentFile()
        display_menu_undirected(start_menu_entries)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
