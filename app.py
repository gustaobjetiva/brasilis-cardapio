# Cardápio Brasilis Gourmet. No PythonAnywhere: o arquivo WSGI faz `from app import app as application`.
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="docs", static_url_path="")


@app.route("/")
def cardapio():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True)
