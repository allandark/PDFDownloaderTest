# Panel Data import
import pandas as pd

class ExcelReader:
    """
    Læser Excel-filer og udtrækker URL’er fra bestemt kolonnenavn til en liste.
    """
    def read_urls(self, file_path: str, column_name: str) -> list[str]:
        ## Læser excel gennem pandas
        file = pd.read_excel(file_path)
        ## Skriv en fejlbesked, hvis kolonnenavnet ikke eksisterer
        if column_name not in file.columns:
            raise ValueError(f"Kolonnen '{column_name}' findes ikke i {file_path}.")
        ## Lægger alle URL'er i en liste og returnere listen
        urls = file[column_name].dropna().tolist()
        return urls
