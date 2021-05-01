from flask import render_template, session_request, redirect, url_for

from shop import app, db

@app.route('/')
def home():
  return "home page of your shop"