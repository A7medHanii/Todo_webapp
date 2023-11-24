import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    # session_state is like adictionary that store user input
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("Todo App")

st.subheader("Created By Ahmed Hany...")

#st.write("this app to increase ur productivity")

# st.warning("error");
for index, todo in enumerate (todos):
   checkbox = st.checkbox(todo, key=todo)
   if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        #del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add A New Todo",on_change=add_todo,key="new_todo")
#st.session_state