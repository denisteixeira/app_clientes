form flask import Flask, render_template, request, redirect, url_for, flash
import 

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def index ():
    con = 