import re


def word_matching(word, i, e, line, v=False):
    match_found = False
    if not v:
        if e:
            match_found = regex_pattern_search(word, line, i)
        else:
            if i:
                if word.lower() in line.lower():
                    match_found = True
            else:
                if word in line:
                    match_found = True
    else:
        if e:
            match_found = regex_pattern_search(word, line, i, v)
        else:
            if i:
                if word.lower() not in line.lower():
                    match_found = True
            else:
                if word not in line:
                    match_found = True
    return match_found


def regex_pattern_search(word, line, i, v=False):
    match_found = False
    if not v:
        if i:
            if re.search(word, line, re.IGNORECASE):
                match_found = True
        else:
            if re.search(word, line):
                match_found = True
    else:
        if i:
            if not re.search(word, line, re.IGNORECASE):
                match_found = True
        else:
            if not re.search(word, line):
                match_found = True

    return match_found
