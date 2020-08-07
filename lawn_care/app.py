import flask

from lawn_care.data import db_session

app = flask.Flask(__name__)


def main():
    register_blueprints()
    # setup_db()
    app.run()


def register_blueprints():
    from lawn_care.views import home_views
    app.register_blueprint(home_views.blueprint)
    from lawn_care.views import account_views
    app.register_blueprint(account_views.blueprint)
    from lawn_care.views import service_views
    app.register_blueprint(service_views.blueprint)

def setup_db():
    db_session.global_init()


if __name__ == '__main__':
    main()
