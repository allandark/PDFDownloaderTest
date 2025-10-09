## Til at gemme PDF-filer på disk

## Operativ system egenskaber importeres
import os
from logger import LoggerService

class FileSaver:
    ## Definerer initialisering og andre elementer
    def __init__(self, logger: LoggerService):
        self.logger = logger

    ## funktion der gemmer filerne via output_dir
    def save(self, file_data: bytes, output_dir: str, filename: str) -> str:
        # Laver en mappe, hvis ikke den eksisterer
        os.makedirs(output_dir, exist_ok=True)
        # Laver en rute til mappen og fil-navn
        path = os.path.join(output_dir, filename)

        # Try-catch for at tjekke om den gemmer korrekt
        try:
            with open(path, "wb") as f:
                f.write(file_data)
        except Exception as e:
            raise IOError(f"Kunne ikke gemme filen '{path}': {e}")

        self.logger.log_info(f"Fil gemt: {path}")
        # returnere path
        return path