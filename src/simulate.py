from event_stream import stream_events
from inference import infer
from raindrop import Raindrop

raindrop = Raindrop()

for event in stream_events():
    result = infer(event)
    adjusted = raindrop.apply(result["output"])
    raindrop.update(adjusted * 0.01)

    print(f"Event received at: {event['timestamp']:.6f}")
    print(f"Inference completed in: {result['inference_time_ms']:.3f} ms")
    print("Action triggered immediately\n")
