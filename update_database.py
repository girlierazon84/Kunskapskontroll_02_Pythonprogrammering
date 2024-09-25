"""Denna modul uppdaterar SQL-tabellen."""

import logging
import sqlite3

def update_database(df, db_path):
    """
    Uppdaterar en SQL-databas med den transformerade datan.

    :param df: DataFrame med den bearbetade datan.
    :param db_path: Sökvägen till SQL-databasen.
    """
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql('bigmac_data', conn, if_exists='replace', index=False)
        cursor = conn.cursor()

           # Make sure the table exists before inserting data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bigmac_data (
                date TEXT,
                currency_code TEXT,
                name TEXT,
                local_price REAL,
                dollar_ex REAL,
                dollar_price REAL
            )
        ''')

        # Insert each row into the database
        for index, row in df.iterrows():
            cursor.execute('''
                INSERT INTO bigmac_data (date, currency_code, name, local_price, dollar_ex, dollar_price)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (row['date'],
                  row['currency_code'],
                  row['name'],
                  row['local_price'],
                  row['dollar_ex'],
                  row['dollar_price']))
            print(f"Inserting row {index}: {row.to_dict()}")  # Debug output

        conn.commit()
        logging.info("Databasen uppdaterad framgångsrikt.")
    except Exception as e:
        logging.error("Fel vid uppdatering av databasen: %s", str(e))
        raise
    finally:
        conn.close()
