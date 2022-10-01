# Anorexia Case:
# The doctor would like to analyze weight changes of anorexia girls who are undergoing a cognitive behavioral therapy.
# Use anorexia.dat to solve each problem:

# (a)Compute for the first therapy (cb) the mean and standard deviation of changes (differences between before and after)

# (b)Refer to last question, compute 95% confidence interval of mean difference

# (c)Compute 95% confidence interval between the difference of the first therapy and the control group in the experimental study

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

patient= pd.read_csv(r"/Users/kaunghtetoo/Desktop/Anorexia.dat", sep= '\s+')
print(patient.head(3))
diff = patient['after'] -patient['before'];
patient['diff'] = diff
print(patient.loc[patient['therapy'] == 'cb']['diff'].describe())

diffCB= patient.loc[patient['therapy'] == 'cb']['diff']
import statsmodels.stats.api as sms

# conduct 95% confidence mean change
print(sms.DescrStatsW(diffCB).tconfint_mean())

#conduct 99% confidence mean change
print(sms.DescrStatsW(diffCB).tconfint_mean(alpha = 0.01))

