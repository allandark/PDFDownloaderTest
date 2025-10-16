import pytest
from unittest.mock import patch

import pandas as pd
import os

from PDFDownloader.excel_reader import ExcelReader
from PDFDownloader.logger import LoggerService


@pytest.fixture
def mock_data_tuple():
    return [
        ('http://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf', 
        'BR50042')] 

@pytest.fixture
def mock_reader():
    return ExcelReader(LoggerService())

@pytest.fixture
def sample_file_path():        
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "test_files")


def test_read_excel_valid_file(mock_reader, mock_data_tuple, sample_file_path):
    result = mock_reader.read_data(
        os.path.join(sample_file_path, "sample_excel_valid.xlsx"), 
        "Pdf_URL", "BRnum")
    assert result == mock_data_tuple

def test_read_excel_no_row_file(mock_reader, mock_data_tuple, sample_file_path):
    with pytest.raises(ValueError):
        result = mock_reader.read_data(
            os.path.join(sample_file_path, "sample_excel_no_row.xlsx"), 
            "Pdf_URL", "BRnum")
        
def test_read_excel_invalid_header_file(mock_reader, mock_data_tuple, sample_file_path):
    with pytest.raises(ValueError):
        result = mock_reader.read_data(
            os.path.join(sample_file_path, "sample_excel_invalid_header.xlsx"), 
            "Pdf_URL", "BRnum")