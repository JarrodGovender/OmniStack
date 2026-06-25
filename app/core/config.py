"""
Centralized brand constants and Streamlit page configuration for OmniStack.
Import from here instead of hardcoding strings/colors across pages.
"""

from pathlib import Path

import streamlit as st

# --- Brand assets ---------------------------------------------------------
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets" / "images"
LOGO_DARK_PATH = ASSETS_DIR / "OmniStack - Dark Mode Logo.png"

# --- Brand identity -----------------------------------------------------
BRAND_NAME = "OmniStack"
BRAND_TAGLINE = "Next-Generation Tech Solutions for Ambitious SMEs"
BRAND_DESCRIPTION = (
    "Enterprise-grade dashboards, AI automation, and secure software "
    "development — built for South African SMEs ready to outpace the competition."
)
CONTACT_EMAIL = "hello@omnistack.co.za"
META_DESCRIPTION = (
    "OmniStack — enterprise-grade dashboards, AI automation, and secure "
    "software for South African SMEs."
)
OG_DESCRIPTION = (
    "Custom data dashboards, AI automation, and secure software development "
    "for ambitious South African SMEs."
)

# --- Legal / company registration details ---------------------------------
COMPANY_LEGAL_NAME = "OmniStack (Pty) Ltd"
COMPANY_REG_NUMBER = "2026/499208/07"
COMPANY_BEE_STATUS = "Level 1 B-BBEE Partner"
PRIVACY_POLICY_EFFECTIVE_DATE = "25 June 2026"
PRIVACY_POLICY_EMAIL = "jarrod@omnistack.co.za"

# --- Color palette (per OmniStack brand identity: Innovation Purple + Data Cyan) ---
COLOR_BG_PRIMARY = "#05060A"
COLOR_BG_SECONDARY = "#0D1117"
COLOR_SURFACE = "rgba(255, 255, 255, 0.04)"
COLOR_SURFACE_BORDER = "rgba(255, 255, 255, 0.08)"
COLOR_DATA_CYAN = "#00E5FF"
COLOR_INNOVATION_PURPLE = "#6A0D91"
COLOR_TEXT_PRIMARY = "#F5F7FA"
COLOR_TEXT_MUTED = "#8B95A5"

# --- Typography (per brand identity: geometric sans for headings, clean sans for body) ---
FONT_HEADING = "'Space Grotesk', sans-serif"
FONT_BODY = "'Inter', sans-serif"
GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Space+Grotesk:wght@500;700;800&family=Inter:wght@400;500;600&display=swap"
)


def configure_page() -> None:
    """Must be the first Streamlit call in the entry-point script."""
    st.set_page_config(
        page_title=f"{BRAND_NAME} | Under Development",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
