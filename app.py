import streamlit as st
import numpy as np
import pickle
import joblib

with open('diabetes_model.pkl','rb') as file:
    model = pickle.load(file)
st.title("Diabetes Prediction App")

st.write("Enter the following health details:")
age = st.slider("Age", 0, 100, 25)
plas= st.slider("Plasma Glucose", 0, 200, 100)
pres = st.slider("Diastolic Blood Pressure", 0, 200, 120)
skin = st.slider("Triceps Skin Fold Thickness", 0, 100, 20)
insu = st.slider("2-Hour Serum Insulin", 0, 1000, 70)
mass = st.slider("Body Mass Index", 0.0, 50.0, 25.0)
preg= st.slider("Number of Pregnancies", 0, 20, 0)
pedi = st.slider("Diabetes Pedigree Function", 0.0, 2.0, 0.5)


if st.button("Predict"):
    features = np.array([[age,plas,pres,skin,insu,mass,pedi,preg]])
    prediction = model.predict(features)[0]

    st.subheader("Prediction Result:")
    st.write(f"Predicted probability of having diabetes: *{prediction:.2f}*")
if submit:
    # Ensure order matches training data
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
        prediction = model.predict(input_data)[0]
    # Moved this section inside the button click block
    if prediction == 1:
        st.error("Warning: High chance of diabetes")
    else:
        st.success("Low chance of diabetes")
