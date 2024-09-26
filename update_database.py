"""Denna modul uppdaterar SQL-tabellen."""

import logging
import sqlite3
import pandas as pd

def update_database(df, db_path):
    """
    Uppdaterar en SQL-databas med den transformerade datan.

    :param df: DataFrame med den bearbetade datan.
    :param db_path: Sökvägen till SQL-databasen.
    """
    try:
        # Öppna anslutning till databasen
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Skapa tabellen om den inte redan finns
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bigmac (
                date TEXT,
                currency_code TEXT,
                name TEXT,
                local_price REAL,
                dollar_ex REAL,
                dollar_price REAL
            )
        ''')

        # Loop igenom DataFrame och lägg in rader i databasen
        for index, row in df.iterrows():
            # Konvertera datum till sträng om det är ett datetime-objekt
            date_value = row['date']
            if isinstance(date_value, pd.Timestamp):
                date_value = date_value.strftime('%Y-%m-%d')

            cursor.execute('''
                INSERT INTO bigmac (
                    date,
                    currency_code,
                    name,
                    local_price,
                    dollar_ex,
                    dollar_price
                )
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                # Korrekt format på datum
                date_value,
                row['currency_code'],
                row['name'],
                row['local_price'],
                row['dollar_ex'],
                row['dollar_price']
            ))
            print(f"Inserting row {index}: {row.to_dict()}")

        # Spara ändringar
        conn.commit()
        logging.info("Databasen uppdaterad framgångsrikt.")
    except Exception as e:
        logging.error("Fel vid uppdatering av databasen: %s", str(e))
        raise
    finally:
        conn.close()
