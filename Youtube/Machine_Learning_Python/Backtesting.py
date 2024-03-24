from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover
import talib

# Google Stock Data
#print(GOOG)

# Create a Strategy
class Rs(Strategy):
    upper_bound = 70
    lower_bound = 30

    def __init__(self):
        self.rsi = self.I(talib.RSI, self.data.Close, 14)


    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()


if __name__ == '__main__':
    bt = Backtest(GOOG, Rs, cash = 10_000)
    stats = bt.run()
    print(stats)