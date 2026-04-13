from flask import render_template, request, redirect

questoes = []

def index():
    return render_template('index.html', questoes=questoes)


def cadastrar():
    pass


def editar(id):
    pass

def deletar(id):
    pass