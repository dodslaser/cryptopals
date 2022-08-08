"""
Cryptopals
"""

import importlib
import pathlib
import inspect

import click

from cryptopals.ui import UI


@click.group()
def main():
    """
    Dummy main function
    """


@main.command()
@click.argument("id")
def solve(id):
    """
    Solve a cryptopals challenge.
    """
    try:
        challenge = importlib.import_module(f"cryptopals.challenges.c{id}")
        instance = challenge.Challenge()
        solution = challenge.Solution(instance.challenge)
    except ModuleNotFoundError:
        click.echo(f"Module not found for challenge {id}")
        return
    except AttributeError as error:
        click.echo(f"{error.name} not found for challenge {id}")
        return
    else:
        solution.pretty()


@main.command()
def list():
    """
    List all challenges.
    """

    module_info = {"ID": [], "Challenge": []}
    challenge_path = pathlib.Path(__file__).parent.joinpath("challenges")
    for path in challenge_path.glob("c*.py"):
        module_name = f"cryptopals.challenges.{path.stem}"
        challenge = importlib.import_module(module_name)
        info = inspect.getdoc(challenge.Challenge).split("\n")[1]
        module_info["ID"].append(str(challenge.Challenge.id))
        module_info["Challenge"].append(info)

    UI.table_view(module_info, widths=[4, None])


if __name__ == "__main__":
    main()
