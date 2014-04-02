import csv
import numpy as np
import pandas as pd
from dateutil import parser
import pylab as pl
import statsmodels.api as sm
import matplotlib.pyplot as plt
import random
from sklearn.preprocessing import scale
from numpy import inf
import scipy.stats as stats
import pylab

### IMPORT DATA ###

data = pd.read_csv("./baseball.csv")

### DROP UNWANTED/UNNECESSARY VARIABELS ###

slimdata = data.drop(['playerID', 'lahmanID', 'managerID', 'birthYear', 'birthMonth', 'birthDay', 
    'birthCountry', 'birthState', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 
    'deathState', 'deathCity', 'nameFirst','nameLast', 'nameNote', 'nameGiven', 'nameNick','bats', 
    'throws', 'debut', 'finalGame', 'college','lahman40ID', 'lahman45ID', 'retroID', 'holtzID', 
    'bbrefID', 'deathDate', 'birthDate','teamID', 'lgID', 'stint','G_batting','X2B', 'X3B',
    'CS', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP', 'G_old', 'hofID', 'yearID','salary'], axis =1)

slimdata = slimdata.dropna() # DROPS OBSERVATIONS WITH MISSING DATA

# SHRINKING THE DATA ONLY TO MAKE VISUALIZATIONS EASIER #

slimdata['random'] = np.random.randn(len(slimdata))
slimdata = slimdata[slimdata.random > 1]
slimdata = slimdata.drop(['random'], axis = 1)

# COLLINEARITY HISTOGRAM #
pd.tools.plotting.scatter_matrix(slimdata, alpha=0.2, diagonal='hist')
plt.show()

# LOG TRANSFORMATIONS WHERE NECESSARY #
slimdata.AB = np.log(slimdata.AB)
slimdata.SB = np.log(slimdata.SB)
slimdata.HR = np.log(slimdata.HR)
slimdata.H = np.log(slimdata.H)
slimdata.BB = np.log(slimdata.BB)
slimdata.G = np.log(slimdata.G)
slimdata.RBI = np.log(slimdata.RBI)
slimdata.salary = np.log(slimdata.salary)
slimdata = slimdata.replace([inf, -inf], np.nan)
slimdata = slimdata.dropna()

### PLOTTING SCATTERPLOT MATRIX FOR COLLINEARITY ###

# HISTOGRAM #
pd.tools.plotting.scatter_matrix(slimdata, alpha=0.2, diagonal='hist')
plt.show()

# KERNEL DENSITY #
pd.tools.plotting.scatter_matrix(slimdata, alpha=0.2, diagonal='kde')
plt.show()

### DEFINING IVs & DVs ###

X = np.array(slimdata.drop(['salary'], axis = 1))
y = np.array(slimdata['salary'])

### RUNNING REGRESSION MDOEL ###

model = sm.OLS(y, X)
results = model.fit()
print results.summary()

### NORMALIZATION ###

# BOX PLOT FOR OUTLIERS #

slimdata.boxplot()
plt.show()
slimdata.drop(['salary'], axis = 1).boxplot()
plt.show()

# SCALING # Mean-center then divide by std dev

data_norm = pd.DataFrame(scale(slimdata), index=slimdata.index, columns=slimdata.columns)
data_norm.boxplot()
plt.show()

### RUNNING REGRESSION MDOEL AGAIN ###

X = np.array(data_norm.drop(['salary'], axis = 1))
y = np.array(data_norm['salary'])

model2 = sm.OLS(y, X)
results2 = model2.fit()
print results2.summary()

### INFLUENCE PLOT ###

influence = results2.get_influence()
#c is the distance and p is p-value
(d, p) = influence.cooks_distance
plt.stem(np.arange(len(d)), d, markerfmt=",")
plt.show()


### RESIDUALS VS FITTED PLOT ###

plt.scatter(results.norm_resid(), results.fittedvalues)
plt.xlabel('Fitted Values')
plt.ylabel('Normalized residuals')

### QQ PLOT ###

stats.probplot(data_norm.height, dist="norm", plot=pylab)
pylab.show()

# THE EFFECT OF RESHAPING/DROPPING VARIABLES #
res_dropped = results.params / results2.params * 100 - 100