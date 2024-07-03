# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle
url = 'http://m.uploadedit.com/bbtc/1578244908842.txt'
fruits = pd.read_table(url)
knn = KNeighborsClassifier(n_neighbors = 5)

lookup_fruits_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
X = fruits[['height', 'width', 'mass', 'color_score']]
y = fruits['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
knn.fit(X_train, y_train)

# Saving model to disk
pickle.dump(knn, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
result = model.predict([[20, 4.3, 5.5,0.75]])
model = lookup_fruits_name[result[0]]
print(model)