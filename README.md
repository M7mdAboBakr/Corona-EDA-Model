# 🦠 Corona Virus Patient Classification Dashboard  

An interactive Streamlit dashboard analyzing COVID-19 patient medical records and predicting diagnosis outcomes using Machine Learning.  

The dataset contains patient demographics and health conditions (e.g. age, diabetes, hypertension, obesity, etc.) with outcomes such as diagnosis.  

---

🔗 **Live Dashboard:** [Click Here](https://corona-eda-model.streamlit.app/)  
📂 **Dataset Source:** [Kaggle COVID-19 Clinical Data](https://www.kaggle.com/) *(replace with exact dataset link)*  
📓 **Notebook:** End-to-end EDA & Model Training included  

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
- Correlation heatmaps and feature distributions  

### 🤖 Prediction Model  
- Input patient health details to predict **COVID diagnosis**  
- Model trained on cleaned dataset  
- **Best performance metric:**  
  - **Recall: 74%** (prioritizing sensitivity over accuracy to reduce false negatives)  
- Displays classification results directly in the app  

---

## 🛠️ Tech Stack  

- **Python 3.10+**  
- **Streamlit** – interactive web app  
- **Plotly Express** – data visualization  
- **Pandas / NumPy** – data manipulation  
- **scikit-learn** – machine learning models & evaluation  
