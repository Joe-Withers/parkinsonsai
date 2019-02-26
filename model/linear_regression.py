import pandas as pd
import numpy as np
from sklearn import preprocessing, model_selection
from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv('./data/parkinsons_updrs.data.txt')
df = shuffle(df)
df.dropna()
df.fillna(-99999, inplace=True)
# X = np.array(df[['sex','age','Jitter(%)','Jitter(Abs)','Jitter:RAP','Jitter:PPQ5','Jitter:DDP','Shimmer','Shimmer(dB)'
#                     ,'Shimmer:APQ3','Shimmer:APQ5','Shimmer:APQ11','Shimmer:DDA','NHR','HNR','RPDE','DFA','PPE']])
X = np.array(df[['sex','age','Jitter(Abs)','Shimmer','NHR','RPDE','DFA','PPE']])
X = preprocessing.scale(X)
y = np.array(df['total_UPDRS'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

plt.scatter(X[:,3],y)
# df['total_UPDRS'].plot()
# df['Jitter(Abs)'].plot()
plt.legend(loc=4)
plt.xlabel('Jitter(Abs)')
plt.ylabel('total_UPDRS')
plt.show()
