import requests
import pandas as pd

API_KEY = 'cola sua chave api aqui'  # Substitua isso pela sua chave de API real



def get_real_time_price(symbol):
    """Obtém o preço em tempo real de um ativo usando a API da Alpha Vantage."""
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        price = data['Global Quote']['05. price']
        return float(price)
    except KeyError:
        print("Error retrieving data. Check the stock symbol and your API key.")
        return None

def get_historical_data(symbol):
    """Obtém dados históricos de preços de uma ação usando a API da Alpha Vantage."""
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        df = pd.DataFrame(data['Time Series (Daily)']).T.astype(float)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.index = pd.to_datetime(df.index)
        return df['close']
    except KeyError:
        print("Error retrieving data or data format changed.")
        return None