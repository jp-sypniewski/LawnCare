import flask

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
def account():
    return flask.render_template('account/account.html')


@blueprint.route('/account/login', methods=['GET'])
def login_get():
    return flask.render_template('account/login.html')


@blueprint.route('/account/login', methods=['POST'])
def login_post():
    return flask.render_template('account/login.html')


@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    # remove the user's cookie once it's made
    return resp
