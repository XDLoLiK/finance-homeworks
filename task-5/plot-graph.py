import matplotlib.pyplot as plt
import numpy as np

S0 = 100
T = 0.5
N = 6
r = 0.05
sigma = 0.2

dt = T / N
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp(r * dt) - d) / (u - d)

K_values = [80, 90, 100, 110, 120]


def american_option(S0, K, r, T, N, u, d, p, option_type="call"):
    dt = T / N
    discount = np.exp(-r * dt)

    prices = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            prices[j, i] = S0 * (u ** (i - j)) * (d**j)

    option = np.zeros((N + 1, N + 1))
    for j in range(N + 1):
        if option_type == "call":
            option[j, N] = max(prices[j, N] - K, 0)
        else:
            option[j, N] = max(K - prices[j, N], 0)

    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            continuation = discount * (
                p * option[j, i + 1] + (1 - p) * option[j + 1, i + 1]
            )

            if option_type == "call":
                exercise = max(prices[j, i] - K, 0)
            else:
                exercise = max(K - prices[j, i], 0)

            option[j, i] = max(continuation, exercise)

    return option[0, 0]


call_prices = []
put_prices = []

for K in K_values:
    call_prices.append(american_option(S0, K, r, T, N, u, d, p, "call"))
    put_prices.append(american_option(S0, K, r, T, N, u, d, p, "put"))

plt.figure()
plt.plot(K_values, call_prices, marker="o")
plt.xlabel("Strike (K)")
plt.ylabel("Option Price")
plt.title("Call Option Price vs Strike")
plt.grid()
plt.savefig("img/call.png")

plt.figure()
plt.plot(K_values, put_prices, marker="o")
plt.xlabel("Strike (K)")
plt.ylabel("Option Price")
plt.title("Put Option Price vs Strike")
plt.grid()
plt.savefig("img/put.png")
