"""cli interface"""

from pathlib import Path

import click

from scaffold_python import core


@click.command()
@click.argument("project_name")
def main(project_name: str):
    """scaffold a python project"""
    core.make_project(location=Path.cwd(), project_name=project_name)


if __name__ == "__main__":
    main()
