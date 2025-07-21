# data_fetch.py
import pandas as pd

def fetch_data():
    # Simulate pulling data from gaming platform
    data = pd.DataFrame({
        'Game': ['Poker', 'Blackjack', 'Roulette'],
        'Players': [1200, 950, 670],
        'Revenue': [15000, 12000, 8000]
    })
    return data
