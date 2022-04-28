from flask import Flask
from views import views
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/views')

if __name__ == "__main__":
    app.run(debug=True, port=8888)
