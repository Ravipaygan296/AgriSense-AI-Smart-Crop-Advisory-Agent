import argparse
from modules.rag_engine.retriever import Retriever
from modules.memory_agent.memory_store import MemoryStore
from modules.weather_agent.weather_api import WeatherAPI
from modules.advisory_agent.decision_engine import DecisionEngine
from utils.logger import get_logger

logger = get_logger()

def main():
    parser = argparse.ArgumentParser(description="AgriSense AI - Smart Crop Advisory Agent")
    parser.add_argument("--query", type=str, required=True, help="Your farming question")
    args = parser.parse_args()

    # Initialize components
    memory = MemoryStore("data/farm_memory.json")
    retriever = Retriever()
    weather = WeatherAPI()
    advisor = DecisionEngine(retriever, memory, weather)

    # Get response
    response = advisor.get_advice(args.query)
    print("\n🌱 AgriSense AI Advice:")
    print(response)

if __name__ == "__main__":
    main()

