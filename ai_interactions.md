# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Challenge 4 — improve the readability of the terminal output by showing the
top recommendations as a formatted table that includes the "reasons" for each
song's score.

**Prompts used:**

- "Improve the readability of our terminal output. Suggest a way to use a
  library like tabulate or simple ASCII formatting to display the top
  recommendations. The table must include the reasons for each score."

**What did the agent generate or change?**

- Checked whether `tabulate` was installed (it was not) and chose a
  dependency-free approach using Python's standard-library `textwrap`.
- Edited `src/main.py`:
  - Added `import textwrap`.
  - Added `_HEADERS` / `_WIDTHS` and two helpers, `_print_row()` (renders a row
    whose cells can span multiple wrapped lines) and `_separator()`.
  - Rewrote `print_recommendations()` to draw a bordered ASCII table with
    columns: #, Title, Artist, Score, and Why (reasons). Each reason is wrapped
    to the column width and printed on its own line inside the cell.
- Ran `python -m src.main` to confirm the table renders for all three profiles.

**What did you verify or fix manually?**

- Confirmed the reasons actually appear in the table (the required part), and
  that the point values in each reason add up to the shown score.
- Checked that long titles/artists wrap instead of breaking the borders, and
  that the `+---+` separators line up with the column widths.
- Chose ASCII over `tabulate` on purpose so no new dependency is needed and the
  project still runs with a clean `python -m src.main`.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
