from graph import app

if __name__ == "__main__":
    result = app.invoke({
        "topic": "How AI agents are used in software engineering"
    })

    print("\n===== RAW RESULT =====\n")
    print(result)

    print("\n===== FINAL REPORT =====\n")
    print(result.get("final_report", "No final report generated"))
