import streamlit as st
from dateutil.parser import parse
from datetime import datetime

tasks = {}

def add_task(task_id, description, due_time):
    tasks[task_id] = {"description": description, "due_time": due_time, "completed": False}

def show_tasks():
    if not tasks:
        st.write("No tasks available.")
    else:
        for task_id, task in tasks.items():
            status = "✅ Completed" if task['completed'] else "❌ Not Completed"
            st.write(f"ID: {task_id}, Task: {task['description']}, Due: {task['due_time']}, Status: {status}")

def complete_task(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        st.success(f"Task {task_id} marked as completed.")
    else:
        st.error("Task ID not found.")

st.title("Personal Task Assistant")

menu = st.sidebar.selectbox("Menu", ["Add Task", "List Tasks", "Complete Task"])

if menu == "Add Task":
    description = st.text_input("Task Description")
    due_time = st.text_input("Due Time (e.g., 'Tomorrow 4 PM')")
    if st.button("Add Task"):
        try:
            due_time_parsed = parse(due_time, fuzzy=True)
            task_id = len(tasks) + 1
            add_task(task_id, description, due_time_parsed)
            st.success(f"Task added: {description} (Due: {due_time_parsed})")
        except Exception:
            st.error("Invalid due time. Please try again.")

elif menu == "List Tasks":
    st.header("Current Tasks")
    show_tasks()

elif menu == "Complete Task":
    task_id = st.number_input("Enter Task ID", min_value=1, step=1)
    if st.button("Complete Task"):
        complete_task(task_id)
