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
    
    def run(self, input_path: str, column_name: str, output_dir: str) -> None:
        self.logger.log_info(f"DEBUG: input_path={input_path}, column_name={column_name}, output_dir={output_dir}")
        urls = self.excel_reader.read_urls(input_path, column_name)
        self.logger.log_info(f"Læste {len(urls)} URL'er fra {input_path}")

        for i, url in enumerate(urls, start=1):
            try:
                data = self.pdf_downloader.download(url)
                filename = f"file_{i:03}.pdf"
                saved_path = self.file_saver.save(data, output_dir, filename)
                self.logger.log_info(f"✅ Gemte: {saved_path}")
            except Exception as e:
                self.logger.log_error(f"❌ Kunne ikke hente {url}: {e}")

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
        "-c", "--column",
        default="url",
        help="Kolonnenavn i Excel-filen, der indeholder URL'er (default: url)"
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
    controller.run(args.input, args.column, args.output)

if __name__ == '__main__':
    main()