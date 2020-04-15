import pandas as pd
import numpy as np
from Animal_class import Animal, return_class_type

Animal_data_train = np.genfromtxt('animals_train.csv',delimiter=',', skip_header=1)
Animal_data_df = pd.read_csv("animal_classes.csv")
x_train, y_train = Animal_data_train[0:101,0:16],  (Animal_data_train[0:101, 16])

Animal_data_test = pd.read_csv('animals_test.csv')
animals = Animal_data_test.animal_name
class_numb=[]
for i in animals:
    Animalia = Animal(i)
    class_numb.append(Animalia.class_number)
y_test =(pd.Series(class_numb)).to_numpy()
x_test = (Animal_data_test.drop( ['animal_name'], axis =1)).to_numpy()

from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier()
knn.fit(X=x_train, y=y_train)

predicted =knn.predict(X=x_test)
expected =y_test
predicted_class_list=[]
for i in predicted:
    predicted_class_type = return_class_type(i)
    predicted_class_list.append(predicted_class_type)
prediction = pd.Series(predicted_class_list, name="Predicted")
Results = pd.concat([animals, prediction],axis=1)
Results.to_csv('predictions.csv',sep=',',index=False)
