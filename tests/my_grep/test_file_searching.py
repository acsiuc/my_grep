import pytest
from my_grep.searching.file_searching import file_opening

def test_file_opening(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text('eu sunt aici')
    assert file_opening('eu', test_file,False, False) == [('eu sunt aici',0, test_file)]

