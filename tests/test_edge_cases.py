import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess


# Edge case 1: negative numbers. parse_guess accepts them as ints, and the
# guess is then compared like any other number (-5 is below the secret).
def test_negative_guess_parses_and_hints_higher():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

    outcome, message = check_guess(value, 37)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# Edge case 2: decimals. parse_guess truncates "3.7" to 3 instead of crashing.
def test_decimal_guess_truncates_to_int():
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None


# Edge case 3: extremely large values. Python ints don't overflow, so the
# guess parses and compares as "Too High" without crashing.
def test_huge_guess_is_too_high_without_crashing():
    huge = "99999999999999999999"
    ok, value, err = parse_guess(huge)
    assert ok is True
    assert value == 99999999999999999999
    assert err is None

    outcome, message = check_guess(value, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


# Edge case 4: text that is not a number, including values that look numeric.
@pytest.mark.parametrize("raw", ["abc", "1e3", "nan", "inf", "12abc"])
def test_non_numeric_input_returns_error(raw):
    ok, value, err = parse_guess(raw)
    assert ok is False
    assert value is None
    assert err == "That is not a number."


# Empty input is also handled gracefully.
@pytest.mark.parametrize("raw", ["", None])
def test_empty_input_asks_for_a_guess(raw):
    ok, value, err = parse_guess(raw)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


# The valid range for each difficulty. The app uses this to reject guesses
# outside it, so an unknown difficulty falls back to 1 to 100.
@pytest.mark.parametrize(
    "difficulty, expected",
    [("Easy", (1, 20)), ("Normal", (1, 100)), ("Hard", (1, 50)), ("Unknown", (1, 100))],
)
def test_range_for_each_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected
