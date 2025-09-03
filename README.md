# AgriSense-AI-Smart-Crop-Advisory-Agent
🌱 AgriSense AI – Smart Crop Advisory Agent

AgriSense AI is an AI-powered digital agronomist that helps farmers make data-driven decisions.
It combines RAG (Retrieval-Augmented Generation), Memory Agents, Weather APIs, and Voice + Local Language Support to deliver personalized, actionable crop advisory.

🚀 Features
📖 Knowledge Retrieval (RAG): Pulls insights from agricultural research PDFs, government advisories, and datasets.
🧠 Memory Agent: Remembers farm details like soil type, crop history, fertilizers used.
☁️ Weather Integration: Connects to weather APIs for irrigation & crop cycle recommendations.
🎙️ Multilingual Voice/Text Support: Farmers can ask queries in local languages (via text or voice).
🌾 Actionable Advice: Fertilizer dosage, irrigation scheduling, pest/disease alerts, and market tips.


⚙️ Installation

Clone repo
git clone https://github.com/your-username/agrisense-ai.git
cd agrisense-ai

Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies
pip install -r requirements.txt

Setup config
Add your API keys (OpenAI, weather API, etc.) in config.yaml.

▶️ Usage
CLI Mode
python main.py

Example query:
"Should I irrigate my paddy field tomorrow?"
Output:
"No, rain is expected in your region tomorrow. Irrigate for 2 hours in the morning after the rain."

🛠️ Tech Stack
LLM + RAG → LangChain / LlamaIndex, FAISS/Chroma for vector search
Memory → Vector DB + JSON/YAML for structured farm memory
APIs → OpenWeatherMap / IMD / Gov advisories
Voice → Whisper (STT), gTTS / ElevenLabs (TTS)
Backend → FastAPI / Flask
Frontend (optional) → React Native / Streamlit for farmer-friendly UI

🌍 Impact
Acts as a personal agronomist for smallholder farmers
Reduces crop loss from weather & pests
Optimizes fertilizer and water usage
Bridges research knowledge with grassroots farming

📌 Roadmap
 Define project structure
 Implement RAG engine (PDF + advisories)
 Build farm memory storage
 Integrate weather API
 Add voice + multilingual support
 Deploy via FastAPI + simple farmer-facing UI
 
🤝 Contributing
Contributions are welcome!
Fork this repo
Create a feature branch
Submit a pull request

📜 License

MIT License © 2025 AgriSense AI
