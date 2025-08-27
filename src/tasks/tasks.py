from crewai import Task
from src.agents import learner_agent, mentor_agent, progress_agent   # import agents


assessment_task = Task(
    description="Assess user's skill level, goals, and learning style.",
    expected_output="JSON with skill_level, gaps, learning_style, recommended_path",
    agent=learner_agent
)

practical_learning_task = Task(
    description="Suggest 3-5 practical mini-projects based on learner assessment.",
    expected_output="Structured learning plan with mini-projects",
    agent=mentor_agent,
    context=[assessment_task]
)

progress_tracking_task = Task(
    description="Track progress and suggest next challenges.",
    expected_output="Clean progress tracking framework with next steps",
    agent=progress_agent,
    context=[assessment_task, practical_learning_task]
)
