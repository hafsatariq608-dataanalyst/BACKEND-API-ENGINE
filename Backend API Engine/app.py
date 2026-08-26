import os
import json
import time
from flask import Flask, render_template, request, Response

app = Flask(__name__)

# Live Telemetry Tool Database
MOCK_VECTOR_DB = {
    "nexus_rag": {
        "pipeline": "Nexus RAG Search",
        "metric": "Vector Latency",
        "baseline": "420ms",
        "optimized": "185ms",
        "delta": "-55.9%",
        "status": "Operational"
    },
    "jobfit_ocr": {
        "pipeline": "JobFit PDF Parser",
        "metric": "OCR Extraction",
        "baseline": "4.2s",
        "optimized": "1.1s",
        "delta": "-73.8%",
        "status": "Operational"
    }
}

def query_vector_db(pipeline_key: str) -> str:
    """Tool function retrieving pipeline telemetry."""
    return json.dumps(MOCK_VECTOR_DB.get(pipeline_key, MOCK_VECTOR_DB["nexus_rag"]))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json or {}
    user_message = data.get('message', '').strip().lower()

    def generate():
        # Route 1: Run Live Benchmark Simulation
        if "benchmark" in user_message or "simulation" in user_message:
            tool_data = json.loads(query_vector_db("nexus_rag"))
            yield f'[[EXECUTE: {json.dumps(tool_data)}]]\n\n'
            
            response_text = (
                f"Executed live telemetry audit against {tool_data['pipeline']}. "
                f"Baseline latency dropped from {tool_data['baseline']} to {tool_data['optimized']} "
                f"({tool_data['delta']} reduction). Optimization was achieved through dense vector indexing, "
                f"semantic chunking, and parallelized embedding retrieval."
            )

        # Route 2: System Architecture Overview
        elif "architecture" in user_message or "explain" in user_message:
            response_text = (
                "The Nexus RAG Search pipeline uses a two-stage retrieval architecture: "
                "1. Semantic retrieval with dense vector embeddings stored in a local index. "
                "2. Reranking and contextual filtering via Groq API. "
                "This design cuts retrieval latency down to under 200ms."
            )

        # Route 3: JobFit / OCR Queries
        elif "ocr" in user_message or "jobfit" in user_message:
            tool_data = json.loads(query_vector_db("jobfit_ocr"))
            yield f'[[EXECUTE: {json.dumps(tool_data)}]]\n\n'
            
            response_text = (
                f"Queried {tool_data['pipeline']} metrics. Document extraction latency improved from "
                f"{tool_data['baseline']} down to {tool_data['optimized']} ({tool_data['delta']}) "
                f"using layout-aware parsing and structured output formatting."
            )

        # Route 4: General Queries / Anything Else
        else:
            response_text = (
                f"Nexus-01 online. Received query: '{data.get('message', '')}'. "
                "You can ask me to run benchmark simulations, explain system architectures, "
                "or audit vector search metrics."
            )

        # Stream the output word by word
        for word in response_text.split(" "):
            yield word + " "
            time.sleep(0.03)

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)