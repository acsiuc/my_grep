import pytest
from my_grep.modules.file_searching import file_opening

def test_file_opening(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text('eu sunt aici')
    assert file_opening('eu', test_file,False, False) == [('eu sunt aici',0, test_file)]










# def split_and_search(user_path, word,i,n,r,c,e):
#     results = []
#     for root, dirs, files in os.walk(user_path):
#         try:
#             for x in files:
#                 to_read = os.path.join(root, x)
#                 results.extend(file_opening(word,to_read,i,e))
#             if not r: 
#                 break
#         except UnicodeDecodeError:
#             continue
#     return results


# def file_opening(word,to_read,i,e):
#     match_data = []
#     with open(to_read, "r") as f:
#             for line_number, line in enumerate(f):
#                 if word_matching(word, i, e, line):
#                     match_data.append((line,line_number, to_read))
#     return match_data
    
    
