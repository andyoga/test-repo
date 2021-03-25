from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('br_model')

def predict(model, input_df):
    
    predictions_df = predict_model(estimator = model, data = input_df)
    predictions = predictions_df['Label'][0]
    return predictions
    



st.title('Radio Monthly Cume Predictor Web App')
st.write('1 month lag. Please enter current month factor level. It will return the following month predicted Cume.')

station = st.selectbox('Station', ['Boom 97.3','CHFI 98.1','CHUM 104.5','Flow 93.5','Indie 88.1','KiSS 92.5','News 680','Newstalk 1010','Q107 (Toronto)','Sportsnet 590','The Edge 102.1 (Toronto)','TSN 1050','Virgin 99.9 (Toronto)','Z103.5','CBC Music (Toronto)','CBC Radio One (Toronto)','Classical 96.3','Energy 95.3','G98.7','Global News 640'])


factor1 = st.slider(label = 'Announcers are down to earth', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor2 = st.slider(label = 'Announcers have a sense of humour I like', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor3 = st.slider(label = 'Announcers have a wide range of knowledge', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor4 = st.slider(label = 'Challenges me to think differently', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)

factor5 = st.slider(label = 'Fun and entertaining weekday morning show', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor6 = st.slider(label = 'Fun to listen to', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor7 = st.slider(label = 'Gives me a different perspective on current events', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor8 = st.slider(label = 'Gives me the information I need to get me through the day', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor9 = st.slider(label = 'Has contests I want to enter', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor10 = st.slider(label = 'Helps me concentrate', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor11 = st.slider(label = 'Is family-friendly', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor12 = st.slider(label = 'It connects me to whats going on in my city', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor13 = st.slider(label = 'It helps me pass the time', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor14 = st.slider(label = 'Keeps me motivated to get things done', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor15 = st.slider(label = 'Keeps me up to date with new music', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor16 = st.slider(label = 'Keeps me up-to-date', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor17 = st.slider(label = 'Like a companion in the car', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor18 = st.slider(label = 'Place to go for sports', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor19 = st.slider(label = 'Plays great background music', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor20 = st.slider(label = 'Plays more music than ads', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor21 = st.slider(label = 'Plays music I love from my past', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor22 = st.slider(label = 'Plays my kind of music', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor23 = st.slider(label = 'Suits everyone else listening', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor24 = st.slider(label = 'Surprises me with songs I havenâ€™t heard in a long time', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor25 = st.slider(label = 'The announcers are interesting to listen to', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor26 = st.slider(label = 'The music brings back memories from my past', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor27 = st.slider(label = 'The music energizes me', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)


factor28 = st.slider(label = 'Traffic updates save me time', min_value = 0.0,
                          max_value = 1.0,
                          value = 0.5,
                          step = 0.01)
                          

month = st.selectbox('Month Name', ['January','February','March','April','May','June','July','August','September','October','November','December'])


output=""


input_dict = {'Announcers are down to earth': factor1, 'Announcers have a sense of humour I like': factor2, 'Announcers have a wide range of knowledge': factor3, 'Challenges me to think differently': factor4, 'Fun and entertaining weekday morning show': factor5, 'Fun to listen to': factor6, 'Gives me a different perspective on current events': factor7, 'Gives me the information I need to get me through the day': factor8, 'Has contests I want to enter': factor9, 'Helps me concentrate': factor10,
              'Is family-friendly': factor11, 'It connects me to whats going on in my city': factor12, 'It helps me pass the time': factor13, 'Keeps me motivated to get things done': factor14, 'Keeps me up to date with new music': factor15, 'Keeps me up-to-date': factor16, 'Like a companion in the car': factor17, 'Place to go for sports': factor18, 'Plays great background music': factor19, 'Plays more music than ads': factor20,
              'Plays music I love from my past': factor21, 'Plays my kind of music': factor22, 'Suits everyone else listening': factor23, 'Surprises me with songs I havenâ€™t heard in a long time': factor24, 'The announcers are interesting to listen to': factor25, 'The music brings back memories from my past': factor26, 'The music energizes me': factor27, 'Traffic updates save me time': factor28,
              'Month Name': month, 'Station': station
            }
 

input_df  = pd.DataFrame([input_dict])

st.table(input_df)  

if st.button('Predict'):
    
    output = predict(model=model, input_df=input_df)
    output = str(output)
    
    st.success('Your predicted Cume for next month is {}'.format(output))