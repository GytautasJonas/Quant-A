import math

from scipy.stats import norm

def Call(S,K,r,t,sigma):
    sigma=sigma/100
    d1=(math.log(S/K)+(r+sigma**2/2)*t)/(sigma*math.sqrt(t))
    d2=(math.log(S/K)+(r-sigma**2/2)*t)/(sigma*math.sqrt(t))
    return (S*(norm.cdf(d1))-(K*math.exp(-r*t)*(norm.cdf(d2))))

def Put(S,K,r,t,sigma):
    sigma=sigma/100
    d1=(math.log(S/K)+(r+sigma**2/2)*t)/(sigma*math.sqrt(t))
    d2=(math.log(S/K)+(r-sigma**2/2)*t)/(sigma*math.sqrt(t))
    return ((K*math.exp(-r*t)*(norm.cdf(d2)))-S*(norm.cdf(d1))) 