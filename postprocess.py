import numpy as np 
import tensorflow as tf

def get_pred(model, x):     
    '''
    Function used to output the predicted numerical label from a 2D array. 
    
    model -> Your ML model 
    x -> The data you want to predict on 
    
    '''
    
    y_pred = [] 

    for pred in model.predict(x): 
        y_pred.append(np.where(pred == max(pred))[0][0]) 
    
    return y_pred 

