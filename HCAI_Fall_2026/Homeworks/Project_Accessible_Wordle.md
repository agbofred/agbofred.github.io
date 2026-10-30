# Project: Wordle for Everyone — An Accessible Word Game for Older Adults

**Course:** AI 380: Human-AI Interaction · Willamette University
**Instructor:** Prof. Fred Agbo
**Format:** Individual or pair project, completed in five milestones
**Provided file:** `english.py` (list of English words). Nothing else is provided: no starter code, no templates.

---

## 1. Project Overview

The New York Times Wordle is popular, but it assumes players can distinguish colors, read small text, move quickly, remember earlier guesses, and tolerate a punishing, one-puzzle-a-day format. Many older adults cannot or do not want to play under those assumptions.

**Your task:** Design and build your own Wordle-style game that an older adult can play comfortably, then go beyond the NYT version with enhancements that make the game more supportive, more inclusive, and more meaningful.

You choose the language, framework, and interface (web, desktop, text, voice, or a combination). The only fixed constraint is that **your game must use `english.py` as its word source**.

### Learning Outcomes

By the end of this project you will be able to:

1. Apply accessibility standards and human-centered design principles for older adults to an interactive system.
2. Design feedback that does not depend on color alone.
3. Justify design decisions with evidence from the literature and from user testing.
4. Evaluate your system with real or simulated users and iterate on the results.
5. Reflect on where AI or automation helps, and where it should not take control.

---

## 2. Core Requirements (Everyone Must Meet These)

### 2.1 Game Rules

| ID | Requirement |
|----|-------------|
| G1 | A hidden five-letter answer is chosen at the start of each game. |
| G2 | The player has a fixed number of guesses (you decide and justify the number; the NYT uses 6). |
| G3 | Every guess is validated against `english.py`. |
| G4 | A guess that is too short, too long, contains non-letters, or is not a real word is **rejected with a clear message and does not cost a guess**. |
| G5 | Repeated letters are scored correctly (for example, a guess with two `E`s when the answer has one). |
| G6 | The game ends with a clear win or loss message and always offers a new game. |
| G7 | The answer pool is **curated by you** from `english.py`, so players are not asked to guess obscure words. Document how you curated it. |

### 2.2 Accessible Letter Feedback (The Heart of the Project)

Each letter of a guess must be shown in exactly one of three states:

| State | Meaning |
|-------|---------|
| **Correct** | Letter is in the answer and in the right position |
| **Present** | Letter is in the answer but in the wrong position |
| **Absent** | Letter is not in the answer |

Your visual design must satisfy **all** of the following:

| ID | Requirement |
|----|-------------|
| F1 | **Redundant encoding:** Each state uses at least **three** independent cues, such as color, a distinct shape or border style, a symbol or icon, a text label, or a pattern. Color can never be the only signal. |
| F2 | **Highlighting is clear:** An older adult can tell the three states apart at a glance, including in grayscale. |
| F3 | **Contrast:** Text and state indicators meet WCAG 2.1 AA contrast ratios (at least 4.5:1 for text, 3:1 for graphical indicators). Report the measured ratios. |
| F4 | **Color-blind safe:** Your palette works for the three common color vision deficiencies (protanopia, deuteranopia, tritanopia). Show evidence, such as simulator screenshots. |
| F5 | **On-screen keyboard (or equivalent letter tracker):** The same three states are reflected on every letter the player has tried, using the same cues as the guess grid. |
| F6 | **Legend:** A visible, always-available key explains what each state means. |
| F7 | **Words as well as visuals:** Every result is also available as plain-language text (for example, "R is in the word, but not in this spot"), so that it works for screen readers and voice. |
| F8 | **User choice:** The player can switch between at least two feedback styles (such as a standard palette and a high-contrast palette) and the choice persists. |

### 2.3 Broader Accessibility for Older Adults

| ID | Requirement |
|----|-------------|
| A1 | **Readable text:** Default letters and messages are large; the player can enlarge text (at least 200%) without losing content or function. |
| A2 | **Easy targets:** Interactive controls are large and well spaced (at least 44×44 px or equivalent). |
| A3 | **Keyboard-only play:** Every function works without a mouse, with a visible focus indicator. |
| A4 | **Screen reader support:** Results, errors, and game state are announced (for example, via ARIA live regions or equivalent). |
| A5 | **No time pressure:** No timers, no forced speed, no countdown; nothing is lost if the player takes a long time. |
| A6 | **Forgiving interaction:** Letters can be easily deleted, mistakes are not punished, and errors are written in plain, kind language. |
| A7 | **Memory support:** Previous guesses and their feedback remain visible for the whole game. |
| A8 | **Plain language:** Instructions are short, jargon-free, and available at any moment through a Help control. |

---

