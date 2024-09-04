import pandas as pd
import plotly.express as px
import streamlit as st

df_main = pd.read_csv('Covid Data Cleaned.csv')

st.set_page_config(
    page_title="Univariate",
    page_icon="",
    layout="wide",
    )

# classification
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Diagnosis Distribution</h1>", unsafe_allow_html=True)
st.markdown("\n")

fig1 = px.pie(df_main.classification.value_counts().reset_index(), names='classification', values='count',
             color_discrete_sequence=px.colors.sequential.RdBu_r,
             template='plotly_dark')
fig1.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=5)
fig1.update_layout(showlegend=False)
st.plotly_chart(fig1, use_container_width=True)
st.divider()

# gender
col1, col2 = st.columns(2)
col1.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Gender Distribution</h1>", unsafe_allow_html=True)
col1.markdown("\n")
fig2 = fig = px.pie(df_main.gender.value_counts().reset_index(), names='gender', values='count',
             template='simple_white')
fig2.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=2)
fig2.update_layout(showlegend=False)
col1.plotly_chart(fig2, use_container_width=True)


col2.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Pregnancy Distribution(Female)</h1>", unsafe_allow_html=True)
fig123 = px.pie(df_main[df_main.gender == 'Female'].pregnant.value_counts().reset_index(), names='pregnant', values='count',
             template='simple_white')
fig123.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)
fig123.update_layout(showlegend=False)
col2.plotly_chart(fig123, use_container_width=True)
st.divider()

# age
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Age Distribution</h1>", unsafe_allow_html=True)
st.markdown("\n")

fig3 = px.histogram(df_main, x='age', marginal='box',
             labels={'age': 'Age', 'count': '# of Patients'},
             template='simple_white')
st.plotly_chart(fig3, use_container_width=True)
st.divider()

# dead
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Death Distribution</h1>", unsafe_allow_html=True)
st.markdown("\n")

fig4 = px.pie(df_main.dead.value_counts().reset_index(), names='dead', values='count',
             template='plotly_dark',
             labels={'dead': 'Dead', 'count': '# of Patients'}, hole=0.6,
             color_discrete_sequence=px.colors.sequential.RdBu)
fig4.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=7)
fig4.add_annotation(text='Deadth', x=0.5, y=0.55, font_size=18, showarrow=False)
fig4.add_annotation(text='Distribution', x=0.5, y=0.45, font_size=18, showarrow=False)
fig4.update_layout(showlegend=False)
st.plotly_chart(fig4, use_container_width=True)

col1, col2 = st.columns(2)

fig5 = px.line(df_main[df_main.dead == "Dead"].dead_year.value_counts().reset_index(), x='dead_year', y='count',
             labels={'dead_year': 'Year', 'count': '# of Dead Patients'}, markers=True,
             template='plotly_dark')
col1.plotly_chart(fig5, use_container_width=True)

fig6 = px.line(df_main[df_main.dead == "Dead"].dead_month.value_counts().reset_index().sort_values('dead_month'), x='dead_month', y='count',
             labels={'dead_month': 'Month', 'count': '# of Dead Patients'}, markers=True,
             template='plotly_dark')
col2.plotly_chart(fig6, use_container_width=True)
st.divider()



st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Filter The Data</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    diagnosis_choice = st.selectbox(options=['All', 'Diagnosed', 'Not Diagnosed'], label='Diagnosis', placeholder='All')

    if diagnosis_choice == 'Diagnosed':
        df = df_main[df_main.classification == 'Diagnosed']

    elif diagnosis_choice == 'Not Diagnosed':
        df = df_main[df_main.classification == 'Not diagnosed']
    else:
        df = df_main

with col2:
    gender_choice = st.selectbox(options=['All', 'Male', 'Female'], label='Gender', placeholder='All')

    if gender_choice == 'Male':
        df = df[df.gender == 'Male']

    elif gender_choice == 'Female':
        df = df[df.gender == 'Female']
    else:
        df = df

with col3:
    death_choice = st.selectbox(options=['All', 'Alive', 'Dead'], label='Death', placeholder='All')

    if death_choice == 'Alive':
        df = df[df.dead == 'Not Dead']

    elif death_choice == 'Dead':
        df = df[df.dead == 'Dead']

        death_year_choice = st.selectbox(options=['All', '2020', '2021'], label='Year of Death', placeholder='All')

        if death_year_choice == '2020':
            df = df[df.dead_year == 2020]

        elif death_year_choice == '2021':
            df = df[df.dead_year == 2021]
        
        death_month_choice = st.multiselect(options=map(str, (map(int,sorted(df.dead_month.unique().tolist())))), label='Month of Death', default=map(str, (map(int,sorted(df.dead_month.unique().tolist())))))
        df = df[df.dead_month.isin(map(int, death_month_choice))]
            
    else:
        df = df



