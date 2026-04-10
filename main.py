from flask import Flask
from routes import cadastrar_router, deletar_router, editar_router, index_router

app = Flask(__name__)

index_router.init_app(app)
cadastrar_router.init_app(app)
editar_router.init_app(app)
deletar_router.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)