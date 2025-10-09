# requests til at downloade gennem HTTP/HTTPS

## Requests import
import requests as req
from logger import LoggerService

class PdfDownloader:
    ## Definerer initialisering og andre elementer
    def __init__(self, logger: LoggerService):
        self.logger = logger

    ## Funktion der henter ned via requests gennem URL
    def download(self, url: str) -> bytes:
        self.logger.log_info(f"Forsøger at downloade fra {url}")

        try:
            response = req.get(url, timeout=10)
            response.raise_for_status()
        except req.RequestException as re:
            raise RuntimeError(f"Fejl ved download af {url}: {re}")
        
        if not response.headers.get("Content-Type", "").startswith("application/pdf"):
            self.logger.log_error(f"Advarsel: Filen fra {url} er muligvis ikke en PDF.")
        
        return response.content