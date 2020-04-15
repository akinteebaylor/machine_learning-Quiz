from sklearn.datasets import load_digits
from numpy import savetxt
digits = load_digits()
#print(digits.data)
# print (digits.target[13])
# print(digits.data[13])
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(digits.data,digits.target, random_state=11)
#print(x_train.shape)
#print(y_train.shape
savetxt('x_train.csv', x_train, delimiter=',')
savetxt('y_train.csv', y_train, delimiter=',')
# import matplotlib.pyplot as plt 
#plt.gray()
#print(digits.images[13]) 
# plt.matshow(digits.images[13]) 
# plt.show()

#scikit prefers that data is stored in 20Dimensional arrays. So lists of lists, dictionaries and panda DataFrames will suffice
#sklearn.preprocessing converts categorical data to numerical data
# figure,axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
# for item in zip(axes.ravel(),digits.images,digits.target):
#     axes,image,target =item
#     axes.imshow(image,cmap=plt.cm.gray_r)
#     axes.set_xticks([])
#     axes.set_yticks([])
#     axes.set_title(target)
# plt.tight_layout()
# plt.show()

# axes = plt.subplot()
# image = plt.imshow(digits.images[22], cmap=plt.cm.gray_r)
# xticks = axes.set_xticks([])
# yticks = axes.set_yticks([])
# plt.show()
