from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="gemma:2b",
    temperature=0.2,
    num_ctx=1024,
    num_predict=256,
    stream=False
)

def editor(state):
    draft = state.get("draft", "")

    prompt = f"""
    Rewrite this into a clear, polished technical article:

    {draft}
    """

    final = llm.invoke(prompt)

    return {"final_report": final}
