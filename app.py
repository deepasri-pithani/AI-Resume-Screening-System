import streamlit as st
import pandas as pd

st.title("AI Resume Screening System")

st.write("Candidate Ranking System")

if st.button("Show Results"):
    result = pd.read_csv("output/candidate_ranking.csv")
    st.dataframe(result)