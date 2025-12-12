# Cerebras Design Rationale

Traditional AI inference pipelines are optimized for throughput, not latency. GPU-based systems rely on batching and scheduling to remain efficient, which introduces unavoidable delays.

Project Surge is designed for **single-event inference**, where each event is processed immediately upon arrival.

Cerebras enables this design by:
- Eliminating batching requirements
- Providing deterministic inference latency
- Supporting massive parallelism at wafer scale

This makes Cerebras uniquely suited for real-time AI systems where:
\[
t_{\text{response}} < 1\text{ ms}
\]

Project Surge is architected specifically to take advantage of these properties.
