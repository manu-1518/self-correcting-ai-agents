from langchain_ollama import OllamaLLM
from ddgs import DDGS


llm = OllamaLLM(
    model="gemma:2b",
    temperature=0.2,
    num_ctx=1024,      # ↓ lower memory
    num_predict=256,   # ↓ limit output length
    stream=False       # 🚨 VERY IMPORTANT
)




def researcher(state):
    topic = state.get("topic")
    if not topic:
        raise ValueError("Missing 'topic' in state")

    with DDGS() as ddgs:
        results = list(ddgs.text(topic, max_results=5))

    sources = "\n".join(
        f"- {r.get('title')} ({r.get('href')})"
        for r in results
    )

    prompt = f"""
    Write a factual research report.
    Use only the sources below.

    Topic: {topic}

    Sources:
    {sources}
    """

    draft = llm.invoke(prompt)

    return {
    "draft": draft,
    "revisions": state.get("revisions", 0) + 1
}

