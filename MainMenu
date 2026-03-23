import streamlit as st

st.set_page_config(page_title="T&T Real Estate Portal", page_icon="🇹🇹")

st.title("🇹🇹 T&T Real Estate Learning Portal")
st.markdown("### Welcome! Choose your study mode below:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Standard Mode")
    if st.button("📝 Take Practice Exam"):
        st.switch_page("pages/exam.py")

with col2:
    st.subheader("Tycoon Mode")
    if st.button("💰 Play Tycoon Game"):
        st.switch_page("pages/game.py")

st.divider()
st.info("Both modes cover the Real Estate Agents Act 2020, RPO, and AML/CFT regulations.")
