import streamlit as st

def main():
    st.set_page_config(
        page_title="BIM&3D",
        page_icon="🏢",
    )
    st.title("BIM and 3D Printing tools")

# st.title("BIM and 3D Printing tools")

if __name__ == "__main__":
    main()
    session = st.session_state