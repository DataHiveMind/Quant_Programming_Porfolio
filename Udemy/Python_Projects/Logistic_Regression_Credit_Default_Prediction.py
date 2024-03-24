# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def data_preprocessing():
    # load data
    data = pd.read_csv("credit_default.csv")
    data.head()
    data.info()
    data.describe()
    data.isnull().sum()
    data["default.payment.next.month"].value_counts()
    data["default.payment.next.month"].value_counts().plot(kind="bar")
    plt.show()



if __name__ == "__main__":
    data_preprocessing()
