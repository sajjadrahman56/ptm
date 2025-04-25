import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# New CSV file name
DATA_FILE = 'ptm_data.csv'

GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY") 

if not GEMINI_API_KEY:
    st.error("Gemini API key is missing. Please set the GEMINI_API_KEY environment variable or Streamlit secret.")
else:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')

@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        st.error(f"Error: The file '{DATA_FILE}' was not found. Make sure it's in the same directory as the app.")
        return pd.DataFrame()

data = load_data()

def generate_gemini_suggestions(student_data, parent_feedback, max_words=100):  # Added max_words
    """Generates suggestions using the Gemini API with a word limit."""

    prompt = f"""
    You are a helpful teacher providing concise suggestions to parents (within {max_words} words) based on their child's performance and their feedback.
    Student Performance Data:
    Name: {student_data['Name']}
    Math: {student_data['Math']}
    Science: {student_data['Science']}
    English: {student_data['English']}
    Attendance: {student_data['Attendance (%)']}%
    Strengths: {student_data['Strengths']}
    Weaknesses: {student_data['Weaknesses']}
    Teacher's Comments: {student_data['Comments']}
    Existing Suggestions: {student_data['Suggestions']}
    Parent Feedback: {parent_feedback}

    Generate 2-3 actionable suggestions for parents to support their child's learning. 
    Keep responses short and practical, aiming for approximately {max_words} words or less.
    """

    try:
        response = model.generate_content(prompt)
        # Word limit enforced inside the prompt itself
        return response.text
    except Exception as e:
        st.error(f"Error generating suggestions from Gemini API: {e}")
        return "Unable to generate suggestions at this time."

def save_feedback(student_name, parent_feedback):
    """Saves parent feedback to the DataFrame and CSV."""
    data.loc[data['Name'] == student_name, 'Parent Feedback'] = parent_feedback
    data.to_csv(DATA_FILE, index=False)
    st.success("Feedback saved!")

if not data.empty:
    # App Title
    st.title("Parent-Teacher Meeting Dashboard")

    # Student selection
    student_name = st.selectbox("Select your child:", data['Name'].unique())

    # Filter selected student
    student_data = data[data['Name'] == student_name].iloc[0]

    # Display report
    st.subheader("Academic Performance")
    cols_performance = st.columns(len(['Math', 'Science', 'English']))
    subjects = ['Math', 'Science', 'English']
    for i, subject in enumerate(subjects):
        cols_performance[i].metric(subject, student_data[subject])

    st.subheader("Attendance")
    st.metric("Attendance", f"{student_data['Attendance (%)']}%")

    st.subheader("Strengths & Weaknesses")
    st.write(f"**Strengths:** {student_data['Strengths']}")
    st.write(f"**Weaknesses:** {student_data['Weaknesses']}")

    st.subheader("Teacher's Comments")
    st.info(student_data['Comments'])

    # Parent Feedback Input
    parent_feedback = st.text_area("Parent Feedback:", value=data.loc[data['Name'] == student_name, 'Parent Feedback'].iloc[0] if 'Parent Feedback' in data.columns and not data[data['Name'] == student_name]['Parent Feedback'].isnull().all() else "")

    if st.button("Generate Suggestions"):
        if GEMINI_API_KEY:
            dynamic_suggestions = generate_gemini_suggestions(student_data, parent_feedback)  # No max_words here now
            st.subheader("Dynamic Suggestions for Parents (Powered by Gemini)")
            st.success(dynamic_suggestions)
        else:
            st.warning("Please set the Gemini API key to generate dynamic suggestions.")

    if st.button("Save Feedback"):
        save_feedback(student_name, parent_feedback)
else:
    st.warning("No student data available. Please ensure the CSV file is correctly loaded.")
