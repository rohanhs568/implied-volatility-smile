def sigma_true(K, S0):
    """
    Synthetic volatility smile as a simple convex function of moneyness K/S0.
    """
    m = K / S0
    return 0.2 + 0.25 * (m - 1.0)**2

def generate_synthetic_prices(Ks, S0, r, T, vol_function):
    """
    Returns synthetic market prices using a given smile function vol_function(K).
    """
    prices = []
    for K in Ks:
        sigma = vol_function(K, S0)
        prices.append(bs_call_price(S0, K, r, sigma, T))
    return np.array(prices)

def compute_implied_vols(Ks, C_mkt, S0, r, T):
    """
    Computes implied volatilities for a list of strikes and market prices.
    """
    imp = []
    for K, C in zip(Ks, C_mkt):
        imp.append(implied_vol_newton_bisection(C, S0, K, r, T))
    return np.array(imp)
