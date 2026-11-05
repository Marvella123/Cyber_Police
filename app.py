import streamlit as st

st.set_page_config(
    page_title="Cyber Police",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp {
  background: radial-gradient(ellipse at 5% 0%, #16344a 0%, transparent 36%), #07111f;
  color: #edf4ff;
}
[data-testid="stSidebar"] {
  background: #0b1727;
  border-right: 1px solid #263c56;
  color: #ffffff;
}

[data-testid="stSidebar"] * {
  color: #f1f6ff !important;
}

[data-testid="stSidebar"] a {
  color: #48d9e8 !important;
}
.cp-hero {
  padding: 2.2rem;
  border: 1px solid #294a65;
  border-radius: 24px;
  background: linear-gradient(120deg, #13334b, #0e1b30);
  margin: .5rem 0 1.2rem;
}
.cp-hero h1 { color: #f4f8ff !important; font-size: 2.8rem; margin: .4rem 0; }
.cp-hero p { color: #c0d0e3 !important; font-size: 1.08rem; }
.cp-eyebrow, .cp-label {
  color: #48d9e8 !important; letter-spacing: .14em; font-size: .78rem;
  font-weight: 800; text-transform: uppercase;
}
.cp-pill {
  display: inline-block; border: 1px solid #2e6679; border-radius: 999px;
  padding: .35rem .75rem; color: #9debf1 !important; font-size: .78rem;
  margin-top: .5rem;
}
.cp-card {
  background: linear-gradient(150deg, #13253a, #0c1b2c);
  border: 1px solid #263c56; border-radius: 16px; padding: 1.15rem;
  min-height: 140px;
}
.cp-card h3 { color: #f1f6ff; font-size: 1.05rem; }
.cp-card p { color: #a9bbd0; font-size: .94rem; }
div.stButton > button { border-radius: 11px; min-height: 2.8rem; font-weight: 750; }
div.stButton > button[kind="primary"] {
  background: linear-gradient(90deg, #087f9b, #1664a6); color: white; border: 0;
}
hr { border-color: #263c56 !important; }
/* Cyber Police sidebar text colour */
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] span,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] strong,
[data-testid="stSidebar"] [data-testid="stPageLink"] span,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    color: #ffffff !important;
}

/* Sidebar navigation links */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    color: #ffffff !important;
}

/* Sidebar captions */
[data-testid="stSidebar"] .stCaption {
    color: #b8cce0 !important;
}
/* Remove Streamlit's default header */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* Remove the white toolbar background */
[data-testid="stToolbar"] {
    background: transparent !important;
}

/* Keep the top area consistent with the dark theme */
.stApp {
    background-color: #07111f;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🛡️ Cyber Police")
    st.caption("AI-ASSISTED CYBER SAFETY")
    st.divider()
    st.markdown("**Explore**")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/1_Security_Scanner.py", label="Launch scanner", icon="🔎")
    st.page_link("pages/2_Analysis_Results.py", label="Latest results", icon="📄")
    st.divider()
    st.caption("This prototype analyses only content you submit. It does not monitor your device or automatically block websites.")

st.markdown("""
<div class="cp-hero">
  <div class="cp-eyebrow">Cybersecurity · Smarter online safety</div>
  <h1>🛡️ CYBER POLICE</h1>
  <p>Your AI-assisted guide to spotting suspicious messages, links, scams, and online abuse.</p>
  <div class="cp-pill">Understand the warning signs · Choose safer next steps</div>
</div>
""", unsafe_allow_html=True)

st.subheader("A little more confidence before you click.")
st.write(
    "Cyber Police helps you examine suspicious content, understand why it may be risky, "
    "and decide what to do next. It is designed for everyday users—not just cybersecurity experts."
)

if st.button("🔎  Launch Cyber Police scanner", type="primary", use_container_width=True):
    st.switch_page("pages/1_Security_Scanner.py")

st.markdown("### What Cyber Police can help you investigate")
cols = st.columns(3, gap="medium")
cards = [
    ("✉️", "Suspicious messages", "Look for urgency, unusual requests, impersonation, and pressure to reveal private information."),
    ("🔗", "Links and URLs", "Inspect basic URL patterns and understand what those signals can—and cannot—tell you."),
    ("🧭", "Safer next steps", "Get practical guidance for checking a message independently and responding if you already interacted."),
]
for col, (icon, title, body) in zip(cols, cards):
    with col:
        st.markdown(
            f'<div class="cp-card"><h3>{icon} &nbsp; {title}</h3><p>{body}</p></div>',
            unsafe_allow_html=True,
        )

st.markdown("### How it works")
steps = st.columns(3, gap="medium")
for col, number, title, body in zip(
    steps,
    ["01", "02", "03"],
    ["Submit", "Investigate", "Act safely"],
    [
        "Paste a suspicious message or URL. Remove passwords and private details first.",
        "The AI reviews the content and any local URL observations available.",
        "Read the evidence, uncertainty, and prioritised recommendations.",
    ],
):
    with col:
        st.markdown(
            f'<div class="cp-card"><p class="cp-eyebrow">{number}</p><h3>{title}</h3><p>{body}</p></div>',
            unsafe_allow_html=True,
        )

st.warning(
    "Important: this prototype does not perform live website, DNS, redirect, or reputation checks. "
    "An AI assessment can be wrong; no warning signs found does not prove a message or website is safe."
)

st.markdown("---")
st.caption("CYBER POLICE · Prototype · AI-assisted triage, not a certified security scanner.")
