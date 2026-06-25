"""
Small utility for injecting CSS strings into the Streamlit app.
Keeps st.markdown(unsafe_allow_html=True) boilerplate out of page code.
"""

import streamlit as st


def inject_css(css: str) -> None:
    """Inject a raw CSS string into the page inside a <style> tag."""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)