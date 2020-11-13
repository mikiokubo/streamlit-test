import streamlit as st
import pandas as pd 
import plotly.express as px

st.title("Covid-19 Analytics")
st.subheader("コロナの死者数のデモ")

df = pd.read_csv("COVID-19.csv")
df["date"] = pd.to_datetime(df.dateRep)

st.write(df.head())

fig = px.line(df,x="date",y="deaths",color="countriesAndTerritories")
st.write(fig)