# Fördjupad Pythonprogrammeringsprojekt: Big Mac Pipeline 

<h2>Projektöversikt</h2>
<p align="justify">Detta projekt består av en pipeline för att läsa, transformera och lagra data från en CSV-fil till en SQL-databas. Den är byggd med hjälp av Python och använder bibliotek som `pandas` och `sqlite3` för att hantera data.</p>

<h2>Funktioner</h2>
<li>Läsning av data från en CSV-fil.</li>
<li>Transformation av data för att säkerställa korrekta datatyper.</li>
<li>Uppdatering av en SQL-databas med den transformerade datan.</li>
<li>Loggning av händelser och fel.</li>

<h2>Filstruktur</h2>
/projekt

├── `main.py`: Huvudscript som kör pipeline

├── `read_csv.py`:  Modul för att läsa in CSV-filen.

├── `transform_data.py`: Modul för att transformera data.

├── `update_database.py`: Modul för att uppdatera SQL-databasen.

├── `logging_config.py`: Konfiguration av loggning.

├── `test_pipeline.py`: Tester för att verifiera pipelinens funktionalitet.

├── `batch_test.bat`: Batchfil för att köra programmet.

├── `bigmac.csv`: CSV-fil som används för datainläsning.

├── `bigmac.db`: SQL-databasfil.

└── `.gitignore`: Ignorera filer vid versionhantering.

<h2>Installationsinstruktioner:</h2>
<b><u>Klona detta repo:</u></b>

`git clone <repo-url>`
                          
`cd <projektmapp>`

<b>Installera nödvändiga bibliotek:</b>

`pip install pandas`

<h2>Användning</h2>
<p align="justify">För att köra pipelinen, kör <b><i>main.py</i></b>:</p>

`python main.py`

<h2>Schemaläggning med Windows Task Scheduler</h2>
<p align="justify">Använd Windows Task Scheduler för att schemalägga `main.py` att köras vid en vald tid. Här är en exempelkonfiguration:</p>
<li><b>Program/script:</b>Där `XX` ska ersättas med din Python-version (t.ex. 39 för Python 3.9).</li>

    C:\PythonXX\python.exe

<li><b>Argument:</b></li>

    "C:\Users\girli\Documents\Kunskapskontroll_02_Pythonprogrammering\main.py"

<li><b>Starta i:</b></li>

    C:\Users\girli\Documents\Kunskapskontroll_02_Pythonprogrammering

<h2>Kodöversikt</h2>

1. <b>`read_csv.py`</b>

   <p>Denna modul läser in en CSV-fil och returnerar en <b><i>DataFrame</i>></b>.</p>

        import logging
        import pandas as pd

        def read_csv(file_path):
            ...
   
2. <b>`transform_data.py`</b>

   <p>Denna modul transformerar <b><i>DataFrame</i></b> för att säkerställa att datatyperna är korrekta.</p>

        import logging
        import pandas as pd

        def transform_data(df):
            ...
   
3. <b>`update_database.py`</b>

   <p>Denna modul uppdaterar en SQL-databas med den transformerade datan.</p>

        import logging
        import sqlite3
        import pandas as pd

        def update_database(df, db_path):
            ...

4. <b>`main.py`</b>

   <p>Huvudscriptet som kör hela pipelinen.</p>

        import logging
        import sqlite3
        import pandas as pd
        import logging_config
        import read_csv
        import transform_data
        import update_database

        def main():
            ...

5. <b>`test_pipeline.py`</b>

   <p>Testar att pipelinen körs utan fel och verifierar att den hanterar undantag korrekt.</p>

        import unittest
        import os
        import sqlite3
        import pandas as pd
        import read_csv
        import transform_data
        import update_database
        import main

        class TestPipeline(unittest.TestCase):
            ...

6. <b>`batch_test.bat`</b>

   <p>Batchfil för att köra programmet.</p>

        @echo off
        echo Running batch file test...
        timeout /t 10
        echo Batch test completed!
   
<h2>Loggning</h2>
<p>Loggar händelser och fel till <b><i>pipeline_log.log</i></b>.</p>

<h2>Testning</h2>
<p>För att köra testerna, använd följande kommando:</p>

        python -m unittest test_pipeline.py

<h2>.gitignore</h2>
<p>Denna fil används för att ignorera filer och kataloger som inte ska spåras av git, inklusive:</p>

        __pycache__/
        *.pyc

<h2>Windows Task Scheduler Screenshots</h2>

<img src="../">
