---
title: "HW3: Wordle for Everyone"
subtitle: "AI 380: Human-AI Interaction · Fall 2026"
format:
  html:
    css: assets/custom-theme.css
    include-after-body: assets/toc-scrollspy-fix.html
    toc: true
    toc-depth: 3
---

::: {.callout-note}
Design and build a Wordle-style game that older adults can play comfortably. Go beyond the familiar daily puzzle with features that make the experience more supportive, inclusive, and meaningful. This is an individual or pair project completed in five milestones.

**Provided file:** [english.py](https://github.com/AI-380/Shared_Libraries/releases/download/English_Library/english.py){download="english.py"}, a list of English words. No starter code or templates are provided.
:::

## Project Overview

The New York Times Wordle is popular, but it assumes players can distinguish colors, read small text, move quickly, remember earlier guesses, and tolerate a one-puzzle-a-day format. Your task is to design and build your own Wordle-style game for older adults.

You choose the language interface (Phone, web, or desktop). The fixed constraint is that your game must use the Rasa Pro, text and voice conversation mode, and the [english.py](https://github.com/AI-380/Shared_Libraries/releases/download/English_Library/english.py){download="english.py"} as its word source, 

### Learning Outcomes

By the end of this project, you will be able to:

1. Apply accessibility standards and human-centered design principles to an interactive system for older adults.
2. Design feedback that does not depend on color alone.
3. Justify design decisions with evidence from literature and user testing.
4. Evaluate your system with real or simulated users and iterate on the results.
5. Reflect on where AI or automation helps, and where it should not take control.

---

## Core Requirements

### Game Rules

| ID | Requirement |
|---|---|
| G1 | Choose a hidden five-letter answer at the start of each game. |
| G2 | Give the player a fixed number of guesses. Choose and justify the number; the NYT uses six. |
| G3 | Validate every guess against [english.py](https://github.com/AI-380/Shared_Libraries/releases/download/English_Library/english.py){download="english.py"}. |
| G4 | Reject guesses that are too short, too long, contain non-letters, or are not real words. Give a clear message and do not use a guess. |
| G5 | Score repeated letters correctly. For example, handle a guess with two `E`s when the answer has one. |
| G6 | End with a clear win or loss message and always offer a new game. |
| G7 | Curate the answer pool from [english.py](https://github.com/AI-380/Shared_Libraries/releases/download/English_Library/english.py){download="english.py"} so players are not asked to guess obscure words. Document your curation method. |

### Accessible Letter Feedback

Each guessed letter must have exactly one of these states:

| State | Meaning |
|---|---|
| **Correct** | The letter is in the answer and in the right position. |
| **Present** | The letter is in the answer but in the wrong position. |
| **Absent** | The letter is not in the answer. |

Your interface should try to meet at least these three accessibility priorities:

| Priority | Requirement |
|---|---|
| **Perceivable feedback** | Distinguish all three letter states without relying on color. Use clear redundant cues, a visible legend, and plain-language results that assistive technology can announce. Verify grayscale and color-vision simulation, and report contrast ratios of at least 4.5:1 for text and 3:1 for indicators. |
| **Operable, forgiving interaction** | Support keyboard-only play with visible focus, controls at least 44 × 44 px, easy correction of mistakes, and no timers or penalties for invalid guesses. Keep Help available. |
| **Readable, supportive design** | Keep text usable at 200% zoom, retain previous guesses, and let players choose a feedback style that persists. Use short, plain-language instructions. |

For more accessibility techniques and success criteria, consult the online [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/). Select criteria relevant to your game; you do not need to implement every criterion.

---

## Enhancements

Implement at least **three enhancements**, with at least one from each of **two different categories**. You may propose your own idea; get it approved first. For every enhancement, state in your report which user problem it addresses and what evidence shows it helps.

### Category A: Cognitive Support

| Idea | Description |
|---|---|
| Smart hints | Limited, player-controlled hints that range from gentle (“the word has two vowels”) to direct (“the second letter is A”). |
| Candidate helper | Show how many words remain possible, or let the player view them, based on the clues so far. |
| “Why this color?” explainer | Let players select any scored letter to hear or read why it received that state. |
| Letter notebook | Provide a scratch area for suspected letters that does not affect the game. |
| Undo / take-back | Let the player retract the last submitted guess once per game. |

### Category B: Flexible Input and Output

| Idea | Description |
|---|---|
| Voice play | Accept spoken guesses and support spelling out letters. |
| Read-aloud mode | Speak each result in plain language. |
| Adjustable pace and layout | Offer choices for font, spacing, animation reduction, and sound. |
| Alternative input | Offer a large on-screen keyboard, switch-style navigation, or one-letter-at-a-time entry. |

### Category C: Emotional and Social Meaning

| Idea | Description |
|---|---|
| Gentle tone | Use encouraging language without shaming streaks, and offer an “I give up” option that kindly reveals the word. |
| Adjustable difficulty | Offer different word lengths, extra guesses, or guaranteed-common words. |
| Play together | Let two players take turns or collaborate on one puzzle, such as a grandparent and grandchild. |
| Save and resume | Let players pause a game and continue later. |
| Word of the day with no penalty | Offer a daily word without streaks or consequences for missing a day. |

### Category D: Learning and Reflection

| Idea | Description |
|---|---|
| Word meaning | After each game, show a short definition or example sentence for the answer. |
| Vocabulary journal | Collect words the player has encountered. |
| Progress view | Show positive, non-competitive progress, such as words discovered. |

::: {.callout-warning}
Every enhancement must still meet the core requirements. An enhancement that breaks accessibility is a defect, not a feature.
:::

---

## Milestones

Due dates are set by the instructor. Each milestone is submitted separately.

| # | Milestone | What to deliver | Done when |
|---|---|---|---|
| **M1** | Design Concept and Data-Flow Diagram | A design concept for the game and a data-flow diagram showing how player input, word validation, game logic, and feedback connect. | The concept is clear, and the diagram shows the main inputs, processes, and outputs. No additional M1 deliverables are required. |
| **M2** | Working Core Game | A playable game meeting G1–G7. | A full game can be won, lost, and restarted; invalid guesses do not cost guesses. |
| **M3** | Accessible Feedback and Interface | Implement the three accessibility priorities and include contrast and color-vision check evidence. | The game passes your accessibility checklist in Section 6. |
| **M4** | Enhancements | Implement and demonstrate at least three working enhancements. | Each enhancement can be demonstrated, with its purpose stated. |
| **M5** | Final Submission and Workshop | Working game, design summary, deployment, README, and workshop flyer. | All items in Final Deliverables are ready for submission and the November workshops. |

---

## Final Deliverables

1. **Working game** that meets the core game and accessibility requirements.
2. **Design summary** (2–3 pages) covering the design concepts, core achievements, and reflection on remaining improvements.
3. **Demo** during the **November 11 usability and pre-workshop**, showing the game and its main features.
4. **Deployed program** submitted with a live link.
5. **Short README** explaining how to access and use the game.
6. **Workshop flyer** introducing the game to older adults at the **November 16 workshop**.

<!--
### Evaluation Requirement

Evaluate your game using at least **two** methods below:

| Method | Minimum |
|---|---|
| Usability test with older adults (age 60+) | At least three participants. Observe them playing and ask short follow-up questions. Obtain consent and do not collect personal or identifying data. |
| Simulated-impairment test | Test grayscale display, a color-blindness simulator, 200% zoom, keyboard-only use, and a screen reader. Record problems found and fixed. |
| Heuristic evaluation | Review the game against a recognized set, such as Nielsen’s heuristics or Microsoft Guidelines for Human-AI Interaction, citing specific screens. |

Report what you observed, what you changed, and what you did not fix and why.
-->

<!-- ---

## Accessibility Self-Checklist

Mark each item **Met**, **Partly Met**, or **Not Met**, and give one sentence of evidence.

- [ ] **Perceivable feedback:** States are clear without color, results are available to assistive technology, and contrast and color-vision checks are documented.
- [ ] **Operable interaction:** The game works by keyboard, has visible focus and large controls, allows easy correction, and has no time pressure.
- [ ] **Readable support:** The game works at 200% zoom, keeps previous guesses visible, provides Help, and remembers the chosen feedback style.

--- -->

## Grading Rubric

### Score Summary

| Criterion | Points |
|---|---:|
| Core game correctness (G1–G7) | 20 |
| Accessible feedback and interaction | 20 |
| Enhancements beyond NYT | 15 |
| M1 design concept and data-flow diagram | 10 |
| Design summary and reflection (2–3 pages) | 10 |
| November 11 demo | 10 |
| Deployed program and short README | 10 |
| November 16 workshop flyer | 5 |
| **Total** | **100** |

### Detailed Rubric

| Criterion | Excellent (90–100%) | Proficient (75–89%) | Developing (50–74%) | Insufficient (<50%) |
|---|---|---|---|---|
| **Core game (20)** | All G1–G7 work correctly, including repeated-letter scoring, kind handling of invalid guesses, restart, and a curated answer pool with its source documented. | The game is complete with minor defects or limited curation notes. | Playable, but several rules fail or answers are not meaningfully curated. | The game does not run or does not use [english.py](https://github.com/AI-380/Shared_Libraries/releases/download/English_Library/english.py){download="english.py"}. |
| **Accessible feedback and interaction (20)** | Feedback is distinct without color and uses redundant cues; keyboard use, visible focus, screen-reader text, forgiving input, zoom, memory support, and contrast checks are demonstrated. | Most accessibility priorities work, with minor gaps or incomplete checks. | Several accessibility priorities are weak or unverified. | Feedback relies on color, or major barriers prevent people from playing. |
| **Enhancements (15)** | At least three enhancements from two or more categories work, are integrated into the game, and address clear user needs. | Three enhancements work with adequate integration. | Fewer than three enhancements work, or several are incomplete. | Enhancements are absent or nonfunctional. |
| **M1 design concept and data-flow diagram (10)** | A clear game concept is paired with an accurate diagram of player input, validation, game logic, and feedback flow. | The concept and diagram are understandable, with minor omissions. | The concept or diagram is incomplete or difficult to follow. | M1 deliverables are missing or do not describe the game flow. |
| **Design summary and reflection (10)** | The 2–3 page summary clearly covers design concepts, core achievements, answer curation, and specific remaining improvements. | Within the requested length and covers most required points. | Too short, too long, or missing important content. | Missing or does not address the requested topics. |
| **November 11 demo (10)** | A clear, prepared demo shows a complete game, key accessible interactions, and enhancements during the usability and pre-workshop. | The demo shows the game and most key features. | The demo is incomplete or difficult to follow. | The demo is not delivered. |
| **Deployed program and short README (10)** | The deployed game works, and the concise README clearly explains how to access and use it. | Deployment works with minor issues or the README has minor gaps. | Deployment or instructions are incomplete and require substantial help. | No usable deployment or README is provided. |
| **November 16 workshop flyer (5)** | A clear, readable flyer introduces the game and explains how older adults can access it at the workshop. | The flyer is usable but has minor clarity or readability issues. | The flyer is incomplete or difficult to understand. | The flyer is missing. |

### Bonus and Deductions

**Bonus (up to 5 points):** Reliable voice play that works with older-adult speech patterns, or a comparison with NYT Wordle that identifies specific barriers and demonstrates how yours removes them.

| Issue | Deduction |
|---|---:|
| Color is the only cue for any letter state | −10 |
| Timer or time-pressure feature | −5 |
| The game does not start or the README lacks basic access and use instructions | −10 |
| Participant data collected without consent or containing identifying information | −10 |
| Uncredited code or ideas | Academic integrity process |

---

## Rules and Expectations

- **Provided:** only [english.py](https://github.com/AI-380/Shared_Libraries/releases/download/English_Library/english.py){download="english.py"}. All other code, design, and writing are your own work.
- **Use of AI tools:** You may use AI assistants for ideas, designs, and debugging, but disclose the tools used and what they contributed. You must be able to explain most part of your code even when it is generated by an AI.
- **Privacy:** Do not store participants’ names, ages, health information, or recordings. Record only anonymous observations.
- **Honesty:** Honestly reporting gaps earns more credit than hiding them and having them discovered.

---

## Suggested References

- W3C, [*Web Content Accessibility Guidelines (WCAG) 2.1 Quick Reference*](https://www.w3.org/WAI/WCAG21/quickref/) (contrast, text resize, keyboard, non-text content, use of color).
- Nielsen Norman Group, *Usability for Senior Citizens* and related articles.
- Microsoft, *Guidelines for Human-AI Interaction* (if you add hints or voice).
- National Institute on Aging, *Making Your Website Senior Friendly*.
- Any color-blindness simulator and contrast checker of your choice.

---

## Quick Success Check

1. Could my grandparent tell the three letter states apart without seeing color?
2. Could they play without a mouse, a timer, or a manual?
3. Did a real or simulated user find a problem that I then fixed?
4. Would my enhancements make someone choose this game over NYT Wordle, and can I show why?