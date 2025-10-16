"""
class ExcelReader
Læser en Excel-fil og returnerer en liste af url- og filnavn tuples.

Args:
    file_path (str):    Stien til Excel-filen
    url_column (str):   Navnet på kolonnen med URL
    name_column (str):  Navnet på kolonnen med filnavne

Functions:
    read_data(file_path, ..): Læser data og lægger det i tuples[url, name]

Returns:
    list[tuple[str, str]]: Liste af url/filnavn par
"""

# Panel Data import
import pandas as pd
from logger import LoggerService

class ExcelReader:
    # initialisering af klassen
    def __init__(self, logger: LoggerService):
        self.logger = logger

    # funktion der forsøger at læse i et Excel-ark og finde udvalgte kolonner
    def read_data(self, file_path: str, url_column: str, name_column: str) -> list[tuple[str, str]]:
        self.logger.log_info(f"Forsøger at læse Excel-ark i '{file_path}'")

        # try-except til hvis filen ikke findes eller ikke kan læses
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Filen '{file_path}' blev ikke fundet.")
        except Exception as e:
            raise ValueError(f"Kunne ikke læse Excel-filen: {e}")
        
        # fjerner whitespace i valgte kolonner
        df.columns = df.columns.astype(str).str.strip()

        # Tjek om url kolonnen eksisterer
        if url_column not in df.columns:
            raise ValueError(f"Mangler kolonnen '{url_column}' i Excel filen.")
        # tjek om name kolonnen eksisterer
        if name_column not in df.columns:
            raise ValueError(f"Mangler kolonnen '{name_column}' i Excel filen.")
        
        # Opsæt data tuples så url og navne danner par
        # Derefter fjern whitespace
        data = []
        for _, row in df.iterrows():
            url = str(row[url_column]).strip()
            name = str(row[name_column]).strip()
            if pd.notna(url) and url:
                data.append((url, name))
        # Tjek om der er URL'er i kolonnerne
        if not data:
            raise ValueError("Ingen gyldige URL'er fundet i filen.")

        return data