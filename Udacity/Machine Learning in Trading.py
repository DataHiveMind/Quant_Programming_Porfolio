import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("sp500sub.csv")
    df[["Close", "Adj Close"]].plot()
    plt.show()

# Building a dataframe in pandas
def date_range(start_date, end_date):
    date = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index = date)
    return df1

# Join SPY data
def joinSPY():
    # Define date range
    start_date = "2010-01-22"
    end_date = "2010-01-26"
    date = pd.date_range(start_date, end_date)

    # Create an empty dataframe
    df1 = pd.DataFrame(index = date)

    #Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("sp500sub.csv", parse_dates = True)
    print(dfSPY)

    # Join the two dataframes using DataFrame.join() function
    df1 = df1.join(dfSPY)
    print(df1)


if __name__ == "__main__":
    test_run()
    date_range("2010-01-22", "2010-01-26")
    joinSPY()
