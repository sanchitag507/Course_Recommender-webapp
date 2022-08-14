import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# <==== Code starts here ====>

courses_list = pickle.load(open('/content/courses.pkl','rb'))
similarity = pickle.load(open('/content/similarity.pkl','rb'))

def recommend(course):
    index = courses_list[courses_list['Course Name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]]
        recommended_course_names.append(course_name)

    return recommended_course_names

st.markdown("<h2 style='text-align: center; color: blue;'>Coursera Course Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Web App created by Sagar Bapodara</h4>", unsafe_allow_html=True)

course_list = courses_list['Course Name'].values
selected_course = st.selectbox(
    "Type or select a course you like :",
    courses_list
)

if st.button('Show Recommended Courses'):
    st.write("Recommended Courses based on your interests are :")
    recommended_course_names = recommend(selected_course)
    st.text(recommended_course_names[0])
    st.text(recommended_course_names[1])
    st.text(recommended_course_names[2])
    st.text(recommended_course_names[3])
    st.text(recommended_course_names[4])
    st.text(recommended_course_names[5])
    st.text(" ")
    st.markdown("<h6 style='text-align: center; color: red;'>Copyright reserved by Coursera and Respective Course Owners</h6>", unsafe_allow_html=True)

# <==== Code ends here ====>