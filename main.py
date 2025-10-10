"""
class MainController
Controller der håndterer hele flowet fra læs til gem.

Args:
    input_path(str):    Stien til Excel-arket der skal læses fra
    url_cloumn(str):    Kolonnen i Excel-arket med URL'er
    name_column(str):   Kolonnen i Excel-arket som PDF-filerne skal navngives efter
    output_dir(str):    Stien hvor PDF-filerne skal gemmes til

Functions:
    run(input_path, ..): Funktion der kører programmets flow
    main(): Den centrale funktion hvor alting køres

Returns:
    Downloaded PDF-filer i den valgte output sti

"""

# Imports
import argparse
from excel_reader import ExcelReader
from pdf_downloader import PdfDownloader
from file_saver import FileSaver
from logger import LoggerService

class MainController:

    # Initialisering af klassen
    def __init__(self, excel_reader, pdf_downloader, file_saver, logger ):
        self.excel_reader = excel_reader
        self.pdf_downloader = pdf_downloader
        self.file_saver = file_saver
        self.logger = logger
    
    # funktion der kører download flow 
    def run(self, input_path: str, url_column: str, name_column, output_dir: str) -> None:
        
        # Saml data med excel_reader
        data = self.excel_reader.read_data(input_path, url_column, name_column)
        self.logger.log_info(f"Læste {len(data)} URL'er fra {input_path}")
        # for-loop der henter hvert PDF med tilknyttet filnavn
        for url, filename in data:
            # try-except hvis PDF kan hentes eller ikke
            try:
                data = self.pdf_downloader.download(url)
                file_name = f"{filename}.pdf"
                self.file_saver.save(data, output_dir, file_name)
                #self.logger.log_info(f"✅ Gemte: {saved_path}")
            except Exception as e:
                self.logger.log_error(f"❌ Kunne ikke hentes: {e}")

# Main funktionen
def main():
    # Parser så programmet kan køres med argumenter gennem CLI (konsolbaseret)
    parser = argparse.ArgumentParser(
        description="PDF Downloader - Læser URL'er fra Excel og hentder PDF automatisk."
    )
    # Tilføjer 'input' argument
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Sti til Excel-filen (f.eks. urls.xlsx)"
    )
    # Tilføjer 'urlcolumn' argument
    parser.add_argument(
        "-uc", "--urlcolumn",
        required=True,
        help="Kolonnenavn i Excel-filen, der indeholder URL'er (default: url)"
    )
    # Tilføjer namecolumn argument
    parser.add_argument(
        "-nc", "--namecolumn",
        required=True,
        help="Kolonnenavn i Excel-filen, der indeholder filnavn (default: filename)"
    )
    # Tiføjer 'output' argument
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Mappen hvor PDF'erne skal gemmes i."
    )

    # initialiserer parser args
    args = parser.parse_args()
    # Debugging hvis man vil se hvilke argumenter der er skrevet
    #print("DEBUG:", vars(args))

    # initialiserer klasserne 
    logger = LoggerService()
    excel_reader = ExcelReader(logger)
    pdf_downloader = PdfDownloader(logger)
    file_saver = FileSaver(logger)

    # initialiser controller
    controller = MainController(excel_reader, pdf_downloader, file_saver, logger)
    # Kør controller med valgte argumenter
    controller.run(args.input, args.urlcolumn, args.namecolumn, args.output)

# hvis main, main
if __name__ == '__main__':
    main()