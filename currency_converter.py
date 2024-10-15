import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv('API_KEY')  # Get your API key from the .env file
API_URL = os.getenv('API_URL')

Supported_Currencies = ['USD', 'EUR', 'CAD', 'TZS']

def get_amount():
  while True:
    try:
      amount = float(input('Enter the amount: '))
      if amount <= 0:
          raise ValueError()
      return amount
    except ValueError:
      print('Invalid amount. Please enter a positive number.')

def get_currency(label):
  currencies = Supported_Currencies
  while True:
      currency = input(f'{label} currency (USD/EUR/CAD/TZS): ').upper()
      if currency not in currencies:
        print('Invalid currency. Please choose from USD, EUR, CAD, TZS.')
      else:
        return currency

def fetch_exchange_rates():
  try:
    response = requests.get(f'{API_URL}?access_key={API_KEY}&symbols={",".join(Supported_Currencies)}')
    data = response.json()

    if response.status_code != 200:
      raise Exception(f"API request failed with status code {response.status_code}.") 
    return data.get('rates', {})
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

def convert(amount, source_currency, exchange_rates):
  base_to_eur_rate = exchange_rates[source_currency]
  print(f'\n{amount}{source_currency} is equivalent to: ')

  for target_currency, eur_to_target_rate in exchange_rates.items():
    if target_currency != source_currency:
      amount_in_target_currency = (amount * base_to_eur_rate) * eur_to_target_rate
      print(f'{amount_in_target_currency:.2f} {target_currency}')

def main():
  amount = get_amount()
  source_currency = get_currency('Source')

  exchange_rates = fetch_exchange_rates()

  if exchange_rates:
    convert(amount, source_currency, exchange_rates)
  else:
    print("Unable to fetch exchange rates. Please try again later.")

if __name__ == "__main__":
  main()
