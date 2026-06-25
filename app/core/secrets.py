"""
Accessor for secrets configured via .streamlit/secrets.toml (gitignored —
see secrets.toml.example for the expected shape). Centralizes access so
components never read st.secrets directly and never crash when the file
hasn't been created yet (e.g. on a fresh local checkout or before
production credentials are configured).
"""

from typing import Optional

import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError


def get_smtp_config() -> Optional[dict]:
    """Return the [smtp] secrets block, or None if not yet configured."""
    try:
        return dict(st.secrets["smtp"])
    except (StreamlitSecretNotFoundError, KeyError):
        return None
