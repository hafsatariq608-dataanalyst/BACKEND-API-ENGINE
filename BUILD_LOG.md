# Checkpoint 1 Build Log — Nexus-01 Audit Co-Pilot

## 1. Core Job & Platform Selection
- **Platform:** Python 3.12 / Flask + Groq API (`llama-3.1-8b-instant`) + Custom Single-Page HTML/JS Interface.
- **Core Job:** Automated ML technical audit co-pilot capable of executing live RAG retrieval simulations and serving architecture reviews for engineering portfolio showcases.
- **Connected Tool:** Backend vector latency telemetry service (`query_vector_db`) returning simulated JSON performance metrics.

---

## 2. Iteration Log (Bug Fixes & Refinement)

### Failure 1: Unparsed Execution Tokens in Chat UI
- **Issue:** The backend tool execution tokens (`[[EXECUTE: ...]]`) streamed directly into user chat bubbles as raw text.
- **Fix:** Implemented client-side regex extraction in `sendMessage()` JavaScript to isolate execution payloads, automatically render a visual tool indicator (`⚡ Live Vector Tool Executed`), and display clean technical output.

### Failure 2: API Model Decommissioning & Fallbacks
- **Issue:** Encountered `404 model_not_found` and `model_decommissioned` errors on legacy model strings (`llama-3.3-70b-versatile` and `llama3-70b-8192`).
- **Fix:** Transitioned backend routing to use active production strings (`llama-3.1-8b-instant`) and added local tool response routing to guarantee uninterrupted demonstration reliability during live evaluations.

---

## 3. Deviations from Specification
- **UI Layout:** Designed a dark-mode dual dashboard layout (System Architecture Cards + Real-Time Copilot Workspace) using standard typography (`Inter`) rather than a simple text-only chatbox. This provides immediate context on benchmark metrics alongside live streaming outputs.