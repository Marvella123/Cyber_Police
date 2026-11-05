import streamlit as st

st.set_page_config(
    page_title="Cyber Police · Investigation Results",
    page_icon="📄",
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
.cp-label { color: #48d9e8 !important; letter-spacing: .14em; font-size: .78rem; font-weight: 800; text-transform: uppercase; }
.cp-card { background: linear-gradient(150deg, #13253a, #0c1b2c); border: 1px solid #263c56; border-radius: 16px; padding: 1rem; }
div.stButton > button { border-radius: 11px; min-height: 2.8rem; font-weight: 750; }
div.stButton > button[kind="primary"] { background: linear-gradient(90deg, #087f9b, #1664a6); color: white; border: 0; }
hr { border-color: #263c56 !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🛡️ Cyber Police")
    st.caption("INVESTIGATION RESULTS")
    st.divider()
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/1_Security_Scanner.py", label="New analysis", icon="🔎")
    st.page_link("pages/2_Analysis_Results.py", label="Latest results", icon="📄")
    st.divider()
    st.caption("Reports are AI-assisted assessments, not proof that content is safe or malicious.")

st.markdown("""
<div class="cp-hero">
  <div class="cp-label">Analysis complete</div>
  <h1>📄 Investigation results</h1>
  <p>Your submitted content has been analysed. Review the evidence and recommended next steps below.</p>
</div>
""", unsafe_allow_html=True)

result = st.session_state.get("cp_latest_result")
if not result:
    st.info("No analysis results are available in this session yet. Start a scan to generate your first report.")
    if st.button("🔎 Open Security Scanner", type="primary", use_container_width=True):
        st.switch_page("pages/1_Security_Scanner.py")
    st.stop()

st.markdown('<div class="cp-label">Submitted for analysis</div>', unsafe_allow_html=True)
st.write(f"**Investigation type:** {result.get('kind', 'Not specified')}")
with st.expander("View submitted content"):
    st.code(result.get("submitted", ""), language=None)

st.divider()
st.markdown('<div class="cp-label">AI investigation report</div>', unsafe_allow_html=True)
st.markdown(result.get("report", "No report text was returned."))

urls = result.get("urls") or []
findings = result.get("findings") or []
if urls:
    st.divider()
    with st.expander("Technical details · Local URL observations", expanded=False):
        st.caption("These are local parsing observations only. No URL was visited, and no live DNS, redirect, or reputation checks were performed.")
        for url in urls:
            st.code(url)
        if findings:
            for item in findings:
                st.markdown(f"**{item.get('url', 'URL')}**")
                for observation in item.get("observations", []):
                    st.write(f"- {observation}")
        else:
            st.write("No listed static URL warning patterns were detected. This does not establish that the URL is safe.")

st.caption("AI-assisted triage only. Confirm important findings through independently verified contact details.")
st.divider()
left, right = st.columns(2)
with left:
    if st.button("🔎 Analyse another item", type="primary", use_container_width=True):
        st.switch_page("pages/1_Security_Scanner.py")
with right:
    if st.button("🏠 Back to home", use_container_width=True):
        st.switch_page("app.py")

st.caption("CYBER POLICE · Prototype · AI-assisted triage, not a certified security scanner.")
