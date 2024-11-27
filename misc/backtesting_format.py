import backtrader as bt
import numpy as np
import pandas as pd

class MovingAverageCrossStrategy(bt.Strategy):
    short_ma = bt.indicators.SimpleMovingAverage
    long_ma = bt.indicators.SimpleMovingAverage

    params = (
        ('short_period', 5),
        ('long_period', 20)
    )

    def __init__(self):
        self.short_sma = self.short_ma(self.data.close, period=self.params.short_period)
        self.long_sma = self.long_ma(self.data.close, period=self.params.long_period)

    def next(self):
        if self.short_sma > self.long_sma:
            if not self.position:
                self.buy()
        elif self.short_sma < self.long_sma:
            if self.position:
                self.sell()

# Generate smoother synthetic data
class RandomData(bt.feeds.PandasData):
    lines = ('close',)
    params = (
        ('datetime', None),
        ('open', -1),
        ('high', -1),
        ('low', -1),
        ('close', -1),
        ('volume', -1),
        ('openinterest', -1),
    )

# Generate smoother data for the backtest (use sine wave with small random noise)
np.random.seed(42)  # For reproducibility
dates = pd.date_range('2020-01-01', '2020-12-31', freq='B')  # Business days in 2020

# Create a smooth upward trend (e.g., a sine wave with small random noise)
trend = np.linspace(200, 300, len(dates))  # A simple linear trend from 200 to 300
noise = np.random.normal(0, 5, len(dates))  # Small noise with a standard deviation of 5
prices = trend + noise  # Add noise to the trend

# Create a DataFrame with correct datetime format
data = pd.DataFrame({
    'datetime': dates,
    'close': prices
})

# Set datetime as index (Backtrader's default)
data.set_index('datetime', inplace=True)

# Backtrader requires 'open', 'high', 'low', 'volume', and 'openinterest'
data['open'] = data['close']  # Assuming open == close for simplicity
data['high'] = data['close']  # Same for high and low
data['low'] = data['close']
data['volume'] = 0  # Volume data (set to 0 if not available)
data['openinterest'] = 0  # Open interest (set to 0 if not available)

# Create a Backtrader data feed from the generated DataFrame
feed = RandomData(dataname=data)

cerebro = bt.Cerebro()
cerebro.addstrategy(MovingAverageCrossStrategy)
cerebro.adddata(feed)

cerebro.broker.set_cash(10000)
cerebro.broker.setcommission(commission=0.001)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
print(f"Current Cash: {cerebro.broker.getcash()}")

cerebro.run()
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
print(f"Current Cash: {cerebro.broker.getcash()}")
cerebro.plot()
