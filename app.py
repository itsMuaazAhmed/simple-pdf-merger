import io
import re
import streamlit as st
from pypdf import PdfWriter

MAX_FILE_MB = 25
MAX_TOTAL_MB = 100

st.set_page_config(page_title="Simple PDF Merger", page_icon="📄")

st.title("📄 Simple PDF Merger")
st.write("Upload PDF files, merge them, and download one combined PDF.")

st.info(
    "Privacy note: Files are processed by this app while it runs. "
    "Do not upload confidential documents to a public app unless you are "
    "comfortable with the hosting provider's data handling."
)

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True,
    help=f"Maximum {MAX_FILE_MB} MB per file and {MAX_TOTAL_MB} MB total."
)

output_name = st.text_input("Output filename", value="CombinedFile.pdf")

if uploaded_files:
    # Sort by filename so the merge order is predictable.
    uploaded_files = sorted(uploaded_files, key=lambda item: item.name.lower())
    total_bytes = sum(item.size for item in uploaded_files)
    st.write(f"Selected files: **{len(uploaded_files)}**")
    st.write(f"Total upload size: **{total_bytes / (1024 * 1024):.1f} MB**")
    with st.expander("Files will be merged in this order"):
        for item in uploaded_files:
            st.write(f"- {item.name}")

    oversized = [
        item.name for item in uploaded_files
        if item.size > MAX_FILE_MB * 1024 * 1024
    ]
    if oversized:
        st.error(
            f"These files exceed the {MAX_FILE_MB} MB per-file limit: "
            + ", ".join(oversized)
        )
    elif total_bytes > MAX_TOTAL_MB * 1024 * 1024:
        st.error(f"Please keep the total upload size under {MAX_TOTAL_MB} MB.")
    elif st.button("Merge PDFs", type="primary"):
        safe_name = output_name.strip()
        if not safe_name:
            st.error("Please enter an output filename.")
        else:
            if not safe_name.lower().endswith(".pdf"):
                safe_name += ".pdf"
            safe_name = re.sub(r'[\\/:*?"<>|]+', "_", safe_name)

            writer = PdfWriter()
            output_buffer = io.BytesIO()
            try:
                for uploaded_file in uploaded_files:
                    writer.append(io.BytesIO(uploaded_file.getvalue()))
                writer.write(output_buffer)
                output_buffer.seek(0)

                st.success(f"Successfully merged {len(uploaded_files)} PDF files.")
                st.download_button(
                    label="Download merged PDF",
                    data=output_buffer.getvalue(),
                    file_name=safe_name,
                    mime="application/pdf",
                    type="primary",
                )
            except Exception as error:
                st.error(
                    "Could not merge the files. One may be damaged, "
                    "password-protected, or not a valid PDF."
                )
                st.caption(f"Technical detail: {error}")
            finally:
                writer.close()
else:
    st.caption("Select two or more PDF files to get started.")
