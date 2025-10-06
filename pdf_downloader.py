# requests til at downloade gennem HTTP/HTTPS

## Requests import
import requests as req

class PdfDownloader:
    ## Definerer initialisering og andre elementer
    def __init__(self):
        pass

    ## Funktion der henter ned via requests gennem URL
    def download(self, url: str) -> bytes:
        # Anmoder om download på url
        response = req.get(url)
        # Sender status besked tilbage
        response.raise_for_status()
        # Returnere indholdet
        return response.content