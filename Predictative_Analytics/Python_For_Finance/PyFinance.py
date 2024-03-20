# Import Libraries
import numpy as np # linear Algebra
import pandas as pd # Data Processing
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style = 'white', color_codes = True)
import warnings
warnings.filterwarnings('ignore')
import os
from scipy.stats import lognorm as log
import pylab as pl

#Fb(face bond), RB(Rate), tb(time of Maturity)
def VFaceval(FB,rb,tb):
    return FB/((1+rb)**tb)

def VCouponVal(c,i,n):
    ans = 0
    for i in range(0,n):
        ans += (c / ((1+i)**n))
        i += 1
        print(i)
    print("Coupon Payment: ", ans)
    
def Exp_and_Log():
    x = np.linspace(-1, 2, 200)
    y = np.exp(x) # Model build
    plt.figure()
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.show()
    
def Log_Normal(): 
    stddev = 0.0
    mean = 0.4
    dist = log([stddev], loc = mean)
    
    x = np.linspace(0, 6, 200)
    pl.plot(x, dist.pdf(x))
    pl.plot(x, dist.cdf(x))
    
    mu, sigma = 3, 1 # mean and std deviation
    s = np.random.log(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 100, denisty = True, align = "mid")
    x = np.linspace(min(bins), max(bins), 10000)
    pdf = (np.exp(-(np.log(x) - mu)**2)/2*sigma**2)/(x*sigma*np.sqrt(2*np.pi))
    
    plt.plot(x, pdf, linewidth = 2, color = 'r')
    plt.axis('tight')
    plt.show()

def Options():
    # Options payoff modelling
    optype = input("Rnter the option type (C/P): ")
    k = int(input("Enter the exercise price: "))
    s = int(input("Enter the stock price: "))
    
    if optype == "C":
        payoff = max(0, (s-k)) # Make Money when Stock goes Up
    elif optype == "P":
        payoff = max(0, (k-s)) # Make Money when Stock goes Down
    print("Payoff is: ", payoff)
    
def black_scholes():
    pass
    
    
if __name__ == "__main__":
    # Basic Statistics 
    df = pd.read_csv("data.csv")
    df.info()
    df.describe()
    sns.boxplot(x = "Species", y = "PetalLengthCm", data = df)
    
    # Bond Valution
    VFaceval(10000, 0.015, 4)
    VCouponVal(25, 0.015, 4)
    
    # Exp and Log Function
    Exp_and_Log()
    
    # Lognormal Distributions
    Log_Normal()
    
    # Options Payoff
    Options()
    
    # Black Scholes Model
    black_scholes()
