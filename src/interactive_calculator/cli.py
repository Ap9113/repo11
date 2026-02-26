import sys
import click
import logging
from interactive_calculator.calculator import add, subtract, multiply, divide, power

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """
    Interactive Calculator CLI
    """
    pass


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add_cmd(a: float, b: float):
    """
    Add two numbers.
    """
    result = add(a, b)
    click.echo(result)


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract_cmd(a: float, b: float):
    """
    Subtract two numbers.
    """
    result = subtract(a, b)
    click.echo(result)


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def multiply_cmd(a: float, b: float):
    """
    Multiply two numbers.
    """
    result = multiply(a, b)
    click.echo(result)


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def divide_cmd(a: float, b: float):
    """
    Divide two numbers.
    """
    try:
        result = divide(a, b)
        click.echo(result)
    except ZeroDivisionError as e:
        logger.error(e)
        click.echo(f"Error: {e}")
        sys.exit(1)


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def power_cmd(a: float, b: float):
    """
    Raise a to the power of b.
    """
    result = power(a, b)
    click.echo(result)


@cli.command()
def interactive():
    """
    Run in interactive mode. Type 'exit' to quit.
    """
    click.echo("Entering interactive mode. Type 'exit' at any prompt to quit.")
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power,
    }

    while True:
        op = click.prompt("Operation [add, subtract, multiply, divide, power]", type=str)
        if op.lower() == 'exit':
            click.echo("Goodbye!")
            break
        if op not in operations:
            click.echo(f"Unknown operation '{op}'. Please choose from add, subtract, multiply, divide, power.")
            continue

        try:
            a_raw = click.prompt("First number (a)", type=str)
            if a_raw.lower() == 'exit':
                click.echo("Goodbye!")
                break
            b_raw = click.prompt("Second number (b)", type=str)
            if b_raw.lower() == 'exit':
                click.echo("Goodbye!")
                break

            a = float(a_raw)
            b = float(b_raw)
            result = operations[op](a, b)
            click.echo(f"Result: {result}")
        except ValueError:
            click.echo("Invalid input. Please enter numeric values.")
        except ZeroDivisionError as e:
            click.echo(f"Error: {e}")


if __name__ == '__main__':  # pragma: no cover
    cli()
