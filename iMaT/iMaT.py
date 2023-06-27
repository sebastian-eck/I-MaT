import os
import sys

from src.cli.cli_menu_entries import start_menu_entries
from src.cli.cli_menu_structures import display_menu_undirected
from src.routines.routines_configure_m21_environment import check_environmentFile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    check_environmentFile()

    display_menu_undirected(start_menu_entries)


if __name__ == '__main__':
    main()
