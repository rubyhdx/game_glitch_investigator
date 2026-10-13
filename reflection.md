# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  (1) The hinting is incorrect. The hint kept showing "Go Higher" until the number reached 99, even though the secret number was 37. The second time, the secret number was 42, but the hint showed "Go Lower" when I typed 15. I think check_guess function is incorrectly calculating the guesses.

  (2) After each game, the "New Game" button doesn't respond. I suspect the new_game code snippet is not working correctly.

  (3) The score is calculated incorrectly. The first time I played and lost after 6 attempts, the score I got was -5. When I typed in the correct secret number in the first try, the score was 70. 

  (4) The number of attempts given was not consistent. In the first game I made 6 attempts, and the game was over. However, the message on top still showed I had 1 attempt remaining. The second time, I went up to 11 attempts when I kept guessing the same number, which is more than the allowed attempts.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Clicked "New Game" button| Expect to restart the game | Does not respond | No output |
| Guessed "99" | Expect the hint to be "go lower" unless the secret number was 100 | The hint showed "go higher" | Showed no error |
| Guess "-5" | Expect the program to show error because -5 is below the allowed guess range | The hint showed "go lower" | Showed no error |
| Guessed "7" and selected "New Game"| Expect the program to start a new game | the original allowed attempts increased from 7 to 8 | Showed no error |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
