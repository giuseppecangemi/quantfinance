#Black&Scholes

import numpy as np
from scipy.stats import norm 
from numpy import mean, sqrt, square, exp, log
import datetime as dt

S=24.629
T=39/360
rf=.0068
sigma=0.2857057186685205
#Higher Long PUT

K=30
def blackscholes_put_long(S,K,T,rf,sigma):
    d1=(log(S/K)+(rf+sigma*sigma/2.0)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return K*exp(-rf*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
 
Put_long_bs=blackscholes_put_long(S, K, T, rf, sigma)

print("prezzo Higher_Long_Put by Black&Scholes", blackscholes_put_long(S, K, T, rf, sigma))

#Lower short PUT

K=25
def blackscholes_put_short(S,K,T,rf,sigma):
    d1=(log(S/K)+(rf+sigma*sigma/2.0)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return K*exp(-rf*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
    
Put_short_bs=blackscholes_put_short(S, K, T, rf, sigma)

print("prezzo Lower_Short_Put by Black&Scholes", blackscholes_put_short(S, K, T, rf, sigma))

#Modello di Black

#Higher Long PUT
S=24.629 # Valore del sottostante
K=30     # Prezzo di esercizio
T=39/360 # Intervallo temporale in anni
rf=.0068 # Tasso risk-free
sigma=0.2857057186685205 #Volatilità storica


def black_put_long(S,K,T,rf,sigma):
    d1=(log(S/K)+((sigma*sigma/2.0)*T))/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return exp(-rf*T)*(K*norm.cdf(-d2)-S*norm.cdf(-d1))
    
Put_long_b=black_put_long(S,K,T,rf,sigma)

print("Prezzo Higher_Long_Put by Black", black_put_long(S,K,T,rf,sigma))

#Lower short PUT
S=24.629
K=25
T=39/360
rf=.0068
sigma=0.2857057186685205


def black_put_short(S,K,T,rf,sigma):
    d1=(log(S/K)+((sigma*sigma/2.0)*T))/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return exp(-rf*T)*(K*norm.cdf(-d2)-S*norm.cdf(-d1))

Put_short_b=black_put_short(S,K,T,rf,sigma)

print("prezzo Lower_Short_Put by Black", black_put_short(S,K,T,rf,sigma))

Discrepancy_long_put = Put_long_b-Put_long_bs
Discrepancy_short_put = Put_short_b-Put_short_bs

print("Discrepancy_long_put",Discrepancy_long_put)
print("Discrepancy_short_put",Discrepancy_short_put)
