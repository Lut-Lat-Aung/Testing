# B.5.2 Chi-Squared Tests Comparing Multiple Proportions in Contin-gency Tables

import numpy as np
import pandas as pd
import matplotlib as plt
Happy = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Happy.dat', sep='\s+')
rowlabel=['Married', 'Divorced/Separated', 'Never married']
collabel=['Very happy', 'Pretty happy', 'Not too happy']
table = pd.crosstab(Happy['marital'], Happy['happiness'], margins = False)
table.index=rowlabel
table.columns=collabel
table # output not shown
# conditional distributions on happiness (proportions within rows):

proptable = pd.crosstab(Happy['marital'], Happy['happiness'], normalize='index')

proptable.index=rowlabel
proptable.columns=collabel
proptable # output not shown

import statsmodels.api as sm # expected frequencies under H0: independence
table = sm.stats.Table(table)
print(table.fittedvalues) # output not shown

X2 = table.test_nominal_association() # chi-squared test of independence
print(X2)

table.standardized_resids # standardized residuals (not shown)
Happy.loc[Happy['happiness'] == 1, 'happiness'] = 'Very'
Happy.loc[Happy['happiness'] == 2, 'happiness'] = 'Pretty'
Happy.loc[Happy['happiness'] == 3, 'happiness'] = 'Not too'
Happy.loc[Happy['marital'] == 1, 'marital'] = 'Married'
Happy.loc[Happy['marital'] == 2, 'marital'] = 'Div/Sep'
Happy.loc[Happy['marital'] == 3, 'marital'] = 'Never'

from statsmodels.graphics.mosaicplot import mosaic
fig, _ = mosaic(Happy, ['marital','happiness'], statistic=True)
