# Mini Project
# A TO-DO List Project
import streamlit as st
with st.container(border= True):
    if "task_list" not in st.session_state:
        st.session_state.task_list = []
    if "completed_task" not in st.session_state:
        st.session_state.completed_task = []
    st.header("TO-DO List")
    input_text = st.text_input("Write Your Task Here", placeholder="Do Shopping, Do Washing, Do Coding, so on...")
    # ADD TASK button
    add_btn = st.button("Add Task")
    # Button Task
    if add_btn == True:
        if input_text.strip():
            st.session_state.task_list.append(input_text.strip())
            st.success(f'{input_text} added successfully!')
        else:
            st.warning("No Task Added")
        st.subheader("Your Tasks: ")
    completed = []
    for i, val in enumerate(st.session_state.task_list):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f'- {val}')
        with col2:
            if st.checkbox ('', key=f'checkbox_{i}'):
                completed.append(val)
# Completed Task
st.session_state.completed_task = completed
with st.container(border=True):
    st.subheader("Completed Task")
    for task in st.session_state.completed_task:
        st.success("Task Completed")
        st.write(f'✅ {task}')

# .strip remove the white space, any extra tab spaces, new line spaces