import pandas as pd
import pickle
import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="Corona Virus Dashboard",
    page_icon="😷",
    layout="wide",
    )

df_original = pd.read_csv('Covid Data.csv')

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 60px; font-weight: bold;">Corona Virus Dashboard</h1>', unsafe_allow_html=True)
st.markdown("\n")

col1, col2 = st.columns(2)
animation_1 = load_lottieurl('https://lottie.host/94cdbd53-60c4-4c6b-8570-3a4ad41abf3f/UMBnDfTH1E.json')
animation_2 = load_lottieurl('https://lottie.host/c9671d4f-28c7-4b63-b8c3-bb36c5963ddf/SKihZXLxK8.json')

with col1:
    st_lottie(animation_1, speed=1, height=350, width=450, loop=True, quality="high")

with col2:
    st_lottie(animation_2, speed=1, height=400, loop=True, quality="high")

st.markdown("""  
            \n- #### The data is about corona virus diagnosed and not diagnosed patients and their medical condition *(age, diabetes, hypertension etc.)*
            \n- #### The data after cleaning contains 219222 rows and 19 columns
            \n- #### The data is available on [kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)
            \n- #### In this dashboard we will analyze, visualize the data and we will also predict if the patient is diagnosed or not based on their medical condition""", unsafe_allow_html=True)

st.divider()

st.markdown('<h1 style="text-align: center; color: #ad79b5; font-size: 40px; font-weight: bold;">Original Data</h1>', unsafe_allow_html=True)
st.markdown("\n")
st.dataframe(df_original.head())

st.divider()
st.markdown("\n")

st.markdown(f"""<h3 style="text-align: center; color: #ad79b5; font-size: 40px; font-weight: bold;">Columns Discription (after cleaning)</h3>""", unsafe_allow_html=True)

st.markdown(" - #### <u>Gender:</u>" + " *The gender of the patient*" + """ <span style="color:green">(Female, Male)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Pregnant:</u>" + " *If the patient is female, is she pregnant or not*" + """ <span style="color:green">(Not pregnant, Pregnant)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Patient Type:</u>" + " *The type of the patient's stay*" + """ <span style="color:green">(Home, Hospitalized)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Age:</u>" + " *The age of the patient*" + """ <span style="color:green">(2, ...., 100)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Pneumonia:</u>" + " *If the patient has pneumonia* " + """<span style="color:#afb3b0">(التهاب رئوي)</span>""" + " *or not*" + """ <span style="color:green">(No Pneumonia, Pneumonia)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Diabetes:</u>" + " *If the patient has diabetes* " + """<span style="color:#afb3b0">(مرض السكري)</span>""" + " *or not*" + """ <span style="color:green">(No Diabetes, Diabetes)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>COPD:</u>" + " *If the patient has COPD* " + """<span style="color:#afb3b0">(انسداد رئوي)</span>"""+ " *or not*" + """ <span style="color:green">(No COPD, COPD)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Asthma:</u>" + " *If the patient has asthma* " + """<span style="color:#afb3b0">(الربو)</span>""" + " *or not*" + """ <span style="color:green">(No Asthma, Asthma)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>InmSupr:</u>" + " *If the patient has inmsupr* " + """<span style="color:#afb3b0">(ضعف المناعة)</span>""" + " *or not*" + """ <span style="color:green">(Not InmSupr, InmSupr)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Hypertension:</u>" + " *If the patient has hypertension* " + """<span style="color:#afb3b0">(ارتفاع ضغط الدم)</span>""" + " *or not*" + """ <span style="color:green">(No Hypertension, Hypertension)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Cardiovascular:</u>" + " *If the patient has cardiovascular* " + """<span style="color:#afb3b0">(أمراض القلب)</span>""" + " *or not*" + """ <span style="color:green">(Not Cardiovascular, Cardiovascular)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Obesity:</u>" + " *If the patient has obesity* " + """<span style="color:#afb3b0">(السمنة)</span>""" + " *or not*" + """ <span style="color:green">(No Obesity, Obesity)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Renal Chronic:</u>" + " *If the patient has renal chronic* " + """<span style="color:#afb3b0">(مرض كلوي مزمن)</span>""" + " *or not*" + """ <span style="color:green">(No Renal Chronic, Renal Chronic)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Other Disease:</u>" + " *If the patient has other disease or not*" + """ <span style="color:green">(No, Yes)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Tobacco:</u>" + " *If the patient is tobacco user or not*" + """ <span style="color:green">(No Tobacco, Tobacco)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Dead:</u>" + " *If the patient is dead or not*" + """ <span style="color:green">(Not Dead, Dead)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Dead Year:</u>" + " *If the patient is dead, the year of death*" + """ <span style="color:green">(2021, 2020)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Dead Month:</u>" + " *If the patient is dead, the month of death*" + """ <span style="color:green">(1, ...., 12)</span>""", unsafe_allow_html=True)
st.markdown(" - #### <u>Classification:</u>" + " *If the patient is diagnosed or not*" + """ <span style="color:green">(Not Diagnosed, Diagnosed)</span>""", unsafe_allow_html=True)





















