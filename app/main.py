from logging import ERROR, CRITICAL, FATAL, ERROR, WARNING, WARN, INFO, DEBUG, NOTSET, _levelToName
# import constants
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from app import ingest_producer
from app.util import generate_time_stamp, generate_trace_id


app = FastAPI()

class AgentActionRequest(BaseModel):
    user_id: str = "a7f3d21e"
    action: str = "login"
    ip_address: str = "192.168.1.45"
    browser: str = "Chrome"
    os: str = "Windows 11"
    location: str = "San Francisco, CA"
    session_id: str = "sess_8291a3cd"
    count: int = 1

def run_test(count: int):
    for i in range(count):
        content = {
            "user_id": "a7f3d21e",
            "action": "login",
            "timestamp": "2025-05-23T13:45:00Z",
            "metadata": {
                "ip_address": "192.168.1.45",
                "browser": "Chrome",
                "os": "Windows 11",
                "location": "San Francisco, CA"
            },
            "session_id": "sess_8291a3cd"
        }
        
        traceId = generate_trace_id()
        ingest_producer.ingest_message( content, traceId)


@app.post("/control/agent-action")
def control_agent_action(request: AgentActionRequest):

    run_test(request.count)
    # traceId = generate_trace_id()
    # ingest_producer.ingest_message(content, traceId)

    return {"status": "success", "message": f"Ingested {request.count} messages."}


