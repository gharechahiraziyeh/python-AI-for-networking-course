from joblib import load
clf = load("/home/razi/Desktop/python-AI-for-networking-course/8-session/knn_model_diabet.pkl")
new_sample = [[9,102,76,37,0,32.9,0.665,46]]
prediction = clf.predict(new_sample)
print(f"new sample: {new_sample}")
print(f"predicted class: {prediction[0]}")