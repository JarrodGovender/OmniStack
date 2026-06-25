"""
Small utilities for injecting CSS and images into the Streamlit app.
Keeps st.markdown(unsafe_allow_html=True) boilerplate out of page code.
"""

import base64
from io import BytesIO
from pathlib import Path

import streamlit as st
from PIL import Image


def inject_css(css: str) -> None:
    """Inject a raw CSS string into the page inside a <style> tag."""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def image_to_data_uri(path: str, max_width: int = 640) -> str:
    """Resize (if needed) and base64-encode a local image as a data URI.

    Embedding lets the logo live inside the same HTML block as the rest of
    the card (st.image renders as a separate element and can't be nested
    inside hand-written markup), which keeps the layout fully controllable
    with our own responsive CSS instead of Streamlit's internal column
    behavior. Source brand assets are full-resolution (multi-MB) — every
    page load would otherwise ship that raw size to mobile visitors, so
    this downsizes to a sane display width and caches the result.
    """
    with Image.open(path) as img:
        if img.width > max_width:
            ratio = max_width / img.width
            img = img.resize((max_width, round(img.height * ratio)), Image.LANCZOS)
        buffer = BytesIO()
        # WebP keeps transparency like the source PNG but at a fraction of the size —
        # critical on mobile data connections. Supported by all current major browsers.
        img.save(buffer, format="WEBP", quality=85)
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/webp;base64,{encoded}"