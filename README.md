# Binance Futures Testnet Trading Bot

This is a small Python command-line bot for placing orders on Binance Futures Testnet. It supports MARKET and LIMIT orders and works with both BUY and SELL sides.

I made this project for the Python Developer Intern assignment. The main goal was to keep it simple, readable, and easy to run, while still including input validation, logging, and error handling.

## What it does

- Places MARKET orders
- Places LIMIT orders
- Supports BUY and SELL
- Takes input from the command line
- Validates user input before placing an order
- Prints order request and response details
- Saves logs for requests, responses, and errors
- Loads API keys from a `.env` file instead of hardcoding them

## Setup

First, download or clone the project.

```bash
git clone your_repository_link_here
cd "Trading Bot"
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on Mac/Linux:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the main project folder and add your Binance Futures Testnet API keys:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

The `.env` file should not be uploaded to GitHub.

## How to run

Run all commands from the main project folder.

To check the available command options:

```bash
python -m bot.cli --help
```

Example MARKET BUY order:

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example MARKET SELL order:

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

Example LIMIT BUY order:

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

Example LIMIT SELL order:

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

## Example output

```
ORDER REQUEST SUMMARY
--------------------------------------------
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001


ORDER RESPONSE DETAILS
---------------------------------------------
Order ID       : 123456789
Status         : NEW
Executed Qty   : 0.001
Average Price  : 0.00

SUCCESS: Order placed successfully.
```

## Logs

The bot creates a log file while running:

```text
logs/trading_bot.log
```

For the assignment submission, I also included sample logs for one MARKET order and one LIMIT order in the `sample_logs` folder.

The logs include the order request, the API response, and any errors if something goes wrong.

## Error handling

The bot checks for common input mistakes before sending an order request.

For example, it handles:

- Invalid side, such as something other than BUY or SELL
- Invalid order type, such as something other than MARKET or LIMIT
- Missing price for a LIMIT order
- Quantity less than or equal to zero
- Missing API credentials
- Binance API errors
- Network or request errors

## Notes

This project is only for Binance Futures Testnet. It uses USDT-M Futures symbols such as `BTCUSDT`.

LIMIT orders use `GTC` as the time in force.

API keys are stored locally in a `.env` file and are not pushed to GitHub.