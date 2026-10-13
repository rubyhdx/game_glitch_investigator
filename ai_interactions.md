# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number (`-5`) | Challenge 1 instructions: identify edge-case inputs and generate pytest cases for them. Follow-up: "we just need pytest." | `test_negative_guess_parses_and_hints_higher` | Yes | Negative guesses are outside the valid range and are a likely input mistake. |
| Decimal (`3.7`) | Same as above | `test_decimal_guess_truncates_to_int` | Yes | The parser turns decimals into ints, so it silently truncates them and that should be tested. |
| Very large number (`99999999999999999999`) | Same as above | `test_huge_guess_is_too_high_without_crashing` | Yes | Checks that a huge number parses and is treated as too high instead of crashing. |
| Non-numeric text (`abc`, `1e3`, `nan`, `inf`, `12abc`) | Same as above | `test_non_numeric_input_returns_error` | Yes | Text like `1e3`, `nan`, and `inf` looks numeric but should still be rejected. |
| Empty input (`""`, `None`) | Same as above | `test_empty_input_asks_for_a_guess` | Yes | An empty submit is the most common blank input. |
| Difficulty range (unknown difficulty) | Same as above | `test_range_for_each_difficulty` | Yes | Confirms each difficulty's bounds and the 1 to 100 fallback for unknown values. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
