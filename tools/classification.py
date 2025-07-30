
# === tools/classification.py ===
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import json

class ClassifyToolInput(BaseModel):
    ticket_data: dict = Field(..., description="Incident ticket data")

class TicketClassificationTool(BaseTool):
    name: str = "Ticket Classification Tool"
    description: str = "Classifies the category of an incident ticket."
    args_schema: type[BaseModel] = ClassifyToolInput

    def _run(self, ticket_data: dict) -> str:
        title = ticket_data.get("title", "").lower()
        if "gateway" in title or "unresponsive" in title:
            category = "Application"
            tags = ["outage", "production"]
        elif "memory" in title or "oom" in title:
            category = "Infrastructure"
            tags = ["memory", "server"]
        elif "database" in title or "db" in title:
            category = "Database"
            tags = ["database", "query"]
        else:
            category = "Other"
            tags = ["misc"]

        result = {
            "ticket_id": ticket_data.get("id"),
            "category": category,
            "tags": tags
        }
        return json.dumps(result, indent=2)

