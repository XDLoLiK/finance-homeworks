import numpy as np
import matplotlib.pyplot as plt
from math import comb

S0 = 100
u = 1.2
d = 0.8
r = 0.05
N = 6

p = (1 + r - d) / (u - d)


def option_price(K, option_type="call"):
    price = 0.0
    for k in range(N + 1):
        ST = S0 * (u**k) * (d ** (N - k))
        prob = comb(N, k) * (p**k) * ((1 - p) ** (N - k))

        if option_type == "call":
            payoff = max(ST - K, 0)
        else:
            payoff = max(K - ST, 0)

        price += prob * payoff

    return price / ((1 + r) ** N)


K_values = np.linspace(50, 150, 50)

call_prices = [option_price(K, "call") for K in K_values]
put_prices = [option_price(K, "put") for K in K_values]

plt.figure()
plt.plot(K_values, call_prices, marker="o")
plt.xlabel("Strike (K)")
plt.ylabel("Option Price")
plt.title("Call Option")
plt.grid()
plt.savefig("img/call.png")

plt.figure()
plt.plot(K_values, put_prices, marker="o")
plt.xlabel("Strike (K)")
plt.ylabel("Option Price")
plt.title("Put Option")
plt.grid()
plt.savefig("img/put.png")