## 3. Going Beyond the NYT: Enhancements

Implement **at least three** enhancements, with **at least one from each of two different categories**. For each, state in your report which user problem it solves and what evidence shows it helps. You may propose your own idea; get it approved first.

### Category A: Cognitive Support

| Idea | Description |
|------|-------------|
| **Smart hints** | Limited, player-controlled hints that range from gentle ("the word has two vowels") to direct ("the second letter is A"). |
| **Candidate helper** | Shows how many words from the list are still possible, or lets the player view them, based on the clues so far. |
| **"Why this color?" explainer** | Click any scored letter to hear or read why it was scored that way. |
| **Letter notebook** | A scratch area where the player can note letters they suspect, without affecting the game. |
| **Undo / take-back** | Lets the player retract the last submitted guess once per game. |

### Category B: Flexible Input and Output

| Idea | Description |
|------|-------------|
| **Voice play** | Speak guesses and hear results, with spelled-out letters supported. |
| **Read-aloud mode** | Each result is spoken in plain language. |
| **Adjustable pace and layout** | Choices for font, spacing, animation reduction, and sound. |
| **Alternative input** | Large on-screen keyboard, switch-style navigation, or one-letter-at-a-time entry. |

### Category C: Emotional and Social Meaning

| Idea | Description |
|------|-------------|
| **Gentle tone** | Encouraging language with no shaming streaks, and an "I give up" option that reveals the word kindly. |
| **Adjustable difficulty** | Different word lengths, extra guesses, or guaranteed-common words. |
| **Play together** | Two players take turns or collaborate on one puzzle, such as a grandparent and grandchild. |
| **Save and resume** | Pause a game and continue it later. |
| **Word of the day with no penalty** | A daily word without streaks; missing a day has no consequence. |

### Category D: Learning and Reflection

| Idea | Description |
|------|-------------|
| **Word meaning** | After each game, show a short definition or example sentence for the answer. |
| **Vocabulary journal** | Collects words the player has encountered. |
| **Progress view** | Shows positive, non-competitive progress, such as words discovered. |

> **Reminder:** Every enhancement must still meet the Core Requirements above. An enhancement that breaks accessibility is a defect, not a feature.

---

## 4. Milestones

Each milestone is submitted separately. Due dates are set by the instructor.

| # | Milestone | What to deliver | Done when |
|---|-----------|-----------------|-----------|
| **M1** | **Research and Design Plan** | 1-page summary of needs of older adults (cite at least 3 sources); two or three user personas; sketches or wireframes of your feedback design; your chosen enhancements. | Plan explains *why* each design choice suits your users. |
| **M2** | **Working Core Game** | Playable game that meets G1–G7. | A full game can be won, lost, and restarted; invalid guesses do not cost guesses. |
| **M3** | **Accessible Feedback and Interface** | Requirements F1–F8 and A1–A8 implemented. Evidence of contrast and color-blind checks. | Passes your own accessibility checklist (Section 6). |
| **M4** | **Enhancements** | Your three or more enhancements implemented and working. | Each enhancement can be demonstrated, with its purpose stated. |
| **M5** | **Evaluation and Final Submission** | Final game, user evaluation results, reflection report, and demo (live or recorded). | Everything in Section 5 is submitted. |

---

## 5. Final Deliverables

1. **Working game** with run instructions that a classmate can follow without help.
2. **Design and evaluation report** (4–6 pages) containing:
   - Target users and design rationale (from M1).
   - Description of your feedback design, with annotated screenshots of all three states, in color and in grayscale.
   - Contrast measurements and color-blind simulation evidence.
   - Description of each enhancement, the problem it solves, and how well it worked.
   - Evaluation results (see below).
   - Reflection: what you changed after testing, what you would still improve, and where automation or AI should not take over from the player.
3. **Accessibility checklist** (Section 6), completed and honest about gaps.
4. **Short demo** (3–5 minutes) showing a full game, the three feedback states, and each enhancement.
5. **Appendix:** how you curated the answer list from `english.py`.

### Evaluation Requirement

Evaluate your game in **at least two** of the following ways:

| Method | Minimum |
|--------|---------|
| **Usability test with older adults (age 60+)** | At least 3 participants, observing them play and asking short follow-up questions. Obtain consent and **do not collect personal or identifying data**. |
| **Simulated-impairment test** | Play your game with: grayscale display, a color-blindness simulator, 200% zoom, keyboard only, and a screen reader. Record the problems you found and fixed. |
| **Heuristic evaluation** | Review your game against a recognized set, such as Nielsen's heuristics or the Microsoft Guidelines for Human-AI Interaction, citing specific screens. |

Report what you observed, what you changed, and what you did not fix and why.

---

## 6. Accessibility Self-Checklist

Mark each item as Met, Partly Met, or Not Met, with one sentence of evidence.

