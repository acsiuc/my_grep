import re


def word_matching(
    word: str,
    ignore_case: bool,
    regex: bool,
    line: str,
    fuzzy: bool,
    invert: bool = False,
):
    match_found = False
    if fuzzy:
        for word_in_line in line.split(" "):
            if fuzzy_matching(word, word_in_line):
                match_found = True
                break
    else:
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


def fuzzy_matching(word: str, word_in_line: str):
    matrix = [
        [0 for col in range(len(word_in_line) + 1)] for row in range(len(word) + 1)
    ]
    for x in range(len(word) + 1):
        for y in range(len(word_in_line) + 1):
            if x < 1:
                matrix[x][y] = y
            else:
                matrix[x][y] = x
                break

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            to_check = []
            if word[x - 1] == word_in_line[y - 1]:
                matrix[x][y] = matrix[x - 1][y - 1]
            else:
                to_check.append(matrix[x - 1][y - 1] + 1)
                to_check.append(matrix[x][y - 1] + 1)
                to_check.append(matrix[x - 1][y] + 1)
                matrix[x][y] = min(to_check)

    if matrix[-1][-1] <= 2:
        return True
    else:
        return False
