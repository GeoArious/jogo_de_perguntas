from controllers import jogo_controller

def init_app(app):

    app.add_url_rule(
        '/',
        view_func=jogo_controller.index,
        methods=['GET']
    )

    app.add_url_rule(
        '/cadastrar',
        view_func=jogo_controller.cadastrar,
        methods=['GET', 'POST']
    )

    app.add_url_rule(
        '/editar/<int:id>',
        view_func=jogo_controller.editar,
        methods=['GET', 'POST']
    )

    app.add_url_rule(
        '/deletar/<int:id>',
        view_func=jogo_controller.deletar,
        methods=['GET']
    )