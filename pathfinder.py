import shutil
from pathlib import Path
from simple_term_menu import TerminalMenu
import sys

def fetch():
    files_found = []
    target_dir = Path.home() / sys.argv[1]
    for item in Path.home().rglob(sys.argv[2]):
        if not item.is_relative_to(target_dir):
            files_found.append(item)
    return files_found

def main():
    files_moved = 0
    files = fetch()
    target_dir = Path.home() / sys.argv[1]
    options = TerminalMenu(
            [str(f) for f in files],
            multi_select=True,
            show_multi_select_hint=True,
            )

    menu_entry_index = options.show()

    for choice in menu_entry_index:
        shutil.move(files[choice], target_dir)
        files_moved += 1

    if files_moved <= 0:
        print("No files were transfered...")
    elif files_moved == 1:
        print(f"Only {files_moved} file was transfered...")
    else:
        print(f"There were a total of {files_moved} transfered to {target_dir}...") 

main()
