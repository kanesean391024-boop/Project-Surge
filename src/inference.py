import time

def infer(event):
    """
    Single-event inference function.
    Designed for ultra-low-latency deployment on Cerebras.
    """
    start = time.time()
    result = event["value"] * 2  # placeholder computation
    end = time.time()

    return {
        "output": result,
        "inference_time_ms": (end - start) * 1000
    }
