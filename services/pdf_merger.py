
import io

from pypdf import PdfWriter


def merge_pdfs(uploaded_files: list) -> bytes:
    """Merge uploaded PDF files and return the resulting PDF bytes."""
    writer = PdfWriter()
    output = io.BytesIO()

    try:
        for pdf_file in uploaded_files:
            pdf_data = io.BytesIO(pdf_file.getvalue())
            writer.append(pdf_data)

        writer.write(output)
        return output.getvalue()

    finally:
        writer.close()
