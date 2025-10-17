import pytest
from unittest.mock import patch

from requests import Request, Response, exceptions

from PDFDownloader.pdf_downloader import PdfDownloader
from PDFDownloader.logger import LoggerService


@pytest.fixture
def mock_test_data():
    return b'this is test data'

@pytest.fixture
def mock_response_valid(mock_test_data):
    res = Response()
    res.headers['Content-Type'] = 'application/pdf'
    res.status_code = 200
    res._content = mock_test_data
    res.url = "http//abc.dk"
    return res 

@pytest.fixture
def mock_response_invalid_content_type(mock_test_data):
    res = Response()
    res.headers['Content-Type'] = 'application/json'
    res.status_code = 200
    res._content = mock_test_data
    res.url = "http//abc.dk"
    return res 

@pytest.fixture
def mock_response_invalid(mock_test_data):
    res = Response()
    res.headers['Content-Type'] = 'application/json'
    res.status_code = 404
    res._content = b'{"error":"Not Found"}'
    res.reason = "Not Found"
    res.url = "http//abc.dk"
    return res 

@pytest.fixture
def mock_downloader():
    return PdfDownloader(LoggerService())

# DEMO: show
def test_download_valid_url(mock_response_valid, mock_test_data, mock_downloader):
    with patch("requests.get", return_value=mock_response_valid):        
        result = mock_downloader.download(mock_response_valid.url)
        assert result == mock_test_data

@pytest.mark.skip(reason="Pipeline test")
def test_download_invalid_content_type(mock_response_invalid_content_type, mock_downloader):
    with patch("requests.get", return_value=mock_response_invalid_content_type):        
        with pytest.raises(RuntimeError):
            mock_downloader.download(mock_response_invalid_content_type.url)

@pytest.mark.skip(reason="Pipeline test")
def test_download_invalid_content_data(mock_response_invalid_content_type, mock_downloader):
    with patch("requests.get", return_value=mock_response_invalid_content_type):      
        mock_response_invalid_content_type._content = b''
        with pytest.raises(RuntimeError):
            mock_downloader.download(mock_response_invalid_content_type.url)
        
def test_download_response_not_found(mock_response_invalid, mock_downloader):
    with patch("requests.get", return_value=mock_response_invalid):  
        with pytest.raises(RuntimeError):
            mock_downloader.download(mock_response_invalid.url)      

def test_download_connection_error(mock_response_invalid, mock_downloader):
    with patch("requests.get", side_effect=ConnectionError):
        with pytest.raises(ConnectionError):
            mock_downloader.download(mock_response_invalid.url)

def test_download_http_error(mock_response_invalid, mock_downloader):
    with patch("requests.get", side_effect=exceptions.HTTPError):
        with pytest.raises(RuntimeError):
            mock_downloader.download(mock_response_invalid.url)

def test_download_request_exception(mock_response_invalid, mock_downloader):
    with patch("requests.get", side_effect=exceptions.RequestException):
        with pytest.raises(RuntimeError):
            mock_downloader.download(mock_response_invalid.url)
