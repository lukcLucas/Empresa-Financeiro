import matplotlib.pyplot as plt
import pandas as pd

def fetch_portfolio_data():
    # Simulação de dados de portfólio
    return pd.DataFrame({
        'Asset': ['Stock A', 'Bond B', 'Crypto C'],
        'Value': [10000, 5000, 15000],
        'Allocation': [0.4, 0.2, 0.4]
    })

def display_portfolio(df):
    print(df)
    df.set_index('Asset')['Value'].plot(kind='pie', title='Portfolio Allocation', autopct='%1.1f%%')
    plt.show()

def plot_asset_performance(history):
    history.plot(title='Asset Performance Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()

def simulate_future_projections(asset, days_ahead):
    # Simulação simples usando crescimento linear
    current_value = 100  # valor fictício
    future_projection = pd.Series([current_value * (1 + 0.01 * i) for i in range(days_ahead)])
    future_projection.plot(title=f'Future Projection for {asset}')
    plt.xlabel('Days')
    plt.ylabel('Projected Value')
    plt.show()
