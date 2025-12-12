import time
import random

def generate_event():
    return {
        "value": random.random(),
        "timestamp": time.time()
    }

def stream_events(n=5):
    for _ in range(n):
        yield generate_event()
        time.sleep(0.01)  # simulate incoming stream
