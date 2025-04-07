from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    # a simple page that says hello
    @app.route("/")
    def hello():
        return "Hello, World!"

    from . import healthz

    app.register_blueprint(healthz.bp)
    return app
