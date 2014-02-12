import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean,log,exp
from sklearn import linear_model

mammals = pd.read_csv('../../../data/mammals.csv')
mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])
regr = linear_model.LinearRegression()
regr2 = linear_model.LinearRegression()
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)

print 'regr.coef_ ' + str(regr.coef_)     #0.96649637
print 'regr.intercept_ ' + str(regr.intercept_) #91.0043962074
print 'mean((regr.predict(body) - brain) ** 2) ' + str(mean((regr.predict(body) - brain) ** 2))  #108423.210573
print 'regr.score(body, brain) ' + str(regr.score(body, brain))   #0.872662084304

log_body = [[x] for x in mammals['log_body'].values]
log_brain = mammals['log_brain'].values
regr2.fit(log_body, log_brain)

print 'regr2.coef_ ' + str(regr2.coef_)     #0.75168594
print 'regr2.intercept_ ' + str(regr2.intercept_) #2.13478867676
print 'mean((regr2.predict(log_body) - log_brain) ** 2) ' + str(mean((regr2.predict(log_body) - log_brain) ** 2))  #0.46649532937839744
print 'regr2.score(log_body, log_brain) ' + str(regr2.score(body, log_brain))   #0.92078371690272565

plt.scatter(body, brain)
plt.plot(body, regr.predict(body), color='blue', linewidth=3)

plt.scatter(log_body, log_brain)

plt.plot(body, regr.predict(body),exp(log_body),exp(regr2.predict(log_body)), color='red')
