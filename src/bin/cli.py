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
@click.option(
    "-l",
    "--list_files",
    is_flag=True,
    help="Shows only the files in which the match is found",
)
@click.option(
    "-f",
    "--fuzzy",
    is_flag=True,
    help="Shows a close match, using Levenshtein distance",
)
@click.argument("word")
@click.argument("user_path")
def matches_found(
    word,
    user_path,
    ignore_case,
    regex,
    count,
    recursive,
    row_number,
    list_files,
    fuzzy,
    invert,
):
    counter = 0
    try:
        if fuzzy and regex:
            raise click.UsageError("Regex and Fuzzy matching flags both active")
        if not list_files:
            for line, line_number, to_read in split_and_search(
                user_path,
                word,
                ignore_case,
                recursive,
                regex,
                list_files,
                fuzzy,
                invert,
            ):
                counter += 1
                if not count:
                    if row_number:
                        click.echo(f"{line_number} {line} found in {to_read}")
                    else:
                        click.echo(f"{line} found in {to_read}")
            if count:
                click.echo(f"{word} has been found {counter} times")
        else:
            for file_found in split_and_search(
                user_path,
                word,
                ignore_case,
                recursive,
                regex,
                list_files,
                fuzzy,
                invert,
            ):
                click.echo(f"{word} was found in {file_found}")
    except ValueError:
        click.echo(f"{user_path} path does not exist")


if __name__ == "__main__":
    matches_found()
