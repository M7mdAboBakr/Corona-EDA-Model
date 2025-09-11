# 🦠 Corona Virus Patient Classification Dashboard  

An interactive Streamlit dashboard analyzing COVID-19 patient medical records and predicting diagnosis outcomes using Machine Learning.  

The dataset contains patient demographics and health conditions (e.g. age, diabetes, hypertension, obesity, etc.) with outcomes such as diagnosis and mortality.  

---

🔗 **Live Dashboard:** [Click Here](https://corona-eda-model.streamlit.app/)  
📂 **Dataset Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/meirnizri/covid19-dataset/data?utm_source=chatgpt.com)  
📓 **Notebook:** [(Part 1/3) Data Cleaning – Preparing the Dataset](https://www.kaggle.com/code/m7mdabobakr/part-1-3-data-cleaning-preparing-the-dataset)  

---

## 📊 Dataset Overview  

- **219,222 patients** after cleaning  
- **19 columns** covering demographics, comorbidities, and outcomes  
- **Features include:**  
  - Gender, Age, Pregnant  
  - Chronic diseases: Diabetes, Hypertension, COPD, Asthma, Cardiovascular, Obesity, Renal Chronic, Immunosuppression  
  - Lifestyle: Tobacco use  
  - Target: **Classification** (COVID diagnosed vs. not diagnosed)  
  - Mortality indicators: Dead, Dead Year, Dead Month  

---

## 🚀 Features of the Dashboard  

The dashboard is divided into two interactive sections:  

### 🏠 Home / EDA  
- Dataset introduction and summary  
- Interactive visualizations of demographics and comorbidities  
- Feature distributions  

### 🤖 Prediction Model  
- Input patient health details to predict **COVID diagnosis**  
- **Best performance metric:**  
  - **Recall: 74%** (prioritizing sensitivity over accuracy to reduce false negatives)  
- Displays classification results directly in the app  

---

## 🛠️ Tech Stack  

- **Python 3.10+**  
- **Streamlit** – interactive web app  
- **Plotly Express** – data visualization  
- **Pandas** – data manipulation  
- **scikit-learn** – machine learning models & evaluation  
