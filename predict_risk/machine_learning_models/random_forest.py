# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("C:\code\heart-disease-prediction\predict_risk\machine_learning_models\HealthData.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 13].values


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer=imputer.fit(X[:,11:13])
X[:,11:13]=imputer.transform(X[:,11:13])




from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=5)


from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
X_train = sc1.fit_transform(X_train)
X_test = sc1.transform(X_test)
#saving StandardScaler file in pickle
from joblib import dump, load
dump(sc1,'C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/production/std_scaler3.pkl', compress=True)


# Fitting Decision Tree Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(random_state=8)
classifier.fit(X_train, y_train)

import joblib
filename = 'C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/production/random_forest_model.pkl'
joblib.dump(classifier,filename)




# Predicting the Test set results
y_pred = classifier.predict(X_test)
#ACCURACY SCORE
from sklearn.metrics import accuracy_score
yp = accuracy_score(y_test,y_pred)
print(yp)
#CONFUSION MATRIX
from sklearn.metrics import classification_report, confusion_matrix
cm=confusion_matrix(y_test, y_pred)
#Interpretation:
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
