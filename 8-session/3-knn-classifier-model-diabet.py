# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, zero_one_loss
from joblib import dump

file_path = "/home/razi/Desktop/python-AI-for-networking-course/8-session/diabetes.csv"

dataset = pd.read_csv(file_path, )



# print loaded dataset information
print(f"the shape is {dataset.shape}")
print("some head rows od dataset:")
print(dataset.head())

# split features and labels
features = dataset.iloc[:, :8]
print("features are:")
print(features)
print(f"type of features is: {type(features)}")
print(f"length of features are: {len(features)}")

labels = dataset.iloc[:, 8]
print("labels are:")
print(labels)
print(f"type of labels is: {type(labels)}")
print(f"length of labels are: {len(labels)}")

# split train from test data
xtrain, xtest, ytrain, ytest = train_test_split(features, labels)

# optional: print split data and labels
print("xtrain is:")
print(xtrain)

print("xtest is: ")
print(xtest)

print("ytrain is:")
print(ytrain)

print("ytest is: ")
print(ytest)

# train model
clf = KNeighborsClassifier(8)
clf.fit(xtrain, ytrain)

ypred = clf.predict(xtest)
print(ypred)
print(f"number of predicted labels are : {len(ypred)}")

#calculate accuracy metric
acc = accuracy_score(ytest, ypred)
loss = zero_one_loss(ytest, ypred)
print(f"accuracy of this model is: {acc * 100:.2f}%")
print(f"loss of this model is: {loss * 100:.2f}%")

# save the model output
dump(clf, "/home/razi/Desktop/python-AI-for-networking-course/8-session/knn_model_diabet.pkl")
print("the model has saved")

