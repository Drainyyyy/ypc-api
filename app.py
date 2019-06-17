from flask import Flask

import config

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(**config.FLASK_RUN_CONFIG)
