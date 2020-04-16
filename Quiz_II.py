from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)

# creates dataframe from Animal Clas data
Animal_data_df = pd.read_csv("animal_classes.csv")
Animal_dict = {}
for i, j in Animal_data_df.iterrows():
    for k in (j[3].split(',')):
        l = k.strip()
        Animal_dict[l] = (j[0], j[2])
class_details = {i: j for i, j in Animal_dict.values()} #dictiomnary comprehnsion
#This next python class module is not needed I could have worked through dictionaries but I fill I need to take every oportunity to practice python classes. I struggled with them while working through my Py-game project
class Animal:
    def __init__(self, name):
        self.name = name
        self.class_number = Animal_dict[self.name][0]
        self.class_type = class_details[self.class_number]
    def return_class_type(self,number):
        self.returned_class = class_details[number]
        return self.returned_class
#The class module above is not needed I could have worked through the dictionary I created but I fill I need to take every oportunity to practice python classes. I noticed a gap while doing my py_game project
#--Read Train data
Animal_data_train = np.genfromtxt('animals_train.csv', delimiter=',', skip_header=1) #read CSV into numpy array
x_train, y_train = Animal_data_train[0:101, 0:16],  (Animal_data_train[0:101, 16]) #split data into X values and Y values
#--Read Test Data
Animal_data_test = pd.read_csv('animals_test.csv')
animals = Animal_data_test.animal_name
class_numb = [(Animal(i)).class_number for i in animals]
y_test = (pd.Series(class_numb)).to_numpy()
x_test = (Animal_data_test.drop(['animal_name'], axis=1)).to_numpy()
#Create Model- Train the model
knn = KNeighborsClassifier()
knn.fit(X=x_train, y=y_train)
#Validate the model with test data
predicted = knn.predict(X=x_test)
expected = y_test #These are the expected class_numbers
#get the animal name for these class_numbers
predicted_class_list = [Animal(animals[i]).return_class_type(i) for i in predicted]
#Create a dataframe that has the animal name and the predicted class_type
prediction = pd.Series(predicted_class_list, name="prediction") #cobnverts the predicted class_type to a panda series
Results = pd.concat([animals, prediction], axis=1) #concatenate the prediction panda series with the animals series to get a result data frame.
#write result data frame to CSV FILE
Results.to_csv('predictions.csv', sep=',', index=False)

