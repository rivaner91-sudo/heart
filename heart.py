import numpy as np
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier


st.write(''' # Predicción de enfermedad del corazon ''')
st.image("enfermedades-del-corazon.jpg", caption="Las enfermedades del corazon son muy peligrosas")

st.header('Datos de evaluación')

def user_input_features():
  # Entrada
  cp	= st.number_input('paro cardiaco:', min_value=0, max_value=0, value = 1, step = 1)
  Sex = st.number_input('Género:', min_value=0, max_value=1, value = 0, step = 1)
  Age = st.number_input('Edad:', min_value=0, max_value=100, value = 0, step = 1)
  chol = st.number_input('colesterol:',min_value=0, max_value=500, value = 0, step = 1)
  fbs= st.number_input('fibrosis:', min_value=0, max_value=1, value = 0, step = 1)
  restecg= st.number_input('restecg:', min_value=0, max_value=2, value = 0, step = 1)
  thalach= st.number_input('thalach:', min_value=0, max_value=2, value = 0, step = 1)
  slop= st.number_input('slop:', min_value=0, max_value=2, value = 0, step = 1)
  ca= st.number_input('ca:', min_value=0, max_value=2, value = 0, step = 1)

user_input_data = {'Sex': Sex,
                  'Age': Age,
                   'cp': cp,
                   'trestbps': trestbps,
                   'chol': chol,
                   'fbs': fbs,
                   'restecg': restecg,
                   'thalach': thalach,
                   'slop,': slop,
                   'ca': ca,
                     }
                     #'Fare': Fare,
                     #'Embarked': Embarked}

features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()

heart =  pd.read_csv('Heart2.csv', encoding='latin-1')

X = df.drop(cp_column, axis=1)
y = df[cp_column]

#X = titanic.drop(columns='Survived')
#Y = titanic['Survived']

classifier = DecisionTreeClassifier(max_depth=9, criterion='entropy', min_samples_leaf=5, max_features=4, random_state=0)
classifier.fit(X, Y)

prediction = classifier.predict(df)

st.subheader('Predicción')
if prediction == 0:
  st.write('enfermedad')
elif prediction == 1:
  st.write('no enfermedad')
else:
  st.write('Sin predicción')
