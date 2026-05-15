import click
from my_grep.searching.file_searching import split_and_search


@click.command()
@click.option(
    "-i", "--ignore_case", is_flag=True, help="Case insensitive searching of keyword"
)
@click.option(
    "-e",
    "--regex",
    is_flag=True,
    help="Works for patterns, check regex documentation for python",
)
@click.option(
    "-c",
    "--count",
    is_flag=True,
    help="How many times the word has been encountered in the files",
)
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    help="Iteratively searching through all subdirectories of root_path",
)
@click.option(
    "-v",
    "--invert",
    is_flag=True,
    help="Everything but the lines that contain the match",
)
@click.option("-n", "--row_number", is_flag=True, help="Gives the number of the line")
@click.argument("word")
@click.argument("user_path")
def matches_found(
    word, user_path, ignore_case, regex, count, recursive, row_number, invert
):
    counter = 0
    for line, line_number, to_read in split_and_search(
        user_path, word, ignore_case, row_number, recursive, count, regex, invert
    ):
        counter += 1
        if not count:
            if row_number:
                click.echo(f"{line_number} {line} found in {to_read}")
            else:
                click.echo(f"{line} found in {to_read}")
    if count:
        click.echo(f"{word} has been found {counter} times")


if __name__ == "__main__":
    matches_found()
