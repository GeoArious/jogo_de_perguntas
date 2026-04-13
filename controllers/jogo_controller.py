from flask import render_template, request, redirect

questoes = []

def index():
    return render_template('index.html', questoes=questoes)


def cadastrar():
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        alt1 = request.form['alt1']
        alt2 = request.form['alt2']
        alt3 = request.form['alt3']
        correta = request.form['correta']

        questoes.append({
            "pergunta": pergunta,
            "alt1": alt1,
            "alt2": alt2,
            "alt3": alt3,
            "correta": correta
        })

        return redirect('/')

    return render_template('cadastrar.html')


def editar(id):
    if request.method == 'POST':
        questoes[id] = {
            "pergunta": request.form['pergunta'],
            "alt1": request.form['alt1'],
            "alt2": request.form['alt2'],
            "alt3": request.form['alt3'],
            "correta": request.form['correta']
        }

        return redirect('/')

    return render_template('editar.html', questao=questoes[id], id=id)


def deletar(id):
    if id < len(questoes):
        questoes.pop(id)

    return redirect('/')
