import tensorflow as tf 
from tensorflow.keras.models import load_model
import pickle 
import pandas as pd 
import numpy as np


#load all utils
model = load_model('model.h5')

# label encoder
with open('encoder_personality.pkl', 'rb') as file : 
    encoder_personality = pickle.load(file)

#standarization scaler
with open('scaler.pkl', 'rb') as file : 
    scaler = pickle.load(file)


def processing_data(input_data) : 
    df = pd.DataFrame([input_data])
    #lowercase all columns
    df.columns = df.columns.str.lower()

    #deleting . in the end of column 
    df.columns = [col.rstrip('.') if isinstance(col, str) and col.endswith('.') else col for col in df.columns]

    #standarization
    input_scaled=scaler.transform(df)
    input_scaled

    #predict
    predicted_probabilities = model.predict(input_scaled)
    predicted_probabilities

    #change predict to categorical
    predicted_class_index = np.argmax(predicted_probabilities, axis=1)
    prediction = encoder_personality.inverse_transform(predicted_class_index)
    prediction = prediction[0]
    
    return prediction