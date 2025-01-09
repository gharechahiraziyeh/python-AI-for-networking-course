from joblib import load
clf = load("/home/razi/Desktop/python-AI-for-networking-course/8-session/knn_model.pkl")
print("model loaded")

new_sample = [[6.7,3.1,4.4,1.4]]
prediction = clf.predict(new_sample)
print(f"new sample: {new_sample}")
print(f"predicted class: {prediction[0]}")