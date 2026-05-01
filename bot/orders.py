from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger


class OrderManager:
    def __init__(self):
        self.logger = setup_logger()
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        self.logger.info(
            f"OrderManager received order: symbol={symbol}, side={side}, "
            f"order_type={order_type}, quantity={quantity}, price={price}"
        )

        if order_type == "MARKET":
            return self.client.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        if order_type == "LIMIT":
            return self.client.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        raise ValueError("Unsupported order type.")