from my_grep.searching.pattern_searching import regex_pattern_search
from my_grep.searching.pattern_searching import word_matching


def test_regex_pattern_search():
    assert regex_pattern_search(
        r"[A-Za-z0-9._%+-]+@gmail\.com", "user@gmail.com", False
    )


def test_regex_false():
    assert not regex_pattern_search(r"[A-Za-z0-9._%+-]+@gmail\.com", "eu sunt", False)


def test_regex_case_insensitive():
    assert regex_pattern_search(r"[A-Za-z0-9._%+-]+@gmail\.com", "User@gmail.com", True)


def test_word_matching():
    assert word_matching("eu", False, False, "eu sunt")


def test_v_word_matching():
    assert not word_matching("eu", False, False, "eu sunt", v=True)


def test_word_matching_false():
    assert not word_matching("eu", False, False, "e sunt")


def test_word_matching_case_insensitive():
    assert word_matching("EU", True, False, "eu sunt")


def test_word_matching_regex():
    assert word_matching(r"[A-Za-z0-9._%+-]+@gmail\.com", False, True, "user@gmail.com")


def test_word_matching_regex_insensitive():
    assert word_matching(r"[A-Za-z0-9._%+-]+@gmail\.com", True, True, "USER@gmail.com")


def test_word_matching_regex_false():
    assert not word_matching(r"[A-Za-z0-9._%+-]+@gmail\.com", False, False, "eu sunt")
