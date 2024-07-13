import json
import pickle
import numpy as np
__locations = None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loi=__data_columns.index(location.lower())
    except:
        loi=-1    
    
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loi>=0:
        x[loi]=1
    
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts....start")
    global __data_columns
    global __locations
    global __model
    
    with open('./artifacts/columns.json','r') as f:
            __data_columns=json.load(f)['data columns']
            __locations=__data_columns[3:]

    with open('./artifacts/bangalore_home_prices_model.pickel','rb') as f:
            __model=pickle.load(f)
    print("loading saved artifacts done")

if __name__=='__main__':
     load_saved_artifacts()
     print (get_location_names()) 

