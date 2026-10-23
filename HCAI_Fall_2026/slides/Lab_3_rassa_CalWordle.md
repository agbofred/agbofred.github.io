# Lab 3: Build Wordle Buddy with Rasa Pro (CALM)

**Course:** AI 380: Human-AI Interaction · Willamette University  
**Instructor:** Prof. Fred Agbo  
**Format:** Hands-on lab: text, voice, and an optional web interface  
**Estimated time:** 10 minutes setup, 30 minutes text play, 15 minutes voice play, optional 25-minute web integration, and optional 20-minute extension

## Goal and Learning Outcomes

Build **Wordle Buddy**, a voice and text assistant that lets older adults play a five-letter word game. The assistant is designed to be forgiving, clear, and accessible.

By the end of the lab, you will be able to:

1. Define a CALM flow using `collect`, `action`, `set_slots`, and branching steps.
2. Declare `from_llm` and `controlled` slots, responses, and actions in the domain.
3. Write custom Python actions with the Rasa SDK.
4. Explain how CALM handles digressions, such as asking for a hint and then resuming a game.
5. Test an assistant by text and voice, and optionally connect it to your own web page.
6. Identify at least three human-AI interaction design choices in Wordle Buddy.

## Background

- **CALM:** An LLM reads the conversation and produces commands, such as setting a slot. The flows determine what happens next; the LLM does not run the game logic.
- **Flow:** The steps that control the game, such as starting, collecting a guess, checking it, and repeating until the game ends.
- **Slot:** Assistant memory, such as the current guess, guesses remaining, or whether the game is over.
- **Custom action:** Python code that performs game operations, such as choosing an answer or scoring a guess.
- **Domain:** The file that declares slots, responses, and actions.

### Rasa References

