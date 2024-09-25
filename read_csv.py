"""Denna modul kommer att läsa in CSV-filen."""

import logging
import pandas as pd

def read_csv(file_path):
    """
    Läser in en CSV-fil och returnerar en DataFrame.

    :param file_path: Sökvägen till CSV-filen.
    :return: Pandas DataFrame med innehållet från CSV-filen.
    :raises FileNotFoundError: Om filen inte hittas.
    :raises pd.errors.EmptyDataError: Om filen är tom.
    :raises pd.errors.ParserError: Om det uppstår ett parserfel vid inläsning.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("CSV fil inläst framgångsrikt.")

        # Normalisera kolumnnamn för att undvika KeyError och ta bort inledande mellanslag.
        data.columns = data.columns.str.strip()

        # Felsökning: skriv ut de första raderna och skriv ut kolumnnamnen.
        print(data.head())
        print(data.columns)
        return data
    except FileNotFoundError as e:
        logging.error("CSV-filen hittades inte: %s", str(e))
        raise
    except pd.errors.EmptyDataError as e:
        logging.error("CSV-filen är tom: %s", str(e))
        raise
    except pd.errors.ParserError as e:
        logging.error("Fel vid inläsning av CSV-filen: %s", str(e))
        raise
    except Exception as e:
        logging.error("Ett oväntat fel inträffade: %s", str(e))
        raise
