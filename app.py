import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title("Student Pass/Fail Prediction")

study_hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance (%)")
previous_marks = st.number_input("Previous Marks")

if st.button("Predict"):
    result = model.predict([[study_hours, attendance, previous_marks]])

    if result[0] == 1:
        st.success("Pass ✅")
    else:
        st.error("Fail ❌")
