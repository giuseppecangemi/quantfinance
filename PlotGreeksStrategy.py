import numpy as np
import scipy.stats
import math
import matplotlib.pyplot as plt


T= 39/360
volatility = 0.28
risk_free =0.0068

def Put_price(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    d2 = ((np.log(Price / strike)) + (risk_free - ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    return ((strike * math.exp(-T * risk_free) * scipy.stats.norm.cdf(d2)-Price * scipy.stats.norm.cdf(d1)))

Price = np.arange(5,70)


fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
plt.xlabel("Stock price")
plt.ylabel("Delta strategia")


def Delta_Put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Delta = scipy.stats.norm.cdf(d1)-1
    return Delta

Delta_Str = -2*(Delta_Put(Price, T, volatility,25, risk_free))+(Delta_Put(Price, T, volatility,30, risk_free))
#print("Delta strategia", Delta_Str)
plt.plot(Price,Delta_Str)
plt.show()

fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
plt.xlabel("Stock price")
plt.ylabel("Gamma strategia")

def Gamma_Put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    phi = (np.exp((-d1**2)/2)/(np.sqrt(2*math.pi)))
    Gamma = (phi)/(Price*volatility*np.sqrt(T))
    return Gamma
Gamma_str=-2*Gamma_Put(Price, T, volatility, 25, risk_free)+Gamma_Put(Price, T, volatility, 30, risk_free)
#print("Gamma strategia", Gamma_str)
plt.plot(Price,Gamma_str)
plt.show()

fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
plt.xlabel("Stock price")
plt.ylabel("Theta strategia")

def Theta_Put (Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    d2 = ((np.log(Price / strike)) + (risk_free - ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    phi = (np.exp((-d1**2)/2)/(np.sqrt(2*math.pi)))
    Nd2 =scipy.stats.norm.cdf(-d2)
    Theta = -((Price*phi*volatility)/(2*np.sqrt(T)))+(risk_free*strike*np.exp(-risk_free*T)*Nd2)
    return Theta
Theta_str= -2*Theta_Put (Price, T, volatility, 25, risk_free)+Theta_Put (Price, T, volatility, 30, risk_free)
#print("Theta strategia", Theta_str)
plt.plot(Price,Theta_str)
plt.show()

fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
plt.xlabel("Stock price")
plt.ylabel("Vega strategia")

def Vega_put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Nd1 = (np.exp((-d1**2)/2))/(np.sqrt(2*np.pi))
    Vega = Price*np.sqrt(T)*Nd1
    return Vega
Vega_str = -2*Vega_put(Price, T, volatility, 25, risk_free)+ Vega_put(Price, T, volatility, 30, risk_free)
#print("Vega strategia", Vega_str)
plt.plot(Price,Vega_str)
plt.show()


fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
plt.xlabel("Stock price")
plt.ylabel("Rho strategia")

def Rho_put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Rho = T*Price*np.exp(-risk_free*T)*scipy.stats.norm.cdf(-d1)
    return Rho
Rho_str = -2*Rho_put(Price, T, volatility,25, risk_free)+Rho_put(Price, T, volatility, 30, risk_free)
#print("Rho strategia", Rho_str)
plt.plot(Price,Rho_str)
plt.show()
