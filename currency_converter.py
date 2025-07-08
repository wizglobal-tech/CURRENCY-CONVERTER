import streamlit as st
import requests

# Function to get exchange rates from an open API
def get_exchange_rates():
    # This URL points to a free exchange rate API that doesn't require an API key
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Streamlit app design
def main():
    # Title of App
    st.title("Currency Converter")

    # Instructions
    st.write("Convert your currency using the latest exchange rates.")

    # User input for the amount of money
    amount = st.number_input("Amount", min_value=1.0, value=1.0)

    # Getting exchange rates
    exchange_rates = get_exchange_rates()

    # Select currencies
    currencies = list(exchange_rates.keys())
    from_currency = st.selectbox("From", currencies)
    to_currency = st.selectbox("To", currencies)

    # Convert amount
    if st.button("Convert"):
        if from_currency == to_currency:
            st.error("You must select different currencies to convert.")
        else:
            converted_amount = round(amount * (exchange_rates[to_currency] / exchange_rates[from_currency]), 2)
            st.success(f"{amount} {from_currency} = {converted_amount} {to_currency}")

# Run the app
if __name__ == "__main__":
    main()
