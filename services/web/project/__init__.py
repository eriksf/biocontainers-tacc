import os
import requests
import json
import simplejson

from flask import Flask, render_template, request, redirect, jsonify, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
app.config.from_object("project.config.Config")
auth = HTTPTokenAuth(scheme='Bearer')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

class Biocontainers(db.Model):
    __tablename__ = "biocontainers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    version = db.Column(db.String())
    category = db.Column(db.String())
    keywords = db.Column(db.String())
    description = db.Column(db.String())
    url = db.Column(db.String())
    modulename = db.Column(db.String())

    def __init__(self, name, version, category, keywords, description,
                url, modulename):
        self.name = name
        self.version = version
        self.category = category
        self.keywords = keywords
        self.description = description
        self.url = url
        self.modulename = modulename

tokens = {
    "secret-token-1": "greg",
    "secret-token-2": "shweta"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

# homepage
@app.route("/")
def home():
    return render_template("homepage.html")

# display all the biocontainers with details and search
@app.route('/search', methods=["POST","GET"])
def search():
    # display all results from database as a table using /api and ajax
    return render_template("search.html")

# api route for searching biocontainer by name
@app.route('/api/<name>')
def biotoolsid_api(name):
    name_val = db.session.execute("SELECT name FROM biocontainers WHERE name = :name", {"name":name}).fetchone()
    if name_val is None:
         return jsonify({"error": "Invalid name for the biocontainer, error 404"}), 404
    biotools_info = db.session.execute("SELECT * FROM biocontainers WHERE name = :name", {"name":name}).fetchone()
    return jsonify({
        "name": biotools_info.name,
        "description": biotools_info.description,
        "url": biotools_info.url,
        "keywords": biotools_info.keywords,
        "category" : biotools_info.category,
        "moduleName":biotools_info.modulename,
        "version": biotools_info.version
    })

# api route for displaying all records as json for ajax render
@app.route('/api')
def biotools_ajax():
    # page to populate all the records from the database as json
    results = db.session.execute("SELECT * FROM biocontainers").fetchall()
    all_tools = []
    for biotool in results:
        tools_info = {
            "name" : biotool.name,
            "description" : biotool.description,
            "category" : biotool.category,
            "moduleName" : biotool.modulename,
            "keywords" : biotool.keywords,
            "url" : biotool.url,
            "version" : biotool.version
        }
        all_tools.append(tools_info)

    return jsonify({
        "data": all_tools
    })

# api route to add new biocontainers with authentication
@app.route('/add', methods=["POST", "GET"])
@auth.login_required
def add_biocontainer():
    posts = request.get_json()
    print(posts['all_entries'])
    all_entries = posts['all_entries']
    for item in all_entries:
        name = item['name']
        description = item['description']
        url= item['url']
        modulename = item['modulename']
        version = item['version']
        category = item['category']
        keywords = item['keywords']
        db.session.execute("INSERT INTO biocontainers (name, description, category, url, version, keywords, modulename) VALUES (:name, :description, :category, :url, :version, :keywords, :modulename)",
                {"name": name, "description": description, "category":category, "url": url, "version":version, "keywords":keywords, "modulename":modulename})
        db.session.commit()

    return jsonify({
        "message": "Success! entries added to database!"
    })
