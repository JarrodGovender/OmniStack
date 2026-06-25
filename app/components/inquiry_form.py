"""
Inquiry form. Captures lead details via a real Streamlit form and emails
them via SMTP if credentials are configured (see core/secrets.py and
.streamlit/secrets.toml.example); falls back to a direct-contact message
instead of crashing when SMTP hasn't been set up yet.
"""

import smtplib
from email.message import EmailMessage

import streamlit as st

from app.core.config import CONTACT_EMAIL
from app.core.secrets import get_smtp_config


def _send_inquiry(name: str, company: str, email: str, message: str) -> bool:
    """Send the inquiry via SMTP. Returns True on success, False if SMTP isn't configured."""
    smtp_config = get_smtp_config()
    if smtp_config is None:
        return False

    msg = EmailMessage()
    msg["Subject"] = f"OmniStack inquiry from {name or 'website visitor'}"
    msg["From"] = smtp_config["user"]
    msg["To"] = smtp_config.get("to_address", smtp_config["user"])
    if email:
        msg["Reply-To"] = email
    msg.set_content(
        f"Name: {name}\nCompany: {company}\nEmail: {email}\n\n{message}"
    )

    with smtplib.SMTP(smtp_config["host"], int(smtp_config["port"])) as server:
        server.starttls()
        server.login(smtp_config["user"], smtp_config["password"])
        server.send_message(msg)
    return True


def render_inquiry_form() -> None:
    # Real Streamlit widgets can't be nested inside a hand-written HTML div
    # (each st.* call renders as a sibling element, not a child) — a keyed
    # container gives us a real wrapping DOM node we can style as a card.
    with st.container(key="omni-inquiry-card"):
        st.markdown(
            """
            <div class="omni-form-title">Tell us about your project</div>
            <div class="omni-form-subtitle">
                Drop us your details and we'll be in touch within 24 hours.
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("omni_inquiry_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            name = col1.text_input("Name", placeholder="Jane Mokoena")
            company = col2.text_input("Company", placeholder="Acme SME (Pty) Ltd")
            email = st.text_input("Email", placeholder="jane@acmesme.co.za")
            message = st.text_area(
                "What are you looking to build?",
                placeholder="Custom dashboard, AI automation, secure software...",
                height=100,
            )
            submitted = st.form_submit_button("Submit Inquiry →")

        if submitted:
            if not name or not email:
                st.warning("Please fill in at least your name and email.")
            else:
                try:
                    sent = _send_inquiry(name, company, email, message)
                except Exception:
                    sent = False

                if sent:
                    st.success("Thanks — we'll be in touch within 24 hours.")
                else:
                    st.info(
                        f"Lead capture is still being wired up on our end — for now, "
                        f"please email us directly at {CONTACT_EMAIL} and we'll "
                        f"respond within 24 hours."
                    )
