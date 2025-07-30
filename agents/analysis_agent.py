
# === agents/analysis_agent.py ===
from crewai import Agent

def create_analysis_agent(llm, tools):
    return Agent(
        role="Final Analysis Agent",
        goal="Use the 'Final Analysis Tool' to combine the ticket and classification. Do nothing else.",
        backstory="You only execute one task. Get input. Run tool. Return result. You are not allowed to think creatively.",
        tools=tools,
        llm=llm,
        verbose=True
    )
