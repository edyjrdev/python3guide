#!/usr/bin/env python

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect("warehouse.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE warehouse (
        compartment_number INTEGER, serial_number INTEGER, 
        component TEXT, supplier TEXT, reserved INTEGER)""")

    cursor.execute("""CREATE TABLE suppliers (
        short_name TEXT, name TEXT, phone_number TEXT)""")

    cursor.execute("""CREATE TABLE customers (
        customer_number INTEGER, name TEXT, address TEXT)""")

