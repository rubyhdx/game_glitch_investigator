# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Game's purpose
   This is a number guessing game built with Streamlit. The player picks a difficulty, which sets the number range and the number of attempts. After each guess, the game says "Go HIGHER!" or "Go LOWER!" until the player finds the secret number. The score goes down for wrong guesses and up for a win, and a win earlier in the game scores more.

- Bugs found: 
   - The hints pointed the wrong way, and on every other attempt the comparison was between an int and a str.
   - New Game didn't work after a game ended, because the status stayed "lost" or "won."
   - The score changed by +5 or -5 on "Too High" depending on whether the attempt number was even or odd.
   - The attempts counter started at 1, so "Attempts left" was one lower than the limit, and New Game made it jump up by one.
   - Guesses outside the range, like -5, were accepted and got a hint.
   - The guess box kept its old text after New Game.
   - The game logic lived in app.py and logic_utils.py had only placeholders, so the tests couldn't run.

- Fixes applied:
   - Swapped the hint messages and removed the string conversion and the TypeError fallback in check_guess.
   - New Game now resets status, score, and history, and uses the difficulty's range for the secret.
   - Made wrong guesses always cost 5 points.
   - Started attempts at 0.
   - Rejected out-of-range guesses, and only counted valid guesses as attempts.
   - Gave the guess box a new key on each New Game, so it starts empty.
   - Moved the logic into logic_utils.py, and added pytest.ini so the tests can import it.
   - Fixed the three check_guess tests to unpack the (outcome, message) pair, and added a score regression test.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 10
2. Game returns "Go LOWER!"
3. User enters a guess of 5
4. Game returns "Go HIGHER!"
5. Score updates correctly after each guess
6. User enters a guess of 6
7. Game returns "Correct!"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
pytest tests -q
....                                                                             [100%]
4 passed in 0.00s
```

## 🚀 Stretch Features

- Challenge 1 test results
```
pytest tests -q
..................                                                                  [100%]
18 passed in 0.02s
```
