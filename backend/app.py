from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from graph import app as agent_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run")
def run_agents(topic: str = Form(...)):
    result = agent_app.invoke({"topic": topic})
    return {
        "final_report": result.get("final_report", "No output generated.")
    }
