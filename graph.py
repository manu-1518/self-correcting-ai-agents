from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.researcher import researcher
from agents.fact_checker import fact_checker
from agents.critic import critic
from agents.editor import editor

class AgentState(TypedDict, total=False):
    topic: str
    draft: str
    revisions: int
    final_report: str


graph = StateGraph(AgentState)

graph.add_node("researcher", researcher)
graph.add_node("fact_checker", fact_checker)
graph.add_node("critic", critic)
graph.add_node("editor", editor)

MAX_REVISIONS = 10

def route(state: AgentState):
    if state.get("revisions", 0) < MAX_REVISIONS:
        return "researcher"
    return "editor"

graph.set_entry_point("researcher")


graph.add_edge("researcher", "critic")
graph.add_edge("critic", "editor")
graph.add_edge("editor", END)





app = graph.compile()
