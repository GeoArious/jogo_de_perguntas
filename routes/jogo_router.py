from controllers import questao_controller

def init_app(app):

    app.add_url_rule(
        '/',
        view_func=questao_controller.index,
        methods=['GET']
    )

    app.add_url_rule(
        '/cadastrar',
        view_func=questao_controller.cadastrar,
        methods=['GET', 'POST']
    )

    app.add_url_rule(
        '/editar/<int:id>',
        view_func=questao_controller.editar,
        methods=['GET', 'POST']
    )

    app.add_url_rule(
        '/deletar/<int:id>',
        view_func=questao_controller.deletar,
        methods=['GET']
    )