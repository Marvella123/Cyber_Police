import streamlit as st
from cyber_police_core import analyse

st.set_page_config(
    page_title="Cyber Police Scanner",
    page_icon="🔎",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
  background: radial-gradient(ellipse at 5% 0%, #16344a 0%, transparent 36%), #07111f;
  color: #edf4ff;
}
[data-testid="stSidebar"] { background: #0b1727; border-right: 1px solid #263c56; }
.cp-hero {
  padding: 1.5rem; border: 1px solid #294a65; border-radius: 22px;
  background: linear-gradient(120deg, #13334b, #0e1b30); margin: .4rem 0 1.2rem;
}
.cp-hero h1 { color: #f4f8ff !important; font-size: 2.2rem; margin: .3rem 0; }
.cp-hero p { color: #c0d0e3 !important; }
.cp-eyebrow, .cp-label {
  color: #48d9e8 !important; letter-spacing: .14em; font-size: .78rem;
  font-weight: 800; text-transform: uppercase;
}
.cp-card {
  background: linear-gradient(150deg, #13253a, #0c1b2c);
  border: 1px solid #263c56; border-radius: 16px; padding: 1rem; min-height: 110px;
}
.cp-card b { color: #f1f6ff; }
.cp-card p { color: #a9bbd0; font-size: .9rem; }
div[data-testid="stTextArea"] textarea {
  background: #f7faff !important; color: #101827 !important;
  -webkit-text-fill-color: #101827 !important; caret-color: #0b7285 !important;
  border: 1px solid #8ca9c3 !important; border-radius: 12px !important;
  font-size: 1rem !important; line-height: 1.55 !important; opacity: 1 !important;
}
div[data-testid="stTextArea"] textarea::placeholder {
  color: #596b80 !important; -webkit-text-fill-color: #596b80 !important; opacity: 1 !important;
}
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
  background: #f7faff !important; color: #101827 !important; border-radius: 10px;
}
div.stButton > button { border-radius: 11px; min-height: 2.8rem; font-weight: 750; }
div.stButton > button[kind="primary"] {
  background: linear-gradient(90deg, #087f9b, #1664a6); color: white; border: 0;
}
hr { border-color: #263c56 !important; }
</style>
""", unsafe_allow_html=True)

def get_api_key():
    try:
        return st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        return ""

with st.sidebar:
    st.markdown("## 🛡️ Cyber Police")
    st.caption("SECURITY ANALYSIS WORKSPACE")
    st.divider()
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/1_Security_Scanner.py", label="Scanner", icon="🔎")
    st.page_link("pages/2_Analysis_Results.py", label="Latest results", icon="📄")
    st.divider()
    st.markdown("### Before you submit")
    st.info("Remove passwords, one-time codes, bank details, and private information.")
    st.caption("This prototype does not monitor your device or automatically block websites.")

st.markdown("""
<div class="cp-hero">
  <div class="cp-eyebrow">Threat analysis workspace</div>
  <h1>🔎 Investigate suspicious content</h1>
  <p>Check the evidence, understand the uncertainty, and choose safer next steps.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.55, 1], gap="large")
with left:
    kind = st.selectbox(
        "What are you investigating?",
        [
            "Suspicious message or email",
            "URL / website address",
            "Possible cyberbullying",
            "Possible scam or impersonation",
            "Other concern",
        ],
    )
    content = st.text_area(
        "Message or URL",
        height=240,
        placeholder="Paste the suspicious message or URL here…",
        max_chars=8000,
        key="submission",
        help="Remove passwords, one-time codes, and private financial information first.",
    )
    go = st.button("🔍  Analyse evidence", type="primary", use_container_width=True)

with right:
    st.markdown("""
    <div class="cp-card"><b>01 · Look for evidence</b><p>Review the actual wording and basic URL patterns.</p></div><br>
    <div class="cp-card"><b>02 · Assess the risk</b><p>Get a preliminary assessment based on the combined indicators.</p></div><br>
    <div class="cp-card"><b>03 · Take safer action</b><p>Get prioritised advice and a clear explanation of what remains unknown.</p></div>
    """, unsafe_allow_html=True)
    st.info("The AI can make mistakes. A report is not proof that a message or site is malicious or safe.")

with st.expander("Try a sample message"):
    st.write(
        "Illustrative sample: Your account will be closed in 25 minutes. "
        "Send your six-digit verification code immediately and do not contact support."
    )
    if st.button("Use sample"):
        st.session_state["submission"] = (
            "Your account will be closed in 25 minutes. "
            "Send your six-digit verification code immediately and do not contact support."
        )
        st.rerun()

if go:
    submitted = content.strip()
    if not submitted:
        st.warning("Enter a message or URL before starting the analysis.")
    elif not get_api_key():
        st.error(
            "Groq API key not found. Add GROQ_API_KEY to "
            ".streamlit/secrets.toml. See the README for setup instructions."
        )
    else:
        with st.spinner("Reviewing the evidence and preparing safety advice…"):
            try:
                report, urls, findings = analyse(submitted, kind, get_api_key())
                # Preserve the completed report across Streamlit page navigation.
                st.session_state["cp_latest_result"] = {
                    "report": report,
                    "urls": urls,
                    "findings": findings,
                    "submitted": submitted,
                    "kind": kind,
                }
                st.session_state["cp_latest_result_ready"] = True
                st.switch_page("pages/2_Analysis_Results.py")
            except Exception:
                st.error(
                    "The AI request failed. Check your internet connection, API key, "
                    "Groq account limits, and model availability, then try again."
                )
                st.caption(
                    "For privacy, this page does not display the raw exception, which "
                    "could contain configuration details."
                )

st.divider()
st.caption("CYBER POLICE · Prototype · AI-assisted triage, not a certified security scanner.")
