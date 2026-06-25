"""
Home / landing page content. Registered as a page via st.Page in app.py.
"""

from app.core.config import BRAND_NAME, META_DESCRIPTION, OG_DESCRIPTION
from app.core.styles import inject_css, inject_meta_tags
from app.assets.css.theme import get_theme_css
from app.components.hero import render_hero
from app.components.inquiry_form import render_inquiry_form
from app.components.footer import render_footer


def render() -> None:
    inject_css(get_theme_css())
    inject_meta_tags(
        description=META_DESCRIPTION,
        og_title=BRAND_NAME,
        og_description=OG_DESCRIPTION,
    )
    render_hero()
    render_inquiry_form()
    render_footer()