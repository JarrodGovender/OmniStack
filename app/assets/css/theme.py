"""
Returns the global dark-mode CSS theme string for the OmniStack landing page.
Pure CSS only — gradients, glassmorphism, and keyframe animation. No images.
"""

from app.core.config import (
    COLOR_BG_PRIMARY,
    COLOR_BG_SECONDARY,
    COLOR_SURFACE,
    COLOR_SURFACE_BORDER,
    COLOR_DATA_CYAN,
    COLOR_INNOVATION_PURPLE,
    COLOR_TEXT_PRIMARY,
    COLOR_TEXT_MUTED,
    FONT_HEADING,
    FONT_BODY,
    GOOGLE_FONTS_URL,
)


def get_theme_css() -> str:
    return f"""
    /* ---------- Brand typography ---------- */
    @import url('{GOOGLE_FONTS_URL}');

    /* =====================================================================
       MOBILE-FIRST BASE STYLES
       Everything below targets small screens by default. Larger-viewport
       refinements are layered in via the min-width media query at the
       bottom of this file — never the other way around.
       ===================================================================== */

    /* Border-box everywhere so padding/border never silently add to a
       declared width — the #1 cause of mobile horizontal overflow. */
    *, *::before, *::after {{
        box-sizing: border-box;
    }}

    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"] {{
        overflow-x: hidden;
        max-width: 100vw;
    }}

    /* ---------- Base app background ---------- */
    .stApp {{
        background: radial-gradient(circle at 15% 20%, {COLOR_BG_SECONDARY} 0%, {COLOR_BG_PRIMARY} 55%);
        color: {COLOR_TEXT_PRIMARY};
        font-family: {FONT_BODY};
    }}

    /* Hide default Streamlit chrome for a clean landing page */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .block-container {{
        position: relative;
        padding-top: 2rem;
        max-width: 1100px;
    }}

    /* ---------- Animated gradient accent glow ---------- */
    @keyframes pulse-glow {{
        0%   {{ opacity: 0.55; filter: blur(30px); }}
        50%  {{ opacity: 0.95; filter: blur(40px); }}
        100% {{ opacity: 0.55; filter: blur(30px); }}
    }}

    /* Anchored to .block-container (position: absolute) rather than the
       viewport (position: fixed) — fixed-position elements visibly lag
       and "swim" during touch-scroll on mobile Safari/Chrome as the
       browser's address bar shows/hides. Absolute scrolls with the page
       like a normal element instead, which removes that jank entirely. */
    .omni-glow {{
        position: absolute;
        top: -100px;
        left: 50%;
        transform: translateX(-50%);
        width: 320px;
        height: 320px;
        background: linear-gradient(135deg, {COLOR_DATA_CYAN}, {COLOR_INNOVATION_PURPLE});
        border-radius: 50%;
        opacity: 0.6;
        z-index: 0;
        animation: pulse-glow 6s ease-in-out infinite;
        pointer-events: none;
    }}

    /* ---------- Glassmorphism card ---------- */
    .omni-card {{
        position: relative;
        z-index: 1;
        background: {COLOR_SURFACE};
        border: 1px solid {COLOR_SURFACE_BORDER};
        border-radius: 16px;
        padding: 1.75rem 1.25rem 1.5rem;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
        animation: fade-in-up 0.8s ease-out;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    @keyframes fade-in-up {{
        from {{ opacity: 0; transform: translateY(24px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}

    /* ---------- Logo ---------- */
    .omni-logo {{
        width: min(220px, 65vw);
        height: auto;
        margin-bottom: 1rem;
    }}

    /* Shown only if the logo image is missing/unreadable (see
       image_to_data_uri's graceful fallback in core/styles.py). */
    .omni-logo-fallback {{
        font-family: {FONT_HEADING};
        font-size: 2rem;
        font-weight: 800;
        margin: 0 0 1rem 0;
        background: linear-gradient(135deg, {COLOR_TEXT_PRIMARY} 35%, {COLOR_DATA_CYAN} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}

    /* ---------- Eyebrow / status badge ---------- */
    .omni-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        background: rgba(0, 240, 255, 0.08);
        border: 1px solid rgba(0, 240, 255, 0.35);
        color: {COLOR_DATA_CYAN};
        font-family: {FONT_HEADING};
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 1.25rem;
    }}

    .omni-badge-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: {COLOR_DATA_CYAN};
        box-shadow: 0 0 8px {COLOR_DATA_CYAN};
        animation: blink 1.8s ease-in-out infinite;
    }}

    @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.25; }}
    }}

    /* ---------- Accessible / SEO-only heading ----------
       Present in the DOM for search engines and screen readers, but not
       visible — the logo image already carries the wordmark visually. */
    .omni-sr-only {{
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
    }}

    /* ---------- Tagline (h2) ---------- */
    .omni-subtitle {{
        font-family: {FONT_HEADING};
        font-size: 1.05rem;
        font-weight: 700;
        color: {COLOR_TEXT_PRIMARY};
        max-width: 640px;
        line-height: 1.4;
        margin: 0 0 0.5rem 0;
        text-align: center;
    }}

    /* ---------- Description paragraph ---------- */
    .omni-desc {{
        font-size: 0.95rem;
        color: {COLOR_TEXT_MUTED};
        max-width: 640px;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        text-align: center;
    }}

    /* ---------- Feature pills row ---------- */
    .omni-pills {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 1.75rem;
    }}

    .omni-pill {{
        padding: 0.45rem 0.85rem;
        border-radius: 12px;
        background: {COLOR_SURFACE};
        border: 1px solid {COLOR_SURFACE_BORDER};
        font-size: 0.8rem;
        color: {COLOR_TEXT_PRIMARY};
        transition: border-color 0.25s ease, transform 0.25s ease;
    }}

    .omni-pill:hover {{
        border-color: {COLOR_DATA_CYAN};
        transform: translateY(-2px);
    }}

    /* ---------- Status footer ---------- */
    .omni-footer {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        padding-top: 1.25rem;
        border-top: 1px solid {COLOR_SURFACE_BORDER};
        color: {COLOR_TEXT_MUTED};
        font-size: 0.85rem;
        text-align: center;
    }}

    .omni-footer a {{
        color: {COLOR_DATA_CYAN};
        text-decoration: none;
        font-weight: 600;
    }}

    .omni-footer a:hover {{
        text-decoration: underline;
    }}

    /* ---------- Inquiry form card ----------
       .st-key-omni-inquiry-card is a real Streamlit container (keyed via
       st.container(key=...)), not a hand-written div — the native
       st.form widgets inside it need an actual DOM wrapper to be styled
       as a card, which a markdown-only div can't provide. */
    .st-key-omni-inquiry-card {{
        background: {COLOR_SURFACE};
        border: 1px solid {COLOR_SURFACE_BORDER};
        border-radius: 16px;
        padding: 1.75rem 1.25rem;
        margin-top: 1.5rem;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }}

    .omni-form-title {{
        font-family: {FONT_HEADING};
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        color: {COLOR_TEXT_PRIMARY};
    }}

    .omni-form-subtitle {{
        font-size: 0.88rem;
        color: {COLOR_TEXT_MUTED};
        margin-bottom: 1.25rem;
    }}

    /* Native form widgets get a light restyle to match the glass aesthetic
       instead of Streamlit's default theme widget chrome. */
    .st-key-omni-inquiry-card [data-testid="stTextInput"] input,
    .st-key-omni-inquiry-card [data-testid="stTextArea"] textarea {{
        background: rgba(255, 255, 255, 0.03);
        border-color: {COLOR_SURFACE_BORDER};
        border-radius: 10px;
        /* 16px floor prevents iOS Safari from auto-zooming the page on input focus */
        font-size: max(0.92rem, 16px);
    }}

    .st-key-omni-inquiry-card [data-testid="stFormSubmitButton"] button {{
        width: 100%;
        border-radius: 10px;
        border: 1px solid {COLOR_SURFACE_BORDER};
        background: linear-gradient(135deg, rgba(0, 229, 255, 0.25), rgba(109, 40, 217, 0.35));
        color: {COLOR_TEXT_PRIMARY};
        font-family: {FONT_HEADING};
        font-weight: 600;
    }}

    /* ---------- Site footer (company / legal details) ---------- */
    .omni-site-footer {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.3rem;
        margin-top: 2rem;
        padding: 1.25rem 1rem;
        text-align: center;
        color: {COLOR_TEXT_MUTED};
        font-size: 0.78rem;
    }}

    .omni-site-footer-sep {{
        display: none;
    }}

    /* Restyle the Privacy Policy button (a real Streamlit widget, since it
       needs to trigger a Python-side dialog) to read as a footer link
       rather than a default button. */
    .st-key-omni-privacy-trigger button {{
        background: transparent;
        border: none;
        color: {COLOR_DATA_CYAN};
        font-family: {FONT_BODY};
        font-size: 0.78rem;
        font-weight: 500;
        text-decoration: underline;
        padding: 0.25rem 0;
    }}

    .st-key-omni-privacy-trigger button:hover {{
        color: {COLOR_TEXT_PRIMARY};
        background: transparent;
        border: none;
    }}

    /* =====================================================================
       DESKTOP / LARGER-VIEWPORT ENHANCEMENTS (progressive, not a fallback)
       ===================================================================== */
    @media (min-width: 768px) {{
        .block-container {{
            padding-top: 4rem;
        }}

        .omni-glow {{
            top: -200px;
            width: 600px;
            height: 600px;
        }}

        @keyframes pulse-glow {{
            0%   {{ opacity: 0.55; filter: blur(40px); }}
            50%  {{ opacity: 0.95; filter: blur(55px); }}
            100% {{ opacity: 0.55; filter: blur(40px); }}
        }}

        .omni-card {{
            border-radius: 20px;
            padding: 3rem 3rem 2.5rem 3rem;
        }}

        .omni-logo {{
            width: min(320px, 40vw);
            margin-bottom: 1.5rem;
        }}

        .omni-badge {{
            font-size: 0.78rem;
            margin-bottom: 1.5rem;
        }}

        .omni-subtitle {{
            font-size: 1.4rem;
            margin-bottom: 0.75rem;
        }}

        .omni-desc {{
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }}

        .omni-pills {{
            gap: 0.75rem;
            margin-bottom: 2.2rem;
        }}

        .omni-pill {{
            padding: 0.55rem 1.1rem;
            font-size: 0.88rem;
        }}

        .omni-footer {{
            flex-direction: row;
            gap: 0.75rem;
            padding-top: 1.5rem;
        }}

        .st-key-omni-inquiry-card {{
            border-radius: 20px;
            padding: 2.5rem 3rem;
            margin-top: 2rem;
        }}

        .omni-form-title {{
            font-size: 1.4rem;
        }}

        .omni-form-subtitle {{
            font-size: 0.92rem;
            margin-bottom: 1.5rem;
        }}

        .st-key-omni-inquiry-card [data-testid="stFormSubmitButton"] button {{
            width: auto;
        }}

        .omni-site-footer {{
            flex-direction: row;
            gap: 0.5rem;
            font-size: 0.85rem;
        }}

        .omni-site-footer-sep {{
            display: inline;
        }}
    }}
    """