col1, col2 = st.columns(2)

# patient_type
fig = px.bar(df.patient_type.value_counts().reset_index(), x='patient_type', y='count', color='patient_type', text_auto=True,
             labels={'patient_type': 'Patient Type', 'count': '# of Patients'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
col1.plotly_chart(fig, use_container_width=True)

# pneumonia
fig = px.bar(df.pneumonia.value_counts().reset_index(), x='pneumonia', y='count', color='pneumonia',
             labels={'pneumonia': 'Pneumonia', 'count': '# of Patients'}, text_auto=True,
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
col2.plotly_chart(fig, use_container_width=True)

# diabetes
fig = px.bar(df.diabetes.value_counts().reset_index(), x='diabetes', y='count', color='diabetes',
             labels={'diabetes': 'Diabetes', 'count': '# of Patients'}, text_auto=True,
             template='plotly_dark')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='white', marker_line_width=0.3)
col1.plotly_chart(fig, use_container_width=True)

# hypertension
fig = px.pie(df.hypertension.value_counts().reset_index(), names='hypertension', values='count',
             template='plotly_dark',
             labels={'hypertension': 'Hypertension', 'count': '# of Patients'},
             color_discrete_sequence=px.colors.sequential.Rainbow)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=7)
fig.update_layout(showlegend=False)
col2.plotly_chart(fig, use_container_width=True)

# obesity
fig = px.pie(df.obesity.value_counts().reset_index(), names='obesity', values='count',
             template='simple_white',
             labels={'obesity': 'Obesity', 'count': '# of Patients'}, hole=0.6)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)
fig.add_annotation(text="Obesity Distribution", x=0.5, y=0.5, showarrow=False, font_size=16)
fig.update_layout(showlegend=False)
col1.plotly_chart(fig, use_container_width=True)

# cardiovascular
fig = px.bar(df.cardiovascular.value_counts().reset_index(), x='cardiovascular', y='count', color='cardiovascular',
             text_auto=True,
             labels={'cardiovascular': 'Cardiovascular', 'count': '# of Patients'},
             template='simple_white')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)
col2.plotly_chart(fig, use_container_width=True)

# inmsupr
fig = px.bar(df.inmsupr.value_counts().reset_index(), x='inmsupr', y='count', color='inmsupr',
             text_auto=True,
             labels={'inmsupr': 'Inmsupr', 'count': '# of Patients'},
             template='seaborn')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=0.3)
col1.plotly_chart(fig, use_container_width=True)

# tobacco
fig = px.bar(df.tobacco.value_counts().reset_index(), x='tobacco', y='count', color='tobacco',
             text_auto=True,
             labels={'tobacco': 'Tobacco', 'count': '# of Patients'},
             template='plotly_dark', color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1)
col2.plotly_chart(fig, use_container_width=True)

# copd
fig = px.bar(df.copd.value_counts().reset_index(), x='copd', y='count', color='copd',
             text_auto=True,
             labels={'copd': 'COPD', 'count': '# of Patients'},
             template='gridon')
fig.update_layout(showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
col1.plotly_chart(fig, use_container_width=True)

# asthma
fig = px.pie(df.asthma.value_counts().reset_index(), names='asthma', values='count',
             template='plotly_dark',
             labels={'asthma': 'Asthma', 'count': '# of Patients'},
             color_discrete_sequence=px.colors.sequential.Rainbow)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=7)
fig.update_layout(showlegend=False)
col2.plotly_chart(fig, use_container_width=True)

# renal_chronic
fig = px.pie(df.renal_chronic.value_counts().reset_index(), names='renal_chronic', values='count',
             template='plotly_dark',
             labels={'renal_chronic': 'Renal Chronic', 'count': '# of Patients'}, hole=0.6,
             color_discrete_sequence=px.colors.sequential.RdBu_r)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)
fig.add_annotation(text="Renal Chronic Distribution", x=0.5, y=0.5, showarrow=False)
fig.update_layout(showlegend=False)
col1.plotly_chart(fig, use_container_width=True)

fig = px.pie(df.other_disease.value_counts().reset_index(), names='other_disease', values='count',
             template='plotly_dark',
             labels={'other_disease': 'Other Disease', 'count': '# of Patients'},
             color_discrete_sequence=px.colors.sequential.Bluered)
fig.update_traces(textposition='inside', textinfo='percent+label', marker_line_color='black', marker_line_width=1)
fig.update_layout(showlegend=False)
col2.plotly_chart(fig, use_container_width=True)
