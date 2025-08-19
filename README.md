Crypto Agent

This project is a simple crypto trading agent that can fetch real-time market prices from the CoinGecko API and help make basic trading decisions like buy or sell.

🚀 Features

Get live crypto prices using the CoinGecko API

Agent-based structure for market analysis

Easy to extend with more tools

Works with any coin and currency supported by CoinGecko

📂 Project Structure

agents.py → Defines the Agent, Runner, and function_tool system

connection.py → Stores configuration (config)

main.py → Entry point to run the Crypto Agent

get_market_data() → Tool to fetch live crypto prices

🛠️ How it Works

The get_market_data function fetches real-time prices for a given coin and currency.

The Crypto_Agent uses this tool to analyze the data.

You run the project and get an output on whether to invest or not.

▶️ Usage

Clone the repo:

git clone https://github.com/your-username/crypto-agent.git
cd crypto-agent


Install dependencies:

pip install requests


Run the project:

python main.py

🔑 Example
get_market_data("bitcoin", "usd")
# Output: {'bitcoin': {'usd': 29450}}

📌 Notes

Make sure you have Python 3.8+ installed

This project uses CoinGecko free API (no API key required)

You can extend the agent with more trading logic and tools
