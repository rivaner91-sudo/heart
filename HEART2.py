import numpy as np
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier


st.write(''' # PREVENCION DE ENFERMEDADES DEL CORAZON''')
st.image("enfermedades-del-corazon.jpg", caption="estas a tiempo para cuidarte.")

st.header('Datos del futurto enfermo')

def user_input_features():
  # Entrada
 
  Age = st.number_input('Edad:', min_value=0, max_value=100, value = 0, step = 1)
  Sex = st.number_input('Género:', min_value=0, max_value=1, value = 0, step = 1)
  ca= st.number_input('Ataque del corazon:', min_value=0, max_value=1, value = 0, step = 1)
  exang= st.number_input('angina:', min_value=0, max_value=1, value = 0, step = 1)
  thalach= st.number_input('frecuaneic cardiaca:', min_value=0, max_value=500, value = 0, step = 1)
  cp= st.number_input('paro cardiaco:', min_value=0, max_value=1, value = 0, step = 1)
  slope= st.number_input('inclinacion:', min_value=0, max_value=180, value = 0, step = 1)
  chole= st.number_input('colesterol:', min_value=0, max_value=500, value = 0, step = 1)
  thal= st.number_input('thal:', min_value=0, max_value=1, value = 0, step = 1)
  oldpeak= st.number_input('pico antiguo:', min_value=0, max_value=500, value = 0, step = 1)
  trestbps= st.number_input('presion en reposo:', min_value=0, max_value=500, value = 0, step = 1)
  fbs= st.number_input('fibrosis:', min_value=0, max_value=800, value = 0, step = 1)
  restecg= st.number_input('restecg:', min_value=0, max_value=1, value = 0, step = 1)


  user_input_data = {'Age': Edad,
                     'Sex': Sexo,
                     'ca': ataque del corazon,
                     'exang': angina,
                     'thalach': frecuencia cardiaca,
                     'cp': paro cardiaco,
                     'slope': inclinacion,
                     'chole': colesterol,
                     'thal': thal,
                     'oldpeak': pico antiguo,
                     'trestbps': presion en reposo,
                     'fbs': fibrosis,
                     'restecg': restecg
                     }


  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()

HEART2 =  pd.read_csv('HEART2csv', encoding='latin-1')

X = df.drop(target_column, axis=1)
y = df[target_column]


classifier = DecisionTreeClassifier(max_depth=5, criterion='entropy', min_samples_leaf=10, max_features=5, random_state=0)
classifier.fit(X, Y)

prediction = classifier.predict(df)

st.subheader('Predicción')
if prediction == 0:
  st.write('No estara enfermo')
elif prediction == 1:
  st.write('si estara enfermo')
else:
  st.write('Sin predicción')
