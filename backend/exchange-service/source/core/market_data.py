import random
import time
from typing import List, Dict, Any
from source.config import config

class MarketDataGenerator:
    def __init__(self, symbols: List[str] = None):
        self.symbols = symbols or config.simulator.default_symbols
        self.prices = {
            symbol: random.uniform(config.simulator.min_price, config.simulator.max_price)
            for symbol in self.symbols
        }

    def update_prices(self):
        for symbol in self.symbols:
            current_price = self.prices[symbol]
            volatility = config.simulator.volatility
            price_change = current_price * random.uniform(-volatility, volatility)
            self.prices[symbol] = max(0.01, current_price + price_change)

    def get_market_data(self, symbols: List[str] = None) -> List[Dict[str, Any]]:
        symbols = symbols or self.symbols
        market_data = []

        for symbol in symbols:
            price = self.prices.get(symbol, 0)
            spread = price * 0.01  # 1% spread
            market_data.append({
                'symbol': symbol,
                'bid': price - spread,
                'ask': price + spread,
                'bid_size': random.randint(100, 1000),
                'ask_size': random.randint(100, 1000),
                'last_price': price,
                'last_size': random.randint(10, 100)
            })

        return market_data