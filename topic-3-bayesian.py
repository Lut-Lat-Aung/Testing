# The doctor would like to analyze weight changes of anorexia girls who are undergoing a cognitive behavioral therapy.
# Use anorexia.dat to solve each problem

# (a)Construct 95% confidence interval for the Bayesian population mean change on the first therapy
# (b)Construct 99% confidence interval for the Bayesian population mean change on the third therapy

import numpy as np
import pandas as pd
from scipy.stats import t

Anor= pd.read_csv(r"/Users/kaunghtetoo/Desktop/Anorexia.dat", sep= '\s+')
diff = Anor['after'] -Anor['before'];
Anor['diff'] = diff
first = Anor.loc[Anor['therapy'] == 'cb']['diff']
m1 = first.mean();
n1 = len(first);
s1 = first.std()
first_posterior = t(loc = m1 , scale = s1/np.sqrt(n1), df= n1-1)
first_posterior.interval(0.95)

import numpy as np
import pandas as pd
from scipy.stats import t

Anor = pd.read_csv(r"/Users/kaunghtetoo/Desktop/Anorexia.dat", sep = '\s+')
diff = Anor['after'] - Anor['before']
Anor['diff'] = diff
third = Anor.loc[Anor['therapy'] == 'c']['diff']
m3 = third.mean(); n3 = len(third); s3 = third.std()
third_posterior = t(loc = m3, scale = s3/np.sqrt(n3), df = n3-1)
third_posterior.interval(0.99)

