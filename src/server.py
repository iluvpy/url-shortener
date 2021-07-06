import re
from flask import Flask, redirect, render_template, url_for, request
import sqlite3
from db import *
app = Flask(__name__)

host = "localhost"
port = 5000

def center(s: str):
    return f"<center>{s}</center>"


def get_conn_and_c():
    conn = sqlite3.connect("db.sqlite")
    return conn, conn.cursor()

@app.route("/<url_id>")
def url(url_id):
    conn, c = get_conn_and_c()
    result = get_url(url_id, c)
    conn.close()
    return redirect(result) if result != None else center("url does not exist")

@app.route("/curl/<url>/<id>/")
def add_new_url(url, id):
    conn, c = get_conn_and_c()
    if "\\\\" in url:
        url = url.replace("\\\\", "//")
    res = add_url_and_id(url, id, conn, c)
    conn.close()
    return center(res)

@app.route("/rurl/<id>")
def delete_url(id):
    conn, c = get_conn_and_c()
    res = remove_url(id, conn, c)
    return center(res)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else: 
        conn, c = get_conn_and_c()
        id = add_url(request.form["url"], conn, c)
        url = f"http://{host}:{port}/{id}"
        ctx = {"url": url}
        return render_template("created.html", context=ctx)

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)