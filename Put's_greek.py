import datetime as dt
import numpy as np
import pandas_datareader.data as web
import scipy.stats
import math


strike = 25
Price = 24.629
T=39/360
volatility = 0.2857
risk_free=0.0068  #tasso decennale dei titoli di stato statunitensi


#GREEKS:

def Delta_Put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Delta = scipy.stats.norm.cdf(d1)-1
    return Delta

print("Delta Put 25:", Delta_Put(Price, T, volatility,25, risk_free))
print("Delta Put 30:", Delta_Put(Price, T, volatility,30, risk_free))
Delta_Str = -2*float(Delta_Put(Price, T, volatility,25, risk_free))+float(Delta_Put(Price, T, volatility,30, risk_free))
print("Delta strategia ", Delta_Str)

def Gamma_Put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    phi = (np.exp((-d1**2)/2)/(np.sqrt(2*math.pi)))
    Gamma = (phi)/(Price*volatility*np.sqrt(T))
    return Gamma
Gamma_str=-2*Gamma_Put(Price, T, volatility, 25, risk_free)+Gamma_Put(Price, T, volatility, 30, risk_free)
print("Gamma strategia ", Gamma_str)


def Theta_Put (Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    d2 = ((np.log(Price / strike)) + (risk_free - ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    phi = (np.exp((-d1**2)/2)/(np.sqrt(2*math.pi)))
    Nd2 =scipy.stats.norm.cdf(-d2)
    Theta = -((Price*phi*volatility)/(2*np.sqrt(T)))+(risk_free*strike*np.exp(-risk_free*T)*Nd2)
    return Theta
Theta_str= -2*Theta_Put (Price, T, volatility, 25, risk_free)+Theta_Put (Price, T, volatility, 30, risk_free)
print("Theta strategia ", Theta_str)

def Vega_put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Nd1 = (np.exp((-d1**2)/2))/(np.sqrt(2*np.pi))
    Vega = Price*np.sqrt(T)*Nd1
    return Vega
Vega_str = -2*Vega_put(Price, T, volatility, 25, risk_free)+ Vega_put(Price, T, volatility, 30, risk_free)
print("Vega strategia ", Vega_str)

def Rho_put(Price, T, volatility, strike, risk_free):
    d1 = ((np.log(Price / strike)) + (risk_free + ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    d2 = ((np.log(Price / strike)) + (risk_free - ((volatility ** 2) / 2)) * T) / (volatility * np.sqrt(T))
    Rho = Rho = (-strike*T*np.exp(-risk_free*T))*scipy.stats.norm.cdf(-d2)
    return Rho
Rho_str = -2*Rho_put(Price, T, volatility,25, risk_free)+Rho_put(Price, T, volatility, 30, risk_free)
print("Rho strategia ", Rho_str)

