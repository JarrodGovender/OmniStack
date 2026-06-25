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

    html, body, .stApp {{
        overflow-x: hidden;
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
        padding-top: 2rem;
        max-width: 1100px;
    }}

    /* ---------- Animated gradient accent glow ---------- */
    @keyframes pulse-glow {{
        0%   {{ opacity: 0.55; filter: blur(30px); }}
        50%  {{ opacity: 0.95; filter: blur(40px); }}
        100% {{ opacity: 0.55; filter: blur(30px); }}
    }}

    .omni-glow {{
        position: fixed;
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

    /* ---------- Subtitle / tagline ---------- */
    .omni-subtitle {{
        font-size: 1rem;
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

    /* ---------- Inquiry form placeholder (UI only, not yet functional) ---------- */
    .omni-form-card {{
        position: relative;
        z-index: 1;
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

    .omni-form-grid {{
        display: grid;
        grid-template-columns: 1fr;
        gap: 0.85rem;
        margin-bottom: 1rem;
    }}

    .omni-form-field {{
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
    }}

    .omni-form-field label {{
        font-size: 0.8rem;
        color: {COLOR_TEXT_MUTED};
        font-weight: 500;
    }}

    .omni-form-field input,
    .omni-form-field textarea {{
        width: 100%;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid {COLOR_SURFACE_BORDER};
        border-radius: 10px;
        padding: 0.65rem 0.9rem;
        color: {COLOR_TEXT_MUTED};
        font-family: {FONT_BODY};
        resize: none;
        /* 16px floor prevents iOS Safari from auto-zooming the page on input focus */
        font-size: max(0.92rem, 16px);
    }}

    .omni-form-submit {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        width: 100%;
        margin-top: 0.5rem;
        padding: 0.85rem 1.4rem;
        border-radius: 10px;
        border: 1px solid {COLOR_SURFACE_BORDER};
        background: linear-gradient(135deg, rgba(0, 229, 255, 0.12), rgba(109, 40, 217, 0.18));
        color: {COLOR_TEXT_MUTED};
        font-family: {FONT_HEADING};
        font-size: 0.9rem;
        font-weight: 600;
        cursor: not-allowed;
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
            font-size: 1.15rem;
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

        .omni-form-card {{
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

        .omni-form-grid {{
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }}

        .omni-form-field.full-width {{
            grid-column: 1 / -1;
        }}

        .omni-form-submit {{
            width: auto;
            padding: 0.7rem 1.4rem;
        }}
    }}
    """