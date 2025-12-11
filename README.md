# Implied Volatility and the Volatility Smile

A numerical study of implied volatility inversion and the construction of a synthetic volatility smile. The project examines how the Black-Scholes pricing map behaves as a function of volatility and how a stable numerical routine can recover strike–dependent volatilities from option prices.

The notebook implements:
- Black-Scholes pricing and Vega
- an objective function for the inversion problem
- a hybrid Newton–bisection solver for implied volatility
- construction of a smooth synthetic smile
- comparison between true and recovered implied volatilities

The workflow mirrors practical calibration tasks: define the forward pricing map, compute its sensitivity, and apply a robust inversion routine across strikes.

## Results and findings

- The Black-Scholes price and Vega behave as expected: the price decreases with strike, and Vega peaks near the money and decays in the wings.
- The Newton-bisection solver is numerically stable. Convergence tests show rapid decay of the pricing error once the iterate enters a region where Vega is sufficiently large.
- A synthetic smile $\sigma_{\text{true}}(K)$ is used to generate market-consistent prices.  
  The inversion routine recovers the smile to numerical precision across the full strike range.
- The experiment illustrates how even a simple volatility function produces the characteristic curvature of a smile, and highlights the role of model monotonicity in ensuring successful inversion.

The project provides a compact example of how implied volatilities are computed in practice and how numerical behaviour interacts with the geometry of the volatility surface.

## Contents

- `notebook.ipynb` - main analysis and plots  
- `notebook.pdf` - static export  
- `src/` - pricing functions and the implied volatility solver  
- `figs/` - generated figures  
