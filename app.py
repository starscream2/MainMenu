import streamlit as st

st.set_page_config(page_title="T&T Real Estate Portal", page_icon="🏠")

# --- HEADER IMAGE ---
st.image("http://googleusercontent.com/image_collection/image_retrieval/14747018523017416153_0", use_container_width=True)

st.title("🇹🇹 T&T Real Estate Learning Portal")
st.markdown("""
    Welcome to your all-in-one preparation hub for the **T&T Real Estate Agents Board Exam**. 
    Choose your path below to get started!
""")

# --- NAVIGATION BUTTONS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Practice")
    if st.button("📝 Standard Exam"):
        st.switch_page("pages/exam.py")

with col2:
    st.subheader("Challenge")
    if st.button("💰 Tycoon Game"):
        st.switch_page("pages/game.py")

with col3:
    st.subheader("Review")
    if st.button("📚 Study Guide"):
        st.switch_page("pages/study_guide.py")

st.divider()
st.caption("Covers: Real Estate Agents Act 2020, RPO, Old Law, and AML/CFT Compliance.")
