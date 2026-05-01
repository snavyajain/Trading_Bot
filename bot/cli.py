import argparse

from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger


def print_order_summary(symbol, side, order_type, quantity, price):
    print("\nORDER REQUEST SUMMARY")
    print("-" * 45)
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    if order_type == "LIMIT":
        print(f"Price       : {price}")

    print("-" * 45)


def print_order_response(response):
    print("\nORDER RESPONSE DETAILS")
    print("-" * 45)
    print(f"Order ID       : {response.get('orderId', 'N/A')}")
    print(f"Status         : {response.get('status', 'N/A')}")
    print(f"Executed Qty   : {response.get('executedQty', 'N/A')}")
    print(f"Average Price  : {response.get('avgPrice', 'N/A')}")
    print("-" * 45)


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(
        description="Simplified Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol, for example BTCUSDT")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity, for example 0.001")
    parser.add_argument("--price", required=False, help="Order price. Required only for LIMIT orders")

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print_order_summary(symbol, side, order_type, quantity, price)

        order_manager = OrderManager()

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print_order_response(response)

        print("\nSUCCESS: Order placed successfully.")
        logger.info("Order placed successfully.")

    except ValueError as error:
        print("\nFAILURE: Invalid input.")
        print(f"Error: {error}")
        logger.error(f"Input validation error: {error}")

    except Exception as error:
        print("\nFAILURE: Order could not be placed.")
        print(f"Error: {error}")
        logger.error(f"Order placement failed: {error}")


if __name__ == "__main__":
    main()