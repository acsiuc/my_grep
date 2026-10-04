from my_grep.searching.pattern_searching import regex_pattern_search
from my_grep.searching.pattern_searching import word_matching
from my_grep.searching.pattern_searching import fuzzy_matching


def test_regex_pattern_search():
    assert regex_pattern_search(
        r"[A-Za-z0-9._%+-]+@gmail\.com", "user@gmail.com", False
    )


def test_regex_false():
    assert not regex_pattern_search(r"[A-Za-z0-9._%+-]+@gmail\.com", "eu sunt", False)


def test_regex_case_insensitive():
    assert regex_pattern_search(r"[A-Za-z0-9._%+-]+@gmail\.com", "User@gmail.com", True)


def test_word_matching():
    assert word_matching("eu", False, False, "eu sunt", False, False)


def test_v_word_matching():
    assert not word_matching("eu", False, False, "eu sunt", False, True)


def test_word_matching_false():
    assert not word_matching("eu", False, False, "e sunt", False)


def test_word_matching_case_insensitive():
    assert word_matching("EU", True, False, "eu sunt", False)


def test_word_matching_regex():
    assert word_matching(
        r"[A-Za-z0-9._%+-]+@gmail\.com", False, True, "user@gmail.com", False
    )


def test_word_matching_regex_insensitive():
    assert word_matching(
        r"[A-Za-z0-9._%+-]+@gmail\.com", True, True, "USER@gmail.com", False, False
    )


def test_word_matching_regex_false():
    assert not word_matching(
        r"[A-Za-z0-9._%+-]+@gmail\.com", False, False, "eu sunt", False, False
    )


def test_fuzzy_matching_one_distance():
    assert fuzzy_matching("sunt", "synt")


def test_fuzzy_matching_perfect_match():
    assert fuzzy_matching("sunt", "sunt")


def test_fuzzy_matching_two_distance():
    assert fuzzy_matching("sunt", "syit")


def test_fuzzy_matching_fail():
    assert not fuzzy_matching("sunt", "myit")
