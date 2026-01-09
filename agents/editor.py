from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="gemma:2b",
    temperature=0.2,
    num_ctx=1024,      # ↓ lower memory
    num_predict=256,   # ↓ limit output length
    stream=False       # 🚨 VERY IMPORTANT
)



def editor(state):
    draft = state.get("draft", "")

    prompt = f"""
    Rewrite this into a polished technical blog post.

    {draft}
    """

    final = llm.invoke(prompt)

    return {"final_report": final}
