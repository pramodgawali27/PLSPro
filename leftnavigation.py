import streamlit as st
from streamlit_quill import st_quill

# Initialize session state variables
if "selected_area" not in st.session_state:
    st.session_state.selected_area = None
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None
if "custom_prompt" not in st.session_state:
    st.session_state.custom_prompt = ""
if "uploaded_prompt_text" not in st.session_state:
    st.session_state.uploaded_prompt_text = None
if "final_prompt" not in st.session_state:
    st.session_state.final_prompt = None

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
def render_left_navigation():
    with st.sidebar:
        st.header("Select Prompt")

        # 1️⃣ Select Therapeutic Area
        selected_area = st.selectbox("Select Therapeutic Area", ["Select"] + list(THERAPEUTIC_PROMPTS.keys()), index=0)

        # 2️⃣ Select Product-Specific Prompt (Dynamically Loaded)
        selected_prompt = None
        if selected_area != "Select":
            selected_prompt = st.selectbox("Select a Predefined Prompt", ["Select"] + THERAPEUTIC_PROMPTS[selected_area], index=0)
        
        # Store selections in session state
        st.session_state.selected_area = selected_area
        st.session_state.selected_prompt = selected_prompt

        st.subheader("      OR")  # Clearly indicate this is an alternative option

        # 3️⃣ Option to Enter a Custom Prompt
        custom_prompt = st.text_area("Enter a Custom Prompt (Optional):")
        if custom_prompt.strip():
            st.session_state.custom_prompt = custom_prompt

        st.subheader("OR")  # Clearly indicate another alternative option

        # 4️⃣ Upload Prompt File (TXT)
        uploaded_prompt_file = st.file_uploader("Upload a Prompt File (TXT)", type=["txt"])
        if uploaded_prompt_file:
            st.session_state.uploaded_prompt_text = uploaded_prompt_file.getvalue().decode("utf-8")

        # 🔹 Main Content Area
        final_prompt = None

        # Set final prompt based on user choice (OR condition)
        if st.session_state.custom_prompt:
            final_prompt = st.session_state.custom_prompt  # User entered a prompt manually
        elif st.session_state.uploaded_prompt_text:
            final_prompt = st.session_state.uploaded_prompt_text  # User uploaded a prompt file
        elif st.session_state.selected_prompt:
            final_prompt = st.session_state.selected_prompt

        # 🔹 Button to Generate Plain Language Summary
        if final_prompt and st.button("Generate Plain Language Summary"):
            st.success("PLS generation triggered! (AI integration can be added here).")

        # 🔹 Display Uploaded File Information (if any)
        if uploaded_prompt_file:
            st.subheader("Uploaded Prompt File Details")
            st.write(f"**File Name:** {uploaded_prompt_file.name}")

    return final_prompt


