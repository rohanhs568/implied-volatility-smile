def implied_vol_newton_bisection(C_mkt, S0, K, r, T,
                                 sigma_min=0.01, sigma_max=3.0,
                                 tol=1e-8, max_iter=100):
    """
    Hybrid Newton–bisection solver for implied volatility.
    """
    f_min = objective_sigma(sigma_min, S0, K, r, T, C_mkt)
    f_max = objective_sigma(sigma_max, S0, K, r, T, C_mkt)

    # ensure the bracket contains a root
    if f_min * f_max > 0:
        return np.nan

    sigma = 0.5 * (sigma_min + sigma_max)

    for _ in range(max_iter):
        f_val = objective_sigma(sigma, S0, K, r, T, C_mkt)
        if abs(f_val) < tol:
            return sigma

        vega = bs_vega(S0, K, r, sigma, T)
        newton_ok = (vega > 1e-8)

        if newton_ok:
            sigma_new = sigma - f_val / vega
            if sigma_min < sigma_new < sigma_max:
                sigma = sigma_new
            else:
                sigma = 0.5 * (sigma_min + sigma_max)
        else:
            sigma = 0.5 * (sigma_min + sigma_max)

        # update bracket
        f_new = objective_sigma(sigma, S0, K, r, T, C_mkt)
        if f_min * f_new <= 0:
            sigma_max = sigma
            f_max = f_new
        else:
            sigma_min = sigma
            f_min = f_new

    return sigma
