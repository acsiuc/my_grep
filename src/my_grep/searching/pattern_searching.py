import re 

def word_matching(word,i,e,line):
    match_found  = False
    if e: 
        match_found = regex_pattern_search(word, line, i)
    else:                
        if i:
            if word.lower() in line.lower():
                match_found = True            
        else:
            if word in line :
                match_found = True
    return match_found
    
def regex_pattern_search(word,line,i):
    match_found = False
    if i:
        if re.search(word, line, re.IGNORECASE):
            match_found = True
    else:
        if re.search(word, line):
            match_found = True

    return match_found


        
