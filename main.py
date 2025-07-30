
# === Root: main.py ===
from agents.classifier_agent import create_classifier_agent
from agents.analysis_agent import create_analysis_agent
from agents.merge_agent import create_merge_agent
#from models.classification_schema import ClassificationOutput, ValidationError
from models.ticket import IncidentTicket
from tools.classification import TicketClassificationTool
from tools.analysis import FinalAnalysisTool
from tools.merge import MergeTool
from config import get_llm, get_embedder_config, reset_memory

from crewai import Task, Crew, Process
from datetime import datetime
import json
import logging

logging.basicConfig(level=logging.INFO)

# Clear memory at startup
reset_memory()

# Setup agents and tools
llm = get_llm()
embedder_config = get_embedder_config()

classification_tool = TicketClassificationTool()
analysis_tool = FinalAnalysisTool()
merge_tool = MergeTool()

classification_agent = create_classifier_agent(llm, [classification_tool])
analysis_agent = create_analysis_agent(llm, [analysis_tool])
merge_agent = create_merge_agent(llm, [merge_tool])

def run_triage(ticket: IncidentTicket):
    ticket_json = ticket.to_json()

    classification_task = Task(
        description=f"Classify the ticket below using the tool:```json\n{ticket_json}\n```",
        agent=classification_agent,
        expected_output="Classification result in JSON",
        output_format="json",
        tools=[classification_tool],
        verbose=True
    )

    analysis_task = Task(
        description=f"Determine severity and merge classification with the original ticket:\n```json\n{ticket_json}\n```",
        agent=analysis_agent,
        expected_output="Final analysis in JSON",
        output_format="json",
        tools=[analysis_tool],
        verbose=True
    )

    merge_task = Task(
        description="Merge classification and analysis results into a single triage summary JSON.",
        agent=merge_agent,
        expected_output="Merged final triage report.",
        output_format="json",
        tools=[merge_tool],
        verbose=True
    )

    crew = Crew(
        agents=[classification_agent, analysis_agent, merge_agent],
        tasks=[classification_task, analysis_task, merge_task],
        process=Process.sequential,
        memory=False,  # Disabled for speed and demo clarity
        embedder=embedder_config,
        verbose=True
    )

    result = crew.kickoff()

    return result

if __name__ == "__main__":
    ticket = IncidentTicket(
        id="INC-001",
        title="API Gateway Down",
        description="API unresponsive",
        reporter="a@b.com"
    )

    output = run_triage(ticket)
    print("\n📝 Final Merged Output:\n")
    print(output)


