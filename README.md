

---

# Practo-Learn – AI-Powered Personalized Learning Assistant 🎓🤖

Practo-Learn is an AI-driven personalized learning assistant built with CrewAI and Google Gemini API in Google Colab (Python).
It adapts to each learner’s background, generates practical mini-projects, and tracks progress in a structured framework.

---

## ✨ Features

### AI Agents with Specialized Roles

* 📊 **Learner Assessment Agent** – Identifies current skill level, gaps, and learning style.
* 🧑‍🏫 **Mentor Agent** – Suggests 3–5 hands-on mini-projects with hints, success criteria, and resources.
* 📈 **Progress Tracking Agent** – Monitors milestones, motivates learners, and generates a clean progress table.

### Sequential Learning Flow

Assessment → Project Design → Progress Tracking

### Structured Progress Framework

Learner’s journey is tracked in a readable table format for continuous improvement.

### Applied Demo

Example: Beginner in Python (loops) → Step-by-step guided path towards web scraping.

---

## 🛠️ Tech Stack

* **Google Colab** – Prototyping & experimentation
* **CrewAI** – Multi-agent orchestration
* **Gemini API (Google LLM)** – AI backend
* **Python** – Core implementation

---

## 📂 Project Structure

```
Practo-learn/
│── src/
│   ├── agents/        # Agent definitions
│   ├── tasks/         # Task setup
│   ├── utils/         # Formatters & helpers
│── main.py            # Run learning session
│── README.md          # Project overview
```

---

## 🚀 Quick Start

### Clone the repo

```bash
git clone https://github.com/your-username/Practo-learn.git
cd Practo-learn
```

### Install dependencies

```bash
pip install crewai
```

### Add Gemini API key

Place your Gemini API key in the code or set it as an environment variable before running.

### Run demo

```bash
python main.py
```

---

## 📖 Example Run

**Input:**

```json
{
  "topic": "Python loops",
  "level": "Beginner",
  "goal": "Build web scraping skills",
  "time_commitment": "2 hours/week",
  "previous_experience": "Basic Python syntax"
}
```

**Output (sample structured):**

```json
{
  "assessment": { ... learner gaps ... },
  "learning_plan": { ... 3–5 mini-projects ... },
  "progress_framework": "## Progress Tracking Framework ...",
  "next_session_prep": "Ready for hands-on coding"
}
```

---

## 📊 Progress Tracking Framework (Auto-Generated)

| Mini-Project | Objective | Status | Completion Date | Notes/Reflections |
| ------------ | --------- | ------ | --------------- | ----------------- |
| Project 1    |           |        |                 |                   |
| Project 2    |           |        |                 |                   |
| Project 3    |           |        |                 |                   |
| Project 4    |           |        |                 |                   |
| Project 5    |           |        |                 |                   |

---

## 🎯 Future Roadmap

* Expand beyond coding → math, design, soft skills.
* Add adaptive difficulty adjustment per learner.
* Build an interactive UI dashboard for tracking.
* Support for voice input and multilingual learning paths.

---


