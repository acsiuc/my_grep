import click
from my_grep.searching.file_searching import split_and_search


@click.command()
@click.option("-i", is_flag=True, help="Case insensitive searching of keyword")
@click.option(
    "-e", is_flag=True, help="Works for patterns, check regex documentation for python"
)
@click.option(
    "-c", is_flag=True, help="How many times the word has been encountered in the files"
)
@click.option(
    "-r",
    is_flag=True,
    help="Iteratively searching through all subdirectories of root_path",
)
@click.option("-n", is_flag=True, help="Gives the number of the line")
@click.argument("word")
@click.argument("user_path")
def show_results(word, user_path, i, e, c, r, n):
    counter = 0
    for line, line_number, to_read in split_and_search(user_path, word, i, n, r, c, e):
        counter += 1
        if not c:
            if n:
                click.echo(f"{line_number} {line} found in {to_read}")
            else:
                click.echo(f"{line} found in {to_read}")
    if c:
        click.echo(f"{word} has been found      {counter} times")


if __name__ == "__main__":
    show_results()
