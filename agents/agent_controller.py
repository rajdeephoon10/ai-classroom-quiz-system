# from langgraph.graph import StateGraph

# from agents.quiz_agent import quiz_generation_agent
# from agents.review_agent import review_agent
# from agents.explanation_agent import explanation_agent


# def build_quiz_agent_graph():
#     """
#     Builds and returns a LangGraph-based multi-agent workflow.
#     """

#     graph = StateGraph(dict)

#     # Register agent nodes
#     graph.add_node("generate_quiz", quiz_generation_agent)
#     graph.add_node("review_quiz", review_agent)
#     graph.add_node("explain_answers", explanation_agent)

#     # Define workflow
#     graph.set_entry_point("generate_quiz")
#     graph.add_edge("generate_quiz", "review_quiz")
#     graph.add_edge("review_quiz", "explain_answers")
#     graph.set_finish_point("explain_answers")

#     return graph.compile()

from langgraph.graph import StateGraph

from agents.adaptive_agent import adaptive_difficulty_agent
from agents.quiz_agent import quiz_generation_agent
from agents.review_agent import review_agent
from agents.explanation_agent import explanation_agent


def build_quiz_agent_graph():
    """
    Builds and returns a LangGraph-based adaptive multi-agent workflow.
    """

    graph = StateGraph(dict)

    # Register agent nodes
    graph.add_node("adaptive_difficulty", adaptive_difficulty_agent)
    graph.add_node("generate_quiz", quiz_generation_agent)
    graph.add_node("review_quiz", review_agent)
    graph.add_node("explain_answers", explanation_agent)

    # NEW WORKFLOW (Adaptive First)
    graph.set_entry_point("adaptive_difficulty")
    graph.add_edge("adaptive_difficulty", "generate_quiz")
    graph.add_edge("generate_quiz", "review_quiz")
    graph.add_edge("review_quiz", "explain_answers")

    graph.set_finish_point("explain_answers")

    return graph.compile()