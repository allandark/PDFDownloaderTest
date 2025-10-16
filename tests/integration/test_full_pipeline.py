import pytest
from unittest.mock import patch

import os
import zlib

from PDFDownloader.pdf_downloader import PdfDownloader
from PDFDownloader.file_saver import FileSaver
from PDFDownloader.excel_reader import ExcelReader
from PDFDownloader.logger import LoggerService
from PDFDownloader.main import MainController


@pytest.fixture
def saver():
    return FileSaver(LoggerService())

@pytest.fixture
def downloader():
    return PdfDownloader(LoggerService())

@pytest.fixture
def reader():
    return ExcelReader(LoggerService())

@pytest.fixture
def sample_file_path():        
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "test_files")

@pytest.fixture
def mock_data_tuple():
    return [
        ('http://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf', 
        'BR50042')] 

@pytest.fixture
def mock_sample_data(sample_file_path):
    with open(
        os.path.join(sample_file_path, "BR50042.pdf"),
        'rb') as f:
        data = f.read()
    yield data


def test_full_pipeline_valid_file_url(
    tmp_path, sample_file_path,
    saver, reader, downloader, 
    mock_data_tuple, mock_sample_data ):
    read_result = reader.read_data(
        os.path.join(sample_file_path, "sample_excel_valid.xlsx"), 
        "Pdf_URL", "BRnum")
    assert read_result == mock_data_tuple

    download_result = downloader.download(read_result[0][0])
    assert download_result == mock_sample_data   

    save_result = saver.save(
        download_result,
        tmp_path,
        read_result[0][1]) 
    result_path = tmp_path / read_result[0][1]
    assert result_path.exists()
    assert zlib.crc32(result_path.read_bytes()) == zlib.crc32(mock_sample_data)         


def test_full_pipeline_invalid_url(
    tmp_path, sample_file_path,
    saver, reader, downloader, 
    mock_data_tuple, mock_sample_data ):
    
    read_result = reader.read_data(
        os.path.join( sample_file_path, "sample_excel_valid.xlsx"), 
        "Pdf_URL", "BRnum")
    assert read_result == mock_data_tuple
    invalid_url = "http://arpeissig.at/wp-content/uploads/2016/02/D7_NHB_ARP_Final_2.pdf"
    
    with pytest.raises(RuntimeError):
        download_result = downloader.download(invalid_url)
          


def test_main_controller_run_valid(
    tmp_path, sample_file_path,
    saver, reader, downloader, 
    mock_data_tuple, mock_sample_data ):
    controller = MainController(reader, downloader, saver, LoggerService())
    try:
        controller.run(os.path.join( sample_file_path, "sample_excel_valid.xlsx"), "Pdf_URL", "BRnum", tmp_path)  
    except Exception as e:
        pytest.fail(f"Unexcepted exception raised: {e}")
    

