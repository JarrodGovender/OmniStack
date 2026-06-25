"""
OmniStack — Streamlit application entry point.
Defines page config, registers pages via st.Page, and runs navigation.
"""

import streamlit as st

from app.core.config import configure_page
from app.pages import home

# Must be the first Streamlit call in the script.
configure_page()

# --- Page registry --------------------------------------------------
# Today: a single landing page. Future pages (Demos, Pricing, Contact,
# individual dashboard demos) are added here as additional st.Page(...)
# entries, optionally grouped into sections via a dict, e.g.:
#
#   pg = st.navigation({
#       "": [home_page],
#       "Demos": [sales_demo_page, ops_demo_page],
#       "Company": [pricing_page, contact_page],
#   })

home_page = st.Page(home.render, title="Home", icon="⚡", default=True)

pg = st.navigation([home_page])
pg.run()