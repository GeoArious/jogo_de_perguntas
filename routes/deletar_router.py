from flask import Flask
from controllers import deletar_controller

def init_app(app):
    app.add_url_rule(
        '/deletar/<int:id>',
        view_func=deletar_controller.deletar,
        methods=['GET']
    )