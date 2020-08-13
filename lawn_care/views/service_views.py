import flask

from lawn_care.services import services_service, quote_service
from lawn_care.viewmodels.quotes.submit_quote_viewmodel import QuoteRequestViewModel

blueprint = flask.Blueprint('service', __name__, template_folder='templates')


@blueprint.route('/request', methods=['GET'])
def get_quote_request():
    vm = QuoteRequestViewModel()
    return flask.render_template('quotes/request.html', vm.to_dict())


@blueprint.route('/request', methods=['POST'])
def post_quote_request():
    vm = QuoteRequestViewModel()

    vm.validate()

    if vm.error():
        return flask.render_template('quotes/request.html', vm.to_dict())

    quote = quote_service.add_quote_request(
        vm.requester_name,
        vm.dttm_requested,
        vm.contact_phone,
        vm.contact_email,
        vm.preference_contact
    )

    if not quote:
        vm.error = 'Your quote request could not be created.'
        return flask.render_template('quotes/request.html', vm.to_dict())

    return flask.render_template('quotes/request.html', vm.to_dict())


@blueprint.route('/services/<service_name>')
def show_service(service_name: str):
    ret_dict = {'name': service_name}
    return flask.render_template('services/display.html', **ret_dict)


@blueprint.route('/services')
def all_services():
    services = services_service.get_db_services()
    ret_dict = {'services': services}
    return flask.render_template('services/all.html', **ret_dict)
