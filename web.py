import streamlit as st
from modules import functions as f

todos = f.get_todos()
testing = False

def add_todo():
    local_todo = st.session_state['new_todo'] + '\n'
    #print(f"local_todo: {local_todo}")
    todos.append(local_todo)
    f.write_todos(todos)


st.title("My Todo App")
st.subheader("This app is my todo app.")
st.write("This app is to increase productivity.")

for i, todo in enumerate( todos):
    todo_key = "st_" + str(i)
    todo_label = str(i)+') '
    chkbox = st.checkbox(todo, key=todo_key)
    if chkbox:
        todos.pop(i)
        f.write_todos(todos)
        del st.session_state[todo_key]
        st.rerun()


st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key='new_todo')

if testing:
    st.subheader("Debug information")
    st.session_state