import streamlit as st

st.set_page_config(page_title="T&T Real Estate Portal", page_icon="🇹🇹")

st.title("🇹🇹 T&T Real Estate Learning Portal")
st.markdown("### Welcome! Choose your study mode below:")

# Three columns for three options
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Exam")
    if st.button("📝 Standard Exam"):
        st.switch_page("pages/exam.py")

with col2:
    st.subheader("Game")
    if st.button("💰 Tycoon Game"):
        st.switch_page("pages/game.py")

with col3:
    st.subheader("Guide")
    if st.button("📚 Study Guide"):
        st.switch_page("pages/study_guide.py")

st.divider()
st.info("Everything you need to pass the Real Estate Agents Board.")
