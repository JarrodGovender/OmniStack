"""
Hero section component for the OmniStack landing page.
Pure render function: builds HTML/CSS-class-driven markup for the hero block.
"""

import streamlit as st

from app.core.config import (
    BRAND_TAGLINE,
    BRAND_DESCRIPTION,
    CONTACT_EMAIL,
    LOGO_DARK_PATH,
)


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

    # Logo rendered as a real Streamlit image (separate from the card below,
    # since raw HTML divs can't be split across st.image/st.markdown calls).
    _, logo_col, _ = st.columns([1, 1, 1])
    with logo_col:
        st.image(str(LOGO_DARK_PATH), width="stretch")

    st.markdown(
        f"""
        <div class="omni-card">
            <div class="omni-badge">
                <span class="omni-badge-dot"></span>
                Under Development
            </div>
            <p class="omni-subtitle">
                <strong>{BRAND_TAGLINE}.</strong><br>
                {BRAND_DESCRIPTION}
            </p>
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