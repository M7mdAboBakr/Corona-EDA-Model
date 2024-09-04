import pandas as pd
import plotly.express as px
import streamlit as st

df_main = pd.read_csv('Covid Data Cleaned.csv')

st.set_page_config(
    page_title="Bivariate & Multivariate",
    page_icon="",
    layout="wide",
    )

st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Death Section</h1>", unsafe_allow_html=True)
st.markdown("\n")

col1, col2, col3 = st.columns(3)

# gender
col1.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Death Distribution with Gender</h1>", unsafe_allow_html=True)
col1.markdown("\n")

fig = px.sunburst(df_main.groupby('gender')['dead'].value_counts().reset_index(),
                   path=['gender', 'dead'], values='count',
                   color_discrete_sequence=px.colors.sequential.RdBu_r)
fig.update_traces(marker=dict(line=dict(color='black', width=1)),
                  textinfo="label+percent parent")
col1.plotly_chart(fig, use_container_width=True)

# patient type
col2.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Death Distribution with Patient Type</h1>", unsafe_allow_html=True)
col2.markdown("\n")

fig = px.sunburst(df_main.groupby('patient_type')['dead'].value_counts().reset_index(),
                   path=['patient_type', 'dead'], values='count',
                   color_discrete_sequence=px.colors.sequential.RdBu_r)
fig.update_traces(marker=dict(line=dict(color='black', width=1)),
                  textinfo="label+percent parent")
col2.plotly_chart(fig, use_container_width=True)


col3.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Death Distribution with Pneumonia</h1>", unsafe_allow_html=True)
fig = px.sunburst(df_main.groupby('pneumonia')['dead'].value_counts().reset_index(),
                   path=['pneumonia', 'dead'], values='count',
                   color_discrete_sequence=px.colors.sequential.RdBu_r)
fig.update_traces(marker=dict(line=dict(color='black', width=1)),
                  textinfo="label+percent parent")
col3.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

