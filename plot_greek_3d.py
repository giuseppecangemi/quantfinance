import numpy as np
import scipy.stats
import math
import matplotlib.pyplot as plt
from matplotlib import cm



volatility = 0.28
risk_free =0.0068
Price = np.linspace(5,70)
T = np.linspace(1,39/360)

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')
plt.xlabel("Prezzo sottostante")
plt.ylabel("Tempo a scadenza")
ax.set_zlabel("Delta")

T, Price =np.meshgrid(T,Price)

strike = 25
def Delta_Put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Delta = scipy.stats.norm.cdf(d1)-1
    return Delta

Delta_Str = -2*(Delta_Put(Price, T, volatility,25, risk_free))+(Delta_Put(Price, T, volatility,30, risk_free))
ax.plot_surface(X=Price,Y=T,Z=Delta_Str)
plt.show()

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')
plt.xlabel("Prezzo sottostante")
plt.ylabel("Tempo a scadenza")
ax.set_zlabel("Gamma")

T, Price =np.meshgrid(T,Price)
def Gamma_Put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    phi = (np.exp((-d1**2)/2)/(np.sqrt(2*math.pi)))
    Gamma = (phi)/(Price*volatility*np.sqrt(T))
    return Gamma
Gamma_str=-2*Gamma_Put(Price, T, volatility, 25, risk_free)+Gamma_Put(Price, T, volatility, 30, risk_free)
surf = ax.plot_surface(X=Price,Y=T,Z=Gamma_str,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')
plt.xlabel("Prezzo sottostante")
plt.ylabel("Tempo a scadenza")
ax.set_zlabel("Theta")

def Theta_Put (Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    d2 = ((np.log(Price / strike)) + (risk_free - ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    phi = (np.exp((-d1**2)/2)/(np.sqrt(2*math.pi)))
    Nd2 =scipy.stats.norm.cdf(-d2)
    Theta = -((Price*phi*volatility)/(2*np.sqrt(T)))+(risk_free*strike*np.exp(-risk_free*T)*Nd2)
    return Theta
Theta_str= -2*Theta_Put (Price, T, volatility, 25, risk_free)+Theta_Put (Price, T, volatility, 30, risk_free)
surf = ax.plot_surface(X=Price,Y=T,Z=Theta_str,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')
plt.xlabel("Prezzo sottostante")
plt.ylabel("Tempo a scadenza")
ax.set_zlabel("Vega")

def Vega_put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Nd1 = (np.exp((-d1**2)/2))/(np.sqrt(2*np.pi))
    Vega = Price*np.sqrt(T)*Nd1
    return Vega
Vega_str = -2*Vega_put(Price, T, volatility, 25, risk_free)+ Vega_put(Price, T, volatility, 30, risk_free)
surf = ax.plot_surface(X=Price,Y=T,Z=Vega_str,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')
plt.xlabel("Prezzo sottostante")
plt.ylabel("Tempo a scadenza")
ax.set_zlabel("Rho")

def Rho_put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Rho = T*Price*np.exp(-risk_free*T)*scipy.stats.norm.cdf(-d1)
    return Rho
Rho_str = -2*Rho_put(Price, T, volatility,25, risk_free)+Rho_put(Price, T, volatility, 30, risk_free)
surf = ax.plot_surface(X=Price,Y=T,Z=Rho_str,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
