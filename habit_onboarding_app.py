import streamlit as st
from datetime import time


# Initialize session state to store user data
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.focus_areas = []
    st.session_state.habits = []
    st.session_state.reminders = {"enabled": False, "time": "09:00 AM"}

# Step 1: Welcome Screen
if st.session_state.step == 1:
    st.title("Welcome to HabitFlow")
    st.subheader("Build small habits, achieve big goals.")
    if st.button("Get Started"):
        st.session_state.step = 2

# Step 2: Focus Areas
elif st.session_state.step == 2:
    st.title("Focus Areas")
    st.subheader("Select the areas you want to improve:")
    health = st.checkbox("Health")
    education = st.checkbox("Education")
    
    if st.button("Next"):
        if health:
            st.session_state.focus_areas.append("Health")
        if education:
            st.session_state.focus_areas.append("Education")
        st.session_state.step = 3

# Step 3: Initial Habits
elif st.session_state.step == 3:
    st.title("Set Your Initial Habits")
    st.subheader("Here are some suggested habits. Feel free to edit them.")
    
    habits = []
    if "Health" in st.session_state.focus_areas:
        habits.append(st.text_input("Habit 1 (Health):", "Drink 2L water daily"))
        habits.append(st.text_input("Habit 2 (Health):", "Walk 5,000 steps"))
    if "Education" in st.session_state.focus_areas:
        habits.append(st.text_input("Habit 1 (Education):", "Read for 15 minutes"))
        habits.append(st.text_input("Habit 2 (Education):", "Review one chapter daily"))
    
    if st.button("Save Habits"):
        st.session_state.habits = habits
        st.session_state.step = 4

# Step 4: Reminders
elif st.session_state.step == 4:
    st.title("Set Reminders")
    reminder_enabled = st.checkbox("Enable reminders", value=st.session_state.reminders["enabled"])
    reminder_time = st.time_input("Reminder Time", value=time(9, 0))  # 9:00 AM
    
    if st.button("Finish"):
        st.session_state.reminders = {"enabled": reminder_enabled, "time": reminder_time}
        st.session_state.step = 5

# Step 5: Dashboard Introduction
elif st.session_state.step == 5:
    st.title("Dashboard Introduction")
    st.write("Track your habits and see your progress here.")
    st.success("You're all set to start building habits!")
    if st.button("Go to Habit Tracker"):
        st.write("🚧 Habit Tracker Under Construction 🚧")
