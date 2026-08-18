from ai_sandbox.schemas import AIRequest, ModelConfig, UserProfile
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

def run_demo():
    print("--- 1. Creating a Valid AI Request ---")
    valid_payload = {
        "request_id": "req-99999",
        "user": {
            "user_id": "usr_77",
            "email": "developer@example.com",
            "is_premium": True,
        },
        "config": {"temperature": 0.8, "model_name": "gpt-4o"},
        "prompt": "Explain Quantum Physics like I am five.",
    }

    # Pydantic validates and parses the raw dictionary into typed objects
    request_obj = AIRequest(**valid_payload)
    print("Successfully instantiated model!")
    print(f"User Email: {request_obj.user.email}")
    print(f"Model Name: {request_obj.config.model_name}")
    print(f"Is Premium: {request_obj.user.is_premium}")

if __name__ == "__main__":
    run_demo()