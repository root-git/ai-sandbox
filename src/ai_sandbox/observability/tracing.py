import phoenix as px # Import the Arize Phoenix library to initialize a local tracing visualization server
from openinference.instrumentation.openai import OpenAIInstrumentor # Import OpenAI instrumentor to auto-capture LLM telemetry spans

def setup_tracing() -> None:
    """Initializes the local Phoenix dashboard and automatically instruments OpenAI API execution calls."""
    # Launch the local Phoenix tracing dashboard session to mnitor latency, prompts and token usage
    session = px.launch_app()

    # Instrument the OpenAI client SDK to automatically expore telemetry spans to the active Phoenix session
    OpenAIInstrumentor().instrument()