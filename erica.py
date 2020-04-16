from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
# creates dataframe from Animal Clas data
Animal_data_df = pd.read_csv("animal_classes.csv")
Animal_dict = {}
for i, j in Animal_data_df.iterrows():
    for k in (j[3].split(',')):
        l = k.strip()
        Animal_dict[l] = (j[0], j[2])
class_details = {i: j for i, j in Animal_dict.values()}

Animal_data_train = np.genfromtxt('animals_train.csv', delimiter=',', skip_header=1) 
x_train, y_train = Animal_data_train[0:101, 0:16],  (Animal_data_train[0:101, 16])


Animal_data_test = pd.read_csv('animals_test.csv')
animals = Animal_data_test.animal_name
class_numb = [(Animal_dict[i])[0] for i in animals]
#y_test = (pd.Series(class_numb)).to_numpy()
y_test = np.array(class_numb)
x_test = (Animal_data_test.drop(['animal_name'], axis=1)).to_numpy()
#Create Model- train the model
knn = KNeighborsClassifier()
knn.fit(X=x_train, y=y_train)
#Validate the model with test data
predicted = knn.predict(X=x_test)
expected = y_test
predicted_class_list = [class_details[i] for i in predicted]
print(class_details[predicted[19]])
prediction = pd.Series(predicted_class_list, name="Predicted")
Results = pd.concat([animals, prediction], axis=1)
Results.to_csv('predictions.csv', sep=',', index=False)

print(Animal_dict['scorpion'])
