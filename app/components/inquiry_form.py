"""
Inquiry form placeholder component.
Per the brand brief, this is a *visual* representation only — disabled
inputs and a disabled submit affordance — to be wired up to a real
lead-capture backend in a later iteration.
"""

import streamlit as st


def render_inquiry_form() -> None:
    st.markdown(
        """
        <div class="omni-form-card">
            <div class="omni-form-title">Tell us about your project</div>
            <div class="omni-form-subtitle">
                Lead capture is coming soon — this form is a preview of what's next.
            </div>
            <div class="omni-form-grid">
                <div class="omni-form-field">
                    <label>Name</label>
                    <input type="text" placeholder="Jane Mokoena" disabled>
                </div>
                <div class="omni-form-field">
                    <label>Company</label>
                    <input type="text" placeholder="Acme SME (Pty) Ltd" disabled>
                </div>
                <div class="omni-form-field full-width">
                    <label>Email</label>
                    <input type="email" placeholder="jane@acmesme.co.za" disabled>
                </div>
                <div class="omni-form-field full-width">
                    <label>What are you looking to build?</label>
                    <textarea rows="3" placeholder="Custom dashboard, AI automation, secure software..." disabled></textarea>
                </div>
            </div>
            <div class="omni-form-submit">Submit Inquiry — Coming Soon</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
