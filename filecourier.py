import shutil
import sys
from pathlib import Path
from simple_term_menu import TerminalMenu

def fetch_mp3(repo, ext):
    files_found = []
    home_dir = Path.home()
    target_dir = Path(f"/home/blackjack/{repo}")
    for item in home_dir.rglob(ext):
        if item.parent != target_dir:
            files_found.append(item)
    return files_found

def main():
    files_moved = 0
    files = fetch_mp3(sys.argv[1], sys.argv[2])
    target_dir = Path(sys.argv[1])
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
