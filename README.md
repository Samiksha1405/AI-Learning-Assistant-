1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install Dependencies
pip install -r requirements.txt
(If you don’t have requirements.txt, you can manually run:)

pip install google-generativeai python-dotenv

3. Set Up API Key
-Go to Google AI Studio.
-Generate a free API key.
-Create a .env file in the project folder:
  GEMINI_API_KEY=your_api_key_here

4.Run the AI Agent
python main.py
You will see:
🤖 Gemini AI Learning Assistant - Type 'exit' to quit.

You: Can you explain Newton's 2nd law in simple words?
Assistant: Newton’s second law means force makes objects speed up or slow down depending on how heavy they are. More force = faster change in motion.
