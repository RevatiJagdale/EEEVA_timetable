import streamlit as st
import pandas as pd
from timetable_module import Timetable

# Load timetable
TT_FILE = "data/timetable.csv"
tt = Timetable(TT_FILE)

st.title("EEEVA - Timetable Module")
st.write("Query the departmental timetable interactively")

# Sidebar menu
option = st.sidebar.selectbox(
    "Choose a function",
    ("Faculty Schedule", "Subject Teachers", "Free Slots")
)

if option == "Faculty Schedule":
    faculty = st.text_input("Enter faculty username (e.g., sunitakulkarni)")
    if faculty:
        result = tt.get_faculty_schedule(faculty)
        st.write(result if not result.empty else "No records found.")

elif option == "Subject Teachers":
    subject = st.text_input("Enter subject name (e.g., Data Analytics)")
    if subject:
        result = tt.get_subject_teachers(subject)
        st.write(result if not result.empty else "No records found.")

elif option == "Free Slots":
    faculty = st.text_input("Enter faculty username (leave blank if not needed)")
    division = st.text_input("Enter division (leave blank if not needed)")
    if faculty or division:
        result = tt.find_free_slots(
            faculty_name=faculty if faculty else None,
            division=division if division else None
        )
        st.write(result if not result.empty else "No free slots found.")
