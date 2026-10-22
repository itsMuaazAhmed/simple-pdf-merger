
from collections import Counter

import streamlit as st
from streamlit_sortables import sort_items

from services.pdf_merger import merge_pdfs
from utils.validators import validate_uploads, sanitize_filename


MAX_FILE_MB = 25
MAX_TOTAL_MB = 100

st.set_page_config(
    page_title="Simple PDF Merger",
    page_icon="📄",
    layout="centered",
)

st.title("📄 Simple PDF Merger")
st.write(
    "Upload your PDF files, drag them into your preferred order, "
    "and download one combined PDF."
)

st.info(
    "Privacy note: Files are processed while the app runs. "
    "Avoid uploading confidential documents to a public app "
    "unless you are comfortable with the hosting provider's data handling."
)

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True,
    help=f"Maximum {MAX_FILE_MB} MB per file and {MAX_TOTAL_MB} MB total.",
)

output_name = st.text_input(
    "Output filename",
    value="CombinedFile.pdf",
)

if uploaded_files:
    # Keep the existing predictable alphabetical starting order.
    uploaded_files = sorted(
        uploaded_files,
        key=lambda item: item.name.lower(),
    )

    # Build unique labels, including duplicate filenames.
    name_counts = Counter(item.name for item in uploaded_files)
    seen_names = Counter()
    label_to_file = {}
    labels = []

    for item in uploaded_files:
        seen_names[item.name] += 1

        label = item.name

        if name_counts[item.name] > 1:
            label = f"{item.name} (copy {seen_names[item.name]})"

        label_to_file[label] = item
        labels.append(label)

    st.subheader("Arrange your PDFs")
    st.caption(
        "Drag the files into the order you want. "
        "The first file will appear first in the merged PDF."
    )

    ordered_labels = sort_items(labels)
    ordered_files = [label_to_file[label] for label in ordered_labels]

    total_bytes = sum(item.size for item in ordered_files)

    st.write(f"**Selected files:** {len(ordered_files)}")
    st.write(f"**Total upload size:** {total_bytes / (1024 * 1024):.1f} MB")

    # Validate uploads using the project's existing utility.
    validation_error = validate_uploads(ordered_files)

    if validation_error:
        st.error(validation_error)
    else:
        st.success("Your files are within the upload limits.")

        if st.button("Merge PDFs", type="primary"):
            try:
                merged_pdf = merge_pdfs(ordered_files)
                safe_name = sanitize_filename(output_name)

                st.success(
                    f"Successfully merged {len(ordered_files)} PDF files."
                )

                st.download_button(
                    label="Download merged PDF",
                    data=merged_pdf,
                    file_name=safe_name,
                    mime="application/pdf",
                    type="primary",
                )

            except Exception as error:
                st.error(
                    "Could not merge the files. A PDF may be damaged, "
                    "password-protected, or invalid."
                )
                st.caption(f"Technical detail: {error}")

else:
    st.caption("Select PDF files to get started.")
