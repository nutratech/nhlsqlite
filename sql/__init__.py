#!/usr/bin/env python3
"""Main module for building db.sqlite3"""

import csv
import os
import sqlite3

OUTPUT_DB_NAME = "db.sqlite3"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DATA_DIR = os.path.join(SCRIPT_DIR, "data")


def build_db(verbose: bool = False) -> bool:
    """Builds and inserts stock data into db.sqlite3"""
    # cd into this script's directory
    os.chdir(SCRIPT_DIR)

    if verbose:
        print("Cleanup...")
    if os.path.isfile(OUTPUT_DB_NAME):
        os.remove(OUTPUT_DB_NAME)

    if verbose:
        print(f"\nPack {OUTPUT_DB_NAME}")
    con = sqlite3.connect(OUTPUT_DB_NAME)
    cur = con.cursor()

    if verbose:
        print("\n-> Create tables")
    with open("tables.sql", encoding="utf-8") as tables:
        cur.executescript(tables.read())

    if verbose:
        print("-> Populate data")
    for file_path in os.listdir(CSV_DATA_DIR):
        if not file_path.endswith(".csv"):
            continue
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        file_path_full = os.path.join("data", file_path)

        # Loop over CSV files
        with open(file_path_full, encoding="utf-8") as csv_file:
            dict_reader = csv.DictReader(csv_file)
            # Skip empty CSV files
            if not dict_reader.fieldnames:
                print(f"WARN: empty CSV? {file_path_full}")
                continue
            # Build values string (not best practice, use parametrized queries instead)
            values = ",".join("?" * len(dict_reader.fieldnames or []))
            reader = csv.reader(csv_file)
            query = f"INSERT INTO {table_name} VALUES ({values});"  # nosec: B608
            if verbose:
                print(f"     {query}")

            cur.executemany(query, reader)

    cur.close()
    con.commit()
    con.close()
    if verbose:
        print("\nDone!")
    return True


if __name__ == "__main__":
    build_db(verbose=True)
