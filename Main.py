import matplotlib.pyplot as plt
from sklearn import svm
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1]
plt.scatter (x, y, s=30, color="green")
plt.xlabel("input values")
plt.ylabel("output values")
plt.title("Input and Output values of data")

clf = svm.SVC()
clf.fit(x, y)
print("prediction for 1.8 is ", clf.predict([[1.8]])) #[1.8, 4.8, 5, 5.49, 5.74, 6, 8.8]
print("prediction for 4.8 is ", clf.predict([[4.8]]))
print("prediction for 5 is ", clf.predict([[5]]))
print("prediction for 5.49 is ", clf.predict([[5.49]]))
print("prediction for 5.74 is ", clf.predict([[5.74]]))
print("prediction for 6 is ", clf.predict([[6]]))
print("prediction for 8.8 is ", clf.predict([[8.8]]))

feature_test = [[1.8, 4.8, 5, 5.49, 5.74, 6, 8.8]]
predict_result = [clf.predict([[1.8]]), clf.predict([[4.8]]), clf.predict([[5]]), clf.predict([[5.49]]), clf.predict([[5.74]]), clf.predict([[6]]), clf.predict([[8.8]])]
plt.scatter (feature_test, predict_result, s=30, color="purple")
plt.text(1, 0, 'input')
plt.text(8.8, clf.predict([[8.8]]), 'predict')

plt.show()
t = input()
