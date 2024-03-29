import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import pickle

st.title("Titanic Survived Analysis and Prediction")

URL = 'titanic_final.csv'

df = pd.read_csv(URL)

st.write(df)

st.subheader('Survival Rate')
survival_counts = df['Survived'].value_counts()
st.text(f'Survival Rate {survival_counts.values[1] / sum(survival_counts):.2%}')

fig, ax = plt.subplots(1, 2, figsize=(15, 5))
survival_counts.plot.bar(ax=ax[0])
df['Age'].plot.hist(ax=ax[1])
st.pyplot(fig)

st.subheader('Making Prediction')

file_path = 'gnb.pkl'

with open(file_path , 'rb') as f:
    clf = joblib.load(f)

sex = st.selectbox('Sex', ['male', 'female'])
age = int(st.number_input('Age', 0, 120, 20))
sib_sp = int(st.number_input('# of siblings / spouse', 0, 10, 0))
parch = int(st.number_input('Parents ', 0, 100, 0))
p_class = int(st.selectbox('Ticket Class ', [1, 2, 3]))
fare = int(st.number_input('Fare', 0, 100, 0))
embarked = st.selectbox('Embarked', ['C','S','Q'])

prediction_state = st.markdown('calculating')

passenger = pd.DataFrame({
    'Pclass' : [p_class],
    'Sex' : [sex],
    'Age' : [age],
    'SibSp' : [sib_sp],
    'Parch' : [parch],
    'Fare' : [fare],
    'Embarked' : [embarked]
})

x_pred = clf.predict(passenger)

if x_pred[0] == 0:
    msg = 'Penumpangnya mati bos'
else:
    msg = 'Penumpangnya selamat bos'

prediction_state.markdown(msg)