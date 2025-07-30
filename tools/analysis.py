
# === tools/analysis.py ===
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import json

class FinalAnalysisInput(BaseModel):
    ticket_data: dict = Field(...)
    classification_context: dict = Field(...)

class FinalAnalysisTool(BaseTool):
    name: str = "Final Analysis Tool"
    description: str = "Merges severity with classification"
    args_schema: type[BaseModel] = FinalAnalysisInput

    def _run(self, ticket_data: dict, classification_context: dict) -> str:
        title = ticket_data.get("title", "").lower()
        if "down" in title or "unresponsive" in title:
            severity = "Critical"
            confidence = 0.9
        else:
            severity = "High"
            confidence = 0.75
            
        result = {
	    "ticket_id": ticket_data.get("id"),  # ✅ Ensure ticket ID is preserved
	    **classification_context,
	    "severity": severity,
	    "confidence": confidence
	}

        return json.dumps(result, indent=2)

