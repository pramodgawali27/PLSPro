import streamlit as st
from streamlit_quill import st_quill

# Initialize session state variables
if "selected_area" not in st.session_state:
    st.session_state.selected_area = None
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None
if "custom_prompt" not in st.session_state:
    st.session_state.custom_prompt = ""

# 🔹 Define Therapeutic Areas and Product-Specific Prompts
THERAPEUTIC_PROMPTS = {
    "Oncology": [
        "Summarize the latest breast cancer study.",
        "Explain how pembrolizumab works in lung cancer.",
        "Compare different immunotherapy treatments for melanoma."
    ],
    "Cardiology": [
        "Describe the effects of beta-blockers on heart failure patients.",
        "Summarize findings of the latest atrial fibrillation study.",
        "Explain how a new pacemaker device improves heart function."
    ],
    "Neurology": [
        "How does this medication affect Alzheimer's disease progression?",
        "Summarize the latest findings on Parkinson’s disease treatment.",
        "Compare different epilepsy medications."
    ],
    "Diabetes": [
        "Explain how SGLT2 inhibitors help patients with Type 2 Diabetes.",
        "Summarize the latest research on insulin therapy.",
        "What does this study mean for Type 1 Diabetes patients?"
    ]
}

# 🔹 Streamlit UI Layout
st.set_page_config(page_title="Medical PLS Generator", layout="wide")
st.title("Medical Plain Language Summary Generator")

# 🔹 Sidebar for Navigation
with st.sidebar:
    st.header("Select Options")

    # 1️⃣ Select Therapeutic Area
    selected_area = st.selectbox("Select Therapeutic Area", ["Select"] + list(THERAPEUTIC_PROMPTS.keys()), index=0)

    # 2️⃣ Select Product-Specific Prompt (Dynamically Loaded)
    if selected_area != "Select":
        selected_prompt = st.selectbox("Select a Predefined Prompt", ["Select"] + THERAPEUTIC_PROMPTS[selected_area], index=0)
        
        # Store selections in session state
        st.session_state.selected_area = selected_area
        st.session_state.selected_prompt = selected_prompt

    # 3️⃣ Upload Medical Document
    uploaded_file = st.file_uploader("Upload a Medical Document", type=["pdf", "docx", "txt"])

# 🔹 Main Content Area
if st.session_state.selected_area and st.session_state.selected_area != "Select":
    st.subheader(f"Selected Area: {st.session_state.selected_area}")

    if st.session_state.selected_prompt and st.session_state.selected_prompt != "Select":
        st.subheader(f"Selected Prompt: {st.session_state.selected_prompt}")

        # Load the selected prompt in Quill editor
        st.session_state.custom_prompt = st_quill(value=st.session_state.selected_prompt, key="quill_editor", html=True)

        # Button to save changes
        if st.button("Save Prompt"):
            st.success("Your changes have been saved.")

# 🔹 Display Uploaded File Information
if uploaded_file:
    st.subheader("Uploaded File Details")
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Type:** {uploaded_file.type}")

    # If text file, display contents
    if uploaded_file.type == "text/plain":
        st.text_area("File Content:", uploaded_file.getvalue().decode("utf-8"), height=200)
