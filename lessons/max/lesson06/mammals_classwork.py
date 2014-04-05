import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
mammals = pd.read_csv('./../../../data/mammals.csv')
lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()
body = [ [x] for x in mammals['body'].values]
log_body = log_body = [ [x] for x in np.log(mammals['body'].values)]
brain = mammals['brain'].values
log_brain = np.log(mammals['brain'].values)
lm.fit(body, brain)
log_lm.fit(log_body, log_brain)


lm.intercept_  # 91.00439620740687
log_lm.intercept_ #2.1347886767646358

lm.coef_ #array([ 0.96649637])
log_lm.coef_ #array([ 0.75168594])

lm.predict(body)
mammals['predict'] = lm.predict(body)
log_lm.predict(log_body)
mammals['log_predict'] = np.exp(log_lm.predict(log_body))

# Sort by response:
mammals = mammals.sort('brain')
# Sort by prediction:
mammals_log_sort = mammals.sort('log_predict')



plt.scatter(mammals['body'],mammals['brain'])
plt.plot(np.exp(log_body),log_lm.predict(np.exp(log_body)))

plt.plot(body,lm.predict(body),np.exp(log_body),np.exp(log_lm.predict(log_body)))
plt.show()