- [ ] The three letter states are distinguishable in grayscale.
- [ ] No information depends on color alone.
- [ ] Text contrast is 4.5:1 or better; indicators are 3:1 or better.
- [ ] Text can be enlarged to 200% without breaking the layout.
- [ ] The complete game can be played by keyboard only.
- [ ] A screen reader announces guess results and errors.
- [ ] No timers or time pressure exist anywhere.
- [ ] Invalid guesses do not cost a guess, and messages are kind and clear.
- [ ] Help is available at any moment.
- [ ] Previous guesses remain visible.

---

## 7. Grading Rubric (100 points)

### 7.1 Score Summary

| Criterion | Points |
|-----------|--------|
| Core game correctness (G1–G7) | 15 |
| Accessible letter feedback (F1–F8) | 25 |
| Broader accessibility (A1–A8) | 15 |
| Enhancements beyond NYT | 20 |
| Evaluation and evidence | 15 |
| Report, demo, and reflection | 10 |
| **Total** | **100** |

### 7.2 Detailed Rubric

| Criterion | Excellent (90–100%) | Proficient (75–89%) | Developing (50–74%) | Insufficient (<50%) |
|-----------|---------------------|---------------------|----------------------|----------------------|
| **Core game (15)** | All G1–G7 met. Repeated letters scored correctly. Invalid guesses handled gracefully. Answer list is thoughtfully curated and documented. | Minor defects, such as one repeated-letter edge case or a weakly documented answer list. | Playable but with several rule defects, or answers are drawn without curation. | Game is not playable or does not use `english.py`. |
| **Accessible feedback (25)** | Three states use three or more independent cues each. Clear in grayscale. Contrast and color-blind evidence is measured and reported. Keyboard, legend, text alternatives, and style switching are all present. | Redundant encoding present but one or two requirements are weak or lack evidence. | Uses color plus one additional cue; some states are hard to tell apart; limited or no evidence. | Relies on color alone, or states are not distinguishable. |
| **Broader accessibility (15)** | A1–A8 all met and verified, with screen reader and keyboard-only testing. | Most met; one or two gaps are acknowledged. | Several gaps; limited verification. | Little attention to older-adult needs. |
| **Enhancements (20)** | Three or more working enhancements from at least two categories. Each is clearly justified, well integrated, and tested. At least one shows original thinking beyond the menu. | Three working enhancements with adequate justification. | Two working enhancements, or three that are partly working or weakly justified. | One or none working. |
| **Evaluation (15)** | Two or more methods used with clear findings. At least one concrete design change is traced directly to evaluation results. Ethical handling of participants. | Two methods used; findings reported but little evidence of change. | One method, or findings are superficial. | No evaluation. |
| **Report, demo, reflection (10)** | Clear, well organized, evidence-based. Reflection is honest and insightful about limits and AI/automation boundaries. Demo covers all features. | Clear and complete with limited depth. | Missing sections or unclear writing. | Incomplete or unclear. |

### 7.3 Bonus (up to 5 points)

- Voice play that works reliably with older-adult speech patterns.
- A published, publicly accessible version with usage instructions.
- A comparison against the NYT Wordle that identifies specific barriers and shows how yours removes them.

### 7.4 Deductions

| Issue | Deduction |
|-------|-----------|
| Color is the only cue for any letter state | -10 |
| Timer or time-pressure feature | -5 |
| Missing run instructions or game does not start | -10 |
| Participant data collected without consent or containing identifying information | -10 |
| Uncredited code or ideas | Academic integrity process |

---

## 8. Rules and Expectations

- **Provided:** only `english.py`. All other code, design, and writing are your own work.
- **Use of AI tools:** You may use AI assistants for ideas and debugging, but you must disclose the tools used and what they contributed, and you must be able to explain every part of your code.
- **Privacy:** Do not store names, ages, health information, or recordings of participants. Record only anonymous observations.
- **Honesty:** Gaps reported honestly earn more credit than gaps that are hidden and then discovered.

---

## 9. Suggested References

- W3C. *Web Content Accessibility Guidelines (WCAG) 2.1* (contrast, text resize, keyboard, non-text content, use of color).
- Nielsen Norman Group. *Usability for Senior Citizens* and related articles.
- Microsoft. *Guidelines for Human-AI Interaction* (if you add hints or voice).
- National Institute on Aging. *Making Your Website Senior Friendly*.
- Any color-blindness simulator and contrast checker of your choice.

---

## 10. Quick Success Check

Before submitting, ask yourself:

1. Could my grandparent tell the three letter states apart without seeing color?
2. Could they play without a mouse, a timer, or a manual?
3. Did a real or simulated user find a problem that I then fixed?
4. Would my enhancements make someone choose this game over the NYT version, and can I show why?
