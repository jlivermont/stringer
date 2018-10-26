import pytest

from app.validators.all_letters import AllLettersValidator

@pytest.fixture
def validator():
    return AllLettersValidator()

@pytest.mark.parametrize("char,expected", [
    ("a", True),
    ("Z", False),
    (".", False),
    ("/", False),
    ("â", False),
    ("अ", False),
])
def test_is_valid_lower_english_letter(char, expected, validator):
    assert (validator._is_lower_english_letter(char) == expected)


@pytest.mark.parametrize("string,expected", [
    ("AbC", ['a', 'b', 'c']),
    ("abC.", ['a', 'b', 'c']),
    ("\tabC.\n", ['a', 'b', 'c']),
    (" a b C . ", ['a', 'b', 'c']),
    ("a.A,a|A+â", ['a']),
    (r",/\+=-_`~|<>/.", []),
])
def test_build_char_dict(string, expected, validator):
    char_dict = validator._build_char_dict(string)
    assert (sorted(char_dict.keys()) == expected)


@pytest.mark.parametrize("string,expected", [
    ('abcdefghijklmnopqrstuvwxyz', True),
    ('    aaaaaaaaabcdefghijklmnopqrstuvwxyz', True),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', True),
    ('abcdefghijklmnopqrstuvwxZy....', True),
    ('bcdefghijklmnopqrstuvwxZy....', False),
    ('âbcdefghijklmnopqrstuvwxZy....', False),
])
def test_validate(string, expected, validator):
    assert (validator.validate(string) == expected)
