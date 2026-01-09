from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.researcher import researcher
from agents.fact_checker import fact_checker
from agents.critic import critic
from agents.editor import editor

class AgentState(TypedDict, total=False):
    topic: str
    draft: str
    final_report: str

graph = StateGraph(AgentState)

graph.add_node("researcher", researcher)
graph.add_node("fact_checker", fact_checker)
graph.add_node("critic", critic)
graph.add_node("editor", editor)

graph.set_entry_point("researcher")

graph.add_edge("researcher", "fact_checker")
graph.add_edge("fact_checker", "critic")
graph.add_edge("critic", "editor")
graph.add_edge("editor", END)

app = graph.compile()
