# Simple Currency Converter

# Function to convert currency
def convert_currency(amount, rate):
    return amount * rate

# Main program
if __name__ == "__main__":
    # Example exchange rates (1 USD to other currencies)
    exchange_rates = {
        "USD_TO_EUR": 0.85,
        "USD_TO_GBP": 0.73,
        "USD_TO_BDT": 84.75  # USD to Bangladeshi Taka
    }

    # Get user input
    amount = float(input("Enter amount in USD: "))
    target_currency = input("Enter target currency (EUR, GBP, BDT): ").upper()

    # Determine the exchange rate
    exchange_rate_key = f"USD_TO_{target_currency}"
    if exchange_rate_key in exchange_rates:
        exchange_rate = exchange_rates[exchange_rate_key]
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} USD is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Exchange rate not available for the given currency.")
