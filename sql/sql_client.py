#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:17:42 2024

@author: shane
"""

import sqlite3
from typing import Any


class SqlClient:
    """SqlClient class"""
    def __init__(self, db_name: str = "db.sqlite3"):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def __enter__(self):  # type: ignore
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None: # type: ignore
        self.con.close()

    def query(self, query: str) -> list:
        """Query (select, insert, update, delete)"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def query_one(self, query: str) -> Any:
        """Query one (or many)"""
        self.cur.execute(query)
        return self.cur.fetchone()

    def query_many(self, query: str, num: int) -> list:
        """Query many"""
        self.cur.execute(query)
        return self.cur.fetchmany(num)
