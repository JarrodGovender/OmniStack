"""
Home / landing page content. Registered as a page via st.Page in app.py.
"""

from app.core.styles import inject_css
from app.assets.css.theme import get_theme_css
from app.components.hero import render_hero
from app.components.inquiry_form import render_inquiry_form


def render() -> None:
    inject_css(get_theme_css())
    render_hero()
    render_inquiry_form()