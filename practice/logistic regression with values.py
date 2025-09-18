# import libraries 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

# give input and classification of pass fail
X = np.array([[100],[80],[60],[85]]).reshape(-1,1)
y = np.array([1,0,0,1])
X_new = np.array([[150]])


# firstly we train the model via logistic regression 
model = LogisticRegression()
# provide X and y to model 
model.fit(X,y)

# it predicts the value according to x_new 
y_predict = model.predict(X_new)[0]
# we also want to know probability which should in between 0 and 1
probability = model.predict_proba(X_new)[0][1]

# here we will plot several points 0 to 120  in 2d format 
X_range = np.linspace(0,120,300).reshape(-1,1)
# now we want probability of pass 
y_proba = model.predict_proba(X_range)[: , 1]


# pltting the sigmoid function
plt.figure(figsize=(10, 9))
plt.scatter(X_new, probability, label="Actual Data")
plt.scatter(X, y, color='blue', label="Training Data")
plt.plot(X_range, y_proba, color='red', label="sigmoid curve")
plt.xlabel("Mark")
plt.ylabel("result" )                   ## 0= fail,1= pass)
plt.title("Logistic Regression: Original Scale")
plt.legend()
plt.grid(True)
plt.show()
