from .pattern_searching import word_matching
import os

def split_and_search(user_path, word,i,n,r,c,e):
    results = []
    for root, dirs, files in os.walk(user_path):
        try:
            for x in files:
                to_read = os.path.join(root, x)
                results.extend(file_opening(word,to_read,i,e))
            if not r: 
                break
        except UnicodeDecodeError:
            continue
    return results


def file_opening(word,to_read,i,e):
    match_data = []
    with open(to_read, "r") as f:
            for line_number, line in enumerate(f):
                if word_matching(word, i, e, line):
                    match_data.append((line,line_number, to_read))
    return match_data
    
    