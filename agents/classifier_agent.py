
# === agents/classifier_agent.py ===
from crewai import Agent

def create_classifier_agent(llm, tools):
    return Agent(
        role="Incident Classification Specialist",
        goal="Your single task is to use the 'Ticket Classification Tool'. That is all.",
        backstory="You are a simple robot. You receive a task, use your one tool, and then you are done. You do not think further.",
        tools=tools,
        llm=llm,
        verbose=True
    )

