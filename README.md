# Cyber Police — updated prototype

This project contains:
- `app.py`: introduction/home page
- `pages/1_Security_Scanner.py`: functional scanner page
- `cyber_police_core.py`: shared AI instructions and local static URL parsing
- `.streamlit/secrets.toml.example`: example API-key configuration

## Setup

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create `.streamlit/secrets.toml` by copying `.streamlit/secrets.toml.example`.
5. Replace `paste_your_groq_api_key_here` with your own Groq API key.
6. Start the app:

   ```bash
   python -m streamlit run app.py
   ```

## Accuracy and limitations

The app performs local static URL parsing and asks the AI to explain evidence and uncertainty.
It does **not** perform live URL, DNS, redirect, domain ownership, or reputation checks.
It does not monitor a device or block websites. AI results may be wrong.

Never commit or share `.streamlit/secrets.toml`. Keep your API key private.


## Stress-test fixes (October 2026)

- Added contextual text-pattern signals for instructions that may weaken security controls.
- Added explicit AI rules against recommending that users follow unverified instructions to disable protections.
- Improved reserved-domain handling so subdomains of `example.com`, `example.org`, and `example.net` are labelled as illustrative test domains.
- Added guidance not to treat URL parameters such as `session=...` as proof of a working session token or hijacking.
- Clarified that possible bullying language and joke framing need context rather than automatic verdicts.

These are targeted improvements, not proof of overall detection accuracy. The project still uses an AI model and local static parsing; it does not perform live DNS, redirect, domain reputation, or website-content checks. Run the stress-test set again after installing this version.


## Separate results page

After a successful scan, Cyber Police stores the report for the current Streamlit session and automatically opens **Investigation Results** (`pages/2_Analysis_Results.py`). The results page shows the report, the submitted content, and any local URL parsing observations. Use **Analyse another item** to return to the scanner. Results are kept in Streamlit session state and are not a permanent report history.
