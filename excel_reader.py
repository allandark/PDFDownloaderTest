# Panel Data import
import pandas as pd
from logger import LoggerService

class ExcelReader:

    def __init__(self, logger: LoggerService):
        self.logger = logger

    """
    Læser Excel-filer og udtrækker URL’er fra bestemt kolonnenavn til en liste.
    """
    def read_urls(self, file_path: str, column_name: str) -> list[str]:
        self.logger.log_info(f"Forsøger at læse Excel-ark i '{file_path}'")
        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            raise RuntimeError(f"Kunne ikke åbne Excel-filen '{file_path}': {e}")

        if column_name not in df.columns:
            raise ValueError(f"Kolonnen '{column_name}' kunne ikke findes i '{file_path}'.")
        
        urls = df[column_name].dropna().tolist()
        if not urls:
            raise ValueError(f"Ingen URL'er er fundet i kolonnen '{column_name}'.")
        self.logger.log_info(f"Excel-arket er læst. Fortsætter.")
        return urls
