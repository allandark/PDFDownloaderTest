# 📜 PDF Downloader

Et simpelt, modulopbygget Python-program der kan downloade PDF-filer fra URL’er gemt i et Excel-ark.  
Programmet er designet med **separation of concerns**, **SOLID-principper** og **modulær arkitektur** for at gøre det nemt at udvide og vedligeholde.

---

## 🚀 Funktioner

- Læser URL’er fra kolonner i et Excel-ark (.xlsx)
- Downloader PDF’er fra de angivne URL’er
- Navngivning efter ønsket kolonnenavn
- Gemmer dem i en valgfri mappe
- Fejlhåndtering ved manglende kolonnenavne og ugyldige URL’er

---

## 🧱 Projektstruktur
```
📁 pdf_downloader/
│
├── main.py            # CLI entry point
├── excel_reader.py    # Læser data fra Excel-ark
├── pdf_downloader.py  # Downloader PDF’er fra URL’er
├── file_saver.py      # Gemmer filer i output-mappe
└── logger.py          # (Valgfrit) Logning af hændelser
```

---

## ⚙️ Installation

1. Klon projektet:
```
   git clone https://github.com/SaneStreet/pdf-downloader.git
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
---

## 🧩 Brug

### Kør programmet fra kommandolinjen:
```
   python main.py -i StiTil/DinMappe -uc KolonnenMedURLer -nc KolonnenMedNavnene -o MappenDu/VilGemmeI
```
---

### Argumenter

| Flag | Beskrivelse | Eksempel |
| --- | --- | --- |
| `-i / --input` | Sti til Excel-filen | `data/input/Data.xlsx` |
| `-uc / --urlcolumn` | Navn på kolonnen med URL’er | `-uc pdf_URL` |
| `-nc / --namecolumn` | Navn på kolonnen med filnavne | `-nc PdfNr` |
| `-o / --output` | Outputmappe, hvor PDF’er gemmes | `-o ./Downloads` |

## 💡 Udvidelser i vente
* Multithreading til asynkront downloading
* Progress bar der viser download-tid
* Mulighed for at hente fra sekundære kolonner
* Potentiel GUI projekt
