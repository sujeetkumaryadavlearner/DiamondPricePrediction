import streamlit as st
import pandas as pd
import pickle


diamond = pd.read_csv("Cleaned_data_diamond.csv")
model = pickle.load(open("DecisionTree.pkl",'rb'))

st.title("Diamond Price Predictor")
carat=st.number_input("Enter Carat")
cut=st.selectbox("Cut",diamond["cut"].unique())
color=st.selectbox("Colour",diamond["color"].unique())
clarity=st.selectbox("Clarity",diamond["clarity"].unique())
depth=st.number_input("Enter Depth")
tabel=st.number_input("Enter Tabel")
x=st.number_input("Enter X")
y=st.number_input("Enter Y")
z=st.number_input("Enter Z")

if st.button("Predict Price"):

    st.title("The Price Of Diamond is : $"+str(int(round(model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, tabel, x, y, z,
       ]] , columns=["carat", "cut", "color", "clarity", "depth", "table", "x", "y", "z"]))[0]))))


