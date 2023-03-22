"""Second example of using Bridge and Template patterns."""

from abc import ABC, abstractmethod
from typing import List


# Here is about Bridge pattern
class Exchange(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass


class Binance(Exchange):
    def connect(self):
        print("Connecting to Binance exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]


class Coinbase(Exchange):
    def connect(self):
        print("Connecting to Coinbase exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 20]


# Here ends Bridge pattern


# Here is about Template pattern
class TradingBot(ABC):
    """Abstract Template class for trading bots."""

    def __init__(self, exchange: Exchange):
        """Initialize the exchange using the Bridge pattern."""
        self.exchange = exchange

    def check_prices(self, coin: str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")

    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass


# Here ends Template pattern


# Classes that use the Template pattern by inheriting from TradingBot
class AverageTrader(TradingBot):
    def list_average(self, lst: List[float]) -> float:
        return sum(lst) / len(lst)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)


application = AverageTrader(Binance())
application.check_prices("BTC/USD")
