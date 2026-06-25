# OmniStack — CTO Daily Code Review
**Date:** 25 June 2026  
**Reviewer:** CTO (AI)  
**Commits reviewed:** `4b949ce` → `792110b` (4 commits, initial scaffold through site footer)  
**Scope:** Full codebase — `app.py`, `core/`, `components/`, `pages/`, `assets/`, `requirements.txt`

---

## Overall Verdict

The foundation is solid. Architecture decisions are sensible for a Streamlit-based platform that needs to grow into live interactive dashboards. Code quality is above average for this stage — brand constants are centralized, CSS is mobile-first, and the component model is properly separated. However, there are **5 issues that must be fixed before this site goes live** and 4 lower-priority items to address in upcoming sprints.

**Current site status:** Acceptable for "under development" phase. NOT acceptable to flip live with these issues unresolved.

---

## Critical Issues (Block Go-Live)

### 1. Zero Semantic Headings — SEO is Dead on Arrival

**File:** `app/components/hero.py`

The entire page has no `<h1>`, `<h2>`, or any heading tag. The brand name and tagline are wrapped in `<p>` and `<strong>` tags. Google cannot determine what this page is about. This will rank for nothing.

**Fix — replace the subtitle block in `hero.py`:**
```html
<!-- CURRENT (wrong) -->
<p class="omni-subtitle">
    <strong>Next-Generation Tech Solutions for Ambitious SMEs.</strong><br>
    Enterprise-grade dashboards...
</p>

<!-- CORRECT -->
<h1 class="omni-heading">OmniStack</h1>
<h2 class="omni-subtitle">Next-Generation Tech Solutions for Ambitious SMEs.</h2>
<p class="omni-desc">Enterprise-grade dashboards...</p>
```

Add corresponding CSS classes. This is a 30-minute fix with significant SEO impact.

---

### 2. Inquiry Form is Completely Non-Functional

**File:** `app/components/inquiry_form.py`

The form renders disabled HTML inputs with no backend. A prospective client cannot contact you. This is the single biggest business risk in the codebase — the site exists to generate leads and currently has no path to capture one.

**Fix:** Replace the static HTML with a real `st.form()` block that writes to Supabase or sends an email via SMTP. Minimum viable version:

```python
import streamlit as st
import smtplib
from email.message import EmailMessage

def render_inquiry_form() -> None:
    with st.form("inquiry", clear_on_submit=True):
        col1, col2 = st.columns(2)
        name = col1.text_input("Name", placeholder="Jane Mokoena")
        company = col2.text_input("Company", placeholder="Acme SME (Pty) Ltd")
        email = st.text_input("Email", placeholder="jane@acmesme.co.za")
        message = st.text_area("What are you looking to build?", rows=3)
        submitted = st.form_submit_button("Submit Inquiry →")

    if submitted:
        _send_inquiry(name, company, email, message)
        st.success("Thanks — we'll be in touch within 24 hours.")

def _send_inquiry(name, company, email, message):
    # Use st.secrets["smtp"] for credentials — see Issue #3
    pass
```

This is the highest-priority development task.

---

### 3. No Secrets Management Pattern Established

**File:** `app/core/config.py`

