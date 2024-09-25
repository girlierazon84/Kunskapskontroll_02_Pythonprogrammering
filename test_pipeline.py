"""
Denna modul är testsystemet som testar att pipelinen körs utan fel
och även verifierar att den hanterar undantag korrekt.
"""

import unittest
import os
import sqlite3
import pandas as pd
import read_csv
import transform_data
import update_database
import main  # Importerar main.py för att testa pipelinen

class TestPipeline(unittest.TestCase):
    """
    TestPipeline är en testklass som verifierar att pipelinen fungerar korrekt
    genom att testa varje modul för sig samt hela pipelinen.
    """

    def setUp(self):
        """
        Denna metod körs före varje test för att sätta upp testdata och testmiljö.
        Skapar en temporär test-CSV och testdatabas.
        """
        self.test_csv = 'test.csv'
        self.test_db = 'test.db'

        # Skapa en test-CSV-fil
        data = {'date': ['2023-01-01', '2023-01-02'], 'col1': [1, 2]}
        pd.DataFrame(data).to_csv(self.test_csv, index=False)

    def tearDown(self):
        """
        Denna metod körs efter varje test för att rensa upp testfiler.
        Tar bort CSV- och databasfiler om de existerar.
        """
        # Ta bort testfilerna efter att testen har körts
        try:
            if os.path.exists(self.test_csv):
                os.remove(self.test_csv)
            if os.path.exists(self.test_db):
                os.remove(self.test_db)
        except OSError as e:
            print(f"Fel vid borttagning av fil: {e}")

    def test_read_csv(self):
        """
        Testar funktionen read_csv för att säkerställa att CSV-filen läses korrekt.
        """
        df = read_csv.read_csv(self.test_csv)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))  # Kontrollera att rätt antal rader och kolumner läses in

    def test_transform_data(self):
        """
        Testar funktionen transform_data för att säkerställa att data transformerats korrekt.
        """
        df = pd.DataFrame({'date': ['2023-01-01', '2023-01-02']})
        transformed_df = transform_data.transform_data(df)
        self.assertEqual(transformed_df['date'].dtype, 'datetime64[ns]')

    def test_update_database(self):
        """
        Testar funktionen update_database för att säkerställa att
        SQL-databasen uppdateras korrekt.
        """
        df = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02'],  # Ensure 'date' column exists
        'currency_code': ['USD', 'USD'],
        'name': ['Big Mac', 'Big Mac'],
        'local_price': [5.00, 5.00],
        'dollar_ex': [1.00, 1.00],
        'dollar_price': [5.00, 5.00]
        })
        update_database.update_database(df, self.test_db)

        # Kontrollera att data finns i databasen
        try:
            conn = sqlite3.connect(self.test_db)
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) FROM bigmac_data")
            result = cursor.fetchone()
            self.assertEqual(result[0], 4)  # Kontrollera att rätt antal rader har lagts till
        except sqlite3.OperationalError as e:
            print(f"Databasfel: {e}")
        finally:
            conn.close()  # Se till att stänga anslutningen

    def test_pipeline(self):
        """
        Testar hela pipelinen genom att anropa huvudfunktionen i main.py.
        Verifierar att datan från test-CSV läggs till i databasen korrekt.
        """
        # Kör pipelinen med testdata
        main.csv_file = self.test_csv  # Uppdatera filvägen för att använda test-CSV
        main.db_path = self.test_db  # Uppdatera databasvägen för att använda testdatabasen
        main.main()  # Kör pipelinen

        # Kontrollera att SQL-databasen har uppdaterats korrekt
        try:
            conn = sqlite3.connect(self.test_db)
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) FROM bigmac_data")
            result = cursor.fetchone()
            self.assertEqual(result[0], 2)  # Kontrollera att rätt antal rader från CSV lades till
        except sqlite3.OperationalError as e:
            print(f"Databasfel: {e}")
        finally:
            conn.close()  # Se till att stänga anslutningen

if __name__ == '__main__':
    unittest.main()
