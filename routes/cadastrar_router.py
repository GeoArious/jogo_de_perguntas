from flask import Flask
from controllers import cadastrar_controller

def init_app(app):
    app.add_url_rule(
        '/cadastrar',
        view_func=cadastrar_controller.cadastrar,
        methods=['GET', 'POST']
    )