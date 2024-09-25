"""Denna är det huvudscriptet som kör hela pipelinen"""

import logging
import sqlite3
import pandas as pd
import logging_config
import read_csv
import transform_data
import update_database

def main():
    """
    Huvudfunktionen som kör hela pipelinen.
    """
    log_file = "pipeline_log.log"
    csv_file = r"C:\Users\girli\Documents\Kunskapskontroll02_Fördjupad_Pythonprogrammering\bigmac.csv"
    db_path = 'bigmac.db'

    # Konfigurera loggning
    logging_config.configure_logging(log_file)

    try:
        # Läs CSV-fil
        df = read_csv.read_csv(csv_file)

        # Transformera data
        transformed_df = transform_data.transform_data(df)

        # Uppdatera SQL-tabell
        update_database.update_database(transformed_df, db_path)

        logging.info("Pipeline kördes framgångsrikt.")

    except FileNotFoundError as fnfe:
        logging.error("Filen kunde inte hittas: %s", str(fnfe))

    except pd.errors.EmptyDataError as ee:
        logging.error("CSV-filen är tom: %s", str(ee))

    except pd.errors.ParserError as pe:
        logging.error("Fel vid parsing av CSV-filen: %s", str(pe))

    except sqlite3.Error as dbe:
        logging.error("Databasfel: %s", str(dbe))

    except Exception as e:
        logging.error("Ett okänt fel inträffade i pipelinen: %s", str(e))

if __name__ == "__main__":
    main()
