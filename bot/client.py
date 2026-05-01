import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logging_config import setup_logger


class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        self.logger = setup_logger()

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError(
                "Missing API credentials. Please add BINANCE_API_KEY and BINANCE_API_SECRET to your .env file."
            )

        self.client = Client(api_key, api_secret)

        # Futures Testnet URL required in the assignment
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        self.logger.info("Binance Futures Testnet client initialized.")

    def place_market_order(self, symbol, side, quantity):
        try:
            self.logger.info(
                f"Sending MARKET order request: symbol={symbol}, side={side}, quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            self.logger.info(f"MARKET order response: {response}")
            return response

        except BinanceAPIException as error:
            self.logger.error(f"Binance API error while placing MARKET order: {error}")
            raise

        except BinanceRequestException as error:
            self.logger.error(f"Network error while placing MARKET order: {error}")
            raise

        except Exception as error:
            self.logger.error(f"Unexpected error while placing MARKET order: {error}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            self.logger.info(
                f"Sending LIMIT order request: symbol={symbol}, side={side}, quantity={quantity}, price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            self.logger.info(f"LIMIT order response: {response}")
            return response

        except BinanceAPIException as error:
            self.logger.error(f"Binance API error while placing LIMIT order: {error}")
            raise

        except BinanceRequestException as error:
            self.logger.error(f"Network error while placing LIMIT order: {error}")
            raise

        except Exception as error:
            self.logger.error(f"Unexpected error while placing LIMIT order: {error}")
            raise