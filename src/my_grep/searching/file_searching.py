from .pattern_searching import word_matching
import os


def split_and_search(
    user_path: str,
    word: str,
    ignore_case: bool,
    row_number: bool,
    recursive: bool,
    count: bool,
    regex: bool,
    invert: bool = False,
) -> list:
    results = []
    if os.path.isdir(user_path):
        for root, dirs, files in os.walk(user_path):
            try:
                for x in files:
                    to_read = os.path.join(root, x)
                    results.extend(
                        file_opening(word, to_read, ignore_case, regex, invert)
                    )
                if not recursive:
                    break
            except UnicodeDecodeError:
                continue
    elif os.path.isfile(user_path):
        results.extend(file_opening(word, user_path, ignore_case, regex, invert))
    else:
        raise ValueError("Path does not exist.")
    return results


def file_opening(word: str, to_read: str, ignore_case: bool, regex: bool, invert: bool):
    match_data = []
    with open(to_read, "r") as f:
        for line_number, line in enumerate(f):
            if word_matching(word, ignore_case, regex, line, invert):
                match_data.append((line, line_number, to_read))
    return match_data
