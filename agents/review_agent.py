def review_agent(state: dict) -> dict:
    """
    Human-in-the-loop placeholder.
    For now, auto-approve generated quiz.
    """
    state["approved"] = True
    return state