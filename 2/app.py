from flask import Flask

from config.router import Router

app = Flask(__name__, template_folder='views')

Router.run(app)

if __name__ == '__main__':
    app.run(
        debug = True,
        port = 80
    )
