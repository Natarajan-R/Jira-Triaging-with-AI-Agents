from crewai.tools import BaseTool
from pydantic import BaseModel
from typing import Dict, Annotated
import json

class MergeInput(BaseModel):
    classification: Dict
    analysis: Dict

class MergeTool(BaseTool):
    name: str = "Merge Tool"
    description: str = "Merges classification and analysis into one final output"
    args_schema: type = MergeInput  # ✅ This fixes the Pydantic 2 error

    def _run(self, classification: Dict, analysis: Dict) -> str:
        result = {
            "ticket_id": classification.get("ticket_id"),
            **classification,
            **analysis
        }
        return json.dumps(result, indent=2)

