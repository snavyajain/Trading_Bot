# Binance Futures Testnet Trading Bot

This is a simple Python trading bot that runs from the command line. It places MARKET and LIMIT orders on Binance Futures Testnet and supports both BUY and SELL.

I made this for the Python Developer Intern assignment.

## Features

- MARKET and LIMIT orders
- BUY and SELL support
- Command-line input
- Basic input validation
- Logs requests, responses, and errors
- API keys are loaded from a `.env` file

## Setup

After downloading or importing the code, open the main project folder in the terminal.

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the main folder and add your Binance Futures Testnet API keys:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

## How to use

Run the bot from the main project folder.

For example, a MARKET order can be placed like this:

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

For a LIMIT order, use the same command format but set the type to `LIMIT` and include a price.

You can change the symbol, side, order type, quantity, and price based on the order you want to place.

## Logs

The bot saves logs in the `logs` folder. I have also included sample logs for one MARKET order and one LIMIT order in the `sample_logs` folder.

## Notes

This project is only for Binance Futures Testnet. LIMIT orders use `GTC` as the time in force. The `.env` file is not pushed to GitHub.