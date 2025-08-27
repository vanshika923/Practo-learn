# src/main.py
from crewai import Task, Crew, Process
import json
from agents.agents import learner_agent, mentor_agent, progress_agent
from utils.formatter import clean_progress_table

# ------------------ Define Tasks ------------------
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

# ------------------ Assemble Crew ------------------
learning_crew = Crew(
    agents=[learner_agent, mentor_agent, progress_agent],
    tasks=[assessment_task, practical_learning_task, progress_tracking_task],
    process=Process.sequential,
    verbose=True
)

# ------------------ Example Input ------------------
learning_session = {
    "topic": "Python loops",
    "level": "Beginner",
    "goal": "Build web scraping skills",
    "time_commitment": "2 hours/week",
    "previous_experience": "Basic Python syntax"
}

# ------------------ Run Crew ------------------
result = learning_crew.kickoff(inputs=learning_session)

# ------------------ Format Output ------------------
def format_learning_plan(result):
    return {
        "assessment": result.tasks_output[0].raw,
        "learning_plan": result.tasks_output[1].raw,
        "progress_framework": clean_progress_table(result.tasks_output[2].raw),
        "next_session_prep": "Ready for hands-on coding"
    }

formatted_result = format_learning_plan(result)
print(json.dumps(formatted_result, indent=2))
