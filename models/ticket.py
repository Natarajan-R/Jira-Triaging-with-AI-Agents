
# === models/ticket.py ===
from dataclasses import dataclass, asdict
from datetime import datetime
import json

@dataclass
class IncidentTicket:
    id: str
    title: str
    description: str
    reporter: str
    created_date: datetime = datetime.now()

    def to_json(self):
        return json.dumps(asdict(self), default=str)

