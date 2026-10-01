# from langchain_community.llms import Ollama
# from langchain_groq import ChatGroq

# llm = ChatGroq(
#     model="qwen/qwen3-32b",
#     temperature=0.2
# )

# def explanation_agent(state: dict) -> dict:
#     """
#     Generates explanations for each quiz answer.
#     """
#     explanations = []

#     quiz = state.get("quiz", [])

#     for q in quiz:
#         prompt = f"""
# Explain why the correct answer is "{q['answer']}"
# for the question:
# "{q['question']}"
# """
#         explanation = llm.invoke(prompt)
#         explanations.append(explanation)

#     state["explanations"] = explanations
#     return state

# def explanation_agent(state:dict)->dict:
#     quiz=state.get("quiz",[])
#     for i,q in enumerate(quiz):
#         prompt=f"""
# Explain why the correct answer is "{q['answer']}" 
# for the question:
# "{q['question']}"
# """
#         response = llm.invoke(prompt)
#         explanation_text=response.content

#         quiz[i]["explanation"]=explanation_text

#         state["quiz"]=quiz
#         return state

import re
from langchain_groq import ChatGroq

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2
)

def explanation_agent(state: dict) -> dict:
    """
    Generates short explanations for each quiz answer
    and attaches them to the quiz structure.
    """

    quiz = state.get("quiz", [])

    if not quiz:
        return state

    for i, q in enumerate(quiz):
        try:
            prompt = f"""
Provide a short explanation (maximum 3 sentences)
for why "{q['answer']}" is the correct answer to:

"{q['question']}"

Return only plain text.
Do NOT include reasoning steps.
Do NOT include <think> tags.
Do NOT include extra formatting.
"""

            response = llm.invoke(prompt)
            explanation_text = response.content

            # Remove <think>...</think> if model still outputs it
            explanation_text = re.sub(
                r"<think>.*?</think>",
                "",
                explanation_text,
                flags=re.S
            ).strip()

            quiz[i]["explanation"] = explanation_text

        except Exception as e:
            quiz[i]["explanation"] = "Explanation generation failed."

    state["quiz"] = quiz
    return state
