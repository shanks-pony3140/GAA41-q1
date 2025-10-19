import re
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/execute")
def execute(q: str):
    # Ticket Status
    ticket_match = re.search(r"What is the status of ticket (\d+)\?", q)
    if ticket_match:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": int(ticket_match.group(1))}),
        }

    # Meeting Scheduling
    meeting_match = re.search(r"Schedule a meeting on ([\d-]+) at ([\d:]+) in (.*).", q)
    if meeting_match:
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": meeting_match.group(1),
                "time": meeting_match.group(2),
                "meeting_room": meeting_match.group(3),
            }),
        }

    # Expense Reimbursement
    expense_match = re.search(r"Show my expense balance for employee (\d+).", q)
    if expense_match:
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({"employee_id": int(expense_match.group(1))}),
        }

    # Performance Bonus Calculation
    bonus_match = re.search(r"Calculate performance bonus for employee (\d+) for (\d+).", q)
    if bonus_match:
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(bonus_match.group(1)),
                "current_year": int(bonus_match.group(2)),
            }),
        }

    # Office Issue Reporting
    issue_match = re.search(r"Report office issue (\d+) for the (.*) department.", q)
    if issue_match:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(issue_match.group(1)),
                "department": issue_match.group(2),
            }),
        }

    return {"error": "Query not recognized"}
