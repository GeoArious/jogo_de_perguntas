from flask import render_template, request, redirect

questoes = []

def index():
    return render_template('index.html', questoes=questoes)