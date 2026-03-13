# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game doesn't look like a game browser, honestly. At first, I thought it was other types of website. Aftering observing and reading, I understand how it works.
- List at least two concrete bugs you noticed at the start  
  After I typed a number, the screen just tell me to go lower every times, eventhough I typed 1. Secondly, the secret number should not be visible when I no click on the "show hint"
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Copilot inside VS Code and ChatGPT-style reasoning to help structure the refactor and the tests.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Copilot suggested moving the core game logic into `logic_utils.py` so it could be unit tested. I verified it by running `pytest` and confirming the tests could import the logic functions and pass.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Copilot initially suggested keeping the secret as a string on even attempts and comparing that way. That caused incorrect hint behavior, so I verified the problem by running the game and seeing the hints not match the numeric comparison. I fixed it by normalizing the secret to an int before comparing.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I wrote a unit test that specifically captures the former bug (guessing against a string secret) and then ran the app to confirm the hints behaved correctly during gameplay.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran `pytest` to ensure the new test passed and that the existing tests still passed, which showed the comparison logic was now correct.
- Did AI help you design or understand any tests? How?
  Yes. Copilot suggested adding a test that directly exercises the edge case from the glitch (string vs int secret), which helped me quickly verify the fix.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
