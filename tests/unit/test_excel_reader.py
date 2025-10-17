import pytest
from unittest.mock import patch

import pandas as pd
from pathlib import Path

from PDFDownloader.excel_reader import ExcelReader
from PDFDownloader.logger import LoggerService


@pytest.fixture
def mock_data_df():
    return pd.DataFrame({"Pdf_URL": ["http://example.com"], "BRnum": ['123']}) 

@pytest.fixture
def mock_reader():
    return ExcelReader(LoggerService())

def test_read_data_valid_data(tmp_path, mock_data_df, mock_reader):
    mock_data = [("http://example.com", '123')]
    with patch("pandas.read_excel", return_value= mock_data_df):        
        result = mock_reader.read_data(tmp_path, "Pdf_URL", "BRnum")        
        assert Path(result) == mock_data

def test_read_data_invalid_excel_file(tmp_path, mock_data_df, mock_reader):
    with patch("pandas.read_excel", 
        side_effect= ValueError,
        return_value= mock_data_df):
        with pytest.raises(ValueError):
            mock_reader.read_data(tmp_path, "Pdf_URL", "BRtum") 


def test_read_data_invalid_column_url(tmp_path, mock_data_df, mock_reader):
    mock_data = [("http://example.com", '123')]
    with patch("pandas.read_excel", return_value= mock_data_df):        
        with pytest.raises(ValueError):
            mock_reader.read_data(tmp_path, "Pdn_URL", "BRnum") 

def test_read_data_invalid_column_name(tmp_path, mock_data_df, mock_reader):
    mock_data = [("http://example.com", '123')]
    with patch("pandas.read_excel", return_value= mock_data_df):        
        with pytest.raises(ValueError):
            mock_reader.read_data(tmp_path, "Pdf_URL", "BRtum") 

# DEMO: show
def test_read_data_file_not_found(tmp_path, mock_reader):
    with patch("pandas.read_excel", side_effect=FileNotFoundError()):        
        with pytest.raises(FileNotFoundError):
            mock_reader.read_data(f"{tmp_path}/missing.xlsx", "Pdf_URL", "BRnum")

@pytest.mark.skip(reason="Pipeline test")
def test_read_data_invalid_url(tmp_path, mock_reader):    
    with patch("pandas.read_excel", return_value=
        pd.DataFrame({"Pdf_URL": ["invalidurl"], "BRnum": ['123']} )):        
        with pytest.raises(ValueError, match="Ingen gyldige URL'er fundet i filen."):
            mock_reader.read_data(tmp_path, "Pdf_URL", "BRnum") 

@pytest.mark.skip(reason="Pipeline test")
def test_read_data_empty_name(tmp_path, mock_reader):    
    with patch("pandas.read_excel", return_value=
        pd.DataFrame({"Pdf_URL": ["http://example.com"], "BRnum": ['']} )):     
        with pytest.raises(ValueError):
            mock_reader.read_data(tmp_path, "Pdf_URL", "BRnum") 

def test_read_data_empty_url(tmp_path, mock_reader):    
    with patch("pandas.read_excel", return_value=
        pd.DataFrame({"Pdf_URL": [""], "BRnum": ['123']} )):        
        with pytest.raises(ValueError, match="Ingen gyldige URL'er fundet i filen."):
            mock_reader.read_data(tmp_path, "Pdf_URL", "BRnum") 

