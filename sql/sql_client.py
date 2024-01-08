#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:17:42 2024

@author: shane
"""

import sqlite3


class SqlClient:
    """SqlClient class"""
    def __init__(self, db_name: str = "db.sqlite3"):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.con.close()

    def query(self, query: str):
        """Query"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def query_one(self, query: str):
        """Query one"""
        self.cur.execute(query)
        return self.cur.fetchone()

    def query_many(self, query: str, num: int):
        """Query many"""
        self.cur.execute(query)
        return self.cur.fetchmany(num)

    def query_all(self, query: str):
        """Query all"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def query_table(self, table_name: str):
        """Query table"""
        self.cur.execute(f"SELECT * FROM {table_name}")
        return self.cur.fetchall()

    def query_table_one(self, table_name: str):
        """Query table one"""
        self.cur.execute(f"SELECT * FROM {table_name}")
        return self.cur.fetchone()

    def query_table_many(self, table_name: str, num: int):
        """Query table many"""
        self.cur.execute(f"SELECT * FROM {table_name}")
        return self.cur.fetchmany(num)

    def query_table_all(self, table_name: str):
        """Query table all"""
        self.cur.execute(f"SELECT * FROM {table_name}")
        return self.cur.fetchall()

    def query_table_column(self, table_name: str, column_name: str):
        """Query table column"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name}")
        return self.cur.fetchall()

    def query_table_column_one(self, table_name: str, column_name: str):
        """Query table column one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name}")
        return self.cur.fetchone()

    def query_table_column_many(self, table_name: str, column_name: str, num: int):
        """Query table column many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name}")
        return self.cur.fetchmany(num)

    def query_table_column_all(self, table_name: str, column_name: str):
        """Query table column all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name}")
        return self.cur.fetchall()

    def query_table_column_where(self, table_name: str, column_name: str, where: str):
        """Query table column where"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_one(self, table_name: str, column_name: str, where: str):
        """Query table column where one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchone()

    def query_table_column_where_many(self, table_name: str, column_name: str, where: str, num: int):
        """Query table column where many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchmany(num)

    def query_table_column_where_all(self, table_name: str, column_name: str, where: str):
        """Query table column where all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_like(self, table_name: str, column_name: str, where: str):
        """Query table column where like"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_like_one(self, table_name: str, column_name: str, where: str):
        """Query table column where like one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchone()

    def query_table_column_where_like_many(self, table_name: str, column_name: str, where: str, num: int):
        """Query table column where like many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchmany(num)

    def query_table_column_where_like_all(self, table_name: str, column_name: str, where: str):
        """Query table column where like all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_not_like(self, table_name: str, column_name: str, where: str):
        """Query table column where not like"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_not_like_one(self, table_name: str, column_name: str, where: str):
        """Query table column where not like one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchone()

    def query_table_column_where_not_like_many(self, table_name: str, column_name: str, where: str, num: int):
        """Query table column where not like many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchmany(num)

    def query_table_column_where_not_like_all(self, table_name: str, column_name: str, where: str):
        """Query table column where not like all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_in(self, table_name: str, column_name: str, where: str):
        """Query table column where in"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_in_one(self, table_name: str, column_name: str, where: str):
        """Query table column where in one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchone()

    def query_table_column_where_in_many(self, table_name: str, column_name: str, where: str, num: int):
        """Query table column where in many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchmany(num)

    def query_table_column_where_in_all(self, table_name: str, column_name: str, where: str):
        """Query table column where in all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_not_in(self, table_name: str, column_name: str, where: str):
        """Query table column where not in"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_where_not_in_one(self, table_name: str, column_name: str, where: str):
        """Query table column where not in one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchone()

    def query_table_column_where_not_in_many(self, table_name: str, column_name: str, where: str, num: int):
        """Query table column where not in many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchmany(num)

    def query_table_column_where_not_in_all(self, table_name: str, column_name: str, where: str):
        """Query table column where not in all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where}")
        return self.cur.fetchall()

    def query_table_column_order_by(self, table_name: str, column_name: str, order: str):
        """Query table column order by"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_order_by_one(self, table_name: str, column_name: str, order: str):
        """Query table column order by one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_order_by_many(self, table_name: str, column_name: str, order: str, num: int):
        """Query table column order by many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_order_by_all(self, table_name: str, column_name: str, order: str):
        """Query table column order by all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_order_by_desc(self, table_name: str, column_name: str, order: str):
        """Query table column order by desc"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_order_by_desc_one(self, table_name: str, column_name: str, order: str):
        """Query table column order by desc one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_order_by_desc_many(self, table_name: str, column_name: str, order: str, num: int):
        """Query table column order by desc many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_order_by_desc_all(self, table_name: str, column_name: str, order: str):
        """Query table column order by desc all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_order_by_asc(self, table_name: str, column_name: str, order: str):
        """Query table column order by asc"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_order_by_asc_one(self, table_name: str, column_name: str, order: str):
        """Query table column order by asc one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_order_by_asc_many(self, table_name: str, column_name: str, order: str, num: int):
        """Query table column order by asc many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_order_by_asc_all(self, table_name: str, column_name: str, order: str):
        """Query table column order by asc all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_limit(self, table_name: str, column_name: str, limit: int):
        """Query table column limit"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit}")
        return self.cur.fetchall()

    def query_table_column_limit_one(self, table_name: str, column_name: str, limit: int):
        """Query table column limit one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit}")
        return self.cur.fetchone()

    def query_table_column_limit_many(self, table_name: str, column_name: str, limit: int, num: int):
        """Query table column limit many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit}")
        return self.cur.fetchmany(num)

    def query_table_column_limit_all(self, table_name: str, column_name: str, limit: int):
        """Query table column limit all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit}")
        return self.cur.fetchall()

    def query_table_column_limit_offset(self, table_name: str, column_name: str, limit: int, offset: int):
        """Query table column limit offset"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchall()

    def query_table_column_limit_offset_one(self, table_name: str, column_name: str, limit: int, offset: int):
        """Query table column limit offset one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchone()

    def query_table_column_limit_offset_many(self, table_name: str, column_name: str, limit: int, offset: int, num: int):
        """Query table column limit offset many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchmany(num)

    def query_table_column_limit_offset_all(self, table_name: str, column_name: str, limit: int, offset: int):
        """Query table column limit offset all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchall()

    def query_table_column_where_order_by(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_order_by_one(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_where_order_by_many(self, table_name: str, column_name: str, where: str, order: str, num: int):
        """Query table column where order by many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_where_order_by_all(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_order_by_desc(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by desc"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_order_by_desc_one(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by desc one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_where_order_by_desc_many(self, table_name: str, column_name: str, where: str, order: str, num: int):
        """Query table column where order by desc many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_where_order_by_desc_all(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by desc all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_order_by_asc(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by asc"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_order_by_asc_one(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by asc one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_where_order_by_asc_many(self, table_name: str, column_name: str, where: str, order: str, num: int):
        """Query table column where order by asc many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_where_order_by_asc_all(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where order by asc all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_limit(self, table_name: str, column_name: str, where: str, limit: int):
        """Query table column where limit"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit}")
        return self.cur.fetchall()

    def query_table_column_where_limit_one(self, table_name: str, column_name: str, where: str, limit: int):
        """Query table column where limit one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit}")
        return self.cur.fetchone()

    def query_table_column_where_limit_many(self, table_name: str, column_name: str, where: str, limit: int, num: int):
        """Query table column where limit many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit}")
        return self.cur.fetchmany(num)

    def query_table_column_where_limit_all(self, table_name: str, column_name: str, where: str, limit: int):
        """Query table column where limit all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit}")
        return self.cur.fetchall()

    def query_table_column_where_limit_offset(self, table_name: str, column_name: str, where: str, limit: int, offset: int):
        """Query table column where limit offset"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchall()

    def query_table_column_where_limit_offset_one(self, table_name: str, column_name: str, where: str, limit: int, offset: int):
        """Query table column where limit offset one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchone()

    def query_table_column_where_limit_offset_many(self, table_name: str, column_name: str, where: str, limit: int, offset: int, num: int):
        """Query table column where limit offset many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchmany(num)

    def query_table_column_where_limit_offset_all(self, table_name: str, column_name: str, where: str, limit: int, offset: int):
        """Query table column where limit offset all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} LIMIT {limit} OFFSET {offset}")
        return self.cur.fetchall()

    def query_table_column_where_like_order_by(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where like order by"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    def query_table_column_where_like_order_by_one(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where like order by one"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchone()

    def query_table_column_where_like_order_by_many(self, table_name: str, column_name: str, where: str, order: str, num: int):
        """Query table column where like order by many"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchmany(num)

    def query_table_column_where_like_order_by_all(self, table_name: str, column_name: str, where: str, order: str):
        """Query table column where like order by all"""
        self.cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {where} ORDER BY {order}")
        return self.cur.fetchall()

    