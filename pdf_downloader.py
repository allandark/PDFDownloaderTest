"""
class PdfDownloader
Downloader PDF-filer fra URL'er

Args:
    url (str): Selve linket der skal downloades fra

Functions:
    download(url): Funktion der downloader fra URL gennem requests

Returns:
    response.content: Response koder og indhold fra URL request modtager
"""

## Requests import
import requests as req
from logger import LoggerService

class PdfDownloader:
    ## Initialisering af klassen
    def __init__(self, logger: LoggerService):
        self.logger = logger

    ## Funktion der henter ned via requests gennem URL
    def download(self, url: str):
        self.logger.log_info(f"↘️ Forsøger at downloade fra {url}")

        # try-except om der er response fra URL-server
        try:
            response = req.get(url, timeout=10)
            response.raise_for_status()
        except req.RequestException as re:
            raise RuntimeError(f"Fejl ved download af {url}:\n {re}")
        
        # Tjek om response headers er korrekt type (application/pdf)
        if not response.headers.get("Content-Type", "").startswith("application/pdf"):
            self.logger.log_error(f"Advarsel: Filen fra {url} er muligvis ikke en PDF.")
        
        # Returner indhold
        return response.content