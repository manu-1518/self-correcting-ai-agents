from langchain_ollama import OllamaLLM



llm = OllamaLLM(
    model="gemma:2b",
    temperature=0.2,
    num_ctx=1024,      # ↓ lower memory
    num_predict=256,   # ↓ limit output length
    stream=False       # 🚨 VERY IMPORTANT
)



def fact_checker(state):
    draft = state.get("draft", "")

    prompt = f"""
    Check the report for factual errors or unsupported claims.

    Report:
    {draft}

    Respond with:
    NEEDS_REVISION: YES or NO
    """

    response = llm.invoke(prompt)

    if "YES" in response:
        return {**state, "revision_needed": True}

    return state
