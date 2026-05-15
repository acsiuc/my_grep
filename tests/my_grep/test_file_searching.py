from my_grep.searching.file_searching import file_opening
from my_grep.searching.file_searching import split_and_search


def test_file_opening(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("eu sunt aici")
    assert file_opening("eu", test_file, False, False, False) == [
        ("eu sunt aici", 0, test_file)
    ]


def test_split_and_search(tmp_path):
    folder = tmp_path / "folder"
    folder.mkdir()
    test_file = folder / "test.txt"
    test_file.write_text("eu sunt aici")
    assert split_and_search(
        test_file, "eu", False, False, False, False, False, False
    ) == [("eu sunt aici", 0, test_file)]
