from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()

# print(california.target.shape)

import pandas as pd

pd.set_option("precision",4)

pd.set_option("max_columns",9)

pd.set_option("display.width",None)

california_df = pd.DataFrame(california.data , columns = california.feature_names)
california_df["MedHouseValue"] = pd.Series(california.target)
#print(california_df.head())
print(california_df)
print(california_df["MedHouseValue"])
sample_df = california_df.sample(frac=0.1, random_state =17)

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set(font_scale=2)
# sns.set_style("whitegrid")

# # for feature in california.feature_names:
# #     plt.figure(figsize=(8,4.5))
# #     sns.scatterplot(data=sample_df, x=feature,y="MedHouseValue", hue="MedHouseValue", palette ="cool", legend=False)
# # plt.show()

# from sklearn.model_selection import train_test_split

# x_train,x_test,y_train,y_test = train_test_split(california.data, california.target, random_state=11)

# # print(x_train.shape)
# # print(x_test.shape)

# # print(y_train.shape)
# # print(y_test.shape)

# from sklearn.linear_model import LinearRegression

# linear_regression = LinearRegression()

# linear_regression.fit(X=x_train, y=y_train)

# for i , name in enumerate(california.feature_names):
#     print(f"{name:>10}:{linear_regression.coef_[i]}")

# predicted = linear_regression.predict(x_test)
# print(predicted[:5])

# expected = y_test
# print(expected[:5])

# df = pd.DataFrame()
# df["Expected"] = pd.Series(expected)
# df["Predicted"]= pd.Series(predicted)

# import matplotlib.pyplot as plt2
# figure = plt2.figure(figsize=(9,9))
# axes = sns.scatterplot(data=df, x="Expected", y ="Predicted", hue="Predicted", palette="cool", legend =False)

# start = min(expected.min(), predicted.min())

# end  = max(expected.max(), predicted.max())

# axes.set_xlim(start,end)
# axes.set_ylim(start, end)
# lines = plt2.plot([start, end],[start, end],"k--")
# plt2.show()

# #good cekan data, divide it up well to get your estimators to do good. the more the data the better

# #Quiz
# # we will do the supervised classification model_selection

