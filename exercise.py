import numpy as np
import pandas as pd
import tools_test as tt
import matplotlib.pyplot as plt

# Logic

def check_uniqueness(lst):
    """
    Check if a list contains only unique values.
    Returns True only if all values in the list are unique, False otherwise
    """
    # Compare the length of the list with and without duplicates
    isUnique = len(set(lst)) == len(lst)
    return isUnique

def smallest_difference(array):
    """
    Code a function that takes an array and returns the smallest
    absolute difference between two elements of this array
    Please note that the array can be large and that the more
    computationally efficient the better
    """
    # Initialize min_diff
    min_diff = float('inf')
    
    # Compare each difference, except itself and retunr the lowest
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and abs(array[i] - array[j]) < min_diff:
                min_diff = abs(array[i] - array[j])      
    return min_diff


# Finance and DataFrame manipulation

data = pd.read_csv('data/data.csv', header=0, index_col=0, parse_dates=True)
output_exp = pd.read_csv('data/output.csv', header=0, index_col=0)

def macd(prices, window_short=12, window_long=26):
    """
    Code a function that takes a DataFrame named prices and
    returns it's MACD (Moving Average Convergence Difference) as
    a DataFrame with same shape
    Assume simple moving average rather than exponential moving average
    The expected output is in the output.csv file
    """
    # Check if prices is a dataframe
    if isinstance(prices, pd.DataFrame):
        prices["MACD"] = prices.iloc[:,0].rolling(window_short).mean() \
        - prices.iloc[:,0].rolling(window_long).mean()
    else:
        print(f'{prices} is not a dataframe')
    return prices

def sortino_ratio(prices):
    """
    Code a function that takes a DataFrame named prices and
    returns the Sortino ratio for each column
    Assume risk-free rate = 0
    On the given test set, it should yield 0.05457
    """
    # Calculate returns
    returns = (prices / prices.shift(1) -1).dropna()
    
    # Calculate annualised returns and semi deviation
    portfolio_returns = tt.compute_annualized_returns(returns)
    semi_deviation = tt.compute_semideviation(returns)
    return portfolio_returns / semi_deviation

def expected_shortfall(prices, level=0.95):
    """
    Code a function that takes a DataFrame named prices and
    returns the expected shortfall at a given level
    On the given test set, it should yield -0.03468
    """
    # Calulate returns 
    returns = (prices / prices.shift(1) -1).dropna()
    
    # Calculate historic VaR
    VaR = -np.percentile(prices, (1 - level)*100, axis=0)
    
    # Calculate average returns beyond VaR
    returns_beyond = returns < -VaR
    mean_beyond = -returns[returns_beyond].mean()
    return mean_beyond

# Plot

def visualize(prices, path):
    """
    Code a function that takes a DataFrame named prices and
    saves the plot to the given path
    """
    
    plt.plot(prices)
    plt.set_title("Price Plot")
    plt.set_xlabel("Date")
    plt.set_ylabel("Price")
    
    plt.savefig('plot.png')
    return print("Le graphique a été sauvegardé")


