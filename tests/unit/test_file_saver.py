import pytest
from unittest.mock import patch, mock_open

from os import makedirs
from pathlib import Path

from PDFDownloader.file_saver import FileSaver
from PDFDownloader.logger import LoggerService


@pytest.fixture
def mock_file_saver():
    return FileSaver(LoggerService())


def test_save_valid_path(tmp_path, mock_file_saver):
    with patch("builtins.open"):
        with patch("os.makedirs"):            
            result = mock_file_saver.save(b'data', tmp_path, 'filename.pdf')
            file_path = tmp_path / "filename.pdf"
            assert result == file_path

# DEMO: show
def test_save_makedirs_permission_denied(tmp_path, mock_file_saver):
    with patch("builtins.open"):
        with patch("os.makedirs", side_effect= PermissionError):            
            with pytest.raises(PermissionError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')
            

def test_save_makedirs_os_error(tmp_path, mock_file_saver):
    with patch("builtins.open"):
        with patch("os.makedirs", side_effect= OSError):            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')
            

def test_save_open_permission_denied(tmp_path, mock_file_saver):
    with patch("builtins.open", side_effect= PermissionError):
        with patch("os.makedirs"):            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')


def test_save_open_is_a_dir(tmp_path, mock_file_saver):
    with patch("builtins.open", side_effect= IsADirectoryError):
        with patch("os.makedirs"):            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')

def test_save_open_dir_not_found(tmp_path, mock_file_saver):
    with patch("builtins.open", side_effect=FileNotFoundError ):
        with patch("os.makedirs"):            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')

def test_save_write_type_error(tmp_path, mock_file_saver):
    with patch("builtins.open", mock_open()) as mocked_open:
        with patch("os.makedirs"):
            mocked_open().write.side_effect = TypeError            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')

def test_save_write_value_error(tmp_path, mock_file_saver):
    with patch("builtins.open", mock_open()) as mocked_open:
        with patch("os.makedirs"):
            mocked_open().write.side_effect = ValueError            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')

def test_save_write_os_error(tmp_path, mock_file_saver):
    with patch("builtins.open", mock_open()) as mocked_open:
        with patch("os.makedirs"):
            mocked_open().write.side_effect = OSError            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')

def test_save_write_block_io(tmp_path, mock_file_saver):
    with patch("builtins.open", mock_open()) as mocked_open:
        with patch("os.makedirs"):
            mocked_open().write.side_effect = BlockingIOError            
            with pytest.raises(OSError):
                mock_file_saver.save(b'data', tmp_path, 'filename.pdf')