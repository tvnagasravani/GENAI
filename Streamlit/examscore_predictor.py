import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


data = pd.read_csv("student_performance.csv")

data.head()

X = data.iloc[:,:-1]
Y = data['exam_score']


Y.head()

X.head()

model = LinearRegression()

model.fit(X,Y)

st.title("Exam Score Prediction ")

st.sidebar.title("Input Features")

study_hours = st.sidebar.slider("Number of Study hours",min_value=0,max_value=24,value=10)

attendance_percent = st.sidebar.slider("Attendance Hours",min_value=50,max_value=100,value = 59)

previous_score = st.sidebar.slider("Previous score",min_value=0,max_value=100,value = 35)

sleep_hours = st.sidebar.slider("Number of Sleep hours",0,12 ,8)

name = st.text_input("Please enter your name : ")

if name :
    st.text(f"Hi! , {name}")

    


button = st.sidebar.button("Predict Score")

if name and not button :
    st.text("Please provide the values with the help of slider  ")


if button : 
    input_features = [[study_hours,attendance_percent,previous_score,sleep_hours]]

    prediction = model.predict(input_features)





    st.metric("Predicted Exam Score", f"{prediction[0]:.2f} / 100")

    