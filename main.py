import streamlit as st
import pandas as pd 
import plotly.express as px

st.title("Test App")
st.write("Welcome")
df = pd.read_csv("covid-19.csv")
df["date"] = pd.to_datetime(df.dateRep)

st.write(df)
fig = px.line(df,x="date",y="deaths",color="countriesAndTerritories")
st.write(fig)