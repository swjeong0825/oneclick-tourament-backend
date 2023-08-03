from flask import Flask
from routers.Tournament.tournament_router import tournament_blueprint

app = Flask(__name__)
app.register_blueprint(tournament_blueprint, url_prefix='/tournament')

@app.route("/")
def hello():
    return '<h1>Hello, World!</h1>'