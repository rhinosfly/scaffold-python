"""
core logic


format:
    project_name
    - README.md
    - .gitignore
    - pyproject.toml
    - src/project_name
        - core.py
        - cli.py
"""

from pathlib import Path


def make_project(location: Path, project_name: str):
    """create project"""

    # define directories
    project_root = location / project_name
    src_dir = project_root / "src" / project_name
    # check if exists
    if project_root.exists():
        raise Exception(f"{project_root} already exists")
    # create directories
    src_dir.mkdir(parents=True)

    # make root files

    # readme
    readme = project_root / "README.md"
    _ = readme.write_text(f"""# {project_name}""")

    # .gitignore
    gitignore = project_root / ".gitignore"
    _ = gitignore.write_text(
        """__pycache__/
*.egg-info/"""
    )

    # pyproject.toml
    pyproject = project_root / "pyproject.toml"
    _ = pyproject.write_text(
        f"""[project]
name = "{project_name}"
version = "0.0.1"

[project.scripts]
{project_name} = "{project_name}.cli:main\""""
    )

    # make src files

    # core.py
    core = src_dir / "core.py"
    _ = core.write_text(
        '''"""core logic"""

def main():
    """placeholder for base logic"""
    print("Hello World")
'''
    )

    # cli.py
    cli = src_dir / "cli.py"
    _ = cli.write_text(
        f'''"""CLI interface"""
  
from {project_name} import core

def main():
    """main function"""
    core.main()


if __name__ == "__main__":
    main()
'''
    )
