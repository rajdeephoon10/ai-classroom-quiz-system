# from dotenv import load_dotenv
# # --------------------------------------------------
# # Importing env file
# # --------------------------------------------------
# import os

# load_dotenv()  # loads variables from .env

# groq_key = os.getenv("GROQ_API_KEY")

# import streamlit as st
# import json

# from rag.document_loader import load_pdf
# from rag.text_chunker import chunk_text
# from rag.embedding_store import build_vector_store
# from rag.retriever import retrieve_context
# from agents.agent_controller import build_quiz_agent_graph





# # --------------------------------------------------
# # Page Config
# # --------------------------------------------------
# st.set_page_config(
#     page_title="AI Assisted Quiz Platform",
#     layout="wide"
# )

# st.title("AI Assisted Quiz Generation Platform")
# st.caption("Manual and AI-based Quiz Creation using RAG and Agentic AI")

# menu = st.sidebar.radio(
#     "Select Module",
#     [
#         "Overview",
#         "Manual Quiz Creation",
#         "AI Quiz Generation (RAG)",
#         "About System Architecture"
#     ]
# )

# # --------------------------------------------------
# # OVERVIEW PAGE
# # --------------------------------------------------
# if menu == "Overview":
#     st.header("Project Overview")

#     st.markdown("""
#     This system demonstrates an **AI-assisted quiz generation platform**
#     that supports both **manual quiz creation** and **document-based
#     AI quiz generation using Retrieval-Augmented Generation (RAG)**.

#     ### Key Capabilities
#     - Manual quiz creation
#     - AI quiz generation from uploaded documents
#     - Context-aware question generation
#     - Agent-based AI workflow
#     - Open-source and offline LLM usage
#     """)

# # --------------------------------------------------
# # MANUAL QUIZ CREATION
# # --------------------------------------------------
# elif menu == "Manual Quiz Creation":
#     st.header("Manual Quiz Creation")

#     quiz_title = st.text_input("Quiz Title")

#     st.subheader("Add Question")
#     question = st.text_input("Question")
#     options = [
#         st.text_input("Option A"),
#         st.text_input("Option B"),
#         st.text_input("Option C"),
#         st.text_input("Option D"),
#     ]
#     answer = st.selectbox("Correct Answer", options)

#     if st.button("Preview Quiz"):
#         quiz = {
#             "title": quiz_title,
#             "questions": [{
#                 "question": question,
#                 "options": options,
#                 "answer": answer
#             }]
#         }
#         st.subheader("Quiz Preview")
#         st.json(quiz)

# # --------------------------------------------------
# # AI QUIZ GENERATION WITH RAG
# # --------------------------------------------------
# elif menu == "AI Quiz Generation (RAG)":
#     st.header("AI Quiz Generation from Document")

#     uploaded_file = st.file_uploader(
#         "Upload Study Material (PDF)",
#         type=["pdf"]
#     )

#     topic = st.text_input(
#         "Enter topic or focus area (used for retrieval)"
#     )

#     num_questions = st.slider(
#         "Number of Questions",
#         min_value=3,
#         max_value=10,
#         value=5
#     )

#     if uploaded_file and topic:
#         if st.button("Generate Quiz Using AI"):
#             with st.spinner("Processing document and generating quiz..."):

#                 # ---- RAG PIPELINE ----
#                 text = load_pdf(uploaded_file)
#                 chunks = chunk_text(text)
#                 index, stored_chunks = build_vector_store(chunks)

#                 context = retrieve_context(
#                     topic, index, stored_chunks
#                 )

#                 # ---- AGENTIC QUIZ GENERATION ----
#                 graph = build_quiz_agent_graph()

#                 state = {
#                     "context": context,
#                     "num_questions": num_questions
#                 }

#                 result = graph.invoke(state)

#             st.subheader("AI Generated Quiz")
#             st.json(result["quiz"])

#             st.success("Quiz generated using RAG and Agentic AI")

# # --------------------------------------------------
# # SYSTEM ARCHITECTURE (REPORT FRIENDLY)
# # --------------------------------------------------
# elif menu == "About System Architecture":
#     st.header("System Architecture Overview")

#     st.markdown("""
#     ### Architecture Summary

#     The system follows a **modular architecture** consisting of:

#     - **Streamlit UI**: User interaction
#     - **RAG Pipeline**:
#         - Document loading
#         - Text chunking
#         - Embedding & vector storage
#         - Context retrieval
#     - **Agentic AI Layer (LangGraph)**:
#         - Quiz generation agent
#         - Review flow
#         - Explanation generation
#     - **Local LLM (Ollama)**:
#         - Open-source model
#         - No paid APIs

