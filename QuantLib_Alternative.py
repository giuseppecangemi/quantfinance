#Calcolo alternativo dei prezzi delle opzioni con Quantlib con confronto tra pricing di Black-Scholes e di Black

from QuantLib import *

#pricing delle opzioni put europee con Black-Scholes (1973)

today = Date(9, May, 2020)
expiration = Date(20, June, 2020)
if expiration.weekday() == Saturday:
    expiration= expiration + 2
elif expiration.weekday() == Sunday:
    expiration = expiration + 1

Settings.instance().evaluationDate = today
short_strike = 25.0
option_put = EuropeanOption(PlainVanillaPayoff(Option.Put, short_strike), EuropeanExercise(expiration))

u = SimpleQuote(24.629)  # prezzo del sottostante
r = SimpleQuote(0.0068)  # risk free
sigma = SimpleQuote(0.2857)  # volatilità

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve),BlackVolTermStructureHandle(volatility))
engine = AnalyticEuropeanEngine(process)
option_put.setPricingEngine(engine)

short_put = option_put.NPV()
delta_short = option_put.delta()
gamma_short = option_put.gamma()
vega_short = option_put.vega()
theta_short = option_put.theta()
rho_short = option_put.rho()
print("Premio short put:    ",short_put)
print("Delta short put:     ", delta_short)
print("Gamma short put:     ", gamma_short)
print("Vega short put:      ", vega_short)
print("Theta short put:     ", theta_short)
print("Rho short put:       ", rho_short)

strike_long = 30.0
option_put = EuropeanOption(PlainVanillaPayoff(Option.Put, strike_long), EuropeanExercise(expiration))

u = SimpleQuote(24.629)
r = SimpleQuote(0.0068)
sigma = SimpleQuote(0.2857)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u),YieldTermStructureHandle(riskFreeCurve), BlackVolTermStructureHandle(volatility))
engine = AnalyticEuropeanEngine(process)

option_put.setPricingEngine(engine)
long_put = option_put.NPV()
delta_long = option_put.delta()
gamma_long = option_put.gamma()
vega_long = option_put.vega()
theta_long = option_put.theta()
rho_long = option_put.rho()
print("Premio long put:     ", long_put)
print("Delta long put:      ", delta_long)
print("Gamma long put:      ", gamma_long)
print("Vega long put:       ", vega_long)
print("Theta long put:      ", theta_long)
print("Rho long put:        ", rho_long)

premio_str = -2*short_put+long_put
delta_strt = -2 * delta_short + delta_long
gamma_strt = -2 * gamma_short + gamma_long
vega_strt = -2 * vega_short + vega_long
theta_strt = -2 * theta_short + theta_long
rho_strt = -2 * rho_short + rho_long
print("Premio strategia:    ", premio_str)
print("Delta strategia:     ", delta_strt)
print("Gamma strategia:     ", gamma_strt)
print("Vega strategia:      ", vega_strt)
print("Theta strategia:     ", theta_strt)
print("Rho strategia:       ", rho_strt)

#Pricing delle opzioni put europee con metodo di Black (1976)
u = 24.629
r = 0.0068
sigma = 0.2857

day_count = ActualActual()      #individua la modalitàdi conteggio dei giorni a scadenza secondo laconvenzione ISDA
curva_rend = FlatForward(today,r,day_count,Compounded,Continuous)
Settings.instance().evaluationDate = today
style = Option.Put

fattore_sconto = curva_rend.discount(expiration)
payoff_short = PlainVanillaPayoff(style,short_strike)
t = curva_rend.dayCounter().yearFraction(today,expiration)
dev_std =sigma*(t**(1/2))

black = BlackCalculator(payoff_short,u,dev_std,fattore_sconto)
short_put_bl = black.value()
print("premio short put secondo black:  ",short_put_bl)
delta_short_bl =black.delta(u)
print("Delta short put secondo Black:   ",delta_short_bl)
gamma_short_bl = black.gamma(u)
print("Gamma shortput secondo Black:    ",gamma_short_bl)
theta_short_bl = black.theta(u,t)
print("Theta short put secondo Black:   ",theta_short_bl)
vega_short_bl = black.vega(t)
print("Vega short put secondo Black:    ",vega_short_bl)
rho_short_bl= black.rho(t)
print("Rho short put secondo Black:     ",rho_short_bl)

