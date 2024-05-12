import sys
from pathlib import Path
from colorama import Fore


def print_directory_structure(directory: Path, deep: int = 0):
    if deep == 0:
        print(f'{Fore.BLUE}{directory.name}/')
        deep += 1

    for item in directory.iterdir():
        if item.is_dir():
            print(f'{"    " * deep}{Fore.BLUE}{item.name}/')
            print_directory_structure(item, deep + 1)
        else:
            print(f'{"  " * deep}{Fore.GREEN}{item.name}')


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + 'Enter the path to the directory')
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + 'Directory does not exist')
        sys.exit(1)

    print_directory_structure(directory)


if __name__ == '__main__':
    main()