`CONTACT_EMAIL` and `PRIVACY_POLICY_EMAIL` are hardcoded strings. The moment the form is wired (Issue #2), the developer will need SMTP credentials or a Supabase key. Without a secrets pattern already in place, those credentials will end up hardcoded or, worse, committed to Git.

**Fix:** Create `.streamlit/secrets.toml` (already gitignored by Streamlit convention) and add a `core/secrets.py` accessor:

```toml
# .streamlit/secrets.toml  (NEVER commit this file)
[smtp]
host = "smtp.gmail.com"
port = 587
user = "hello@omnistack.co.za"
password = "..."

[supabase]
url = "https://xxx.supabase.co"
key = "..."
```

```python
# app/core/secrets.py
import streamlit as st

def get_smtp_config() -> dict:
    return st.secrets["smtp"]
```

Add `secrets.toml` to `.gitignore` now, before any key lands in the repo.

---

### 4. Privacy Policy Hardcoded in Python Source

**File:** `app/components/footer.py` (lines 16–112)

97 lines of legal text are embedded as a Python f-string. When the legal policy needs updating (and it will — at minimum when Render/Supabase contract terms change), the developer must touch Python code. This is a maintenance anti-pattern and a compliance risk.

**Fix:** Extract to `app/assets/legal/privacy_policy.md` and load at runtime:

```python
# footer.py
from pathlib import Path

_POLICY_PATH = Path(__file__).resolve().parent.parent / "assets" / "legal" / "privacy_policy.md"

def _load_privacy_policy() -> str:
    return _POLICY_PATH.read_text(encoding="utf-8").format(
        effective_date=PRIVACY_POLICY_EFFECTIVE_DATE,
        legal_name=COMPANY_LEGAL_NAME.upper(),
        reg_number=COMPANY_REG_NUMBER,
        email=PRIVACY_POLICY_EMAIL,
    )
```

---

### 5. Missing `__init__.py` in `app/assets/` and `app/assets/css/`

**Files:** `app/assets/`, `app/assets/css/`

Every other package directory in the project has an `__init__.py`. These two don't. Python 3 namespace packages mean `from app.assets.css.theme import get_theme_css` currently works, but certain deployment tools (PyInstaller, some CI scanners) and linters will not recognize these as proper packages. It's also inconsistent with the rest of the codebase.

**Fix:** `touch app/assets/__init__.py app/assets/css/__init__.py` — 2 minutes.

---

## Medium Priority (Next Sprint)

### 6. `requirements.txt` is a Raw `pip freeze` Output

**File:** `requirements.txt`

The file contains `GitPython==3.1.50` and `smmap==5.0.3`. GitPython is a dev tool that has no business in a production deployment. This is `pip freeze` output masquerading as a curated requirements file. On a cloud host like Render, you're installing 10+ unnecessary packages on every deploy.

**Fix:** Maintain two files:
- `requirements.in` — direct dependencies only (`streamlit`, `pillow`)
- `requirements.txt` — the full lockfile generated by `pip-compile` from the `.in` file

Remove `GitPython`, `smmap`, and `gitdb` from the locked set.

---

### 7. `image_to_data_uri` Has No Error Handling

**File:** `app/core/styles.py` (lines 20–40)

If the logo file is missing — renamed, not committed, or deployment path differs — `Image.open(path)` raises an unhandled `FileNotFoundError` and the entire page crashes.

**Fix:**
```python
@st.cache_data(show_spinner=False)
def image_to_data_uri(path: str, max_width: int = 640) -> str:
    try:
        with Image.open(path) as img:
            # ... existing logic
    except FileNotFoundError:
        return ""  # Components must handle empty string gracefully
```

In `hero.py`, guard: `if logo_data_uri: <render img tag> else: <render text fallback>`.

---

### 8. No Meta Description or Open Graph Tags

**File:** `app/core/config.py` / `app/pages/home.py`

Streamlit doesn't set `<meta name="description">` or `<meta property="og:*">` tags. When this URL is shared on LinkedIn or WhatsApp, it will show no preview card. Google will generate its own description from page text, which is unreliable.

**Fix:** Inject via `st.markdown()` in `home.py`:

```python
inject_css(f"""
</style>
<meta name="description" content="OmniStack — enterprise-grade dashboards, AI automation, and secure software for South African SMEs.">
<meta property="og:title" content="OmniStack">
<meta property="og:description" content="Custom data dashboards, AI automation, and secure software development for ambitious South African SMEs.">
<meta property="og:image" content="...">
<style>
""")
```

Note the style tag trick is a known Streamlit workaround since `st.markdown` only supports a `<style>` block natively.

---

### 9. Disabled Form Button Has No Tooltip

**File:** `app/assets/css/theme.py` (`.omni-form-submit`)

The submit button shows `cursor: not-allowed` but gives the user zero indication of why it's disabled or how to actually contact OmniStack.

**Fix (immediate, 1 line):** Add a `title` attribute to the div in `inquiry_form.py`:
```html
<div class="omni-form-submit" title="Coming soon — email us at hello@omnistack.co.za">
    Submit Inquiry — Coming Soon
</div>
```

---

## What's Done Well

- **Config centralization** (`core/config.py`) is excellent. No magic strings scattered across components.
- **Mobile-first CSS** is properly implemented — mobile base styles, desktop progressively enhanced via `min-width`. The `overflow-x: hidden` coverage is thorough.
- **`@st.cache_data` on image processing** — the WebP conversion with Pillow is a smart optimization. Saves meaningful load time on mobile.
- **`position: absolute` for the glow** instead of `fixed` — the comment explaining mobile Safari scroll jank is exactly the kind of reasoning that prevents regressions.
- **Privacy Policy as `st.dialog`** — the right pattern. Triggered by a real Streamlit button (so it participates in the widget lifecycle) but styled to look like a footer link.
- **POPIA compliance** is clearly thought through and named explicitly in the policy text.
- **Comment quality** throughout — explains the WHY, not just the WHAT. This is production-grade documentation.

---

## Sprint Priorities

| # | Task | Effort | Impact |
|---|------|--------|--------|
| 1 | Add H1/H2 heading tags to hero | 0.5h | SEO critical |
| 2 | Wire inquiry form to real backend | 4–6h | Revenue critical |
| 3 | Establish `st.secrets` + `secrets.toml` pattern | 1h | Security critical |
| 4 | Extract privacy policy to `.md` file | 1h | Maintenance |
| 5 | Add `__init__.py` to `app/assets/` dirs | 0.1h | Hygiene |
| 6 | Curate `requirements.txt` (remove GitPython) | 0.5h | Hygiene |
| 7 | Error handling in `image_to_data_uri` | 0.5h | Resilience |
| 8 | Inject OG/meta description tags | 1h | SEO/Marketing |
| 9 | Add tooltip to disabled form button | 0.1h | UX |

**Next review:** Tomorrow, same time. Expected: Items 3, 5, 6, 9 closed (quick wins). Item 2 in progress.
