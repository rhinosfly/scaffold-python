"""cli interface"""

from pathlib import Path

import click

from scaffold_python import core


@click.command()
@click.argument("project_name")
@click.option(
    "--from-inside",
    "-i",
    "from_inside",
    is_flag=True,
    help="current working directory is project root directory",
)
def main(project_name: str, from_inside: bool):
    """scaffold a python project"""
    core.make_project(
        location=Path.cwd(), project_name=project_name, from_inside=from_inside
    )


if __name__ == "__main__":
    main()
