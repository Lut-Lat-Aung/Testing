# Income case:
# The recruiter company would like to know the difference between income with race and education.
# Then they decide to randomly collect the data from private employees. Use income.dat to perform the following problem:

# (a)Generate the ANOVA table and the Tukey comparisons of the difference for three type of therapy
# (b)Generate the corresponding ANOVA table

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

income = pd.read_csv("L:\School Work\Statistics", sep= '\s+')
print(income.head(1))
fit = smf.ols(formula = 'income ~ C(race)', data = income).fit()
print(fit.summary())
sm.stats.anova_lm(fit)

# Perform Tukey
import statsmodels.stats.multicomp as mc
comp = mc.MultiComparison(income['income'], income['race'])
post_hoc_res= comp.tukeyhsd()
print(post_hoc_res.summary())

post_hoc_res.plot_simultaneous(ylabel= 'race', xlabel= 'mean income difference')
fit2 = smf.ols(formula = 'income ~ C(race) + education', data = income).fit()

print(fit2.summary())
sm.stats.anova_lm(fit2, typ=2)
