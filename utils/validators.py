
import re


MAX_FILE_MB = 25
MAX_TOTAL_MB = 100


def validate_uploads(uploaded_files: list) -> str | None:
    """
    Validate uploaded PDF files.

    Returns:
        An error message if validation fails, otherwise None.
    """
    if not uploaded_files:
        return "Please upload at least one PDF file."

    max_file_size = MAX_FILE_MB * 1024 * 1024
    max_total_size = MAX_TOTAL_MB * 1024 * 1024

    for pdf_file in uploaded_files:
        if pdf_file.size > max_file_size:
            return (
                f"{pdf_file.name} exceeds "
                f"the {MAX_FILE_MB} MB per-file limit."
            )

    total_size = sum(pdf_file.size for pdf_file in uploaded_files)

    if total_size > max_total_size:
        return (
            f"Total upload size exceeds "
            f"{MAX_TOTAL_MB} MB."
        )

    return None


def sanitize_filename(filename: str) -> str:
    """
    Clean the output filename and ensure it ends with .pdf.
    """
    filename = filename.strip()

    if not filename:
        filename = "CombinedFile.pdf"

    filename = re.sub(r'[\\/:*?"<>|]+', "_", filename)

    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"

    return filename
