✅ Chapter 3 — What You MUST Keep in Mind (Core Rules)

These are the laws of clean functions according to Uncle Bob:

🔥 1. Functions Should Be Small

Smaller than you think.

“The first rule of functions is that they should be small. The second rule is that they should be smaller than that.”

🔥 2. Do One Thing

A function must do exactly one thing, and do it well.

Ask:
➡️ "Can I meaningfully extract another function from this?"
If yes → it's doing more than one thing.

🔥 3. Use Descriptive Names

Functions should read like English.

Examples:

calculate_total_price

is_valid_email

load_user_profile

Avoid:

doStuff()

handle()

manage()

🔥 4. Avoid Long Argument Lists

Best:

0 arguments
Good:

1–2 arguments
Avoid:

3+ arguments
Never:

Flag arguments (booleans)

Output arguments

🔥 5. No Side Effects

A function should not:

Modify global state

Modify parameters

Do hidden work (like logging, caching, IO) unless its name says so

🔥 6. Command Query Separation

A function that does something (command) should not return a value.
A function that returns a value (query) should not change state.

❌ Bad

if user.register():
    ...


✔️ Good

if user.is_registered():
    user.register()

🔥 7. Prefer Exceptions Over Error Codes

Return values should be data, not error signals.

🔥 8. Extract Try/Catch into Their Own Function

Error handling is one thing and should be a separate function.

🔥 9. DRY — Don’t Repeat Yourself

Duplicate code = bugs + waste.

🔥 10. Write Functions That Are Like Stories

Your code should read top-to-bottom like a narrative, each function calling the next.


This exam checks everything from Chapter 3 (Functions):

Small functions

Do one thing

No flag arguments

No output arguments

Avoid side effects

Eliminate duplication

Meaningful extraction

Clear separation of concerns

Intent-revealing names

Proper argument usage

You will get 5 questions.
Solve each one. After every answer, I’ll review it line-by-line.