#     ### Why RAG?
#     - Prevents hallucination
#     - Grounds questions in source documents
#     - Enables domain-specific quizzes

#     ### Why Agentic AI?
#     - Explicit workflow control
#     - Modular intelligence
#     - Explainable AI behavior
#     """)

#     st.code("""
# Document → Chunks → Embeddings → Vector DB
#                        ↑
#                     Query
#                        ↓
#                Relevant Context
#                        ↓
#                Agentic Quiz Generator
#     """)

# from dotenv import load_dotenv
# import os
# load_dotenv()

# import streamlit as st
# import json

# from rag.document_loader import load_pdf
# from rag.text_chunker import chunk_text
# from rag.embedding_store import build_vector_store
# from rag.retriever import retrieve_context

# from agents.agent_controller import build_quiz_agent_graph

# from database.db import init_db
# from database.session_manager import create_session, get_session_quiz
# from database.attempt_manager import store_attempt, get_session_attempts


# # ---------- INIT DB ----------
# init_db()

# st.set_page_config(page_title="AI Classroom Quiz System", layout="wide")

# st.title("AI Adaptive Classroom Quiz System")

# menu = st.sidebar.radio(
#     "Navigation",
#     ["Teacher Panel", "Student Panel", "System Overview"]
# )

# # =========================================================
# # TEACHER PANEL
# # =========================================================
# if menu == "Teacher Panel":

#     st.header("Teacher: Generate Quiz & Create Session")

#     uploaded_file = st.file_uploader("Upload Study PDF", type=["pdf"])
#     topic = st.text_input("Topic Focus")
#     num_questions = st.slider("Number of Questions", 3, 10, 5)

#     if uploaded_file and topic:

#         if st.button("Generate Quiz"):

#             with st.spinner("Generating Quiz..."):

#                 text = load_pdf(uploaded_file)
#                 chunks = chunk_text(text)
#                 index, stored_chunks = build_vector_store(chunks)
#                 context = retrieve_context(topic, index, stored_chunks)

#                 graph = build_quiz_agent_graph()

#                 state = {
#                     "context": context,
#                     "num_questions": num_questions
#                 }

#                 result = graph.invoke(state)
#                 st.session_state.quiz = result["quiz"]

#         if "quiz" in st.session_state:

#             st.subheader("Generated Quiz")
#             st.json(st.session_state.quiz)

#             if st.button("Create Live Session"):
#                 code = create_session(topic, st.session_state.quiz)
#                 st.success(f"Session Created! Code: {code}")

#     st.divider()

#     st.subheader("View Session Analytics")
#     session_code = st.text_input("Enter Session Code")

#     if st.button("Load Analytics"):
#         attempts = get_session_attempts(session_code)

#         if attempts:
#             for a in attempts:
#                 st.write(f"Student: {a[0]} | Score: {a[1]}/{a[2]}")
#         else:
#             st.warning("No attempts yet")


# # =========================================================
# # STUDENT PANEL
# # =========================================================
# elif menu == "Student Panel":

#     st.header("Student: Join Quiz Session")

#     name = st.text_input("Enter Your Name")
#     session_code = st.text_input("Enter Session Code")

#     if st.button("Join Quiz"):

#         quiz = get_session_quiz(session_code)

#         if quiz:
#             st.session_state.student_quiz = quiz
#             st.session_state.session_code = session_code
#             st.session_state.student_name = name
#         else:
#             st.error("Invalid Session Code")

#     if "student_quiz" in st.session_state:

#         st.subheader("Quiz")

#         answers = []
#         for i, q in enumerate(st.session_state.student_quiz):
#             ans = st.radio(q["question"], q["options"], key=i)
#             answers.append(ans)

#         if st.button("Submit Quiz"):

#             score = 0
#             for i, q in enumerate(st.session_state.student_quiz):
#                 if answers[i] == q["answer"]:
#                     score += 1

#             store_attempt(
#                 st.session_state.session_code,
#                 st.session_state.student_name,
#                 score,
#                 len(st.session_state.student_quiz)
#             )

#             st.success(f"Your Score: {score}/{len(st.session_state.student_quiz)}")


# # =========================================================
# # SYSTEM OVERVIEW
# # =========================================================
# else:

#     st.header("System Architecture Overview")

#     st.markdown("""
#     ### AI Classroom Quiz System

#     This system demonstrates:

