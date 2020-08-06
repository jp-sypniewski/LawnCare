import flask

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/login')
def show_login():
    return flask.render_template('account/login.html')
