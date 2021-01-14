#!/usr/bin/env python3
# -*- coding utf8 -*-
"""HTTP route definitions"""


from flask import request, render_template
from app import app
from app.database import create, read, delete, scan
from datetime import datetime

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%f %H:%M:%S")
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/products")
def get_all_products():
    out = scan()
    out["ok"] = True
    out["message"] = "Success"
    return out

@app.route("/products/<pid>")
def get_one_product(pid):
    out = read(int(pid))
    out["ok"] = True
    out["message"] = "Success"
    return out

@app.route("/products", methods=["POST"])
def create_product():
    product_data = request.json
    new_id = create(
        product_data.get("name"),
        product_data.get("price"),
        product_data.get("category"),
        product_data.get("description"),
    )

    return {"ok": True, "message": "Success", "new_id": new_id}

@app.route("/products/<pid>", methods=["PUT"])
def update_product(pid):
    product_data = request.json
    out = update(int(pid), product_data)
    return {"ok": out, "message": "Updated"
    }


@app.route("/agent")
def agent():
    user_agent = request.headers.get("User_Agent")
    return "<p>Your user agent is %s</p>" % user_agent

@app.route("/myroute")
def my_view_function():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@app.route("/about")
def about():
    return render_template("about.html", first_name="Raven", last_name="Mirabeau", hobbies="RPI projects")