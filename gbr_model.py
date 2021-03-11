from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('gbr_model')

def predict(model, input_df):
    
    predictions_df = predict_model(estimator = model, data = input_df)
    predictions = predictions_df['Label'][0]
    return predictions
    



st.title('Insurance predictor Web App')
st.write('Test.')



bmi = st.slider(label = 'BMI', min_value = 10,
                          max_value = 50 ,
                          value = 20,
                          step = 1)

age = st.slider(label = 'Age', min_value = 1,
                          max_value = 100 ,
                          value = 25,
                          step = 1)
                          
children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])

region = st.selectbox('Region', ['southwest','northwest','northeast','southeast'])

smoker = st.selectbox('Smoker', ['yes','no'])

sex = st.selectbox('Sex', ['male','female'])

output=""


input_dict = {'bmi': bmi, 'age': age,
            'children': children, 'region': region,
            'smoker': smoker, 'sex': sex
            }
 

input_df  = pd.DataFrame([input_dict])

st.table(input_df)  

if st.button('Predict'):
    
    output = predict(model=model, input_df=input_df)
    output = '$' + str(output)
    
    st.success('The output is {}'.format(output))