## Til at gemme PDF-filer på disk

## Operativ system egenskaber importeres
import os

class FileSaver:
    ## Definerer initialisering og andre elementer
    def __init__(self):
        pass

    ## funktion der gemmer filerne via output_dir
    def save(self, file_data: bytes, output_dir: str, filename: str) -> str:
        # Laver en mappe, hvis ikke den eksisterer
        os.makedirs(output_dir, exist_ok=True)
        # Laver en rute til mappen og fil-navn
        path = os.path.join(output_dir, filename)
        # Nedskriver indholdet på path
        with open(path, "wb") as f:
            f.write(file_data)
        # returnere path
        return path