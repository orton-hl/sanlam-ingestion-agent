import shortuuid
from datetime import datetime

def generate_trace_id():
    return shortuuid.uuid()

def generate_time_stamp():
    return datetime.utcnow().isoformat()
