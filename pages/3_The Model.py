import pandas as pd
import pickle
import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="The Model",
    page_icon="",
    layout="wide",
    )

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

animation_1 = load_lottieurl('https://lottie.host/60b6d659-4cf3-4678-8ce4-382a4023bf14/MaEyxklSaK.json')


# st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>The Model</h1>", unsafe_allow_html=True)
st_lottie(animation_1, speed=1, height=400, loop=True, quality="high")

age = st.slider('Age', 0, 100, 25)

col1, col2 = st.columns(2)

preprocessor, threshold = pickle.load(open('preprocessor_threshold.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb')) 

gender = col2.radio('Gender', ('Male', 'Female'))

patient_type = col1.radio('Patient Type', ('Home', 'Hospitalized'))

pneumonia = col2.radio('Pneumonia', ("No Pneumonia", "Pneumonia"))

dead = col1.radio('Death', ("Not Dead", "Dead"))

tobacco = col2.radio('Tobacco', (('No Tobacco', 'Tobacco')))

diabetes = col1.radio('Diabetes', ('No Diabetes', 'Diabetes'))

copd = col2.radio('COPD', ('No COPD', 'COPD'))

asthma = col1.radio('Asthma', ('No Asthma', 'Asthma'))

inmsupr = col2.radio('Inmsupr', ('Not Inmsupr', 'Inmsupr'))

hypertension = col1.radio('Hypertension', ('No Hypertension', 'Hypertension'))

other_disease = col2.radio('Other Disease', ('No', 'Yes'))

cardiovascular = col1.radio('Cardiovascular', ('Not Cardiovascular', 'Cardiovascular'))

renal_chronic = st.radio('Renal Chronic', ('No Renal Chronic', 'Renal Chronic'))

# order them like than
prediction = pd.DataFrame({'gender': [gender], 'patient_type': [patient_type], 'pneumonia': [pneumonia], 
 'age': [age], 'diabetes': [diabetes], 'copd': [copd], 'asthma': [asthma], 
 'inmsupr': [inmsupr], 'hypertension': [hypertension], 'other_disease': [other_disease], 
 'cardiovascular': [cardiovascular], 'obesity':['Obesity'], 'renal_chronic': [renal_chronic], 
 'tobacco': [tobacco], 'dead': [dead]})


prediction_preprocessed = pd.DataFrame(preprocessor.transform(prediction), columns=prediction.columns)
prediction_preprocessed.drop('obesity', axis=1, inplace=True)

if st.button('Predict'):

    y_proba = model.predict_proba(prediction_preprocessed)
    y_pred = (y_proba[:, 1] >= threshold).astype(int)

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    if y_pred == 0:
        st.success("No Corona Virus")

    else:
        st.error("Corona Virus Detected")

    # st.markdown(f"<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>{y_pred[0]}</h1>", unsafe_allow_html=True)

