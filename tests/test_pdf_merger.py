
import io

from pypdf import PdfReader, PdfWriter

from services.pdf_merger import merge_pdfs


class FakeUpload:
    def __init__(self, name: str, content: bytes):
        self.name = name
        self._content = content

    def getvalue(self) -> bytes:
        
        return self._content


def create_test_pdf(text: str) -> bytes:
    writer = PdfWriter()
    writer.add_blank_page(width=300, height=300)

    output = io.BytesIO()
    writer.write(output)
    writer.close()

    return output.getvalue()


def test_merges_two_pdfs():
    first_pdf = FakeUpload("first.pdf", create_test_pdf("First"))
    second_pdf = FakeUpload("second.pdf", create_test_pdf("Second"))

    merged_bytes = merge_pdfs([first_pdf, second_pdf])
    reader = PdfReader(io.BytesIO(merged_bytes))

    assert len(reader.pages) == 2
