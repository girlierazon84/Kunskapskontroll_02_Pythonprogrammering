"""Loggning av fel och undantag."""

import logging
import pandas as pd
import read_csv  # Make sure you have this module available

def configure_logging(log_file):
    """
    Konfigurerar loggningsinställningar.

    :param log_file: Sökväg till loggfilen.
    """
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')


def main():
    """
    Huvudfunktionen som demonstrerar loggning och CSV-läsning.
    """
    log_file = "pipeline_log.log"
    configure_logging(log_file)

    # Använd funktionen
    try:
        # Ange sökvägen till din CSV-fil
        df = read_csv.read_csv(r"C:\Users\girli\Documents\Kunskapskontroll_02_Pythonprogrammering\bigmac.csv")
        print(df)
    except FileNotFoundError as e:
        logging.error("CSV-filen hittades inte: %s", str(e))
        print("Ett fel inträffade: CSV-filen hittades inte.")
    except pd.errors.EmptyDataError as e:
        logging.error("CSV-filen är tom: %s", str(e))
        print("Ett fel inträffade: CSV-filen är tom.")
    except pd.errors.ParserError as e:
        logging.error("Fel vid inläsning av CSV-filen: %s", str(e))
        print("Ett fel inträffade: Det uppstod ett parserfel.")
    except Exception as e:
        logging.error("Ett oväntat fel inträffade: %s", str(e))
        print(f"Ett oväntat fel inträffade: {e=}, {type(e)=}")

if __name__ == "__main__":
    main()
