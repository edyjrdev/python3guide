#!/usr/bin/env python

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect("warehouse.db")
    cursor = con.cursor()

    sql = """
        SELECT warehouse.compartment_number, warehouse.component, suppliers.name 
        FROM warehouse, suppliers 
        WHERE suppliers.phone_number='011235813' AND
          warehouse.supplier=suppliers.short_name"""
    cursor.execute(sql)
    print(cursor.fetchall())