# obesity
col1.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Death Distribution with Obesity</h1>", unsafe_allow_html=True)
col1.markdown("\n")
fig = px.sunburst(df_main.groupby('obesity')['dead'].value_counts().reset_index(),
                   path=['obesity', 'dead'], values='count', template='plotly_dark',
                   color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(marker=dict(line=dict(color='black', width=7)),
                  textinfo="label+percent parent")
col1.plotly_chart(fig, use_container_width=True)

# classification
col2.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Death Distribution with Diagnosis</h1>", unsafe_allow_html=True)
col2.markdown("\n")
fig = px.sunburst(df_main.groupby('classification')['dead'].value_counts().reset_index(),
                   path=['classification', 'dead'], values='count', template='plotly_dark',
                   color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(marker=dict(line=dict(color='black', width=7)),
                  textinfo="label+percent parent")
col2.plotly_chart(fig, use_container_width=True)

st.divider()


# diagnosis section
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Diagnosis Section</h1>", unsafe_allow_html=True)
st.markdown("\n")


col1, col2, col3 = st.columns(3)
col1.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Diagnosis Distribution with Gender</h1>", unsafe_allow_html=True)
col1.markdown("\n")

# gender
fig = px.sunburst(df_main.groupby('gender')['classification'].value_counts().reset_index(),
                   path=['gender', 'classification'], values='count', template='plotly_dark',
                   color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(marker=dict(line=dict(color='black', width=7)),
                  textinfo="label+percent parent")
col1.plotly_chart(fig, use_container_width=True)


col2.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Diagnosis Distribution with Patient Type</h1>", unsafe_allow_html=True)
col2.markdown("\n")

# patient type
fig = px.sunburst(df_main.groupby('patient_type')['classification'].value_counts().reset_index(),
                   path=['patient_type', 'classification'], values='count', template='plotly_dark',
                   color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(marker=dict(line=dict(color='black', width=7)),
                  textinfo="label+percent parent")
col2.plotly_chart(fig, use_container_width=True)


col3.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Diagnosis Distribution with Pneumonia</h1>", unsafe_allow_html=True)
col3.markdown("\n")

# pneumonia
fig = px.sunburst(df_main.groupby('pneumonia')['classification'].value_counts().reset_index(),
                   path=['pneumonia', 'classification'], values='count', template='plotly_dark',
                   color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(marker=dict(line=dict(color='black', width=7)),
                  textinfo="label+percent parent")
col3.plotly_chart(fig, use_container_width=True)

st.divider()

# age section
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Age Section</h1>", unsafe_allow_html=True)
st.markdown("\n")



# patient type
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Age Distribution with Patient Type</h1>", unsafe_allow_html=True)
st.markdown("\n")

fig = px.histogram(df_main, x='age', color='patient_type', barmode='group',
                   labels={'age': 'Age', 'patient_type': 'Patient Type'})
st.plotly_chart(fig, use_container_width=True)

# pneumonia
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Age Distribution with Pneumonia</h1>", unsafe_allow_html=True)
st.markdown("\n")

fig = px.histogram(df_main, x='age', color='pneumonia', barmode='group',
                   labels={'age': 'Age', 'pneumonia': 'Pneumonia'})
st.plotly_chart(fig, use_container_width=True)


# hypertension
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 30px; font-weight: bold;'>Age Distribution with Hypertension</h1>", unsafe_allow_html=True)
st.markdown("\n")
fig = px.histogram(df_main, x='age', color='hypertension', barmode='group',
                   labels={'age': 'Age', 'hypertension': 'Hypertension'})
st.plotly_chart(fig, use_container_width=True)

st.divider()

# filter
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Filter The Data</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)


index = col1.selectbox(options=['gender', 'patient_type', 'pneumonia', 'diabetes',
       'copd', 'asthma', 'inmsupr', 'hypertension', 'other_disease',
       'cardiovascular', 'obesity', 'renal_chronic', 'tobacco',
       'classification', 'dead'], label='Index (Inner Circle)')

column = col2.selectbox(options=['gender', 'patient_type', 'pneumonia', 'diabetes',
       'copd', 'asthma', 'inmsupr', 'hypertension', 'other_disease',
       'cardiovascular', 'obesity', 'renal_chronic', 'tobacco',
       'classification', 'dead'], label='Column (Outer Circle)')

st.markdown("\n")
if index == column:
    st.warning('Please select two different columns')

else:
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.markdown("\n")
    col1.dataframe(df_main.pivot_table(index=index, columns=column, values='age', aggfunc='count'))

    fig = px.sunburst(df_main.groupby(index)[column].value_counts().reset_index(), path=[index, column], values='count', template='plotly_dark',
                 color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_traces(marker=dict(line=dict(color='black', width=7)), textinfo="label+percent parent")

    col2.plotly_chart(fig, use_container_width=True)

st.divider()

st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Insights</h1>", unsafe_allow_html=True)
st.markdown("""  
            \n- #### The death distribution is slitly affected by gender, the precentage of dead patients is higher in males
            \n- #### The death distribution is strongly affected by patient type, if the patient is hospitalized, it is more likely to die
            \n- #### The death distribution is strongly affected with pneumonia but not as much as patient type, more than 80% of patients that haven't pneumonia are not dead unlike the patients that have pneumonia more than 50% of them are dead
            \n- #### Unlike the expectation, the number of dead patients that haven't obesity is more than the number of patients who have obesity
            \n- #### More than 4/5 of the not diagnosed patients are alive and more than the half of the diagnosed patients are dead
            \n- #### The percentage of diagnosed females is less than the percentage of diagnosed males
            \n- #### If the patient is hospitalized, he is more likely to be diagnosed
            \n- #### More than 60% percent of patients who have pneumonia are diagnosed, Unlike the patients who haven't pneumonia, only about 40% of them are diagnosed
            \n- #### After 45 years old, the number of hospitalized patients is getting bigger than the number of home patients
            \n- #### Under 58 year old, the number of patients who have pneumonia is lower the number of patients who haven't pneumonia
            \n- #### The patients whose age is less than 67 are more likely to not have hypertension
            """, unsafe_allow_html=True)
  


