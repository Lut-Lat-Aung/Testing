import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Anor = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
Anor.head(3)
change = Anor['after'] - Anor['before']
Anor['change'] = change # add new variable to the data frame
Anor.loc[Anor['therapy'] == 'cb']['change'].describe()
# showing only n and mean and standard deviation of change
bins=list(range(-10,30,5)) # histogram with pre-specified bins:
plt.hist(Anor.loc[Anor['therapy']=='cb']['change'],bins, edgecolor='k')
plt.xlabel('Weight change'); plt.ylabel('Frequency')
changeCB = Anor.loc[Anor['therapy'] == 'cb']['change']
import statsmodels.stats.api as sms
sms.DescrStatsW(changeCB).tconfint_mean() # default alpha=0.05
plt.show()
