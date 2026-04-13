from flask import Flask
from routes import jogo_router

app = Flask(__name__)

jogo_router.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)