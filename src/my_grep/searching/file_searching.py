from .pattern_searching import word_matching
import os


def split_and_search(
    user_path: str,
    word: str,
    ignore_case: bool,
    recursive: bool,
    regex: bool,
    list_files: bool,
    invert: bool = False,
) -> list:
    results = []
    if os.path.isdir(user_path):
        for root, dirs, files in os.walk(user_path):
            try:
                for x in files:
                    to_read = os.path.join(root, x)
                    results.extend(
                        file_opening(
                            word, to_read, ignore_case, regex, invert, list_files
                        )
                    )
                if not recursive:
                    break
            except UnicodeDecodeError:
                continue
    elif os.path.isfile(user_path):
        results.extend(
            file_opening(word, user_path, ignore_case, regex, invert, list_files)
        )
    else:
        raise ValueError("Path does not exist.")
    return results


def file_opening(
    word: str,
    to_read: str,
    ignore_case: bool,
    regex: bool,
    invert: bool,
    list_files: bool,
):
    match_data = []
    try:
        with open(to_read, "r") as f:
            if not list_files:
                for line_number, line in enumerate(f):
                    if word_matching(word, ignore_case, regex, line, invert):
                        match_data.append((line, line_number, to_read))
            else:
                for line_number, line in enumerate(f):
                    if word_matching(word, ignore_case, regex, line, invert):
                        match_data.append(to_read)
                        break
    except UnicodeDecodeError:
        return match_data
    return match_data
