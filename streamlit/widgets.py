import streamlit as st
import pandas as pd


st.title("Streamlit Text input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age", 0,100,25)

st.write(f"Your age: {age}")

options=["Python","java","c++","Javascript"]
choice = st.selectbox("choose your fav language:", options)
st.write(f"You selected: {choice}.")


if name:
    st.write(f"Hello,{name}")

data={
    "Name":["Ankur","raj","nakul","Gill"],
    "Age":[28,44,12,1],
    "City":["INDIA","LA","chicago","new york"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("choose a CSV file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)