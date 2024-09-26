# Fördjupad Pythonprogrammeringsprojekt: Big Mac Pipeline 

<h2 style="bold">Projektöversikt</h2>
<p align="justify">Detta projekt består av en pipeline för att läsa, transformera och lagra data från en CSV-fil till en SQL-databas. Den är byggd med hjälp av Python och använder bibliotek som `pandas` och `sqlite3` för att hantera data.</p>

<h2 style="bold">Funktioner</h2>
<li>Läsning av data från en CSV-fil.</li>
<li>Transformation av data för att säkerställa korrekta datatyper.</li>
<li>Uppdatering av en SQL-databas med den transformerade datan.</li>
<li>Loggning av händelser och fel.</li>

<h2 style="bold">Filstruktur</h2>
/projekt

├── `main.py`: Huvudscript som kör pipeline

├── `read_csv.py`:  Modul för att läsa in CSV-filen.

├── `transform_data.py`: Modul för att transformera data.

├── `update_database.py`: Modul för att uppdatera SQL-databasen.

├── `logging_config.py`: Konfiguration av loggning.

├── `test_pipeline.py`: Tester för att verifiera pipelinens funktionalitet.

├── `run_batch.bat`: Batchfil för att köra programmet.

├── `bigmac.csv`: CSV-fil som används för datainläsning.

├── `bigmac.db`: SQL-databasfil.

└── `.gitignore`: Ignorera filer vid versionhantering.

<h2><b>Installationsinstruktioner:</b></h2>
<b><u>Klona detta repo:</u></b>

`git clone <repo-url>`
                          
`cd <projektmapp>`

<b>Installera nödvändiga bibliotek:</b>

`pip install pandas`

<h2>Användning</h2>










