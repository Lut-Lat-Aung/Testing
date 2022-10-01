# Assume the data have different degree of freedom values as 5, 50, 500 and 5000

# (a)Construct 0.975 quantile for the given degree of freedom values
# (b)Construct cumulative probabilities for the given degree of freedom values

import numpy as np
df= np.array([5, 50, 500, 5000])
from scipy.stats import t

## construct 0.975 quantile
print(t.ppf(0.975, df))

## construct cumulative probabilities
print(t.cdf(1.96043855, df))

import numpy as np
from scipy.stats import t
from scipy.stats import norm
from matplotlib import pyplot as plt
import statsmodels.api as sm
import pylab as py
fig, ax = plt.subplots()
df=np.array([5, 50, 500, 5000]) # degrees of freedom
y = np.linspace(-4,4, 100)
def t_pdfs(): # function that creates plot as in Figure 4.5
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    for i in range(4):
        ax.plot(y, t.pdf(y, df[i]), lw=2)
    ax.plot(y, norm.pdf(y), lw=2, linestyle='dashed')
    ax.legend(['df=5','df=50','df=500','df=500','normal'],loc='upper right')
t_pdfs()#run the function
plt.xlabel("y")
plt.ylabel("Probability density function")
plt.show()


