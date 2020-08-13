import flask

from lawn_care.services import user_service
from lawn_care.viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
def account():
    return flask.render_template('account/index.html')


@blueprint.route('/account/register', methods=['GET'])
def register_get():
    vm = RegisterViewModel()
    return flask.render_template('account/register.html', **vm.to_dict())


@blueprint.route('/account/register', methods=['POST'])
def register_post():
    vm = RegisterViewModel()

    vm.validate()

    if vm.error:
        return flask.render_template('account/register.html', **vm.to_dict())

    user = user_service.create_user(
        vm.username,
        vm.password,
        vm.email,
        vm.first_name,
        vm.last_name
    )
    if not user:
        vm.error = 'Error creating account.'
        return flask.render_template('account/register.html', **vm.to_dict())
    resp = flask.redirect('/account')

    return resp


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
