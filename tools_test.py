import numpy as np
import pandas as pd

def compute_annualized_returns(returns, annual_frequency = 252):
    """
    Compute annualized returns
    """
    n_period = len(returns)
    annualized_returns = (returns +1).prod()**(annual_frequency/n_period) -1
    return annualized_returns

def compute_semideviation(returns, annual_frequency = 252):
    """
    Compute semi deviation
    """
    semi_std = returns[returns < returns.mean()].std(ddof=0) *np.sqrt(annual_frequency)
    return semi_std