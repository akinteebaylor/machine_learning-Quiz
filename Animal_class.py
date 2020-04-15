import pandas as pd
Animal_data_df = pd.read_csv("animal_classes.csv")
Animalia = {}
class_type = {}
a = 0
for i in Animal_data_df.Class_Type:
    Animalia[i] = ((Animal_data_df.iat[a, 3]).split(','))
    class_type[i] = Animal_data_df.iat[a, 0]
    a += 1

def return_class_type(number):
    for key, value in class_type.items():
        if value == number:
            return key

class Animal:
    def __init__(self, name):
        self.name = name

        def get_class(self, name):
            for key, value in Animalia.items():
                for i in value:
                    if i.strip() == name:
                        return key            
        self.class_type = get_class(self, name)
        self.class_number = class_type[get_class(self, name)]