- [CALM overview](https://rasa.com/docs/learn/concepts/calm)
- [Flows](https://rasa.com/docs/reference/primitives/flows)
- [Flow steps](https://rasa.com/docs/reference/primitives/flow-steps/)
- [Slots](https://rasa.com/docs/reference/primitives/slots)
- [Custom actions](https://rasa.com/docs/reference/primitives/custom-actions)
- [Trying your assistant: Inspector, text, and voice](https://rasa.com/docs/pro/testing/trying-assistant)
- [Speech integrations](https://rasa.com/docs/reference/integrations/speech-integrations/)
- [WebSocket voice channel](https://rasa.com/docs/reference/channels/websockets-voice/)
- [Connecting to your own website](https://rasa.com/docs/reference/channels/your-own-website.md)

## Prerequisites

- Rasa Pro installed, with your Developer Edition license set in `RASA_LICENSE`.
- No separate LLM key is needed with the tutorial template, which uses a Rasa-hosted model. If you change the model group in `endpoints.yml`, you may need that provider's API key.
- A Deepgram API key (`DEEPGRAM_API_KEY`) for Stages 2 and 3.
- Chrome or Edge and a microphone; headphones are recommended to avoid echo.
- The instructor-provided `Calm_Wordle_files_to_copy.zip` bundle.

> **Version note:** Stage 3 voice using `websockets_voice` requires Rasa Pro 3.19 or later. Check your version with `rasa --version`. Stages 1 and 2 do not depend on this requirement.

## Project Setup and File Copying

Create the project from Rasa's tutorial template. It starts with a money-transfer demo that you will replace:

```bash
mkdir Calm_Wordle && cd Calm_Wordle
rasa init --template tutorial
```

The template includes this structure:

```text
Calm_Wordle/
├── actions/
│   ├── __init__.py        KEEP (empty file)
│   └── actions.py         REPLACE (template money-transfer action)
├── config.yml             KEEP
├── credentials.yml        KEEP for Stages 1 and 2 (REST and browser_audio)
├── endpoints.yml          KEEP (action endpoint, model groups, and NLG)
├── domain.yml             REPLACE (one file, not a domain/ folder)
└── data/
    ├── flows.yml          REPLACE (template transfer_money flow)
    └── patterns.yml       KEEP
```

Unzip `Calm_Wordle_files_to_copy.zip`. It mirrors this structure. Copy the files as follows:

| Bundle file | Destination | Action |
|---|---|---|
| `actions/actions.py` | `Calm_Wordle/actions/actions.py` | Overwrite |
| `actions/wordle_logic.py` | `Calm_Wordle/actions/` | Add |
| `actions/answers.py` | `Calm_Wordle/actions/` | Add |
| `actions/english.py` | `Calm_Wordle/actions/` | Add course dictionary |
| `actions/__init__.py` | Skip | The project already has this file |
| `data/flows.yml` | `Calm_Wordle/data/flows.yml` | Overwrite |
| `domain.yml` | `Calm_Wordle/domain.yml` | Overwrite |

The optional `web/` folder is only needed for Stage 3. The optional `tests/` folder can be copied to the project root; run its logic tests with `python tests/test_logic.py` without Rasa.

**Do not delete `data/patterns.yml`.** It defines chitchat and search-repair patterns used by CALM.

Alternatively, copy the files from the terminal, adjusting the unzip path if needed:

```bash
cp ~/Downloads/Calm_Wordle_files_to_copy/Calm_Wordle/actions/*.py actions/
cp ~/Downloads/Calm_Wordle_files_to_copy/Calm_Wordle/data/flows.yml data/flows.yml
cp ~/Downloads/Calm_Wordle_files_to_copy/Calm_Wordle/domain.yml domain.yml
ls actions
```

You should see `__init__.py`, `actions.py`, `answers.py`, `english.py`, and `wordle_logic.py` in `actions/`. The copy command also copies the bundle's empty `__init__.py`; that is harmless.

| File | Purpose |
|---|---|
| `actions/actions.py` | Four custom actions: start game, check guess, hint, and progress |
| `actions/wordle_logic.py` | Scoring, validation, and hints in plain Python |
| `actions/answers.py` | 490 common five-letter answer words |
| `actions/english.py` | Course dictionary (`isEnglishWord`) |
| `data/flows.yml` | `play_wordle`, `wordle_rules`, `wordle_hint`, and `show_progress` flows |
| `domain.yml` | Slots, responses, and actions; also includes the Wordle chitchat response |

## Stage 0: Check Your Setup (10 minutes)

1. Export your Rasa license in the terminal you will use:

   ```bash
   export RASA_LICENSE=YOUR_LICENSE_KEY
   ```

   The tutorial template points its command generator to a Rasa-hosted model, so no OpenAI key is needed unless you change the model configuration.

2. Complete the file-copy steps above.

3. Inspect these template settings without changing them:
   - `endpoints.yml` has `action_endpoint: actions_module: "actions"`. This runs the Python actions inside the assistant, so a separate action server is not needed.
   - `endpoints.yml` has an `nlg: type: rephrase` block. It lets an LLM reword responses marked for rephrasing; this lab uses it only for chitchat. If game feedback is unexpectedly reworded, comment out this block. Chitchat will then show the word `placeholder`.
   - `config.yml` uses `CompactLLMCommandGenerator` and `FlowPolicy`.

**Checkpoint 0:** `rasa train` finishes without errors. If it reports a flow or domain error, use the message to find the file and line to inspect.

## Stage 1: Play by Text in the Inspector (30 minutes)

From the project root, train and launch the Inspector:

```bash
rasa train
rasa inspect
```

A browser tab opens with the Inspector. Click **Inspect** in the header to show the Flow, History, and Memory panels.

### Run the Test Script

Enter each message one at a time and record what happens.

| # | You type | Expected behavior |
|---|---|---|
| 1 | `let's play` | Welcome message, followed by “What is your guess?” |
| 2 | `crane` | Word-based feedback: correct position, wrong position, absent letters, and guesses remaining |
| 3 | `what have I guessed?` | Guesses so far and a pattern such as `_ R A _ _`; then asks for another guess |
| 4 | `give me a hint` | Gives a hint (maximum two per game), then requests a guess |
| 5 | `how does this work?` | Explains the rules, then requests a guess |
| 6 | `zzzzz` | Says it is not in the word list; the guess does not count |
| 7 | `cat` | Says a guess must have exactly five letters; the guess does not count |
| 8 | `c r a n e` (after trying `crane`) | Joins the spelled letters; since `crane` was already tried, asks for a different word |
| 9 | `I give up` | Reveals the secret word and ends the game |
| 10 | `let's play` | Starts a brand-new game |

### Inspect the Conversation

- **Flow panel:** Identify the active step in `play_wordle`.
- **History panel:** When a hint or rules flow runs, `play_wordle` should show as *Interrupted*, then return to *Active*.
- **Memory panel:** Inspect `guess`, `guesses_left`, `game_over`, and `won`. The secret word is intentionally not stored here; see [Understanding the Design](#understanding-the-design).
- Click a command in the chat log to inspect the LLM-produced commands, such as `start flow` or `set slot`.

### If Something Does Not Work

| Symptom | Likely cause and fix |
|---|---|
| Assistant does not start the game | The LLM uses each flow's `description` to decide when it applies. Confirm `data/flows.yml` was copied, the sample flows were removed, and you retrained with `rasa train`. |
| Game does not end after a win | The branch condition `if: slots.game_over` may need the bare form `if: game_over`. Rasa documentation shows both forms; try the other form and retrain. |
| “I give up” produces a generic cancel message | The LLM may have issued `cancel flow` instead of setting the guess to `giveup`. Improve the `collect: guess` description or complete Extension A. |
| Custom action errors | Confirm `actions_module: actions` is set in `endpoints.yml` and `actions/__init__.py` exists. |

**Checkpoint 1:** Complete a game by winning or giving up, and observe at least one digression (hint, rules, or progress) resume correctly.

## Stage 2: Play by Voice in the Browser (15 minutes)

1. Export your Deepgram key in the same terminal you use to run the Inspector:

   ```bash
   export DEEPGRAM_API_KEY=YOUR_DEEPGRAM_KEY
   ```

2. Start or restart the Inspector:

   ```bash
   rasa inspect
   ```

3. Switch from chat to **voice** using the control in the chat input. Allow microphone access and say, “Let's play.”

4. The template's `credentials.yml` already has a `browser_audio` block configured for Deepgram listening and speaking. If you hear no spoken replies, check that the key is exported in this terminal and that the block still resembles:

   ```yaml
   browser_audio:
     server_url: localhost
     asr:
       name: deepgram
     tts:
       name: deepgram
   ```

**Voice tips:** Speak clearly, spell a word as “C R A N E” if speech recognition mishears it, wait for the assistant to finish, and use headphones.

**Checkpoint 2:** Finish a game by voice. Record any word that speech recognition gets wrong; you will use this observation in the discussion.

## Stage 3 (Optional): Your Own Web Page with Text and Voice (25 minutes)

> Requires Rasa Pro 3.19 or later. Rasa does not provide a ready-made browser demo for this voice channel. The provided `web/index.html` is a starting point that follows Rasa's documented protocol: 24 kHz, 16-bit mono audio, with audio encoded as base64 inside JSON. Expect to debug it; that is part of the lab.

1. In `credentials.yml`, uncomment the template's `socketio` entry and fill it in for the chat widget. Then add the voice channel:

   ```yaml
   socketio:
     user_message_evt: user_uttered
     bot_message_evt: bot_uttered
     session_persistence: true
   ```

   ```yaml
   websockets_voice:
     server_url: localhost:5005     # Host only; do not include ws:// or wss://
     asr:
       name: deepgram
     tts:
       name: deepgram
     interruptions:
       enabled: true
       min_words: 3
     silence_timeout: 3.0
   ```

2. Start the assistant. If the browser reports a CORS error, allow your page's origin. Check `rasa run --help` for the exact option; the template's suggested command is:

   ```bash
   rasa run --cors "*"
   ```

3. Copy `web/` from the bundle into the project, then serve it:

   ```bash
   cd web
   python -m http.server 8000
   ```

4. Open [http://localhost:8000](http://localhost:8000) in Chrome or Edge.
   - **Text:** Use the Rasa chat widget in the bottom-right corner. It connects through the `socketio` channel.
   - **Voice:** Select **Start talking**, allow microphone access, and say, “Let's play.”

5. Check the voice server at [http://localhost:5005/webhooks/websockets_voice/](http://localhost:5005/webhooks/websockets_voice/). It should return `{"status": "ok"}`.

6. Open the browser developer console (F12) to inspect errors.

**Known limitations:** This voice channel handles text and audio only; it does not support buttons or images. It has no built-in authentication. For a public site, use `wss://`, set `USE_TLS = true` in `index.html`, and use a secure tunnel or properly configured domain.

**Checkpoint 3:** Verify that both the text widget and voice button reach the same assistant.

## Understanding the Design

For your lab report, connect each design choice to its implementation and explain why it matters for older adults.

| Design choice | Where to find it | Why it matters |
|---|---|---|
| Feedback uses **words**, not colors or emojis | `describe_feedback()` in `wordle_logic.py` | Works with voice, screen readers, and color-blind players |
| Invalid guesses **do not cost a guess** | `validate_guess()`; messages say the guess “does not count” | Forgiving interaction can reduce anxiety |
| **Hints** (two per game) and **progress** are available on request | `action_give_hint`, `action_show_progress` | Gives users control and makes system state visible |
| **“I give up”** reveals the word kindly | `action_check_guess` | Provides a graceful ending instead of a dead end |
| Spelled-out letters are accepted | `normalize_guess()` | Speech recognizers may split or spell words |
| The secret word stays **out of slots** | `GAMES` dictionary in `actions.py` | Slots appear in the Inspector and may appear in LLM prompts |
| Answers use a **curated list** of 490 words | `answers.py`; answers are validated against the full dictionary | The full dictionary may contain obscure words, such as “zymes,” that frustrate players |
| Digressions resume the game | `wordle_hint`, `wordle_rules`, and `show_progress` flows | CALM's stack-based resumption supports natural conversation |

**Trade-off:** The game state is held in server memory, so restarting the assistant ends the current game.

## Deliverables and Discussion

Submit a short report (1–2 pages) containing:

1. A screenshot of the Inspector showing a digression and the resumed game, with the Flow and History panels visible.
2. Your completed test table from Stage 1, noting any behavior that differed from expectations.
3. Three speech-recognition errors, or “none,” and how you handled them.
4. Answers to these questions:
   - Which Microsoft HAI guidelines does the assistant satisfy? For example, does it support efficient correction or clearly explain what it can do? Point to a flow or action as evidence.
   - What would make the assistant safer or kinder for someone with hearing loss, slower speech, or memory difficulties?
   - Where is the trust boundary between the LLM and your game code? What could go wrong if the LLM issued the wrong command?
   - What did you need to change from the starter project to make it work on your machine?

## Extensions (Choose One)

- **A. Reveal the word on cancel:** Write a custom `pattern_cancel_flow` so that any “stop” request ends the game and reveals the word.
- **B. Add a difficulty setting:** Add a categorical slot (`easy`, `normal`) to change the number of guesses, such as eight or six. The constants are at the top of `wordle_logic.py`.
- **C. Make speech slower or clearer:** Review Rasa's speech integration options and change the voice or language.
- **D. Add a daily word:** Choose the answer based on the date instead of randomly.
- **E. Add a new digression:** For example, add a flow and action for “What vowels have I found?”

## Troubleshooting Quick Reference

| Problem | Try this |
|---|---|
| `rasa train` fails on flows | Check YAML indentation; every flow needs a `description` and `steps`. |
| LLM errors or timeouts | The template uses a Rasa-hosted tutorial model. Check your internet connection and `RASA_LICENSE`; if you switched providers, check that provider's key. |
| Python import errors in actions | Run commands from the project root, keep `actions/__init__.py`, and check the relative imports (`from . import ...`). |
| No voice | Confirm `DEEPGRAM_API_KEY` is set in this terminal and the browser has microphone permission. |
| Voice page connects, then goes silent | Confirm `websockets_voice` is in `credentials.yml` and its health-check URL returns `{"status": "ok"}`. |
| Echo or the assistant hears itself | Use headphones. |
| Firefox audio error | Use Chrome or Edge for Stage 3. |

## Instructor Notes

- The instructor-side build tested the Python game logic, including repeated-letter scoring, validation, hints, and win/lose/give-up behavior. It did **not** test training, flows, Inspector behavior, or either voice path, which require Rasa Pro and API keys. Run Stages 0–2 before teaching and adjust the troubleshooting section as needed.
- Rasa documentation does not fully confirm these details; verify them in your version: looping back to an earlier step, the `slots.game_over` condition syntax, and the CORS option for `rasa run`.
- Voice and LLM calls use third-party services (Deepgram and your LLM provider). Check costs and rate limits before a whole class connects at once.
- Do not collect real personal data from older adults without appropriate review. This lab uses a word game and does not require personal data.

## Sources

- Rasa documentation: CALM, Flows, Flow Steps, Slots, Custom Actions, Rasa SDK Actions, LLM Configuration, Trying Your Assistant, Speech Integrations, WebSocket Voice Channel, and Connecting to Your Own Website. See [rasa.com/docs](https://rasa.com/docs/).
- Course dictionary: instructor-provided `english.py`.
