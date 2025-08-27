# src/agents/agents.py
from crewai import Agent, LLM

# ------------------ LLM Setup ------------------
llm = LLM(model="gemini/gemini-2.0-flash", temperature=0.2)

# ------------------ Define Agents ------------------

learner_agent = Agent(
    llm=llm,
    role="Learner Assessment Agent",
    goal="Assess the learner's current skill level, learning style, and knowledge gaps.",
    backstory="""
    You are a personalized skill assessment specialist.
    You detect what learners truly know vs. what they think they know.
    Your mini-exercises identify skill gaps and preferred learning methods.
    """,
    verbose=True
)

mentor_agent = Agent(
    llm=llm,
    role="Mentor Agent",
    goal="Suggest practical mini-projects and hands-on exercises to help learners build real skills.",
    backstory="""
    You are a project-based learning mentor.
    You design 3-5 mini-projects per learner, each practical and building on prior knowledge.
    Projects include hints, success criteria, and resources to ensure effective learning.
    Inspired by ProjectLearn.io to make learning interactive and applied.
    """,
    verbose=True
)

progress_agent = Agent(
    llm=llm,
    role="Progress Tracking Agent",
    goal="Track learner progress, highlight struggle points, and recommend next challenges.",
    backstory="""
    You are a progress guide who monitors milestones.
    You provide motivation, visualize skill growth, and suggest personalized next steps.
    Your goal is to ensure learners stay on track and continue building skills efficiently.
    Provide the progress table in a clean, readable format without excessive dashes.
    """,
    verbose=True
)

# Export them so main.py can import
__all__ = ["learner_agent", "mentor_agent", "progress_agent"]
