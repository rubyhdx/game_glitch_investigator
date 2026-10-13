from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_wrong_guess_always_costs_five_points():
    # Regression: "Too High" used to add 5 points on even attempts and
    # subtract 5 on odd attempts, so the score depended on the attempt number.
    for attempt in range(1, 9):
        assert update_score(50, "Too High", attempt) == 45
