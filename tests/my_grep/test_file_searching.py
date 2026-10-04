from my_grep.searching.file_searching import file_opening
from my_grep.searching.file_searching import split_and_search
import pytest


def test_file_opening(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("eu sunt aici")
    assert file_opening("eu", test_file, False, False, False, False, False) == [
        ("eu sunt aici", 0, test_file)
    ]


def test_split_and_search(tmp_path):
    folder = tmp_path / "folder"
    folder.mkdir()
    test_file = folder / "test.txt"
    test_file.write_text("eu sunt aici")
    assert split_and_search(test_file, "eu", False, False, False, False, False) == [
        ("eu sunt aici", 0, test_file)
    ]


def test_incorrect_path_split_and_search(tmp_path):
    folder = tmp_path / "folder"
    folder.mkdir()
    test_file = folder / "test.txt"
    test_file.write_text("eu sunt aici")
    with pytest.raises(ValueError):
        split_and_search(r"C:\not\exist", "eu", False, False, False, False, False)


def test_file_only_file_opening(tmp_path):
    folder = tmp_path / "folder"
    folder.mkdir()
    test_file = folder / "test.txt"
    test_file.write_text("eu sunt aici")
    assert file_opening("eu", test_file, False, False, False, False, True) == [
        test_file
    ]


def test_folder_split_and_search(tmp_path):
    folder = tmp_path / "folder"
    folder.mkdir()
    test_file = folder / "test.txt"
    second_file = folder / "second_test.txt"
    test_file.write_text("eu sunt aici")
    second_file.write_text("nimeni")
    assert split_and_search(folder, "eu", False, False, False, True, False, False) == [
        str(test_file)
    ]
