import streamlit as st
import random

# --- DATA: THE 30 QUESTIONS ---
QUESTIONS = [
    {"q": "Under the Real Property Act (RPA), what is the 'Curtain Principle'?", "a": "B", "options": ["A) The right to hide the owner's name.", "B) The register is the sole source of information; no need to look behind it.", "C) Taxes are hidden from the public.", "D) The deed is kept in a dark room."]},
    # ... [Keep all 30 questions here] ...
]

if 'game_data' not in st.session_state:
    st.session_state.game_data = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.game_submitted = False

st.title("💰 Real Estate Tycoon Challenge")
st.markdown("### Close the deals and build your empire!")

with st.form("game_form"):
    user_answers = []
    for i, item in enumerate(st.session_state.game_data):
        st.markdown(f"**Deal #{i+1}:** {item['q']}")
        choice = st.radio("Choose your move:", item['options'], key=f"g{i}", index=None)
        user_answers.append(choice[0] if choice else None)
        st.divider()
    
    submitted = st.form_submit_button("Finalize All Deals")

if submitted:
    st.session_state.game_submitted = True
    score = sum(1 for i, item in enumerate(st.session_state.game_data) if user_answers[i] == item['a'])
    percent = (score / len(st.session_state.game_data)) * 100
    commission = score * 10000 
    
    st.header(f"Total Commission Earned: ${commission:,}")
    st.progress(score / len(st.session_state.game_data))

    # --- GAMIFIED REWARDS & IMAGES ---
    if percent == 100:
        st.success("🏆 RANK: MANAGING BROKER (CEO Status)")
        st.image("http://googleusercontent.com/image_collection/image_retrieval/11496554388869851435_0", caption="You've earned the Broker of the Year Trophy!")
        st.balloons()
    elif percent >= 80:
        st.success("🏢 RANK: SENIOR NEGOTIATOR")
        st.image("http://googleusercontent.com/image_collection/image_retrieval/17837677463845512802_0", caption="New Office Unlocked: Luxury Penthouse Suite")
    elif percent >= 60:
        st.warning("💼 RANK: LICENSED AGENT")
        st.image("http://googleusercontent.com/image_collection/image_retrieval/6812034333723871614_0", caption="Credential Unlocked: Certificate of Enrollment")
    elif percent >= 40:
        st.info("📂 RANK: JUNIOR ASSOCIATE")
        st.image("http://googleusercontent.com/image_collection/image_retrieval/15727273888450215261_0", caption="Workspace Unlocked: Professional Executive Desk")
    else:
        st.error("📎 RANK: REAL ESTATE INTERN")
        st.write("Keep practicing to unlock your first office item!")

    # Review Section
    incorrect_indices = [i for i, item in enumerate(st.session_state.game_data) if user_answers[i] != item['a']]
    if incorrect_indices:
        with st.expander("📝 Review Failed Negotiations"):
            for idx in incorrect_indices:
                q_item = st.session_state.game_data[idx]
                st.markdown(f"**Deal #{idx+1} Failed:** {q_item['q']}")
                correct_text = next((opt for opt in q_item['options'] if opt.startswith(q_item['a'])), q_item['a'])
                st.write(f"✅ **The Correct Move Was:** {correct_text}")
                st.divider()

if st.session_state.game_submitted:
    if st.button("Start New Career"):
        st.session_state.game_data = random.sample(QUESTIONS, len(QUESTIONS))
        st.session_state.game_submitted = False
        st.rerun()
