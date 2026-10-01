# import json
# import re
# from langchain_groq import ChatGroq

# def get_llm():
#     return ChatGroq(
#         model="qwen/qwen3-32b",
#         temperature=0.2
#     )

# def quiz_generation_agent(state: dict) -> dict:
#     """
#     Generates MCQ quiz questions from retrieved context.
#     """
#     context = state.get("context", "")
#     num_questions = state.get("num_questions", 5)

#     prompt = f"""
# You are an expert quiz creator.

# Using ONLY the context below, generate {num_questions} MCQ questions.
# Each question must have:
# - question
# - 4 options
# - correct answer

# Return STRICTLY valid JSON.
# No explanations.
# No markdown.
# No extra text.

# Format:
# [
#   {{
#     "question": "",
#     "options": ["", "", "", ""],
#     "answer": ""
#   }}
# ]

# Context:
# {context}
# """

#     llm = get_llm()
#     response = llm.invoke(prompt)
#     response_text = response.content

#     try:
#         match = re.search(r"\[\s*\{.*\}\s*\]", response_text, re.S)
#         if match:
#             quiz = json.loads(match.group())
#         else:
#             print("No JSON found in response.")
#             print("MODEL OUTPUT:", response_text)
#             quiz = []
#     except Exception as e:
#         print("JSON ERROR:", e)
#         print("MODEL OUTPUT:", response_text)
#         quiz = []

#     state["quiz"] = quiz
#     return state

import json
import re
from langchain_groq import ChatGroq


def get_llm():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2
    )


def quiz_generation_agent(state: dict) -> dict:
    """
    Generates adaptive MCQ quiz questions from retrieved context.
    """

    context = state.get("context", "")
    num_questions = state.get("num_questions", 5)

    # NEW: adaptive difficulty instruction
    difficulty_instruction = state.get(
        "difficulty_instruction",
        "Generate balanced conceptual questions."
    )

    prompt = f"""
You are an expert quiz creator.

{difficulty_instruction}

Using ONLY the context below, generate {num_questions} MCQ questions.

Each question must have:
- question
- 4 options
- correct answer

Ensure:
- Questions reflect conceptual understanding
- Avoid trivial factual recall unless instructed
- Maintain academic rigor

Return STRICTLY valid JSON.
No explanations.
No markdown.
No extra text.

Format:
[
  {{
    "question": "",
    "options": ["", "", "", ""],
    "answer": ""
  }}
]

Context:
{context}
"""

    llm = get_llm()
    response = llm.invoke(prompt)
    response_text = response.content

    try:
        match = re.search(r"\[\s*\{.*\}\s*\]", response_text, re.S)
        if match:
            quiz = json.loads(match.group())
        else:
            print("No JSON found in response.")
            print("MODEL OUTPUT:", response_text)
            quiz = []
    except Exception as e:
        print("JSON ERROR:", e)
        print("MODEL OUTPUT:", response_text)
        quiz = []

    state["quiz"] = quiz
    return state
