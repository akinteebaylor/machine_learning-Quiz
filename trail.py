from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

# creates dataframe from Animal Clas data
Animal_data_df = pd.read_csv("animal_classes.csv")
Animal_dict={}
for i, j in Animal_data_df.iterrows():
    for k in (j[3].split(',')):
        l= k.strip()
        Animal_dict[l]=(j[0],j[2])

class_details ={i:j for i,j in Animal_dict.values()}

class Animal:
    def __init__ (self,name):
        self.name = name
        self.class_number = Animal_dict[self.name][0]
        self.class_type = class_details[self._class_number]
    @property
    def class_number(self):
        return self._class_number
    @class_number.setter
    def class_number(self, number):
        self._class_number = number
        self.class_type= class_details[self.class_number]

Animalia= Animal('octopus')
print (Animalia.class_number, Animalia.class_type)
Animalia.class_number =2
print(Animalia.class_number, Animalia.class_type)
