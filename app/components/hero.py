"""
Hero section component for the OmniStack landing page.
Pure render function: builds HTML/CSS-class-driven markup for the hero block.
"""

import streamlit as st

from app.core.config import (
    BRAND_NAME,
    BRAND_TAGLINE,
    BRAND_DESCRIPTION,
    CONTACT_EMAIL,
    LOGO_DARK_PATH,
)
from app.core.styles import image_to_data_uri


def render_hero() -> None:
    """Render the full hero section: glow backdrop, logo, badge, title, pills, footer."""

    # Background ambient glow (behind the glass card, purely decorative)
    st.markdown('<div class="omni-glow"></div>', unsafe_allow_html=True)

    feature_pills = [
        "📊 Custom Data Dashboards",
        "🤖 AI Automation",
        "🔒 Secure Software Development",
    ]
    pills_html = "".join(f'<span class="omni-pill">{p}</span>' for p in feature_pills)
    logo_data_uri = image_to_data_uri(str(LOGO_DARK_PATH))

    if logo_data_uri:
        # Logo image carries the wordmark visually, so the real <h1> only
        # needs to exist for search engines and screen readers, not be seen.
        brand_markup = (
            f'<img class="omni-logo" src="{logo_data_uri}" alt="{BRAND_NAME} logo">'
            f'<h1 class="omni-sr-only">{BRAND_NAME}</h1>'
        )
    else:
        # Logo file missing/unreadable (image_to_data_uri returns "" rather
        # than raising) — fall back to a real visible text heading instead.
        brand_markup = f'<h1 class="omni-logo-fallback">{BRAND_NAME}</h1>'

    st.markdown(
        f"""
        <div class="omni-card">
            {brand_markup}
            <div class="omni-badge">
                <span class="omni-badge-dot"></span>
                Under Development
            </div>
            <h2 class="omni-subtitle">{BRAND_TAGLINE}.</h2>
            <p class="omni-desc">{BRAND_DESCRIPTION}</p>
            <div class="omni-pills">
                {pills_html}
            </div>
            <div class="omni-footer">
                <span>We're building something fast, secure, and built for scale.</span>
                <a href="mailto:{CONTACT_EMAIL}">Get in touch →</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )