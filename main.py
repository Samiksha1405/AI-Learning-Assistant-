import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --------------- AI AGENT CORE LOGIC -----------------

# Input Understanding Layer
def input_understanding(user_input):
    prompt = f"You are an AI tutor. Understand the user's intent clearly and summarize it in one sentence.\nUser: {user_input}\nSummary:"
    return chat_with_gemini(prompt)

# State Tracker Layer (simple memory for now)
conversation_history = []

def state_tracker(user_input, ai_response):
    conversation_history.append({"user": user_input, "ai": ai_response})
    return conversation_history

# Task Planner Layer
def task_planner(user_intent):
    prompt = f"Plan step-by-step how to best answer the user's intent: {user_intent}"
    return chat_with_gemini(prompt)

# Output Generator Layer
def output_generator(user_input):
    prompt = f"You are a friendly AI tutor. Answer the following question in simple words:\n{user_input}"
    return chat_with_gemini(prompt)

# Gemini Chat Function
def chat_with_gemini(prompt):
    model = genai.GenerativeModel("models/gemini-1.5-flash")  # or "models/gemini-1.5-pro"
    response = model.generate_content(prompt)
    return response.text.strip()

# ---------------- MAIN CHAT LOOP -----------------

def main():
    print("🤖 Gemini AI Learning Assistant - Type 'exit' to quit.\n")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Assistant: Goodbye! Keep learning! 👋")
            break

        # 1. Understand User Intent
        intent = input_understanding(user_query)

        # 2. Plan Response
        plan = task_planner(intent)

        # 3. Generate Answer
        answer = output_generator(user_query)

        # 4. Track State
        state_tracker(user_query, answer)

        print(f"\nAssistant: {answer}\n")

if __name__ == "__main__":
    main()
