from flask import Flask, redirect
import sqlite3 as sql

app = Flask(__name__)

@app.route("/<url_id>")
def get_url(url_id):
    pass