fattore_sconto = curva_rend.discount(expiration)
payoff_long = PlainVanillaPayoff(style,strike_long)
black = BlackCalculator(payoff_long,u,dev_std,fattore_sconto)

long_put_bl =black.value()
print("premio long put secondo black:   ",long_put_bl)
delta_long_bl = black.delta(u)
print("Delta long put secondo Black:    ",delta_long_bl)
gamma_long_bl = black.gamma(u)
print("Gamma longput secondo Black:     ",gamma_long_bl)
theta_long_bl = black.theta(u,t)
print("Theta long put secondo Black:    ",theta_long_bl)
vega_long_bl = black.vega(t)
print("Vega long put secondo Black:     ",vega_long_bl)
rho_long_bl =black.rho(t)
print("Rho long put secondo Black:      ",rho_long_bl)

premio_str_bl = -2*short_put_bl+long_put_bl
delta_strt_bl = -2 * delta_short_bl + delta_long_bl
gamma_strt_bl = -2 * gamma_short_bl + gamma_long_bl
vega_strt_bl = -2 * vega_short_bl + vega_long_bl
theta_strt_bl = -2 * theta_short + theta_long
rho_strt_bl = -2 * rho_short_bl + rho_long_bl
print("Premio strategia secondo black:   ", premio_str_bl)
print("Delta strategia secondo black:    ", delta_strt_bl)
print("Gamma strategia secondo black:    ", gamma_strt_bl)
print("Vega strategia secondo black:     ", vega_strt_bl)
print("Theta strategia secondo black:    ", theta_strt_bl)
print("Rho strategia secondo black:      ", rho_strt_bl)

#differenza di prezzo e valori delle greche tra i due metodi di pricing

short_put_diff = abs(short_put-short_put_bl)
long_put_diff = abs(long_put-long_put_bl)
premio_str_diff =abs(premio_str-premio_str_bl)

short_delta_diff = abs(delta_short-delta_short_bl)
long_delta_diff = abs(delta_long - delta_short)
str_delta_diff = abs(delta_strt- delta_strt_bl)

short_gamma_diff = abs(gamma_short-gamma_short_bl)
long_gamma_diff = abs(gamma_long-gamma_long_bl)
gamma_str_diff = abs(gamma_strt-gamma_strt_bl)

short_vega_diff = abs(vega_short-vega_short_bl)
long_vega_diff = abs(vega_long-vega_long_bl)
vega_str_diff = abs(vega_strt-vega_strt_bl)

short_theta_diff = abs(theta_short-theta_short_bl)
long_theta_diff = abs(theta_long-theta_long_bl)
theta_str_diff = abs(theta_strt-theta_strt_bl)

short_rho_diff = abs(rho_short-rho_short_bl)
long_rho_diff = abs(rho_long-rho_long_bl)
rho_str_diff =abs(rho_strt-rho_strt_bl)

short_difference = [("premio",short_put_diff),("delta",short_delta_diff),("gamma",short_gamma_diff),
                    ("vega",short_vega_diff),("theta",short_theta_diff), ("rho",short_rho_diff)]
long_difference = [("premio",long_put_diff), ("delta",long_delta_diff),("gamma",long_gamma_diff),
                   ("vega",long_vega_diff),("theta",long_theta_diff),("rho",long_rho_diff)]
str_difference = [("premio",premio_str_diff),("delta",str_delta_diff),("gamma",gamma_str_diff),
                  ("vega",vega_str_diff),("theta",theta_str_diff),("rho",rho_str_diff)]

print ("Differenza per short",*short_difference, sep="\n")
print ("Differenza per long",*long_difference, sep="\n")
print ("Differenza per strategia",*str_difference, sep="\n")
