import streamlit as st
from helpers import carousel

def main():
    st.set_page_config(
        page_title="BIM&3D",
        page_icon="🏢",
    )
    st.header("_:red[GRUA Investigación aplicada en Construcción]_")
    carousel.createCarousel()

if __name__ == "__main__":
    main()
    session = st.session_state
    