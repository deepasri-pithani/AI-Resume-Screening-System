import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="AI Resume Screening", layout="wide")

st.title("🤖 AI Resume Screening System")
st.write("### Candidate Ranking System using NLP")

# Button
if st.button("Show Results"):

    # Read CSV
    result = pd.read_csv("output/candidate_ranking.csv")

    # Show Table
    st.subheader("📋 Candidate Ranking")
    st.dataframe(result)

    # Bar Chart
    st.subheader("📊 Match Percentage")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(result["Candidate Name"], result["Match %"])

    ax.set_xlabel("Candidate")

    ax.set_ylabel("Match Percentage")

    ax.set_title("Candidate Match Percentage")

    st.pyplot(fig)

    # Pie Chart
    st.subheader("🥧 Status Distribution")

    fig2, ax2 = plt.subplots(figsize=(6,6))

    status = result["Status"].value_counts()

    ax2.pie(
        status,
        labels=status.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax2.set_title("Candidate Status")

    st.pyplot(fig2)

    # Download CSV
    csv = result.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Candidate Ranking",
        data=csv,
        file_name="candidate_ranking.csv",
        mime="text/csv"
    )
