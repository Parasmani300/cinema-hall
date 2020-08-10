from application import app,db,auth
from flask import Flask, render_template, request, json, Response,redirect,flash,url_for,session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book')
def book():
    return render_template('index.html')