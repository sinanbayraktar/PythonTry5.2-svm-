import matplotlib.pyplot as plt
from sklearn import svm
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1]
plt.scatter (x, y, s=30, color="green")
plt.xlabel("input values")
plt.ylabel("output values")
plt.title("Input and Output values of data")
plt.show()
clf = svm.SVC()
clf.fit(x, y)
print("prediction for 1.8 is ", clf.predict([[1.8]])) #[1.8, 4.8, 5, 5.1, 5.8, 6, 8.7]
print("prediction for 4.8 is ", clf.predict([[4.8]]))
print("prediction for 5 is ", clf.predict([[5]]))
print("prediction for 5.8 is ", clf.predict([[5.8]]))
print("prediction for 6 is ", clf.predict([[6]]))
print("prediction for 8.8 is ", clf.predict([[8.8]]))
t = input()