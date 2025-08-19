from agents import Agent, Runner, function_tool
from connection import config
import requests

@function_tool
def get_market_data(coin , currency):
    """Fetch real-time crypto price from CoinGecko"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}

Crypto_Agent = Agent(
    name="Crypto Agent",
    instructions="You are a crypto trading agent. Analyze market data and decide whether to buy or sell. And always call tools to get real-time data.",
    tools=[get_market_data]
)

def main():
    runner = Runner.run_sync(
        Crypto_Agent,
        "What coin is best to invest right now",
        run_config=config
        )
    print(runner.final_output)

if __name__ == "__main__":
    main()
