#!/usr/bin/env python3
# -*- coding utf8 -*-
"""Simple database Operations"""

from flask import g
import sqlite3

DATABASE="catalog_db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["name"] = result[1]
        res_dict["price"] = result[2]
        res_dict["category"] = result[3]
        res_dict["description"] = result[4]
        res_dict["active"] = result[5]
        out["body"].append(res_dict)
    return out

def scan():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def read(prod_id):
    query = """
        SELECT *
        FROM product
        WHERE id = ?
        """
    cursor = get_db().execute(query, (prod_id))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

""" UPDATE user SET first_name='Raven', last_name='Mirabeau' WHERE id=1; """
def update(prod_id, fields: dict):
    field_string = ", ".join(
                    "%s=\"%s\"" % (key, val)
                    for key, val
                    in fields.items())

    query = """
            UPDATE product
            SET %s
            WHERE id = ?
            """ % field_string
    cursor  = get_db()
    cursor.execute(query, (prod_id))
    cursor.commit()
    return True

def create(name, price, category, description):
    value_tuple = (name, price, category, description)
    query = """
            INSERT INTO product(
                name,
                price,
                category,
                description)
            VALUES (?, ?, ?, ?)
        """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).last_row_id
    cursor.commit()
    return last_row_id

def delete(prod_id): # Use "UPDATE" and change active from "True" to False" for a soft delete
    query = "DELETE FROM product WHERE id=%s" % prod_id
    cursor = get_db()
    cursor.execute(query,())
    cursor.commit()
    return True

