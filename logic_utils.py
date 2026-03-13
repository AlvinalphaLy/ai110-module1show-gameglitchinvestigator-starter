# core game logic has been moved here so it can be tested independently
# FIX: Refactored logic into logic_utils.py using Copilot Agent mode.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    This was originally defined in `app.py` and copied here so the web
    interface can stay thin. Keeping it in a separate module made it
    easier to write unit tests.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)

    AI helped by suggesting the basic structure for handling blanks,
    non‑numbers and floats. I verified the behavior by using the function
    in the live app and by writing tests.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"

    This function is designed to be robust if the secret comes in as a
    string (a remnant of the original glitch), but it always compares
    numerically to avoid strange lexicographic behavior.
    """
    try:
        secret_int = int(secret)
    except (TypeError, ValueError):
        return "Error", "Secret value became invalid."

    if guess == secret_int:
        return "Win", "🎉 Correct!"
    if guess > secret_int:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