#     - Agentic AI quiz generation
#     - Retrieval Augmented Generation
#     - Teacher-Student live quiz sessions
#     - Multi-student performance tracking
#     - Explainable AI quiz explanations

#     ### Research Contributions

#     - Multi-agent orchestration using LangGraph
#     - Adaptive quiz intelligence (next phase)
#     - AI-assisted classroom assessment automation
#     """)

from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st

from rag.document_loader import load_pdf
from rag.text_chunker import chunk_text
from rag.embedding_store import build_vector_store
from rag.retriever import retrieve_context

from agents.agent_controller import build_quiz_agent_graph

from database.db import init_db
from database.session_manager import create_session, get_session_quiz
from database.attempt_manager import store_attempt, get_session_attempts
from analytics.analytics_dashboard import plot_session_analytics


# ---------- INIT DB ----------
init_db()

st.set_page_config(page_title="AI Classroom Quiz System", layout="wide")

st.title("AI Adaptive Classroom Quiz System")

menu = st.sidebar.radio(
    "Navigation",
    ["Teacher Panel", "Student Panel", "System Overview"]
)

# =========================================================
# TEACHER PANEL
# =========================================================
if menu == "Teacher Panel":

    st.header("Teacher: Generate Quiz & Create Session")

    uploaded_file = st.file_uploader("Upload Study PDF", type=["pdf"])
    topic = st.text_input("Topic Focus")
    previous_session_code = st.text_input(
    "Previous Session Code (for Adaptive Difficulty)",
    help="Enter previous session code to enable AI difficulty adaptation"
    )
    num_questions = st.slider("Number of Questions", 3, 10, 5)

    if uploaded_file and topic:

        if st.button("Generate Quiz"):

            with st.spinner("Generating Quiz..."):

                text = load_pdf(uploaded_file)
                chunks = chunk_text(text)
                index, stored_chunks = build_vector_store(chunks)
                context = retrieve_context(topic, index, stored_chunks)

                graph = build_quiz_agent_graph()

                state = {
                    "context": context,
                    "num_questions": num_questions,
                    "session_code": previous_session_code
                }

                result = graph.invoke(state)
                st.session_state.quiz = result["quiz"]

        if "quiz" in st.session_state:

            st.subheader("Generated Quiz")
            st.json(st.session_state.quiz)

            if st.button("Create Live Session"):
                code = create_session(topic, st.session_state.quiz)
                st.success(f"Session Created! Code: {code}")

    st.divider()

    st.subheader("View Session Analytics")
    session_code = st.text_input("Enter Session Code")

    if st.button("Load Analytics"):

        fig1, fig2 = plot_session_analytics(session_code)

        if fig1:
            st.pyplot(fig1)
            st.pyplot(fig2)
        else:
            st.warning("No attempts yet")


# =========================================================
# STUDENT PANEL
# =========================================================
elif menu == "Student Panel":

    st.header("Student: Join Quiz Session")

    name = st.text_input("Enter Your Name")
    session_code = st.text_input("Enter Session Code")

    if st.button("Join Quiz"):

        quiz = get_session_quiz(session_code)

        if quiz:
            st.session_state.student_quiz = quiz
            st.session_state.session_code = session_code
            st.session_state.student_name = name
        else:
            st.error("Invalid Session Code")

    if "student_quiz" in st.session_state:

        st.subheader("Quiz")

        answers = []

        for i, q in enumerate(st.session_state.student_quiz):
            ans = st.radio(
                q["question"],
                ["Select an answer"] + q["options"],
                key=i
            )
            answers.append(ans)

        if st.button("Submit Quiz"):

            score = 0

            for i, q in enumerate(st.session_state.student_quiz):

                if answers[i] == "Select an answer":
                    st.error("Please answer all questions")
                    st.stop()

                if answers[i] == q["answer"]:
                    score += 1

            store_attempt(
                st.session_state.session_code,
                st.session_state.student_name,
                score,
                len(st.session_state.student_quiz)
            )

            st.success(f"Your Score: {score}/{len(st.session_state.student_quiz)}")


# =========================================================
# SYSTEM OVERVIEW
# =========================================================
else:

    st.header("System Architecture Overview")

    st.markdown("""
    ### AI Classroom Quiz System

    This system demonstrates:

    - Agentic AI quiz generation
    - Retrieval Augmented Generation
    - Teacher-Student live quiz sessions
    - Multi-student performance tracking
    - Explainable AI quiz explanations

    ### Research Contributions

    - Multi-agent orchestration using LangGraph
    - Adaptive quiz intelligence (next phase)
    - AI-assisted classroom assessment automation
    """)