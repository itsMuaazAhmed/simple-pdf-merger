
from utils.validators import validate_uploads, sanitize_filename


class FakeUpload:
    def __init__(self, name: str, size_mb: int):
        self.name = name
        self.size = size_mb * 1024 * 1024


def test_rejects_empty_uploads():
    assert validate_uploads([]) == "Please upload at least one PDF file."


def test_accepts_valid_uploads():
    files = [FakeUpload("first.pdf", 5), FakeUpload("second.pdf", 10)]
    assert validate_uploads(files) is None


def test_rejects_file_over_limit():
    error = validate_uploads([FakeUpload("large.pdf", 26)])
    assert error is not None
    assert "large.pdf" in error
    assert "25 MB" in error


def test_rejects_total_size_over_limit():
    files = [FakeUpload(f"file{i}.pdf", 21) for i in range(5)]
    error = validate_uploads(files)
    assert error is not None
    assert "100 MB" in error


def test_sanitizes_filename():
    assert sanitize_filename("my:report") == "my_report.pdf"


def test_keeps_pdf_extension():
    assert sanitize_filename("combined.PDF") == "combined.PDF"


def test_uses_default_for_empty_filename():
    assert sanitize_filename("") == "CombinedFile.pdf"
