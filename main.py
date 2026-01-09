from graph import app

if __name__ == "__main__":
    result = app.invoke({
        "topic": "How AI agents are used in software engineering"
    })

    print("\n===== FINAL REPORT =====\n")
    print(result["final_report"])
