# Simple PDF Merger

A lightweight, web-based PDF merger built with Python and Streamlit. Upload multiple PDF files, arrange them in your preferred order using drag and drop, and merge them into a single downloadable PDF.

## Features

- **Multiple PDF uploads:** Select multiple PDF files at once.
- **Drag-and-drop reordering:** Arrange uploaded files before merging.
- **PDF merging:** Combine multiple PDF documents into one file.
- **Custom output filename:** Choose a name for the merged PDF.
- **Upload validation:** Check individual and total upload sizes.
- **Filename sanitization:** Clean unsafe characters from the output filename.
- **Downloadable result:** Download the combined PDF directly from the browser.
- **Modular code structure:** Separate PDF processing, validation, and user interface logic.
- **Automated tests:** Test upload validation, filename handling, and PDF merging.
- **Free deployment option:** Host the application using Streamlit Community Cloud.

## Tech Stack

- **Python** — Application logic
- **Streamlit** — Web interface
- **pypdf** — PDF processing and merging
- **streamlit-sortables** — Drag-and-drop file ordering
- **pytest** — Automated testing
- **Git and GitHub** — Version control and source code hosting
- **Streamlit Community Cloud** — Web deployment

## Project Structure

```text
simple_pdf_merger_web/
├── app.py
├── services/
│   ├── __init__.py
│   └── pdf_merger.py
├── utils/
│   ├── __init__.py
│   └── validators.py
├── tests/
│   ├── test_pdf_merger.py
│   └── test_validators.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `app.py` | Provides the Streamlit interface, accepts uploads, handles file ordering, validates input, and offers the merged PDF for download. |
| `services/pdf_merger.py` | Contains the PDF merging logic. |
| `utils/validators.py` | Validates upload sizes and sanitizes output filenames. |
| `tests/test_pdf_merger.py` | Tests the PDF merging functionality. |
| `tests/test_validators.py` | Tests upload validation and filename sanitization. |
| `requirements.txt` | Lists the Python dependencies required by the application. |
| `.gitignore` | Excludes generated files and local development files from version control. |

## Requirements

Before running the project locally, make sure you have:

- Python 3.10 or later
- pip
- Git
- A web browser

Python 3.10 or later is required for the type-hint syntax used in the validation module.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/itsMuaazAhmed/simple-pdf-merger.git
```

Navigate to the project directory:

```bash
cd simple-pdf-merger
```

### 2. Create a Virtual Environment

Creating a virtual environment keeps project dependencies separate from your system Python installation.

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

If the project dependencies have not yet been added to `requirements.txt`, ensure that it contains:

```text
streamlit
pypdf
streamlit-sortables
pytest
```

### 4. Run the Application

Start the Streamlit development server:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal. By default, Streamlit usually serves the application at:

`http://localhost:8501`

### 5. Use the Application

1. Upload two or more PDF files.
2. Arrange the files by dragging them into the desired order.
3. Enter a filename for the combined PDF.
4. Click **Merge PDFs**.
5. Download the merged document.
6. Open the downloaded PDF to verify the page order.

The order of the files determines the order in which their pages appear in the merged document.

## Upload Limits

The application uses the following upload limits:

| Setting | Limit |
|---|---:|
| Maximum individual PDF size | 25 MB |
| Maximum combined upload size | 100 MB |

These are application-level validation limits. Hosting platforms may impose additional resource or request-size restrictions.

## Running Automated Tests

The project uses pytest to test its validation utilities and PDF merging service.

With the virtual environment activated, run:

```bash
python -m pytest -v
```

To run only the validation tests:

```bash
python -m pytest tests/test_validators.py -v
```

To run only the PDF merging tests:

```bash
python -m pytest tests/test_pdf_merger.py -v
```

The current test suite contains eight tests:

- Seven tests for upload validation and filename sanitization.
- One test verifying that two PDFs merge into a document containing two pages.

The tests verify these core functions; they do not replace manual testing of the Streamlit interface or drag-and-drop behavior.

## Deploying on Streamlit Community Cloud

You can deploy the application using Streamlit Community Cloud.

### 1. Push the Project to GitHub

Make sure your repository includes:

- `app.py`
- `services/`
- `utils/`
- `tests/`
- `requirements.txt`
- `README.md`
- `.gitignore`

Commit and push your changes:

```bash
git add .
git commit -m "Update PDF merger application"
git push origin main
```

### 2. Open Streamlit Community Cloud

Visit:

https://share.streamlit.io/

Sign in and connect your GitHub account if you have not already done so.

### 3. Deploy the Application

Create a new app and configure:

- **Repository:** `itsMuaazAhmed/simple-pdf-merger`
- **Branch:** `main`
- **Main file path:** `app.py`

Deploy the application.

Streamlit Community Cloud installs the dependencies from `requirements.txt` and starts the application.

### 4. Verify the Deployment

After deployment completes:

1. Open the application URL.
2. Upload multiple PDF files.
3. Reorder the files using drag and drop.
4. Merge and download the result.
5. Verify that the merged document has the expected page order.

If you update the source code and push changes to the configured branch, Streamlit Community Cloud can redeploy the application automatically.

## Development Workflow

A typical workflow for making changes is:

1. Create or activate the project's virtual environment.
2. Install dependencies.
3. Make changes to the source code.
4. Run the automated tests.
5. Test the application locally.
6. Review the changed files using Git.
7. Commit the changes.
8. Push the changes to GitHub.
9. Verify the deployed application.

Useful Git commands:

```bash
git status
git add app.py requirements.txt
git commit -m "Describe your changes"
git push origin main
```

## Error Handling and Limitations

- Only PDF files are accepted through the upload interface.
- Files exceeding the configured size limits are rejected.
- Damaged, invalid, or password-protected PDFs may fail to merge.
- The application does not currently provide OCR, PDF editing, page deletion, or page-level reordering.
- Drag-and-drop ordering applies to whole PDF files, not individual pages within a PDF.
- Large files may require additional memory and processing time.
- Deployment resource limits depend on the hosting environment.

## Privacy and Security

Uploaded documents may contain confidential or personal information.

Use only documents you are authorized to process. If the application is publicly deployed, review the hosting provider's data-handling policies before uploading sensitive files. Avoid logging document contents or retaining uploaded files unnecessarily.

The application's upload limits are not a substitute for comprehensive security controls.

## Future Improvements

Potential improvements include:

- Reordering individual pages before merging.
- Previewing PDF pages before merging.
- Removing selected files from the upload list.
- Adding PDF page counts and file-size summaries.
- Improving error messages for encrypted or damaged PDFs.
- Adding more automated tests for invalid PDF content and edge cases.
- Improving the interface for mobile devices.

## Contributing

Contributions, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the automated tests.
5. Submit a pull request describing your changes.

## License

No license has been specified for this project yet. Add a `LICENSE` file and update this section if you decide to distribute the project under an open-source license.

## Author

**Muaaz Ahmed**

- GitHub: https://github.com/itsMuaazAhmed
- Portfolio: https://itsmuaazahmed.github.io/

---

Built with Python and Streamlit to make combining PDF documents simple and convenient.
