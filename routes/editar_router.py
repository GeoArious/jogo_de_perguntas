from flask import Flask
from controllers import editar_controller

def init_app(app):
    app.add_url_rule(
        '/editar/<int:id>',
        view_func=editar_controller.editar,
        methods=['GET', 'POST']
    )