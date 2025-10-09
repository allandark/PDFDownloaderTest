# 🧩 PDF Downloader

Et simpelt, modulopbygget Python-program der kan downloade PDF-filer fra URL’er gemt i et Excel-ark.  
Programmet er designet med **separation of concerns**, **SOLID-principper** og **modulær arkitektur** for at gøre det nemt at udvide og vedligeholde.

---

## 🚀 Funktioner

- Læser URL’er og filnavne fra et Excel-ark (.xlsx)
- Downloader PDF’er fra de angivne URL’er
- Gemmer dem i en valgfri mappe
- Fejlhåndtering ved manglende filer, ugyldige URL’er og kolonnenavne

---

## 🧱 Projektstruktur
```
📁 pdf_downloader/
│
├── main.py # CLI entry point
├── excel_reader.py # Læser data fra Excel-ark
├── pdf_downloader.py # Downloader PDF’er fra URL’er
├── file_saver.py # Gemmer filer i output-mappe
└── logger.py # (Valgfrit) Logning af hændelser
```

---

## ⚙️ Installation

1. Klon projektet:
```
   bash
   git clone https://github.com/<brugernavn>/pdf-downloader.git
   cd pdf-downloader 
```
2. Opret et virtuelt miljø (valgfrit men anbefalet):
```
   python -m venv venv
   source venv/bin/activate # på MacOS/Linux
   venv\Scripts\activate    # på Windows
```
3. Installer requirements:
```
   pip install -r requirements.txt
```

🧩 Brug

Kør programmet fra kommandolinjen:
```
   python main.py -i StiTil/DinMappe -uc KolonnenMedURLer -nc KolonnenMedNavnene -o MappenDu/VilGemmeI
```

Argumenter
Flag	Beskrivelse	Eksempel
--input / -i	Sti til Excel-filen	data/input/Test_ark.xlsx
--url-column / -u	Navn på kolonnen med URL’er	Pdf_URL
--name-column / -n	Navn på kolonnen med filnavne	Pdf_Name
--output / -o	Outputmappe, hvor PDF’er gemmes	data/output
