import click
import importlib

@click.command()
@click.argument('id', type=int, required=True, nargs=1)
def main(id):
    """
    Main function.
    """
    try:
        c = importlib.import_module(f"cryptopals.challenges.c{id}")
        challenge = c.Challenge()
        solution = c.Solution(challenge.challenge)
    except ModuleNotFoundError:
        click.echo(f"Module not found for challenge {id}")
        return
    except AttributeError as e:
        click.echo(f"{e.name} not found for challenge {id}")
        return
    else:
        solution.pretty()


if __name__ == "__main__":
    main()