# Simple PDF Merger (Streamlit)

A small web app that merges uploaded PDF files and lets the user download the result.

## Run locally on macOS

1. Open Terminal and move into this project folder:

   ```bash
   cd path/to/pdf_merger_web
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate it:

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

Streamlit will show a local URL, usually `http://localhost:8501`.

## Deploy free with Streamlit Community Cloud

1. Create/sign in to GitHub.
2. Create a repository named `simple-pdf-merger`.
3. Upload `app.py`, `requirements.txt`, and `README.md` to the repository root.
4. Visit https://share.streamlit.io/ and connect your GitHub account.
5. Choose **Create app**, select your repository and branch (`main`), and set the app file path to `app.py`.
6. Click **Deploy**. Streamlit will give you a public `*.streamlit.app` URL.

Official guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy

## Notes

- Files are merged alphabetically by filename.
- This demo limits each PDF to 25 MB and all uploads combined to 100 MB.
- Public hosting is best for non-confidential documents. Do not treat this simple app as a secure document-storage service.
- Free hosting resources and limits may change.
