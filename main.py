import argparse
from excel_reader import ExcelReader
from pdf_downloader import PdfDownloader
from file_saver import FileSaver
from logger import LoggerService

class MainController:

    def __init__(self, excel_reader, pdf_downloader, file_saver, logger ):
        self.excel_reader = excel_reader
        self.pdf_downloader = pdf_downloader
        self.file_saver = file_saver
        self.logger = logger
    
    def run(self, input_path: str, url_column: str, name_column, output_dir: str) -> None:
        
        data = self.excel_reader.read_data(input_path, url_column, name_column)
        self.logger.log_info(f"Læste {len(data)} URL'er fra {input_path}")
        for url, filename in data:
            try:
                data = self.pdf_downloader.download(url)
                file_name = f"{filename}.pdf"
                saved_path = self.file_saver.save(data, output_dir, file_name)
                self.logger.log_info(f"✅ Gemte: {saved_path}")
            except Exception as e:
                self.logger.log_error(f"❌ Kunne ikke hentes: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="PDF Downloader - Læser URL'er fra Excel og hentder PDF automatisk."
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Sti til Excel-filen (f.eks. urls.xlsx)"
    )
    parser.add_argument(
        "-uc", "--urlcolumn",
        required=True,
        help="Kolonnenavn i Excel-filen, der indeholder URL'er (default: url)"
    )
    parser.add_argument(
        "-nc", "--namecolumn",
        required=True,
        help="Kolonnenavn i Excel-filen, der indeholder filnavn (default: filename)"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Mappen hvor PDF'erne skal gemmes i."
    )

    args = parser.parse_args()
    print("DEBUG:", vars(args))

    logger = LoggerService()
    excel_reader = ExcelReader(logger)
    pdf_downloader = PdfDownloader(logger)
    file_saver = FileSaver(logger)

    controller = MainController(excel_reader, pdf_downloader, file_saver, logger)
    controller.run(args.input, args.urlcolumn, args.namecolumn, args.output)

if __name__ == '__main__':
    main()