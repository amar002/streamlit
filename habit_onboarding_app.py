import streamlit as st
from datetime import time, datetime, timedelta
from dateutil.parser import parse
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
import random

# Initialize session state to store user data
if "habits_data" not in st.session_state:
    st.session_state.habits_data = [
        {"name": "Drink 2L water", "due": "Today", "status": "Pending"},
        {"name": "Read 15 pages", "due": "Today", "status": "Pending"},
        {"name": "Walk 5000 steps", "due": "Tomorrow", "status": "Upcoming"}
    ]

# Dashboard View
st.title("Habit Dashboard")

# Section 1: Add Habits Directly
with st.expander("Add New Habit", expanded=True):
    st.write("### Create a New Habit")
    new_habit_name = st.text_input("Habit Name:", "")
    new_habit_due = st.selectbox("Due Date:", ["Today", "Tomorrow", "This Week"])
    if st.button("Add Habit"):
        if new_habit_name.strip():
            st.session_state.habits_data.append({"name": new_habit_name, "due": new_habit_due, "status": "Pending"})
            st.success(f"Habit '{new_habit_name}' added successfully!")
        else:
            st.error("Please enter a valid habit name.")

# Section 2: Overall Habits
with st.expander("Overall Habits", expanded=True):
    st.write("### All Habits Overview")
    for habit in st.session_state.habits_data:
        progress = 100 if habit["status"] == "Completed" else 0
        st.write(f"{habit['name']} - Status: {habit['status']}")
        st.progress(progress / 100)

# Section 3: Habits for This Week
with st.expander("Habits for This Week", expanded=True):
    st.write("### Weekly Habits Schedule")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        st.write(f"#### {day}")
        for habit in st.session_state.habits_data:
            if habit["due"] in ["Today", "This Week"]:
                st.write(f"- {habit['name']} - Due: {habit['due']}")

# Section 4: Today's Habits
with st.expander("Today's Habits", expanded=True):
    st.write("### Habits for Today")
    for habit in st.session_state.habits_data:
        if habit["due"] == "Today":
            st.write(f"📝 {habit['name']}")
            progress = 100 if habit["status"] == "Completed" else 0
            st.progress(progress / 100)
            if st.button("Mark as Done", key=habit["name"]):
                habit["status"] = "Completed"
                st.success(f"Completed: {habit['name']}")

# Footer
st.write("---")
st.write("Keep building small habits daily! 🚀")
