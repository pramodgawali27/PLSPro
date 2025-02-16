import streamlit as st
from streamlit_quill import st_quill

# Function to render the popup for editing a prompt
def edit_prompt_popup():
    if "is_editing" not in st.session_state:
        st.session_state.is_editing = False
    if "current_prompt" not in st.session_state:
        st.session_state.current_prompt = ""

    if st.session_state.is_editing:
        # Custom CSS for a fullscreen overlay popup
        st.markdown("""
        <style>
        .fullscreen-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            z-index: 1000;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: white;
        }
        .popup-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            width: 80%;
            max-width: 800px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }
        .button-container {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

        # Overlay container
        st.markdown('<div class="fullscreen-overlay">', unsafe_allow_html=True)

        st.markdown('<div class="popup-box">', unsafe_allow_html=True)

        st.subheader("Edit Prompt")
        edited_prompt = st_quill(value=st.session_state.current_prompt, key="quill_editor", html=True)

        # Buttons for Save and Cancel
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save Changes"):
                # Update the prompt in the session state
                index = st.session_state.prompts.index(st.session_state.current_prompt)
                st.session_state.prompts[index] = edited_prompt
                st.session_state.is_editing = False
                st.experimental_rerun()  # Refresh the page to update the prompt list
        with col2:
            if st.button("Cancel"):
                st.session_state.is_editing = False
                st.experimental_rerun()  # Close the popup

        st.markdown('</div>', unsafe_allow_html=True)  # Close popup box
        st.markdown('</div>', unsafe_allow_html=True)  # Close overlay
