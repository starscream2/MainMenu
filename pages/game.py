import streamlit as st
import random

# --- DATA: THE FULL 30 QUESTIONS ---
QUESTIONS = [
    {"q": "Under the Real Property Act (RPA), what is the 'Curtain Principle'?", "a": "B", "options": ["A) The right to hide the owner's name.", "B) The register is the sole source of information; no need to look behind it.", "C) Taxes are hidden from the public.", "D) The deed is kept in a dark room."]},
    {"q": "What is 'Escheat' in T&T land law?", "a": "C", "options": ["A) Cheating on a land survey.", "B) A type of mortgage.", "C) Reversion of property to the State if there are no heirs.", "D) Building on someone else's land."]},
    {"q": "A 'Search' at the Registrar General's office for Old Law land is meant to:", "a": "A", "options": ["A) Verify the 'Chain of Title' is unbroken.", "B) See how much the agent is getting paid.", "C) Check if the neighbors are nice.", "D) Find buried treasure."]},
    {"q": "Under RPO, a 'Caveat' is used to:", "a": "D", "options": ["A) Speed up a sale.", "B) Reduce stamp duty.", "C) Change the land use to commercial.", "D) Forbid the registration of any dealing with the land until a claim is settled."]},
    {"q": "The 'Insurance Principle' in the Torrens system means:", "a": "B", "options": ["A) You must buy fire insurance.", "B) The State compensates those who lose interest due to administrative error.", "C) The agent must have life insurance.", "D) The bank is insured against default."]},
    {"q": "Which of these is NOT a requirement for an individual license under the 2020 Act?", "a": "D", "options": ["A) Being at least 18 years old.", "B) Being a fit and proper person.", "C) Having the required educational qualifications.", "D) Owning at least three properties in T&T."]},
    {"q": "The 'Committee' established under the 2020 Act is the:", "a": "A", "options": ["A) Real Estate Discharge Committee.", "B) Real Estate Agents Licensing Committee.", "C) Property Tax Committee.", "D) FIU Oversight Body."]},
    {"q": "If an agent changes their business address, they must notify the Registrar within:", "a": "B", "options": ["A) 24 hours.", "B) 5 working days.", "C) 30 days.", "D) 1 year."]},
    {"q": "An 'Auctioneer' selling land in T&T:", "a": "C", "options": ["A) Needs no license.", "B) Must be a lawyer.", "C) Must be a licensed real estate agent or specifically exempted.", "D) Must work for the Central Bank."]},
    {"q": "A 'Property Developer' selling their own developed units:", "a": "A", "options": ["A) Is considered an 'Agent' under the 2020 Act and must be licensed.", "B) Is totally exempt from all laws.", "C) Only needs a driver's license.", "D) Must pay the buyer a commission."]},
    {"q": "What is 'Layering' in money laundering?", "a": "B", "options": ["A) Painting a house with multiple coats.", "B) Moving money through complex transactions to hide its origin.", "C) Buying land in different countries.", "D) Subdividing a large estate."]},
    {"q": "A 'Compliance Officer' in a real estate firm is responsible for:", "a": "C", "options": ["A) Making sure the office is clean.", "B) Checking the sales targets.", "C) Ensuring the firm follows FIU and AML/CFT laws.", "D) Valuing the properties."]},
    {"q": "For AML purposes, 'UBO' stands for:", "a": "A", "options": ["A) Ultimate Beneficial Owner.", "B) Under-Budget Option.", "C) United Business Office.", "D) Universal Bank Operator."]},
    {"q": "An agent must file a Terrorist Property Report (TPR) to the FIU:", "a": "D", "options": ["A) Monthly.", "B) Annually.", "C) Only if they feel like it.", "D) Immediately if they have property in their possession linked to a terrorist."]},
    {"q": "In T&T, 'Structuring' (Smurfing) involves:", "a": "B", "options": ["A) Designing a better house.", "B) Breaking down large cash sums into small amounts to avoid reporting thresholds.", "C) Building multiple houses on one lot.", "D) Creating a fake real estate company."]},
    {"q": "The 'Residual Method' is primarily used to value:", "a": "C", "options": ["A) Old houses.", "B) Government buildings.", "C) Land with development or redevelopment potential.", "D) Rented apartments."]},
    {"q": "What is 'Market Value'?", "a": "A", "options": ["A) The estimated price between a willing buyer and willing seller at arm's length.", "B) The price the owner wants.", "C) The price the bank says it is worth for a quick sale.", "D) The tax assessment value."]},
    {"q": "A 'Valuation Report' in T&T must be signed by:", "a": "D", "options": ["A) The Real Estate Agent.", "B) The Lawyer.", "C) The Buyer.", "D) A qualified professional Valuer (usually a member of RICS or similar)."]},
    {"q": "The 'Investment Method' uses 'Years Purchase' (YP). What does YP represent?", "a": "B", "options": ["A) The number of years the owner has held the property.", "B) The multiplier used to convert annual income into capital value.", "C) The age of the building.", "D) The length of the mortgage."]},
    {"q": "In construction, 'Liquidated Damages' are:", "a": "C", "options": ["A) Damage caused by a flood.", "B) Money paid to the agent if the sale fails.", "C) A pre-agreed sum paid by a contractor for late completion.", "D) The cost of tearing down a wall."]},
    {"q": "A 'Fixed Rate Mortgage' means:", "a": "A", "options": ["A) The interest rate stays the same for a set period.", "B) The house is fixed to the ground.", "C) The bank cannot sell the house.", "D) The price of the house is fixed."]},
    {"q": "What is an 'Equity' in a property?", "a": "C", "options": ["A) The total debt.", "B) The legal title.", "C) The market value minus any outstanding mortgages/liens.", "D) The monthly rent."]},
    {"q": "In T&T, 'Stamp Duty' on a $2.5 Million residential property is roughly:", "a": "B", "options": ["A) 0% (Exempt).", "B) Calculated on a tiered scale (5%, 7.5%, etc.).", "C) Flat fee of $500.", "D) Paid by the government."]},
    {"q": "An 'Encroachment' occurs when:", "a": "D", "options": ["A) A tenant leaves early.", "B) A buyer backs out.", "C) The bank raises interest rates.", "D) A neighbor builds a structure that crosses the property boundary line."]},
    {"q": "Which of the following is an 'Incorporeal Hereditament'?", "a": "A", "options": ["A) An Easement (Right of Way).", "B) A physical house.", "C) A bag of cement.", "D) A fence."]},
    {"q": "Who pays the 'Deed of Lease' preparation fee usually?", "a": "B", "options": ["A) The Landlord.", "B) The Tenant.", "C) The Agent.", "D) The FIU."]},
    {"q": "What is a 'Negative Covenant'?", "a": "C", "options": ["A) A bad review of the agent.", "B) A debt owed to the bank.", "C) A promise NOT to do something on the land (e.g., no commercial use).", "D) An unsigned contract."]},
    {"q": "What is 'Adverse Possession' in T&T?", "a": "A", "options": ["A) Gaining legal title to land by occupying it without permission for 16+ years (Old Law).", "B) Buying land from the state.", "C) Renting a property for a long time.", "D) Inheriting property from a stranger."]},
    {"q": "A 'Qualified Title' under RPO means:", "a": "B", "options": ["A) The owner is a qualified doctor.", "B) The title has some reservation or defect that the Registrar has noted.", "C) The title is perfect.", "D) The land is for farming only."]},
    {"q": "What is the 'Highest and Best Use' concept in valuation?", "a": "D", "options": ["A) Building the tallest skyscraper possible.", "B) Using the land for a park.", "C) Selling the land as quickly as possible.", "D) The use that is legally permissible, physically possible, and results in the highest value."]}
]

