import pandas as pd
from scipy.stats import chi2_contingency

import seaborn as sns
import matplotlib.pyplot as plt

INSPECT = True  # flip to True to see outputs

df = pd.DataFrame({
    'Gender': ['M', 'M', 'M', 'F', 'F', ] * 10,
    'isSmoker': ['Smoker', 'Smoker', 'Non-Smoker', 'Non-Smoker', 'Smoker'] * 10
})

if INSPECT:
    print(df.head())

# convert data to contingency table
contingency = pd.crosstab(df['Gender'], df['isSmoker'])

if INSPECT:
    print(contingency)

# get percentages by gender
# normalize='columns' -> percentages by column
# normalize='all'     -> total percentage
contingency_pct = pd.crosstab(df['Gender'], df['isSmoker'], normalize='index')

if INSPECT:
    print(contingency_pct)

plt.figure(figsize=(12, 8))
sns.heatmap(contingency, annot=True, cmap='YlGnBu')

# chi-square test of independence
c, p, dof, expected = chi2_contingency(contingency)

if INSPECT:
    # print the p-value
    print(p)

# The p-value is 37.67% -> we do not reject the null hypothesis at 95% level of confidence
# The null hypothesis was that `Smokers` and `Gender` are independent
# The contingency table was 2×2, we could have applied z-test for proportions instead of chi-square test
# Chi-square test can be extended to m×n contingency tables

