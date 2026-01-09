from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="gemma:2b",
    temperature=0.2,
    num_ctx=1024,
    num_predict=128,
    stream=False
)

def critic(state):
    draft = state.get("draft", "")

    prompt = f"""
    Point out 1–2 major factual or logical issues (if any).
    If none, say "No major issues found."

    Report:
    {draft[:1000]}
    """

    feedback = llm.invoke(prompt)

    return {**state, "critic_feedback": feedback}