st.set_page_config(page_title="T&T Real Estate Tycoon", page_icon="💰")

# --- INITIALIZE STATE ---
if 'game_data' not in st.session_state:
    # Randomly select 10 questions each time
    st.session_state.game_data = random.sample(QUESTIONS, 10)
    st.session_state.submitted = False

st.title("💰 Real Estate Tycoon Challenge")
st.markdown("### Close the deals and build your empire!")

# --- THE GAME FORM ---
with st.form("game_form"):
    user_answers = []
    for i, item in enumerate(st.session_state.game_data):
        st.markdown(f"### Deal #{i+1}")
        # Note: choice[0] extracts 'A', 'B', 'C', or 'D' from the option string
        choice = st.radio(item['q'], item['options'], key=f"g{i}", index=None)
        user_answers.append(choice[0] if choice else None)
        st.divider()
    
    submitted = st.form_submit_button("Finalize All Deals")

if submitted:
    st.session_state.submitted = True
    score = sum(1 for i, item in enumerate(st.session_state.game_data) if user_answers[i] == item['a'])
    commission = score * 25000 
    
    st.balloons()
    st.header(f"💼 Total Commission Earned: ${commission:,}")
    
    # Milestone Rewards
    if score == 10:
        st.success("🏆 RANK: MANAGING BROKER")
        st.image("http://googleusercontent.com/image_collection/image_retrieval/11496554388869851435_0", caption="Top Performer!")
    elif score >= 7:
        st.info("🏢 RANK: SENIOR NEGOTIATOR")
        st.image("http://googleusercontent.com/image_collection/image_retrieval/17837677463845512802_0")
    elif score >= 5:
        st.warning("💼 RANK: LICENSED AGENT")
    else:
        st.error("📎 RANK: INTERN")

    # Incorrect Answer Review
    with st.expander("📝 Review Your Negotiations"):
        for i, item in enumerate(st.session_state.game_data):
            status = "✅ Correct" if user_answers[i] == item['a'] else "❌ Incorrect"
            st.markdown(f"**Deal #{i+1}:** {status}")
            if user_answers[i] != item['a']:
                # Find the text of the correct option
                correct_text = next((opt for opt in item['options'] if opt.startswith(item['a'])), item['a'])
                st.write(f"The correct move was: **{correct_text}**")
            st.divider()

if st.session_state.submitted:
    if st.button("Start New Career (Restart)"):
        # Reset questions and submission state
        del st.session_state['game_data']
        st.session_state.submitted = False
        st.rerun()
