import streamlit as st

st.set_page_config(page_title="T&T Real Estate Study Guide", page_icon="📚")

st.title("📚 Quick Revision Guide")
st.write("Essential summaries for the T&T Real Estate Exam.")

# --- TOPIC 1 ---
with st.expander("⚖️ Real Estate Agents Act 2020"):
    st.markdown("""
    * **Licensing:** You must be 18+, 'fit and proper', and have the required qualifications.
    * **The Committee:** The *Real Estate Agents Licensing Committee* handles the issuing of licenses.
    * **Address Changes:** You must notify the Registrar within **5 working days** of moving business locations.
    * **Developers:** Any developer selling their own units is considered an 'Agent' and must be licensed.
    """)

# --- TOPIC 2 ---
with st.expander("🏠 Land Law (RPO & Old Law)"):
    st.markdown("""
    * **Curtain Principle:** The Register is the sole source of truth; you don't need to look 'behind the curtain' for other interests.
    * **Insurance Principle:** The State compensates people for errors made by the registry.
    * **Caveat:** A formal notice to stop any land dealings until a claim is settled.
    * **Adverse Possession:** Under Old Law, 16+ years of undisputed occupation is required.
    * **Escheat:** Property goes back to the State if there are no heirs.
    """)

# --- TOPIC 3 ---
with st.expander("💰 AML/CFT & FIU"):
    st.markdown("""
    * **Layering:** Moving money through complex layers to hide the source.
    * **Structuring (Smurfing):** Breaking large cash amounts into small ones to avoid reporting limits.
    * **UBO:** Ultimate Beneficial Owner (who really owns the property).
    * **TPR:** Terrorist Property Reports must be filed **immediately** if suspicious property is found.
    """)

st.info("💡 Tip: Use the 'Tycoon Game' to test how well you remember these facts!")
