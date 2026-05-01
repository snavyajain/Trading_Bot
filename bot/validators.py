def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    symbol = symbol.upper().strip()

    if not symbol.isalnum():
        raise ValueError("Symbol should contain only letters and numbers. Example: BTCUSDT")

    return symbol


def validate_side(side):
    if not side:
        raise ValueError("Side cannot be empty.")

    side = side.upper().strip()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL.")

    return side


def validate_order_type(order_type):
    if not order_type:
        raise ValueError("Order type cannot be empty.")

    order_type = order_type.upper().strip()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be either MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a valid number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price, order_type):
    if order_type == "MARKET":
        return None

    if price is None:
        raise ValueError("Price is required for LIMIT orders.")

    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a valid number.")

    if price <= 0:
        raise ValueError("Price must be greater than 0.")

    return price