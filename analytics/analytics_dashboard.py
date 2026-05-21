import pandas as pd
import matplotlib.pyplot as plt
from database.attempt_manager import get_session_attempts

def plot_session_analytics(session_code):

    attempts = get_session_attempts(session_code)

    if not attempts:
        return None, None

    df = pd.DataFrame(attempts, columns=["student", "score", "total"])
    df["percentage"] = (df["score"] / df["total"]) * 100

    # --- Average Score Plot ---
    avg_score = df["percentage"].mean()

    fig1 = plt.figure()
    plt.bar(df["student"], df["percentage"])
    plt.axhline(avg_score)
    plt.title("Student Performance Distribution")
    plt.ylabel("Score %")

    # --- Histogram ---
    fig2 = plt.figure()
    plt.hist(df["percentage"])
    plt.title("Score Distribution Histogram")
    plt.xlabel("Score %")

    return fig1, fig2