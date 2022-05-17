```python

#MOTO BROWNIANO PER IL SOTTOSTANTE!!!!!

import numpy as np
from matplotlib import pyplot as plt
import datetime as dt
import pandas_datareader.data as web

start = dt.datetime(2020,4,1) #modificato la data per determinare la volatilità storica in 39 giorni
end = dt.datetime(2020,5,9)

#Volatilità
df = web.DataReader('CL=F','yahoo',start,end)   #cl=f codice del sottostante scelto tramite yahoo finance (Wti)
df['Log Return'] = np.log(df['Adj Close'])- np.log(df['Adj Close'].iloc[0])
sigma = df['Log Return'].std()
Prices = df['Adj Close'].to_list()
S0 = Prices[-1]    #PREZZO A CHIUSURA DEL 9 MAGGIO 2020
print("Prezzo del sottostante:", S0)  
print("Volatilità storica:", sigma)


r = 0.0068 #tasso risk free
T = 39/360 #periodo
N = 100 #numero di steps dentro la simulazione
deltat = T/N 
i = 1000 #numero di simulazioni
discount_factor = np.exp(-r*T) #fattore di sconto

S = np.zeros([i,N]) #distribuzione normale delle simulazioni
t = range(0,N,1) 


for y in range(0,i-1): 
    S[y,0]=S0
    for x in range(0,N-1):
        S[y,x+1] = S[y,x]*(np.exp((r-(sigma**2)/2)*deltat + sigma*deltat*np.random.normal(0,1)))
    plt.plot(t,S[y])

plt.title('Simulazioni %d Steps %d Sigma %.2f r %.4f S0 %.2f' % (i, N, sigma, r, S0))
plt.xlabel('Numero di steps')
plt.ylabel('Prezzo del sottostante')
plt.show()

Prezzo_previsto= np.average(S) #prezzo previsto come media di tutte le simulazioni
print ("Prezzo previsto:", Prezzo_previsto)
Prezzo_previsto 
```
