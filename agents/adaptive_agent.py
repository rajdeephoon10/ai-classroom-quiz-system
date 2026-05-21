from database.attempt_manager import get_session_attempts


def adaptive_difficulty_agent(state: dict) -> dict:
    """
    Adjusts quiz difficulty based on class performance.
    """

    session_code = state.get("session_code")

    if not session_code:
        state["difficulty_instruction"] = "Generate balanced conceptual questions."
        return state

    attempts = get_session_attempts(session_code)

    if not attempts:
        state["difficulty_instruction"] = "Generate balanced conceptual questions."
        return state

    scores = []
    for a in attempts:
        score = a[1]
        total = a[2]
        scores.append(score / total)

    avg_score = sum(scores) / len(scores)

    if avg_score < 0.4:
        instruction = "Generate simpler recall-based conceptual questions."
    elif avg_score < 0.7:
        instruction = "Generate moderate analytical conceptual questions."
    else:
        instruction = "Generate highly analytical and application-based challenging questions."

    state["difficulty_instruction"] = instruction

    return state