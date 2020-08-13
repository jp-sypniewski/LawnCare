import flask

from lawn_care.services import services_service

blueprint = flask.Blueprint('service', __name__, template_folder='templates')


@blueprint.route('/request', methods=['GET'])
def get_quote_request():
    pass


@blueprint.route('/request', methods=['POST'])
def post_quote_request():
    pass


@blueprint.route('/services/<service_name>')
def show_service(service_name: str):
    ret_dict = {'name': service_name}
    return flask.render_template('services/display.html', **ret_dict)


@blueprint.route('/services')
def all_services():
    services = services_service.get_db_services()
    ret_dict = {'services': services}
    return flask.render_template('services/all.html', **ret_dict)
