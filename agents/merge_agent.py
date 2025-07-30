
# === agents/merge_agent.py ===
from crewai import Agent

def create_merge_agent(llm, tools):
    return Agent(
        role="Triage Report Combiner",
        goal="Merge classification and severity analysis into one summary report.",
        backstory="You are responsible for preparing the final triage summary for stakeholders.",
        tools=tools,
        llm=llm,
        verbose=True
    )
