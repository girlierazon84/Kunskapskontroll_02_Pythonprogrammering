"""Här sker datakonvertering och formatering."""

import logging
import pandas as pd


def transform_data(df):
    """
    Transformera DataFrame för att säkerställa att datatyperna är korrekta.

    :param df: Inmatad DataFrame.
    :return: Transformera DataFrame.
    """
    try:
        # Omvandla 'date' kolumnen till datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        logging.info("Data har transformerats framgångsrikt.")
        return df
    except KeyError as ke:
        logging.error("Fel: Kolumnen saknas %s", str(ke))
        raise
    except Exception as e:
        logging.error("Fel vid datatransformation: %s", str(e))
        raise
