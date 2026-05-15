import re


def word_matching(
    word: str, ignore_case: bool, regex: bool, line: str, invert: bool = False
):
    match_found = False
    if not invert:
        if regex:
            match_found = regex_pattern_search(word, line, ignore_case, invert)
        else:
            if ignore_case:
                if word.lower() in line.lower():
                    match_found = True
            else:
                if word in line:
                    match_found = True
    else:
        if regex:
            match_found = regex_pattern_search(word, line, ignore_case, invert)
        else:
            if ignore_case:
                if word.lower() not in line.lower():
                    match_found = True
            else:
                if word not in line:
                    match_found = True
    return match_found


def regex_pattern_search(word: str, line: str, ignore_case: bool, invert: bool = False):
    match_found = False
    if not invert:
        if ignore_case:
            if re.search(word, line, re.IGNORECASE):
                match_found = True
        else:
            if re.search(word, line):
                match_found = True
    else:
        if ignore_case:
            if not re.search(word, line, re.IGNORECASE):
                match_found = True
        else:
            if not re.search(word, line):
                match_found = True

    return match_found
