"""
Site-wide footer: company registration details and a Privacy Policy
link that opens the full policy in a modal dialog window.
"""

from pathlib import Path

import streamlit as st

from app.core.config import (
    COMPANY_LEGAL_NAME,
    COMPANY_REG_NUMBER,
    COMPANY_BEE_STATUS,
    PRIVACY_POLICY_EFFECTIVE_DATE,
    PRIVACY_POLICY_EMAIL,
)

# Legal text lives in a markdown file, not Python source — updating the
# policy (which will happen whenever hosting/contract terms change)
# shouldn't require touching application code.
_POLICY_PATH = Path(__file__).resolve().parent.parent / "assets" / "legal" / "privacy_policy.md"


def _load_privacy_policy() -> str:
    return _POLICY_PATH.read_text(encoding="utf-8").format(
        effective_date=PRIVACY_POLICY_EFFECTIVE_DATE,
        legal_name=COMPANY_LEGAL_NAME.upper(),
        reg_number=COMPANY_REG_NUMBER,
        email=PRIVACY_POLICY_EMAIL,
    )


@st.dialog("Privacy Policy", width="large")
def _show_privacy_policy() -> None:
    st.markdown(_load_privacy_policy())


def render_footer() -> None:
    st.markdown(
        f"""
        <div class="omni-site-footer">
            <span>{COMPANY_LEGAL_NAME}</span>
            <span class="omni-site-footer-sep">•</span>
            <span>Reg. No. {COMPANY_REG_NUMBER}</span>
            <span class="omni-site-footer-sep">•</span>
            <span>{COMPANY_BEE_STATUS}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, privacy_col, _ = st.columns([1, 1, 1])
    with privacy_col:
        with st.container(key="omni-privacy-trigger"):
            if st.button("Privacy Policy", width="stretch"):
                _show_privacy_policy()
