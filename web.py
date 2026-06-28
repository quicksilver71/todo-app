import streamlit as st
import functions

todos = functions.get_todos()
st.title("To-Do App")
st.subheader("This is my todos app")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="add new todo...")