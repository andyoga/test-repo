from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('best_model')

def predict(model, input_df):
    
    predictions_df = predict_model(estimator = model, data = input_df)
    predictions = predictions_df['Label'][0]
    return predictions
    



st.title('Radio Cume Predictor Web App')
st.write('Please enter factor level. It will return the predicted Cume.')

station = st.selectbox('Station', ['102.1  102.1 The Edge', '103.5  Z103.5', '104.5  CHUM 104-5',
       '107.3 \tQ107', '92.5    KiSS 92.5', '93.5    93.5 Today Radio',
       '97.3    Boom 97.3', '98.1    98.1 CHFI',
       '99.9    99.9 Virgin Radio', 'FM88.1    Indie 88'])


factor1 = st.slider(label = 'Announcers have a sense of humour I like', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor2 = st.slider(label = 'Announcers have a wide range of knowledge', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor3 = st.slider(label = 'Fun and entertaining weekday morning show', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor4 = st.slider(label = 'Fun to listen to', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)

factor5 = st.slider(label = 'Gives me the information I need to get me through the day', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor6 = st.slider(label = 'Has contests I want to enter', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor7 = st.slider(label = 'Is family-friendly', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor8 = st.slider(label = 'Keeps me up to date with new music', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor9 = st.slider(label = 'Plays great background music', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor10 = st.slider(label = 'Plays more music than ads', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor11 = st.slider(label = 'Plays music I love from my past', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor12 = st.slider(label = 'Plays my kind of music', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor13 = st.slider(label = 'Suits everyone else listening', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor14 = st.slider(label = 'The announcers are interesting to listen to', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor15 = st.slider(label = 'The music brings back memories from my past', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor16 = st.slider(label = 'The music energizes me', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)
                          


output=""


input_dict = {
                'Announcers have a sense of humour I like': factor1, 
                'Announcers have a wide range of knowledge': factor2, 
                'Fun and entertaining weekday morning show': factor3, 
                'Fun to listen to': factor4, 
                'Gives me the information I need to get me through the day': factor5, 
                'Has contests I want to enter': factor6, 
                'Is family-friendly': factor7, 
                'Keeps me up to date with new music': factor8, 
                'Plays great background music': factor9, 
                'Plays more music than ads': factor10,
                'Plays music I love from my past': factor11, 
                'Plays my kind of music': factor12, 
                'Suits everyone else listening': factor13, 
                'The announcers are interesting to listen to': factor14, 
                'The music brings back memories from my past': factor15, 
                'The music energizes me': factor16,
                'Friendly Station': station
            }
 

input_df  = pd.DataFrame([input_dict])

st.table(input_df)  

if st.button('Predict'):
    
    output = predict(model=model, input_df=input_df)
    output = str(output)
    
    st.success('Your predicted Cume is {}'.format(output))