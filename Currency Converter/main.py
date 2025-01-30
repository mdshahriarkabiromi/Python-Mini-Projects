# Simple Currency Converter

# Function to convert currency
def convert_currency(amount, rate):
    return amount * rate

# Main program
if __name__ == "__main__":
    # Example exchange rates (1 USD to other currencies)
    exchange_rates = {
        "USD_TO_EUR": 0.96,
        "USD_TO_GBP": 0.80,
        "USD_TO_BDT": 121.86,   # USD to Bangladeshi Taka
        "USD_TO_INR": 86.59,    # USD to Indian Rupee
        "USD_TO_CAD": 1.44,     # USD to Canadian Dollar
        "USD_TO_AUD": 1.61,     # USD to Australian Dollar
        "USD_TO_JPY": 154.38    # USD to Japanese Yen
    }

    # Get user input
    amount = float(input("Enter amount in USD: "))
    target_currency = input("Enter target currency (EUR, GBP, BDT, INR, CAD, AUD, JPY): ").upper()

    # Determine the exchange rate
    exchange_rate_key = f"USD_TO_{target_currency}"
    if exchange_rate_key in exchange_rates:
        exchange_rate = exchange_rates[exchange_rate_key]
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} USD is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Exchange rate not available for the given currency.")
