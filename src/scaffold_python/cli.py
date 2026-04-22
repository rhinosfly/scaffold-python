"""cli interface"""

from scaffold_python import core
from pathlib import Path
import sys

def main():
    """main function"""
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: scaffold-python <project_name>")
        sys.exit(1)
    core.make_project(location=Path.cwd(), project_name=args[0])


if __name__ == "__main__":
    main()
