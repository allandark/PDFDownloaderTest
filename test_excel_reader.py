from excel_reader import ExcelReader

def main():
    reader = ExcelReader()

    try:
        urls = reader.read_urls("data/input/Test_ark.xlsx", "Pdf_URL")
        print("ExcelReader virker. Læste rækker:", len(urls))
        print("Første 3:", urls[:3])
    except Exception as e:
        print("Fejl i ExcelReader:", e)
    
if __name__ == "__main__":
    main()