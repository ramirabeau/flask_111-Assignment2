#!/usr/bin/env python3
# -*- coding utf8 -*-

"""Simple pyhon request test for visual confirmation 
    These aren't unit tests
"""

import requests
from pprint import pprint

def test_scan():
    resp = requests.get("http://127.0.0.1:5000/products")
    pprint(resp.json())

def test_read():
    resp = requests.get("http://127.0.0.1:5000/products/1")
    pprint(resp.json())

def test_create():
    sample = {"name": "laptop", "price": 1000.0, "description": "Black"}
    resp = request.post("http://127.0.0.1:5000/products", json=sample)
    pprint(resp.json())

def test_update():
    sample = {"name": "banana", "price": 2000.0,}
    resp = request.post("http://127.0.0.1:5000/products/8", json=sample)
    pprint(resp.json())

if __name__ == "__main__":
    test_scan()
    test_read()
    test_create()
    test_update()