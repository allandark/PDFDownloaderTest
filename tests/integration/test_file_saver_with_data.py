import pytest
from unittest.mock import patch

import zlib
import os

from PDFDownloader.file_saver import FileSaver
from PDFDownloader.logger import LoggerService


@pytest.fixture
def sample_file_path():        
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "test_files")

@pytest.fixture
def mock_sample_data(sample_file_path):
    with open(
        os.path.join(sample_file_path, "BR50042.pdf"),
        'rb') as f:
        data = f.read()
    yield data


@pytest.fixture
def saver():
    return FileSaver(LoggerService())

# DEMO: show
def test_save_valid(
        saver, 
        mock_sample_data, 
        tmp_path):
    result = saver.save(
        mock_sample_data,
        tmp_path,
        "saver_test.pdf") 
    result_path = tmp_path / "saver_test.pdf"
    assert result_path.exists()
    assert zlib.crc32(result_path.read_bytes()) == zlib.crc32(mock_sample_data)