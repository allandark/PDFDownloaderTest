import pytest
from unittest.mock import patch

import pandas as pd
import os

from PDFDownloader.pdf_downloader import PdfDownloader
from PDFDownloader.logger import LoggerService

@pytest.fixture
def mock_data_tuple():
    return [
        ('http://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf', 
        'BR50042')] 

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
def mock_downloader():
    return PdfDownloader(LoggerService())

def test_download_valid_url(mock_downloader,mock_sample_data, mock_data_tuple ):
    result = mock_downloader.download(mock_data_tuple[0][0])
    assert result == mock_sample_data            


