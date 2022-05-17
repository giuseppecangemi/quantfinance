```python

#PUT SPREAD RATIO

import numpy as np
import matplotlib.pyplot as plt


def Put_PeL (strike_price, premium, sT):
  return np.where(sT<strike_price, strike_price-sT,0)-premium

S0 = 24.629
# Long PUT
strike_long_put = 30
premium_long_put = 5.3658840165872235

# Short PUT
strike_short_put = 25
premium_short_put = 1.117133125644612
sT = np.arange(1,60)

# Higher Strike Long Put Payoff
Long_put_pel = Put_PeL(strike_long_put, premium_long_put, sT)
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT, Long_put_pel, color='g')
ax.set_title('Strike Long Put')
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
plt.show()

# Short PUT Payoff
Short_put_pel = Put_PeL(strike_short_put, premium_short_put, sT)*-1.0
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT, Short_put_pel, color='r')
ax.set_title('Strike Short Put')
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
plt.show()

#Composizione Put_Spread_Ratio
Put_spread_ratio_pel = Long_put_pel + 2 * Short_put_pel
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,Put_spread_ratio_pel ,color='b', label= 'Put Spread Ratio P&L')
ax.plot(sT,Long_put_pel,'--', color='g', label='Long Put P&L')
ax.plot(sT, Short_put_pel, '--', color='r', label='Short Put P&L')
plt.legend()
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
plt.show()

#Strategia finale Put_Spread_Ratio
Put_spread_ratio_pel = Long_put_pel + 2 * Short_put_pel
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,Put_spread_ratio_pel ,color='b', label= 'Put Spread Ratio P&L')
plt.legend()
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
plt.show()


profit = max(Put_spread_ratio_pel)
loss = min(Put_spread_ratio_pel)
print ("maxP&L Put Spread Ratio:" "%.2f" %profit)
print ("minP&L Put Spread Ratio:" "%.2f" %loss)

```
